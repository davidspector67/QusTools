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
        self.selectDataLabel.setGeometry(QRect(540, 100, 431, 131))
        self.selectDataLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 29px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectDataLabel.setTextFormat(Qt.AutoText)
        self.selectDataLabel.setScaledContents(False)
        self.selectDataLabel.setAlignment(Qt.AlignCenter)
        self.selectDataLabel.setWordWrap(True)
        self.phantomPathLabelVerasonics = QLabel(selectImage)
        self.phantomPathLabelVerasonics.setObjectName(u"phantomPathLabelVerasonics")
        self.phantomPathLabelVerasonics.setGeometry(QRect(790, 290, 271, 51))
        self.phantomPathLabelVerasonics.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: white;\n"
"	font-size: 17px;\n"
"}")
        self.phantomPathLabelVerasonics.setAlignment(Qt.AlignCenter)
        self.phantomPathLabelVerasonics.setTextInteractionFlags(Qt.NoTextInteraction)
        self.choosePhantomFileButton = QPushButton(selectImage)
        self.choosePhantomFileButton.setObjectName(u"choosePhantomFileButton")
        self.choosePhantomFileButton.setGeometry(QRect(792, 390, 131, 41))
        self.choosePhantomFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.phantomPathInput = QLineEdit(selectImage)
        self.phantomPathInput.setObjectName(u"phantomPathInput")
        self.phantomPathInput.setGeometry(QRect(820, 350, 201, 31))
        self.phantomPathInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.clearPhantomPathButton = QPushButton(selectImage)
        self.clearPhantomPathButton.setObjectName(u"clearPhantomPathButton")
        self.clearPhantomPathButton.setGeometry(QRect(930, 390, 131, 41))
        self.clearPhantomPathButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.imagePathLabelVerasonics = QLabel(selectImage)
        self.imagePathLabelVerasonics.setObjectName(u"imagePathLabelVerasonics")
        self.imagePathLabelVerasonics.setGeometry(QRect(440, 290, 271, 51))
        self.imagePathLabelVerasonics.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: white;\n"
"	font-size: 17px;\n"
"}")
        self.imagePathLabelVerasonics.setAlignment(Qt.AlignCenter)
        self.imagePathLabelVerasonics.setTextInteractionFlags(Qt.NoTextInteraction)
        self.chooseImageFileButton = QPushButton(selectImage)
        self.chooseImageFileButton.setObjectName(u"chooseImageFileButton")
        self.chooseImageFileButton.setGeometry(QRect(442, 390, 131, 41))
        self.chooseImageFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.imagePathInput = QLineEdit(selectImage)
        self.imagePathInput.setObjectName(u"imagePathInput")
        self.imagePathInput.setGeometry(QRect(470, 350, 201, 31))
        self.imagePathInput.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.clearImagePathButton = QPushButton(selectImage)
        self.clearImagePathButton.setObjectName(u"clearImagePathButton")
        self.clearImagePathButton.setGeometry(QRect(580, 390, 131, 41))
        self.clearImagePathButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.generateImageButton = QPushButton(selectImage)
        self.generateImageButton.setObjectName(u"generateImageButton")
        self.generateImageButton.setGeometry(QRect(690, 510, 131, 41))
        self.generateImageButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.selectImageErrorMsg = QLabel(selectImage)
        self.selectImageErrorMsg.setObjectName(u"selectImageErrorMsg")
        self.selectImageErrorMsg.setGeometry(QRect(550, 590, 421, 81))
        self.selectImageErrorMsg.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 0, 23);\n"
