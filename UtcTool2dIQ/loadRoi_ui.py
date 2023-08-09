# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadRoi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_loadRoi(object):
    def setupUi(self, loadRoi):
        if not loadRoi.objectName():
            loadRoi.setObjectName(u"loadRoi")
        loadRoi.resize(406, 324)
        loadRoi.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(42, 42, 42);\n"
"}")
        self.editImageDisplayLabel = QLabel(loadRoi)
        self.editImageDisplayLabel.setObjectName(u"editImageDisplayLabel")
        self.editImageDisplayLabel.setGeometry(QRect(100, -30, 201, 131))
        self.editImageDisplayLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 29px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.editImageDisplayLabel.setTextFormat(Qt.AutoText)
        self.editImageDisplayLabel.setScaledContents(False)
        self.editImageDisplayLabel.setAlignment(Qt.AlignCenter)
        self.editImageDisplayLabel.setWordWrap(True)
        self.newFolderPathLabel = QLabel(loadRoi)
        self.newFolderPathLabel.setObjectName(u"newFolderPathLabel")
        self.newFolderPathLabel.setGeometry(QRect(100, 50, 201, 51))
        self.newFolderPathLabel.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: white;\n"
"	font-size: 17px;\n"
"}")
        self.newFolderPathLabel.setAlignment(Qt.AlignCenter)
        self.newFolderPathLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.roiPathInput = QLineEdit(loadRoi)
        self.roiPathInput.setObjectName(u"roiPathInput")
        self.roiPathInput.setGeometry(QRect(100, 100, 201, 31))
        self.roiPathInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.chooseFileButton = QPushButton(loadRoi)
        self.chooseFileButton.setObjectName(u"chooseFileButton")
        self.chooseFileButton.setGeometry(QRect(65, 140, 131, 41))
        self.chooseFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.clearFileButton = QPushButton(loadRoi)
        self.clearFileButton.setObjectName(u"clearFileButton")
        self.clearFileButton.setGeometry(QRect(205, 140, 131, 41))
        self.clearFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.openRoiButton = QPushButton(loadRoi)
        self.openRoiButton.setObjectName(u"openRoiButton")
        self.openRoiButton.setGeometry(QRect(90, 210, 221, 41))
        self.openRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.backButton = QPushButton(loadRoi)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(90, 270, 221, 41))
        self.backButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")

        self.retranslateUi(loadRoi)

        QMetaObject.connectSlotsByName(loadRoi)
    # setupUi

    def retranslateUi(self, loadRoi):
        loadRoi.setWindowTitle(QCoreApplication.translate("loadRoi", u"Load Region of Interest (ROI)", None))
        self.editImageDisplayLabel.setText(QCoreApplication.translate("loadRoi", u"Load ROI:", None))
        self.newFolderPathLabel.setText(QCoreApplication.translate("loadRoi", u"ROI file: (.csv)", None))
        self.chooseFileButton.setText(QCoreApplication.translate("loadRoi", u"Choose File", None))
        self.clearFileButton.setText(QCoreApplication.translate("loadRoi", u"Clear File", None))
        self.openRoiButton.setText(QCoreApplication.translate("loadRoi", u"Open", None))
        self.backButton.setText(QCoreApplication.translate("loadRoi", u"Back", None))
    # retranslateUi

