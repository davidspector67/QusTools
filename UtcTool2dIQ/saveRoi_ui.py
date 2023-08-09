# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saveRoi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_saveRoi(object):
    def setupUi(self, saveRoi):
        if not saveRoi.objectName():
            saveRoi.setObjectName(u"saveRoi")
        saveRoi.resize(633, 500)
        saveRoi.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(42, 42, 42);\n"
"}")
        self.saveRoiLabel = QLabel(saveRoi)
        self.saveRoiLabel.setObjectName(u"saveRoiLabel")
        self.saveRoiLabel.setGeometry(QRect(210, -20, 201, 131))
        self.saveRoiLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 29px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.saveRoiLabel.setTextFormat(Qt.AutoText)
        self.saveRoiLabel.setScaledContents(False)
        self.saveRoiLabel.setAlignment(Qt.AlignCenter)
        self.saveRoiLabel.setWordWrap(True)
        self.roiFolderPathLabel = QLabel(saveRoi)
        self.roiFolderPathLabel.setObjectName(u"roiFolderPathLabel")
        self.roiFolderPathLabel.setGeometry(QRect(210, 80, 201, 51))
        self.roiFolderPathLabel.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: white;\n"
"	font-size: 17px;\n"
"}")
        self.roiFolderPathLabel.setAlignment(Qt.AlignCenter)
        self.roiFolderPathLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.newFolderPathInput = QLineEdit(saveRoi)
        self.newFolderPathInput.setObjectName(u"newFolderPathInput")
        self.newFolderPathInput.setGeometry(QRect(210, 130, 201, 31))
        self.newFolderPathInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.chooseFolderButton = QPushButton(saveRoi)
        self.chooseFolderButton.setObjectName(u"chooseFolderButton")
        self.chooseFolderButton.setGeometry(QRect(175, 170, 131, 41))
        self.chooseFolderButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.clearFolderButton = QPushButton(saveRoi)
        self.clearFolderButton.setObjectName(u"clearFolderButton")
        self.clearFolderButton.setGeometry(QRect(315, 170, 131, 41))
        self.clearFolderButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.saveRoiButton = QPushButton(saveRoi)
        self.saveRoiButton.setObjectName(u"saveRoiButton")
        self.saveRoiButton.setGeometry(QRect(200, 440, 221, 41))
        self.saveRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.dataSavedSuccessfullyLabel = QLabel(saveRoi)
        self.dataSavedSuccessfullyLabel.setObjectName(u"dataSavedSuccessfullyLabel")
        self.dataSavedSuccessfullyLabel.setGeometry(QRect(100, 190, 421, 81))
        self.dataSavedSuccessfullyLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(23, 255, 0);\n"
"	font-size: 30px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.dataSavedSuccessfullyLabel.setAlignment(Qt.AlignCenter)
        self.newFileNameLabel = QLabel(saveRoi)
        self.newFileNameLabel.setObjectName(u"newFileNameLabel")
        self.newFileNameLabel.setGeometry(QRect(170, 230, 271, 51))
        self.newFileNameLabel.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: white;\n"
"	font-size: 17px;\n"
"}")
        self.newFileNameLabel.setAlignment(Qt.AlignCenter)
        self.newFileNameLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.newFileNameInput = QLineEdit(saveRoi)
        self.newFileNameInput.setObjectName(u"newFileNameInput")
        self.newFileNameInput.setGeometry(QRect(210, 290, 201, 31))
        self.newFileNameInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.newFileNameInput.setAlignment(Qt.AlignCenter)
        self.fileNameErrorLabel = QLabel(saveRoi)
        self.fileNameErrorLabel.setObjectName(u"fileNameErrorLabel")
        self.fileNameErrorLabel.setGeometry(QRect(100, 320, 421, 81))
        self.fileNameErrorLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 0, 23);\n"
"	font-size: 20px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.fileNameErrorLabel.setAlignment(Qt.AlignCenter)
        self.fileNameWarningLabel = QLabel(saveRoi)
        self.fileNameWarningLabel.setObjectName(u"fileNameWarningLabel")
        self.fileNameWarningLabel.setGeometry(QRect(100, 350, 421, 81))
        self.fileNameWarningLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 0, 23);\n"
"	font-size: 20px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.fileNameWarningLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(saveRoi)

        QMetaObject.connectSlotsByName(saveRoi)
    # setupUi

    def retranslateUi(self, saveRoi):
        saveRoi.setWindowTitle(QCoreApplication.translate("saveRoi", u"Save Region Of Interest (ROI)", None))
        self.saveRoiLabel.setText(QCoreApplication.translate("saveRoi", u"Save ROI:", None))
        self.roiFolderPathLabel.setText(QCoreApplication.translate("saveRoi", u"Folder to save ROI in:", None))
        self.chooseFolderButton.setText(QCoreApplication.translate("saveRoi", u"Choose Folder", None))
        self.clearFolderButton.setText(QCoreApplication.translate("saveRoi", u"Clear Folder", None))
        self.saveRoiButton.setText(QCoreApplication.translate("saveRoi", u"Save", None))
        self.dataSavedSuccessfullyLabel.setText(QCoreApplication.translate("saveRoi", u"ROI saved successfully!", None))
        self.newFileNameLabel.setText(QCoreApplication.translate("saveRoi", u"Type name of new file:\n"
"(no spaces,  must end in \".csv\")", None))
        self.fileNameErrorLabel.setText(QCoreApplication.translate("saveRoi", u"ERROR: Filename must not contain a space\n"
"and must end in \".csv\"", None))
        self.fileNameWarningLabel.setText(QCoreApplication.translate("saveRoi", u"WARNING: If file of specified folder and filename\n"
"already exists,  that file will be\n"
"deleted and overwritten", None))
    # retranslateUi