"	font-size: 20px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectImageErrorMsg.setAlignment(Qt.AlignCenter)
        self.choosePhantomFolderButton = QPushButton(selectImage)
        self.choosePhantomFolderButton.setObjectName(u"choosePhantomFolderButton")
        self.choosePhantomFolderButton.setGeometry(QRect(790, 390, 131, 41))
        self.choosePhantomFolderButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.chooseImageFolderButton = QPushButton(selectImage)
        self.chooseImageFolderButton.setObjectName(u"chooseImageFolderButton")
        self.chooseImageFolderButton.setGeometry(QRect(440, 390, 131, 41))
        self.chooseImageFolderButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.selectImageMethodLabel = QLabel(selectImage)
        self.selectImageMethodLabel.setObjectName(u"selectImageMethodLabel")
        self.selectImageMethodLabel.setGeometry(QRect(540, 170, 431, 131))
        self.selectImageMethodLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 29px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectImageMethodLabel.setTextFormat(Qt.AutoText)
        self.selectImageMethodLabel.setScaledContents(False)
        self.selectImageMethodLabel.setAlignment(Qt.AlignCenter)
        self.selectImageMethodLabel.setWordWrap(True)
        self.canonButton = QPushButton(selectImage)
        self.canonButton.setObjectName(u"canonButton")
        self.canonButton.setGeometry(QRect(590, 340, 301, 51))
        self.canonButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
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
        self.imageLabel.setGeometry(QRect(-60, 40, 191, 51))
        self.imageLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 16px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.phantomLabel = QLabel(self.imageSelectionSidebar)
        self.phantomLabel.setObjectName(u"phantomLabel")
        self.phantomLabel.setGeometry(QRect(-50, 70, 191, 51))
        self.phantomLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 16px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold\n"
"}")
        self.phantomLabel.setAlignment(Qt.AlignCenter)
        self.imageFilenameDisplay = QLabel(self.imageSelectionSidebar)
        self.imageFilenameDisplay.setObjectName(u"imageFilenameDisplay")
        self.imageFilenameDisplay.setGeometry(QRect(100, 40, 241, 51))
        self.imageFilenameDisplay.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"}")
        self.imageFilenameDisplay.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.phantomFilenameDisplay = QLabel(self.imageSelectionSidebar)
        self.phantomFilenameDisplay.setObjectName(u"phantomFilenameDisplay")
        self.phantomFilenameDisplay.setGeometry(QRect(100, 70, 241, 51))
        self.phantomFilenameDisplay.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"}")
        self.phantomFilenameDisplay.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
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
        self.roiSidebarLabel.setGeometry(QRect(0, 40, 341, 51))
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
        self.rfAnalysisSidebar.setGeometry(QRect(0, 360, 341, 121))
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
        self.exportResultsSidebar = QFrame(self.sidebar)
        self.exportResultsSidebar.setObjectName(u"exportResultsSidebar")
        self.exportResultsSidebar.setGeometry(QRect(0, 480, 341, 121))
        self.exportResultsSidebar.setStyleSheet(u"QFrame {\n"
"	background-color:  rgb(49, 0, 124);\n"
"	border: 1px solid black;\n"
"}")
        self.exportResultsSidebar.setFrameShape(QFrame.StyledPanel)
        self.exportResultsSidebar.setFrameShadow(QFrame.Raised)
        self.exportResultsLabel = QLabel(self.exportResultsSidebar)
        self.exportResultsLabel.setObjectName(u"exportResultsLabel")
        self.exportResultsLabel.setGeometry(QRect(20, 30, 301, 51))
        self.exportResultsLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.exportResultsLabel.setAlignment(Qt.AlignCenter)
        self.backButton = QPushButton(self.sidebar)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 690, 131, 41))
        self.backButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
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
        self.verasonicsButton = QPushButton(selectImage)
        self.verasonicsButton.setObjectName(u"verasonicsButton")
        self.verasonicsButton.setGeometry(QRect(590, 460, 301, 51))
        self.verasonicsButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.imagePathLabelCanon = QLabel(selectImage)
        self.imagePathLabelCanon.setObjectName(u"imagePathLabelCanon")
        self.imagePathLabelCanon.setGeometry(QRect(440, 290, 271, 51))
        self.imagePathLabelCanon.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: white;\n"
"	font-size: 17px;\n"
"}")
        self.imagePathLabelCanon.setAlignment(Qt.AlignCenter)
        self.imagePathLabelCanon.setTextInteractionFlags(Qt.NoTextInteraction)
        self.phantomPathLabelCanon = QLabel(selectImage)
        self.phantomPathLabelCanon.setObjectName(u"phantomPathLabelCanon")
        self.phantomPathLabelCanon.setGeometry(QRect(790, 290, 271, 51))
        self.phantomPathLabelCanon.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: white;\n"
