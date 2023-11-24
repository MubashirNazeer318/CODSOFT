import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



# Function to perform face detection and recognition
def detect_and_recognize_faces(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection using Haar cascade
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Extract the face region
            face = frame[y:y+h, x:x+w]

            # Preprocess the face for face recognition
            face = cv2.resize(face, (224, 224))  # Adjust size as needed
            face = np.expand_dims(face, axis=0)
            face = face / 255.0  # Normalize pixel values

          
            # Perform further processing with the obtained embeddings, e.g., compare with a database

            # Draw rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Face Detection and Recognition', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage
detect_and_recognize_faces('C:/Users/mubas/AppData/Local/Programs/Python/Python311/video.mp4')
