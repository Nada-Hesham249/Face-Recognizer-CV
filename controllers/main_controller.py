import os
from core import FaceDetector, FaceRecognizer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class MainController:
    def __init__(self):
        self.detector = FaceDetector()
        self.recognizer = FaceRecognizer()

    def handle_image_upload(self, file_path):
        display_img, prepared_face = self.detector.process_image(file_path)
        
        prediction = None
        match_img_path = None
        
        if prepared_face is not None:
            prediction = self.recognizer.predict_face(prepared_face)
            
            person_folder = os.path.join(BASE_DIR, "cropped_dataset", "train", prediction)
            if os.path.exists(person_folder):
                imgs = os.listdir(person_folder)
                if imgs:
                    match_img_path = os.path.join(person_folder, imgs[0])
        
        print(f"DEBUG: prediction={prediction}, match_img_path={match_img_path}")
        return display_img, prepared_face, prediction, match_img_path