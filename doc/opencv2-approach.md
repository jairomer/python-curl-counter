# OpenCV2 Approach to body tracking

**Def. Cascade Classifier**
- [Haar Cascades](https://medium.com/analytics-vidhya/haar-cascades-explained-38210e57970d)
- http://www.staroceans.org/documents/ICIP2002.pdf
- https://medium.com/analytics-vidhya/haar-cascades-explained-38210e57970d


**Def. Adaboost:** A Boosting technique that combines multiple weak classifiers into a single strong classifier.
- [Adaboost](https://mccormickml.com/2013/12/13/adaboost-tutorial/#:~:text=AdaBoost%20is%20a%20popular%20boosting,female%20based%20on%20their%20height.)

**MediaPipe:** A framework for building machine learning pipelines for processing time-series data like video, audio, etc.
- Cross-platform framework available in Desktop/Server, Android, ioS and embedded devices based in ARM.
- Toolkit
  + Framework
    * Calculator API in C++
    * Graph construction API in Protobuf
    * Graph Execution API in C++, Java, Obj-C
  + Solutions

The mediapipe perception pipeline is called a Graph. Inside the MediaPipe Graph the nodes are called **calculators** and edges are called **streams**.

Every stream carries a sequence of packets that have ascending time stamps.

**Calculators**
- Specific computations written in C++ with assigned tasks to process.
- The packets of data enter and leave throyugh the ports in a calculator.
- When init. a calculator it declares the packet payload type that will traverse the port.
- Every time a graph runs, the FW implements  Open, Process and Close methods in thsoe calculators.
  + Open: Initiates the calculator.
  + Process: Repeatedly runs when a packet enters.
  + Close: Code to execute after an entire graph run.
- Calculator types in MediaPipe
  +  All the calculators can  be grouped into four categories:
    * Pre processing calculators : Are a family of image and media processing calculators.
    * Inference calculators: Allow native integration with Tensodorflows and Tensorflow Lite for ML inference.
    * Post-processing calculators perform ML post-processing tasks such as detection, segmentation and classification.
    * Utility calculators are a family of calculators performing final tasks such as image annotation.
- MediaPipe Solutions
  + Open-source pre-built examples based on a specific pre-trained TensorFlow or TFLite model.

## AI Processors

https://geohot.github.io/blog/jekyll/update/2021/06/13/a-breakdown-of-ai-chip-companies.html


## Training/Tagging

- [Amazon Mechanical Turk](https://www.mturk.com/)

## Pose estimation with Python and MediaPipe

(Pose estimation with multiple people)[https://shawntng.medium.com/multi-person-pose-estimation-with-mediapipe-52e6a60839dd]

**Process**
1. Setting up Media Pipe
2. Estimating poses
3. Extracting joint coordinates
4. Calculating angles between joints
5. Building a gym curl counter.

**MediaPipe Pose**
- Inferring 33 3D landmarks and background segmentation mask on the whole body from the RGB videoframes.
- BlazePose research based on a ML google model.
- Realtime performance on mobile phoes with CPU inference.
- Topology
  + COCO Topology
  + 17 landmarks across the torso, arms, legs and face with 33 pose points.

I am concerned with the effectiveness of this model when involving several persons.
In a possible application we can do the folowing:
1. Detect all possible frames.
2. Show them on the screen to the user.
3. User selects the frame to monitor.
4. Segment frame, then feed it to the neural network.

[Video processing facts](https://pyimagesearch.com/2017/02/06/faster-video-file-fps-with-cv2-videocapture-and-opencv/)

[OpenCv in Android](https://medium.com/android-news/a-beginners-guide-to-setting-up-opencv-android-library-on-android-studio-19794e220f3c)

```
Esta mañana me he puesto a estudiar el código de este video. Estaba intentando usar Docker para ejecutar opencv en python, resulta que la captura de video integrada con opencv no funciona dentro de los contenedores, puedes encontrar a un montón de peña Internet sufriendo por ello.

El workaround es usar el viejo y fiable virtualenv de Python.

Yo terminaria ese video cuanto antes y empezaria a pensar en portarlo a una aplicación de Android cuanto antes. He investigado un poco y parece que el way to go es construir una libreria en C++ usando a OpenCV como dependencia e integrarla dentro de la app. Si tu idea inicial era hacer un proyecto en C++ esto podría interesarte.

https://medium.com/android-news/a-beginners-guide-to-setting-up-opencv-android-library-on-android-studio-19794e220f3c 

También vamos a tener que ponernos los guantes de cirujano y ver como podemos extraer el modelo de la libreria de google para integrarlo en la nuestra.

https://github.com/google/mediapipe

Me parece que el siguiente paso lógico es construir esa libreria standalone en C++ donde consigamos hacer exactamente lo mismo que se propone en este video y posteriormente extenderla con las funcionalidades que deseamos meter en la app.

Hay otras cosillas interesantes que se pueden hacer desde el punto de vista de sistemas, como por ejemplo un pipeline de video para accelerar el procesado de las imagenes antes de pasarselas al modelo. Pero ya veremos esas cuestiones más adelante.

https://pyimagesearch.com/2017/02/06/faster-video-file-fps-with-cv2-videocapture-and-opencv/
```

### Model

- The pose detection system will return an array of 32 landmarks, one for each articulation.
- Each articulation is connected to one or more articulations.
- Each landmark is a coordinate in the model.
- From each three connected joints, we can extract the angle between the outermosts.
- We can also check if the joint is visible or not.


## Android

https://google.github.io/mediapipe/getting_started/install.html
https://google.github.io/mediapipe/getting_started/android
https://bazel.build/
