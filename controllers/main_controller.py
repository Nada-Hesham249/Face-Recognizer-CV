import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import FaceDetector, FaceRecognizer, ModelEvaluator
from core.Roc import ROC_Curve

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class MainController:
    def __init__(self):
        self.detector = FaceDetector()
        self.recognizer = FaceRecognizer()
        self.evaluator = ModelEvaluator(self.recognizer, BASE_DIR)
        self.roc_image_path = os.path.join(BASE_DIR, "saved_models", "roc_curve.png")

    def generate_roc(self):
        """Generate ROC curve using ModelEvaluator data."""
        X_test_pca, y_test_encoded = self.evaluator.get_test_data()

        if X_test_pca is None:
            return None

        os.makedirs(os.path.dirname(self.roc_image_path), exist_ok=True)
        roc_curve = ROC_Curve(self.recognizer.svm)
        roc_curve.plot_roc(X_test_pca, y_test_encoded, save_path=self.roc_image_path)

        return self.roc_image_path

    def calculate_accuracy(self):
        """Calculate and return model accuracy."""
        return self.evaluator.calculate_accuracy()

    def handle_image_upload(self, file_path):
        display_img, prepared_faces = self.detector.process_image(file_path)
        
        prediction = None
        match_img_path = None
        
        if prepared_faces and len(prepared_faces) > 0:
            # Get the first (and only) detected face
            first_face = prepared_faces[0]
            prediction = self.recognizer.predict_face(first_face)
            
            person_folder = os.path.join(BASE_DIR, "cropped_dataset", "train", prediction)
            if os.path.exists(person_folder):
                imgs = os.listdir(person_folder)
                if imgs:
                    match_img_path = os.path.join(person_folder, imgs[0])
        
        print(f"DEBUG: prediction={prediction}, match_img_path={match_img_path}")
        return display_img, prepared_faces, prediction, match_img_path