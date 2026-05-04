# main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Qt
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

    def label_clicked(self, event):
        self.upload_image()

    def generate_roc(self):
        # TODO
        ...

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.pgm)"
        )

        if file_path:
            try:
                display_img, prepared_faces, prediction, match_img_path = self.controller.handle_image_upload(file_path)

                pixmap = cv_img_to_pixmap(display_img)
                self.ui.image_label.setPixmap(pixmap.scaled(
                    self.ui.image_label.width(), self.ui.image_label.height(),
                    Qt.KeepAspectRatio, Qt.SmoothTransformation
                ))

                if prediction is not None:
                    self.ui.subject_info.setText(f"Matched Subject: {prediction}")
                    self.ui.distance_info.setText("Confidence Score: High")

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

            except Exception as e:
                print(f"Error processing image: {e}")
                self.ui.subject_info.setText("Error")
                self.ui.match_label.setText(f"✗ {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())  