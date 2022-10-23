FROM spmallick/opencv-docker:opencv-4
RUN pip install --upgrade pip
RUN pip install mediapipe opencv-python
COPY app.py /app.py
ENTRYPOINT ["python3", "/app.py"]
