# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exportData.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_exportData(object):
    def setupUi(self, exportData):
        if not exportData.objectName():
            exportData.setObjectName(u"exportData")
        exportData.resize(1175, 749)
        exportData.setStyleSheet(u"QWidget {\n"
"	background: rgb(42, 42, 42);\n"
"}")
        self.widget = QWidget(exportData)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 341, 751))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(28, 0, 101);\n"
"}")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 341, 121))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(99, 0, 174);\n"
"	border: 1px solid black;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 0, 191, 51))
        self.label.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-60, 40, 191, 51))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font-size: 16px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-50, 70, 191, 51))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font-size: 16px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.imagePathInput = QLabel(self.frame)
        self.imagePathInput.setObjectName(u"imagePathInput")
        self.imagePathInput.setGeometry(QRect(100, 40, 241, 51))
        self.imagePathInput.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"}")
        self.imagePathInput.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.phantomPathInput = QLabel(self.frame)
        self.phantomPathInput.setObjectName(u"phantomPathInput")
        self.phantomPathInput.setGeometry(QRect(100, 70, 241, 51))
        self.phantomPathInput.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"}")
        self.phantomPathInput.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 120, 341, 121))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(99, 0, 174);;\n"
"	border: 1px solid black;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 40, 341, 51))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 360, 341, 121))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	background-color:  rgb(99, 0, 174);\n"
"	border: 1px solid black;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 30, 341, 51))
        self.label_7.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 480, 341, 121))
        self.frame_5.setStyleSheet(u"QFrame {\n"
"	background-color:  rgb(99, 0, 174);\n"
"	border: 1px solid black;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 30, 301, 51))
        self.label_8.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.frame_3 = QFrame(exportData)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 240, 341, 121))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(99, 0, 174);\n"
"	border: 1px solid black;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 30, 341, 51))
        self.label_6.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight:bold;\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.backButton = QPushButton(exportData)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 690, 131, 41))
        self.backButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.selectDataLabel = QLabel(exportData)
        self.selectDataLabel.setObjectName(u"selectDataLabel")
        self.selectDataLabel.setGeometry(QRect(530, 60, 431, 131))
        self.selectDataLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 29px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectDataLabel.setTextFormat(Qt.AutoText)
        self.selectDataLabel.setScaledContents(False)
        self.selectDataLabel.setAlignment(Qt.AlignCenter)
        self.selectDataLabel.setWordWrap(True)
        self.appendFileOptionButton = QPushButton(exportData)
        self.appendFileOptionButton.setObjectName(u"appendFileOptionButton")
        self.appendFileOptionButton.setGeometry(QRect(600, 320, 301, 51))
        self.appendFileOptionButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.clearAppendFileButton = QPushButton(exportData)
        self.clearAppendFileButton.setObjectName(u"clearAppendFileButton")
        self.clearAppendFileButton.setGeometry(QRect(750, 380, 131, 41))
        self.clearAppendFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.appendFileLabel = QLabel(exportData)
        self.appendFileLabel.setObjectName(u"appendFileLabel")
        self.appendFileLabel.setGeometry(QRect(610, 270, 271, 51))
        self.appendFileLabel.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: white;\n"
