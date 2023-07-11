# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectImage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_selectImage(object):
    def setupUi(self, selectImage):
        if not selectImage.objectName():
            selectImage.setObjectName(u"selectImage")
        selectImage.resize(1175, 749)
        selectImage.setStyleSheet(u"QWidget {\n"
"	background: rgb(42, 42, 42);\n"
"}")
        self.selectDataLabel = QLabel(selectImage)
        self.selectDataLabel.setObjectName(u"selectDataLabel")
        self.selectDataLabel.setGeometry(QRect(540, 70, 431, 131))
        self.selectDataLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 29px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectDataLabel.setTextFormat(Qt.AutoText)
        self.selectDataLabel.setScaledContents(False)
        self.selectDataLabel.setAlignment(Qt.AlignCenter)
        self.selectDataLabel.setWordWrap(True)
        self.chooseNiftiImageFileButton = QPushButton(selectImage)
        self.chooseNiftiImageFileButton.setObjectName(u"chooseNiftiImageFileButton")
        self.chooseNiftiImageFileButton.setGeometry(QRect(622, 380, 131, 41))
        self.chooseNiftiImageFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.niftiImagePathInput = QLineEdit(selectImage)
        self.niftiImagePathInput.setObjectName(u"niftiImagePathInput")
        self.niftiImagePathInput.setGeometry(QRect(650, 330, 201, 31))
        self.niftiImagePathInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.clearNiftiImageFileButton = QPushButton(selectImage)
        self.clearNiftiImageFileButton.setObjectName(u"clearNiftiImageFileButton")
        self.clearNiftiImageFileButton.setGeometry(QRect(760, 380, 131, 41))
        self.clearNiftiImageFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.generateImageButton = QPushButton(selectImage)
        self.generateImageButton.setObjectName(u"generateImageButton")
        self.generateImageButton.setGeometry(QRect(690, 600, 131, 41))
        self.generateImageButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.selectImageErrorMsg = QLabel(selectImage)
        self.selectImageErrorMsg.setObjectName(u"selectImageErrorMsg")
        self.selectImageErrorMsg.setGeometry(QRect(700, 660, 111, 41))
        self.selectImageErrorMsg.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 0, 23);\n"
"	font-size: 25px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectImageErrorMsg.setAlignment(Qt.AlignCenter)
        self.selectNiftiImageOptionButton = QPushButton(selectImage)
        self.selectNiftiImageOptionButton.setObjectName(u"selectNiftiImageOptionButton")
        self.selectNiftiImageOptionButton.setGeometry(QRect(630, 280, 251, 51))
        self.selectNiftiImageOptionButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.selectXmlFolderImageOptionButton = QPushButton(selectImage)
        self.selectXmlFolderImageOptionButton.setObjectName(u"selectXmlFolderImageOptionButton")
        self.selectXmlFolderImageOptionButton.setGeometry(QRect(630, 370, 251, 51))
        self.selectXmlFolderImageOptionButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.xmlImagePathInput = QLineEdit(selectImage)
        self.xmlImagePathInput.setObjectName(u"xmlImagePathInput")
        self.xmlImagePathInput.setGeometry(QRect(648, 260, 201, 31))
        self.xmlImagePathInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.clearXmlImageFolderButton = QPushButton(selectImage)
        self.clearXmlImageFolderButton.setObjectName(u"clearXmlImageFolderButton")
        self.clearXmlImageFolderButton.setGeometry(QRect(758, 300, 131, 41))
        self.clearXmlImageFolderButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.chooseXmlImageFolderButton = QPushButton(selectImage)
        self.chooseXmlImageFolderButton.setObjectName(u"chooseXmlImageFolderButton")
        self.chooseXmlImageFolderButton.setGeometry(QRect(620, 300, 131, 41))
        self.chooseXmlImageFolderButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.niftiImageDestinationPath = QLineEdit(selectImage)
        self.niftiImageDestinationPath.setObjectName(u"niftiImageDestinationPath")
        self.niftiImageDestinationPath.setGeometry(QRect(648, 390, 201, 31))
        self.niftiImageDestinationPath.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.clearNiftiImageDestinationButton = QPushButton(selectImage)
        self.clearNiftiImageDestinationButton.setObjectName(u"clearNiftiImageDestinationButton")
        self.clearNiftiImageDestinationButton.setGeometry(QRect(758, 430, 131, 41))
        self.clearNiftiImageDestinationButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.niftiImageDestinationButton = QPushButton(selectImage)
        self.niftiImageDestinationButton.setObjectName(u"niftiImageDestinationButton")
        self.niftiImageDestinationButton.setGeometry(QRect(620, 430, 131, 41))
        self.niftiImageDestinationButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.selectNiftiImageLabel = QLabel(selectImage)
        self.selectNiftiImageLabel.setObjectName(u"selectNiftiImageLabel")
        self.selectNiftiImageLabel.setGeometry(QRect(610, 250, 271, 51))
        self.selectNiftiImageLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectNiftiImageLabel.setAlignment(Qt.AlignCenter)
        self.selectNiftiImageLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.imageBackButton = QPushButton(selectImage)
        self.imageBackButton.setObjectName(u"imageBackButton")
        self.imageBackButton.setGeometry(QRect(690, 490, 131, 41))
        self.imageBackButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.selectXmlFolderImageLabel = QLabel(selectImage)
        self.selectXmlFolderImageLabel.setObjectName(u"selectXmlFolderImageLabel")
        self.selectXmlFolderImageLabel.setGeometry(QRect(620, 210, 271, 51))
        self.selectXmlFolderImageLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectXmlFolderImageLabel.setAlignment(Qt.AlignCenter)
        self.selectXmlFolderImageLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.niftiDestinationImageLabel = QLabel(selectImage)
        self.niftiDestinationImageLabel.setObjectName(u"niftiDestinationImageLabel")
        self.niftiDestinationImageLabel.setGeometry(QRect(620, 340, 271, 51))
        self.niftiDestinationImageLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.niftiDestinationImageLabel.setAlignment(Qt.AlignCenter)
        self.niftiDestinationImageLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sidebar = QWidget(selectImage)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(0, 0, 341, 751))
        self.sidebar.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(28, 0, 101);\n"
