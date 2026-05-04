import cv2
import numpy as np


class FaceDetector:
    def __init__(self):
        # Load OpenCV's pre-trained Haar cascade for frontal faces
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

        # Standard ORL database image dimensions (width, height)
        self.target_size = (92, 112)

    def process_image(self, image_path):
        """
        Reads an image, detects all faces, and prepares them for PCA.
        Returns: (display_image, list_of_prepared_face_matrices)
        """
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Could not read the image.")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect all faces in the image
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        display_img = img.copy()
        prepared_faces = []

        # Loop through every single face detected
        for (x, y, w, h) in faces:
            # Draw a green bounding box around this face
            cv2.rectangle(display_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Crop the face
            cropped_face = gray[y:y + h, x:x + w]

            # Resize to match ORL and add to our list
            resized_face = cv2.resize(cropped_face, self.target_size)
            prepared_faces.append(resized_face)

        return display_img, prepared_faces