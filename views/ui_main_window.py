# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 768)
        MainWindow.setMinimumSize(QSize(1000, 700))
        MainWindow.setStyleSheet(u"\n"
"QMainWindow { background-color: #0f1419; }\n"
"QWidget#centralwidget { background-color: #1a202c; }\n"
"\n"
"/* Left Panel Styles */\n"
"QLabel#image_label {\n"
"    background-color: #2d3748;\n"
"    color: #e2e8f0;\n"
"    border: 2px dashed #667eea;\n"
"    border-radius: 12px;\n"
"    font-size: 18px;\n"
"}\n"
"QLabel#image_label:hover {\n"
"    border: 2px dashed #764ba2;\n"
"    background-color: #354054;\n"
"}\n"
"\n"
"/* Right Panel Styles */\n"
"QGroupBox#results_group {\n"
"    color: #e2e8f0;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #4a5568;\n"
"    border-radius: 8px;\n"
"    margin-top: 15px;\n"
"}\n"
"QGroupBox#results_group::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"}\n"
"QLabel#subject_info, QLabel#distance_info, QLabel#accuracy_info {\n"
"    color: #cbd5e0;\n"
"    font-size: 14px;\n"
"    font-weight: normal;\n"
"}\n"
"QLabel#match_label {\n"
"    background-color: #0f1419;\n"
"    border: 1px solid #4a5568;\n"
"    border-radius: 8px;\n"
"}\n"
"QLabel#roc_label {\n"
"    background-color: #0f1419;\n"
"    border: 1px solid #4a5568;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* Buttons */\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 12px;\n"
"    min-height: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #764ba2, stop:1 #667eea);\n"
"}\n"
"   ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setContentsMargins(40, 40, 40, 40)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_layout = QVBoxLayout()
        self.left_layout.setSpacing(20)
        self.left_layout.setObjectName(u"left_layout")
        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.image_label.setAlignment(Qt.AlignCenter)

        self.left_layout.addWidget(self.image_label)

        self.upload_btn = QPushButton(self.centralwidget)
        self.upload_btn.setObjectName(u"upload_btn")
        self.upload_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.left_layout.addWidget(self.upload_btn)

        self.left_layout.setStretch(0, 1)

        self.horizontalLayout.addLayout(self.left_layout, 1)

        self.results_group = QGroupBox(self.centralwidget)
        self.results_group.setObjectName(u"results_group")
        self.verticalLayout_2 = QVBoxLayout(self.results_group)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setContentsMargins(20, 15, 20, 20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.subject_info = QLabel(self.results_group)
        self.subject_info.setObjectName(u"subject_info")

        self.verticalLayout_2.addWidget(self.subject_info)

        self.distance_info = QLabel(self.results_group)
        self.distance_info.setObjectName(u"distance_info")

        self.verticalLayout_2.addWidget(self.distance_info)

        self.accuracy_info = QLabel(self.results_group)
        self.accuracy_info.setObjectName(u"accuracy_info")

        self.verticalLayout_2.addWidget(self.accuracy_info)

        self.match_label = QLabel(self.results_group)
        self.match_label.setObjectName(u"match_label")
        self.match_label.setMinimumSize(QSize(150, 120))
        self.match_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.match_label)

        self.roc_label = QLabel(self.results_group)
        self.roc_label.setObjectName(u"roc_label")
        self.roc_label.setMinimumSize(QSize(150, 240))
        self.roc_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.roc_label, 1)


        self.horizontalLayout.addWidget(self.results_group, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Eigenface Recognition System", None))
        self.image_label.setText(QCoreApplication.translate("MainWindow", u"Click here or use button to upload image", None))
        self.upload_btn.setText(QCoreApplication.translate("MainWindow", u"Upload New Image", None))
        self.results_group.setTitle(QCoreApplication.translate("MainWindow", u"Recognition Analysis", None))
        self.subject_info.setText(QCoreApplication.translate("MainWindow", u"Matched Subject: Pending...", None))
        self.distance_info.setText(QCoreApplication.translate("MainWindow", u"Confidence Score: N/A", None))
        self.accuracy_info.setText(QCoreApplication.translate("MainWindow", u"Model Accuracy: Loading...", None))
        self.match_label.setText(QCoreApplication.translate("MainWindow", u"Match Preview", None))
        self.roc_label.setText(QCoreApplication.translate("MainWindow", u"ROC Curve", None))
    # retranslateUi