"}")
        self.imageSelectionSidebar = QFrame(self.sidebar)
        self.imageSelectionSidebar.setObjectName(u"imageSelectionSidebar")
        self.imageSelectionSidebar.setGeometry(QRect(0, 0, 341, 121))
        self.imageSelectionSidebar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(99, 0, 174);\n"
"	border: 1px solid black;\n"
"}")
        self.imageSelectionSidebar.setFrameShape(QFrame.StyledPanel)
        self.imageSelectionSidebar.setFrameShadow(QFrame.Raised)
        self.imageSelectionLabelSidebar = QLabel(self.imageSelectionSidebar)
        self.imageSelectionLabelSidebar.setObjectName(u"imageSelectionLabelSidebar")
        self.imageSelectionLabelSidebar.setGeometry(QRect(70, 0, 191, 51))
        self.imageSelectionLabelSidebar.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.imageSelectionLabelSidebar.setAlignment(Qt.AlignCenter)
        self.imageLabel = QLabel(self.imageSelectionSidebar)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(-60, 50, 191, 51))
        self.imageLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 16px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageFilenameDisplay = QLabel(self.imageSelectionSidebar)
        self.imageFilenameDisplay.setObjectName(u"imageFilenameDisplay")
        self.imageFilenameDisplay.setGeometry(QRect(100, 50, 241, 51))
        self.imageFilenameDisplay.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"}")
        self.imageFilenameDisplay.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.roiSidebar = QFrame(self.sidebar)
        self.roiSidebar.setObjectName(u"roiSidebar")
        self.roiSidebar.setGeometry(QRect(0, 120, 341, 121))
        self.roiSidebar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(49, 0, 124);\n"
"	border: 1px solid black;\n"
"}")
        self.roiSidebar.setFrameShape(QFrame.StyledPanel)
        self.roiSidebar.setFrameShadow(QFrame.Raised)
        self.roiSidebarLabel = QLabel(self.roiSidebar)
        self.roiSidebarLabel.setObjectName(u"roiSidebarLabel")
        self.roiSidebarLabel.setGeometry(QRect(0, 30, 341, 51))
        self.roiSidebarLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.roiSidebarLabel.setAlignment(Qt.AlignCenter)
        self.rfAnalysisSidebar = QFrame(self.sidebar)
        self.rfAnalysisSidebar.setObjectName(u"rfAnalysisSidebar")
        self.rfAnalysisSidebar.setGeometry(QRect(0, 480, 341, 121))
        self.rfAnalysisSidebar.setStyleSheet(u"QFrame {\n"
"	background-color:  rgb(49, 0, 124);\n"
"	border: 1px solid black;\n"
"}")
        self.rfAnalysisSidebar.setFrameShape(QFrame.StyledPanel)
        self.rfAnalysisSidebar.setFrameShadow(QFrame.Raised)
        self.rfAnalysisLabel = QLabel(self.rfAnalysisSidebar)
        self.rfAnalysisLabel.setObjectName(u"rfAnalysisLabel")
        self.rfAnalysisLabel.setGeometry(QRect(0, 30, 341, 51))
        self.rfAnalysisLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.rfAnalysisLabel.setAlignment(Qt.AlignCenter)
        self.ticAnalysisSidebar = QFrame(self.sidebar)
        self.ticAnalysisSidebar.setObjectName(u"ticAnalysisSidebar")
        self.ticAnalysisSidebar.setGeometry(QRect(0, 360, 341, 121))
        self.ticAnalysisSidebar.setStyleSheet(u"QFrame {\n"
"	background-color:  rgb(49, 0, 124);\n"
"	border: 1px solid black;\n"
"}")
        self.ticAnalysisSidebar.setFrameShape(QFrame.StyledPanel)
        self.ticAnalysisSidebar.setFrameShadow(QFrame.Raised)
        self.ticAnalysisLabel = QLabel(self.ticAnalysisSidebar)
        self.ticAnalysisLabel.setObjectName(u"ticAnalysisLabel")
        self.ticAnalysisLabel.setGeometry(QRect(0, 30, 341, 51))
        self.ticAnalysisLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.ticAnalysisLabel.setAlignment(Qt.AlignCenter)
        self.analysisParamsSidebar = QFrame(selectImage)
        self.analysisParamsSidebar.setObjectName(u"analysisParamsSidebar")
        self.analysisParamsSidebar.setGeometry(QRect(0, 240, 341, 121))
        self.analysisParamsSidebar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(49, 0, 124);\n"
