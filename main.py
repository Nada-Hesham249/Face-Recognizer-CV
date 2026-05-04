# main.py
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap

from views.ui_main_window import Ui_MainWindow
from controllers.main_controller import MainController
from utils.image_utils import cv_img_to_pixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.controller = MainController()

        self.ui.upload_btn.clicked.connect(self.upload_image)
        self.ui.image_label.mousePressEvent = self.label_clicked

        QTimer.singleShot(0, self.initialize_ui)

    def label_clicked(self, event):
        self.upload_image()

    def initialize_ui(self):
        """Initialize UI with ROC and accuracy on startup."""
        self.generate_roc()
        self.update_accuracy()

    def update_accuracy(self):
        """Update and display model accuracy."""
        accuracy = self.controller.calculate_accuracy()
        accuracy_percent = accuracy * 100
        self.ui.accuracy_info.setText(f"Model Accuracy: {accuracy_percent:.2f}%")

    def generate_roc(self):
        roc_path = self.controller.generate_roc()

        if roc_path and os.path.exists(roc_path):
            roc_pixmap = QPixmap(roc_path)
            target_width = max(self.ui.roc_label.width(), 500)
            target_height = max(self.ui.roc_label.height(), 300)
            self.ui.roc_label.setPixmap(roc_pixmap.scaled(
                target_width, target_height,
                Qt.KeepAspectRatio, Qt.SmoothTransformation
            ))
            self.ui.roc_label.setText("")
        else:
            self.ui.roc_label.setText("ROC Curve unavailable")

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.pgm)"
        )

        if file_path:
            try:
                display_img, prepared_face, prediction, match_img_path, distance = self.controller.handle_image_upload(file_path)

                pixmap = cv_img_to_pixmap(display_img)
                self.ui.image_label.setPixmap(pixmap.scaled(
                    self.ui.image_label.width(), self.ui.image_label.height(),
                    Qt.KeepAspectRatio, Qt.SmoothTransformation
                ))

                if prediction is not None:
                    self.ui.subject_info.setText(f"Matched Subject: {prediction}")
                    if distance < 2500:
                        self.ui.distance_info.setText("Confidence Score: High ")
                    else:
                        self.ui.distance_info.setText("Confidence Score: Not Match")
                    if match_img_path:
                        match_pixmap = QPixmap(match_img_path)
                        self.ui.match_label.setPixmap(match_pixmap.scaled(
                            self.ui.match_label.width(), self.ui.match_label.height(),
                            Qt.KeepAspectRatio, Qt.SmoothTransformation
                        ))
                    else:
                        self.ui.match_label.setText("✓ Recognized")
                else:
                    self.ui.subject_info.setText("Matched Subject: Not detected")
                    self.ui.distance_info.setText("Confidence Score: N/A")
                    self.ui.match_label.setText("✗ No face detected in image")
                print(f"DEBUG distance: {distance}")
            except Exception as e:
                print(f"Error processing image: {e}")
                self.ui.subject_info.setText("Error")
                self.ui.match_label.setText(f"✗ {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())  