"	font-size: 17px;\n"
"}")
        self.phantomPathLabelCanon.setAlignment(Qt.AlignCenter)
        self.phantomPathLabelCanon.setTextInteractionFlags(Qt.NoTextInteraction)

        self.retranslateUi(selectImage)

        QMetaObject.connectSlotsByName(selectImage)
    # setupUi

    def retranslateUi(self, selectImage):
        selectImage.setWindowTitle(QCoreApplication.translate("selectImage", u"Select Ultrasound Image", None))
        self.selectDataLabel.setText(QCoreApplication.translate("selectImage", u"Select Data and Phantom Files to Generate Ultrasound Image:", None))
        self.phantomPathLabelVerasonics.setText(QCoreApplication.translate("selectImage", u"Input Path to Phantom file (.mat)", None))
        self.choosePhantomFileButton.setText(QCoreApplication.translate("selectImage", u"Choose File", None))
        self.clearPhantomPathButton.setText(QCoreApplication.translate("selectImage", u"Clear Path", None))
        self.imagePathLabelVerasonics.setText(QCoreApplication.translate("selectImage", u"Input Path to Image file (.mat)", None))
        self.chooseImageFileButton.setText(QCoreApplication.translate("selectImage", u"Choose File", None))
        self.clearImagePathButton.setText(QCoreApplication.translate("selectImage", u"Clear Path", None))
        self.generateImageButton.setText(QCoreApplication.translate("selectImage", u"Generate Image", None))
        self.selectImageErrorMsg.setText(QCoreApplication.translate("selectImage", u"ERROR: At least one dimension of phantom data\n"
"smaller than corresponding dimension\n"
"of image data", None))
        self.choosePhantomFolderButton.setText(QCoreApplication.translate("selectImage", u"Choose Folder", None))
        self.chooseImageFolderButton.setText(QCoreApplication.translate("selectImage", u"Choose Folder", None))
        self.selectImageMethodLabel.setText(QCoreApplication.translate("selectImage", u"Select Transducer Brand:", None))
#if QT_CONFIG(tooltip)
        self.canonButton.setToolTip(QCoreApplication.translate("selectImage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.canonButton.setText(QCoreApplication.translate("selectImage", u"Canon", None))
#if QT_CONFIG(tooltip)
        self.sidebar.setToolTip(QCoreApplication.translate("selectImage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.imageSelectionLabelSidebar.setText(QCoreApplication.translate("selectImage", u"Image Selection:", None))
        self.imageLabel.setText(QCoreApplication.translate("selectImage", u"Image:", None))
        self.phantomLabel.setText(QCoreApplication.translate("selectImage", u"Phantom:", None))
        self.imageFilenameDisplay.setText(QCoreApplication.translate("selectImage", u"Sample filename ", None))
        self.phantomFilenameDisplay.setText(QCoreApplication.translate("selectImage", u"Sample filename ", None))
        self.roiSidebarLabel.setText(QCoreApplication.translate("selectImage", u"Region of Interest (ROI) Selection", None))
        self.rfAnalysisLabel.setText(QCoreApplication.translate("selectImage", u"Radio Frequency Data Analysis", None))
        self.exportResultsLabel.setText(QCoreApplication.translate("selectImage", u"Export Results", None))
        self.backButton.setText(QCoreApplication.translate("selectImage", u"Back", None))
        self.analysisParamsLabel.setText(QCoreApplication.translate("selectImage", u"Analysis Parameter Selection", None))
#if QT_CONFIG(tooltip)
        self.verasonicsButton.setToolTip(QCoreApplication.translate("selectImage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.verasonicsButton.setText(QCoreApplication.translate("selectImage", u"Verasonics", None))
        self.imagePathLabelCanon.setText(QCoreApplication.translate("selectImage", u"Input Path to Image file (.bin)", None))
        self.phantomPathLabelCanon.setText(QCoreApplication.translate("selectImage", u"Input Path to Phantom file (.bin)", None))
    # retranslateUi