"	border: 1px solid black;\n"
"}")
        self.analysisParamsSidebar.setFrameShape(QFrame.StyledPanel)
        self.analysisParamsSidebar.setFrameShadow(QFrame.Raised)
        self.analysisParamsLabel = QLabel(self.analysisParamsSidebar)
        self.analysisParamsLabel.setObjectName(u"analysisParamsLabel")
        self.analysisParamsLabel.setGeometry(QRect(0, 30, 341, 51))
        self.analysisParamsLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight:bold;\n"
"}")
        self.analysisParamsLabel.setAlignment(Qt.AlignCenter)
        self.backButton = QPushButton(selectImage)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 690, 131, 41))
        self.backButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")

        self.retranslateUi(selectImage)

        QMetaObject.connectSlotsByName(selectImage)
    # setupUi

    def retranslateUi(self, selectImage):
        selectImage.setWindowTitle(QCoreApplication.translate("selectImage", u"Select Ultrasound Image", None))
        self.selectDataLabel.setText(QCoreApplication.translate("selectImage", u"Select set of 3D Images to Analyze:", None))
        self.chooseNiftiImageFileButton.setText(QCoreApplication.translate("selectImage", u"Choose File", None))
        self.clearNiftiImageFileButton.setText(QCoreApplication.translate("selectImage", u"Clear Path", None))
        self.generateImageButton.setText(QCoreApplication.translate("selectImage", u"Generate Image", None))
        self.selectImageErrorMsg.setText(QCoreApplication.translate("selectImage", u"Error Msg", None))
#if QT_CONFIG(tooltip)
        self.selectNiftiImageOptionButton.setToolTip(QCoreApplication.translate("selectImage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.selectNiftiImageOptionButton.setText(QCoreApplication.translate("selectImage", u"NIFTI Format", None))
#if QT_CONFIG(tooltip)
        self.selectXmlFolderImageOptionButton.setToolTip(QCoreApplication.translate("selectImage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.selectXmlFolderImageOptionButton.setText(QCoreApplication.translate("selectImage", u"XML Folder", None))
        self.clearXmlImageFolderButton.setText(QCoreApplication.translate("selectImage", u"Clear Path", None))
        self.chooseXmlImageFolderButton.setText(QCoreApplication.translate("selectImage", u"Choose Folder", None))
        self.clearNiftiImageDestinationButton.setText(QCoreApplication.translate("selectImage", u"Clear Path", None))
        self.niftiImageDestinationButton.setText(QCoreApplication.translate("selectImage", u"Choose Folder", None))
        self.selectNiftiImageLabel.setText(QCoreApplication.translate("selectImage", u"Select NIFTI Image: (.nii,  .nii.gz)", None))
        self.imageBackButton.setText(QCoreApplication.translate("selectImage", u"Back", None))
        self.selectXmlFolderImageLabel.setText(QCoreApplication.translate("selectImage", u"Select XML Data Folder:", None))
        self.niftiDestinationImageLabel.setText(QCoreApplication.translate("selectImage", u"Destination for Converted NIFTI:", None))
#if QT_CONFIG(tooltip)
        self.sidebar.setToolTip(QCoreApplication.translate("selectImage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.imageSelectionLabelSidebar.setText(QCoreApplication.translate("selectImage", u"Image Selection:", None))
        self.imageLabel.setText(QCoreApplication.translate("selectImage", u"Image:", None))
        self.imageFilenameDisplay.setText(QCoreApplication.translate("selectImage", u"Sample filename ", None))
        self.roiSidebarLabel.setText(QCoreApplication.translate("selectImage", u"Volume of Interest (VOI) Selection", None))
        self.rfAnalysisLabel.setText(QCoreApplication.translate("selectImage", u"Export Results", None))
        self.ticAnalysisLabel.setText(QCoreApplication.translate("selectImage", u"Contrast-Enhanced Ultrasound\n"
"(CEUS) Analysis", None))
        self.analysisParamsLabel.setText(QCoreApplication.translate("selectImage", u"TIC Modification", None))
        self.backButton.setText(QCoreApplication.translate("selectImage", u"Back", None))
    # retranslateUi

