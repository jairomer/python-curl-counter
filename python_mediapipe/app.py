#!/bin/env python3

import cv2
import mediapipe as mp
import numpy as np
import os

def get_radians(point, center):
    return np.arctan2(point[1]-center[1], point[0]-center[0])

def calculate_angle(first, mid, end):
    first = np.array(first)
    mid = np.array(mid)
    end = np.array(end)

    radians = get_radians(end, mid) - get_radians(first, mid)
    angle = np.abs(radians*180.0/np.pi)

    if angle>190.0:
        angle = 360-angle
    return angle


def main():
    capture_device = os.environ.get('CAM', '/dev/video0')
    assert os.path.exists(capture_device)
    
    # Drawing utility to visualize the pose results.
    mp_drawing = mp.solutions.drawing_utils
    
    # Specifications for drawing landmarks.
    #   0. landmark drawing
    #   1. connection drawing
    specs = [
        mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
        mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)]
    
    # Pose solution used to make detections
    mp_pose = mp.solutions.pose
    
    cap = cv2.VideoCapture(capture_device)
    if not cap.isOpened():
        print("Cannot open capture device, exiting")
        exit()
    
    # Setup an instance of our mediapipe feed
    #   You can tune the detection parameters of the model.
    #with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    curls = 0
    extended = True
    while cap.isOpened():
        ret, frame = cap.read()
    
        # Recolor image from BGR to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
    
        # Make pose detection
        #   - Results stored on an array.
        results = pose.process(image)
    
        # Recolor image back to BGR to use it with opencv.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
        try:
            landmarks = results.pose_landmarks.landmark
            # Get a specific landmark for the left shoulder.
            #print(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value])
            lshoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            lelbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            lwrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            # Calculate angle
            langle = calculate_angle(lshoulder, lelbow, lwrist)
            # Camera values used to denormalized the location of the landmarks.
            if langle < 55 and extended:
                extended=False
                curls = curls + 1
                print(curls)
            elif langle >= 55 and not extended:
                extended=True

            height = int(image.shape[0])
            width = int(image.shape[1])
            # Visualize
            cv2.putText(image,
                        str(langle),
                        tuple(np.multiply(lelbow, [height, width]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (255,255,255),
                        2,
                        cv2.LINE_AA)
        except:
            # No landmarks to detect
            pass

        # Render curls
        cv2.rectangle(image, (0,0), (225,73), (245,117,16),-1)
        cv2.putText(image,
                    'REPS',
                    (15,12),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0,0,0),
                    1,
                    cv2.LINE_AA)
        cv2.putText(image,
                    str(curls),
                    (10,60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (255,255,255),
                    2,
                    cv2.LINE_AA)
    
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, specs[0], specs[1])
    
        cv2.imshow('Mediapipe Feed', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break;
    
    cap.release()
    cv2.destroyAllWindows()


main()
