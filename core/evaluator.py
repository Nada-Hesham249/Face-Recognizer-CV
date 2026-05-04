import os
import cv2
import numpy as np


class ModelEvaluator:
    """Evaluate model performance on test dataset."""

    def __init__(self, recognizer, base_dir):
        """
        Args:
            recognizer: FaceRecognizer instance
            base_dir: Base directory path for dataset access
        """
        self.recognizer = recognizer
        self.base_dir = base_dir
        self.test_root = os.path.join(base_dir, "cropped_dataset", "test")

    def _load_test_data(self):
        """Load and prepare test dataset."""
        X_test = []
        y_test = []

        for person in sorted(os.listdir(self.test_root)):
            person_folder = os.path.join(self.test_root, person)
            if not os.path.isdir(person_folder):
                continue

            for img_name in sorted(os.listdir(person_folder)):
                img_path = os.path.join(person_folder, img_name)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    continue

                img = cv2.resize(img, (100, 100))
                X_test.append(img.flatten())
                y_test.append(person)

        if not X_test:
            return None, None

        X_test = np.array(X_test)
        y_test_encoded = self.recognizer.le.transform(y_test)

        X_test_pca = self.recognizer.pca.transform(X_test)

        return X_test_pca, y_test_encoded

    def calculate_accuracy(self):
        """Calculate and return model accuracy on test dataset."""
        X_test_pca, y_test_encoded = self._load_test_data()

        if X_test_pca is None:
            return 0.0

        predictions = self.recognizer.svm.predict(X_test_pca)
        accuracy = np.mean(predictions == y_test_encoded)
        return accuracy

    def get_test_data(self):
        """Get processed test data (used by ROC)."""
        return self._load_test_data()