"	font-size: 17px;\n"
"}")
        self.appendFileLabel.setAlignment(Qt.AlignCenter)
        self.appendFileLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.chooseAppendFileButton = QPushButton(exportData)
        self.chooseAppendFileButton.setObjectName(u"chooseAppendFileButton")
        self.chooseAppendFileButton.setGeometry(QRect(612, 380, 131, 41))
        self.chooseAppendFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.appendFilePath = QLineEdit(exportData)
        self.appendFilePath.setObjectName(u"appendFilePath")
        self.appendFilePath.setGeometry(QRect(640, 330, 201, 31))
        self.appendFilePath.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.newFileOptionButton = QPushButton(exportData)
        self.newFileOptionButton.setObjectName(u"newFileOptionButton")
        self.newFileOptionButton.setGeometry(QRect(600, 430, 301, 51))
        self.newFileOptionButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.newFolderPathInput = QLineEdit(exportData)
        self.newFolderPathInput.setObjectName(u"newFolderPathInput")
        self.newFolderPathInput.setGeometry(QRect(640, 260, 201, 31))
        self.newFolderPathInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.chooseNewFolderButton = QPushButton(exportData)
        self.chooseNewFolderButton.setObjectName(u"chooseNewFolderButton")
        self.chooseNewFolderButton.setGeometry(QRect(610, 300, 131, 41))
        self.chooseNewFolderButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.newFolderPathLabel = QLabel(exportData)
        self.newFolderPathLabel.setObjectName(u"newFolderPathLabel")
        self.newFolderPathLabel.setGeometry(QRect(610, 200, 271, 51))
        self.newFolderPathLabel.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: white;\n"
"	font-size: 17px;\n"
"}")
        self.newFolderPathLabel.setAlignment(Qt.AlignCenter)
        self.newFolderPathLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.clearNewFolderButton = QPushButton(exportData)
        self.clearNewFolderButton.setObjectName(u"clearNewFolderButton")
        self.clearNewFolderButton.setGeometry(QRect(750, 300, 131, 41))
        self.clearNewFolderButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.newFileNameInput = QLineEdit(exportData)
        self.newFileNameInput.setObjectName(u"newFileNameInput")
        self.newFileNameInput.setGeometry(QRect(650, 440, 201, 31))
        self.newFileNameInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.newFileNameInput.setAlignment(Qt.AlignCenter)
        self.createNewFileButton = QPushButton(exportData)
        self.createNewFileButton.setObjectName(u"createNewFileButton")
        self.createNewFileButton.setGeometry(QRect(640, 590, 221, 41))
        self.createNewFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.newFileNameLabel = QLabel(exportData)
        self.newFileNameLabel.setObjectName(u"newFileNameLabel")
        self.newFileNameLabel.setGeometry(QRect(610, 380, 271, 51))
        self.newFileNameLabel.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: white;\n"
"	font-size: 17px;\n"
"}")
        self.newFileNameLabel.setAlignment(Qt.AlignCenter)
        self.newFileNameLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.appendFileButton = QPushButton(exportData)
        self.appendFileButton.setObjectName(u"appendFileButton")
        self.appendFileButton.setGeometry(QRect(640, 520, 221, 41))
        self.appendFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.appendFileBackButton = QPushButton(exportData)
        self.appendFileBackButton.setObjectName(u"appendFileBackButton")
        self.appendFileBackButton.setGeometry(QRect(640, 590, 221, 41))
        self.appendFileBackButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.newFileBackButton = QPushButton(exportData)
        self.newFileBackButton.setObjectName(u"newFileBackButton")
        self.newFileBackButton.setGeometry(QRect(640, 650, 221, 41))
        self.newFileBackButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.fileNameErrorLabel = QLabel(exportData)
        self.fileNameErrorLabel.setObjectName(u"fileNameErrorLabel")
        self.fileNameErrorLabel.setGeometry(QRect(540, 480, 421, 81))
        self.fileNameErrorLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 0, 23);\n"
"	font-size: 20px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.fileNameErrorLabel.setAlignment(Qt.AlignCenter)
        self.fileNameWarningLabel = QLabel(exportData)
        self.fileNameWarningLabel.setObjectName(u"fileNameWarningLabel")
        self.fileNameWarningLabel.setGeometry(QRect(540, 490, 421, 81))
        self.fileNameWarningLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 0, 23);\n"
"	font-size: 20px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.fileNameWarningLabel.setAlignment(Qt.AlignCenter)
        self.dataSavedSuccessfullyLabel = QLabel(exportData)
        self.dataSavedSuccessfullyLabel.setObjectName(u"dataSavedSuccessfullyLabel")
        self.dataSavedSuccessfullyLabel.setGeometry(QRect(540, 300, 421, 81))
        self.dataSavedSuccessfullyLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(23, 255, 0);\n"
"	font-size: 30px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.dataSavedSuccessfullyLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(exportData)

        QMetaObject.connectSlotsByName(exportData)
    # setupUi

    def retranslateUi(self, exportData):
        exportData.setWindowTitle(QCoreApplication.translate("exportData", u"Export Data", None))
#if QT_CONFIG(tooltip)
        self.widget.setToolTip(QCoreApplication.translate("exportData", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("exportData", u"Image Selection:", None))
        self.label_2.setText(QCoreApplication.translate("exportData", u"Image:", None))
        self.label_3.setText(QCoreApplication.translate("exportData", u"Phantom:", None))
        self.imagePathInput.setText(QCoreApplication.translate("exportData", u"Sample filename ", None))
        self.phantomPathInput.setText(QCoreApplication.translate("exportData", u"Sample filename ", None))
        self.label_4.setText(QCoreApplication.translate("exportData", u"Region of Interest (ROI) Selection", None))
        self.label_7.setText(QCoreApplication.translate("exportData", u"Radio Frequency Data Analysis", None))
        self.label_8.setText(QCoreApplication.translate("exportData", u"Export Results", None))
        self.label_6.setText(QCoreApplication.translate("exportData", u"Analysis Parameter Selection", None))
        self.backButton.setText(QCoreApplication.translate("exportData", u"Back", None))
        self.selectDataLabel.setText(QCoreApplication.translate("exportData", u"Select Data Export Method:", None))
#if QT_CONFIG(tooltip)
        self.appendFileOptionButton.setToolTip(QCoreApplication.translate("exportData", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.appendFileOptionButton.setText(QCoreApplication.translate("exportData", u"Append Data onto Existing Excel File", None))
        self.clearAppendFileButton.setText(QCoreApplication.translate("exportData", u"Clear Path", None))
        self.appendFileLabel.setText(QCoreApplication.translate("exportData", u"Excel File to Append to:", None))
        self.chooseAppendFileButton.setText(QCoreApplication.translate("exportData", u"Choose File", None))
#if QT_CONFIG(tooltip)
        self.newFileOptionButton.setToolTip(QCoreApplication.translate("exportData", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.newFileOptionButton.setText(QCoreApplication.translate("exportData", u"Save to New Excel File", None))
        self.chooseNewFolderButton.setText(QCoreApplication.translate("exportData", u"Choose Folder", None))
        self.newFolderPathLabel.setText(QCoreApplication.translate("exportData", u"Folder to save new file in:", None))
        self.clearNewFolderButton.setText(QCoreApplication.translate("exportData", u"Clear Path", None))
        self.createNewFileButton.setText(QCoreApplication.translate("exportData", u"Create File", None))
        self.newFileNameLabel.setText(QCoreApplication.translate("exportData", u"Type name of new file:\n"
"(no spaces,  must end in \".xlsx\")", None))
        self.appendFileButton.setText(QCoreApplication.translate("exportData", u"Append Data to File", None))
        self.appendFileBackButton.setText(QCoreApplication.translate("exportData", u"Back", None))
        self.newFileBackButton.setText(QCoreApplication.translate("exportData", u"Back", None))
        self.fileNameErrorLabel.setText(QCoreApplication.translate("exportData", u"ERROR: Filename must not contain a space\n"
"and must end in \".xlsx\"", None))
        self.fileNameWarningLabel.setText(QCoreApplication.translate("exportData", u"WARNING: If file of specified folder and filename\n"
"already exists,  that file will be\n"
"deleted and overwritten", None))
        self.dataSavedSuccessfullyLabel.setText(QCoreApplication.translate("exportData", u"Data saved successfully!", None))
    # retranslateUi

