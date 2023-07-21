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
        self.chooseSpreadsheetFileButton = QPushButton(selectImage)
        self.chooseSpreadsheetFileButton.setObjectName(u"chooseSpreadsheetFileButton")
        self.chooseSpreadsheetFileButton.setGeometry(QRect(622, 380, 131, 41))
        self.chooseSpreadsheetFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.spreadsheetPath = QLineEdit(selectImage)
        self.spreadsheetPath.setObjectName(u"spreadsheetPath")
        self.spreadsheetPath.setGeometry(QRect(650, 330, 201, 31))
        self.spreadsheetPath.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(249, 249, 249);\n"
"	color: black;\n"
"}")
        self.clearSpreadsheetFileButton = QPushButton(selectImage)
        self.clearSpreadsheetFileButton.setObjectName(u"clearSpreadsheetFileButton")
        self.clearSpreadsheetFileButton.setGeometry(QRect(760, 380, 131, 41))
        self.clearSpreadsheetFileButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.generateImageButton = QPushButton(selectImage)
        self.generateImageButton.setObjectName(u"generateImageButton")
        self.generateImageButton.setGeometry(QRect(760, 600, 131, 41))
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
        self.selectSpreadsheeetLabel = QLabel(selectImage)
        self.selectSpreadsheeetLabel.setObjectName(u"selectSpreadsheeetLabel")
        self.selectSpreadsheeetLabel.setGeometry(QRect(610, 250, 271, 51))
        self.selectSpreadsheeetLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectSpreadsheeetLabel.setAlignment(Qt.AlignCenter)
        self.selectSpreadsheeetLabel.setTextInteractionFlags(Qt.NoTextInteraction)
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
        self.findImagesButton = QPushButton(selectImage)
        self.findImagesButton.setObjectName(u"findImagesButton")
        self.findImagesButton.setGeometry(QRect(690, 500, 131, 41))
        self.findImagesButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.undoSpreadsheetButton = QPushButton(selectImage)
        self.undoSpreadsheetButton.setObjectName(u"undoSpreadsheetButton")
        self.undoSpreadsheetButton.setGeometry(QRect(610, 600, 131, 41))
        self.undoSpreadsheetButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.imagesScrollArea = QTableWidget(selectImage)
        if (self.imagesScrollArea.columnCount() < 1):
            self.imagesScrollArea.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.imagesScrollArea.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.imagesScrollArea.setObjectName(u"imagesScrollArea")
        self.imagesScrollArea.setGeometry(QRect(550, 210, 421, 331))
        self.imagesScrollArea.setStyleSheet(u" QTableWidget {\n"
"        background-color: black; \n"
"        border-radius: 10px;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	Background-color:white;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"        color: black;                    \n"
"        background-color: grey;\n"
"    }\n"
"\n"
"    QTableWidget::item:selected {\n"
"        background-color: blue;\n"
"        color: white;\n"
"    }")
        self.imagesScrollArea.setRowCount(0)
        self.imagesScrollArea.setColumnCount(1)
        self.imagesScrollArea.horizontalHeader().setCascadingSectionResizes(False)

        self.retranslateUi(selectImage)

        QMetaObject.connectSlotsByName(selectImage)
    # setupUi

    def retranslateUi(self, selectImage):
        selectImage.setWindowTitle(QCoreApplication.translate("selectImage", u"Select Ultrasound Image", None))
        self.selectDataLabel.setText(QCoreApplication.translate("selectImage", u"Select set of 2D Images to Analyze:", None))
        self.chooseSpreadsheetFileButton.setText(QCoreApplication.translate("selectImage", u"Choose File", None))
        self.clearSpreadsheetFileButton.setText(QCoreApplication.translate("selectImage", u"Clear Path", None))
        self.generateImageButton.setText(QCoreApplication.translate("selectImage", u"Generate Image", None))
        self.selectImageErrorMsg.setText(QCoreApplication.translate("selectImage", u"Error Msg", None))
        self.selectSpreadsheeetLabel.setText(QCoreApplication.translate("selectImage", u"Select Excel Spreadsheet: (.xlsx)", None))
#if QT_CONFIG(tooltip)
        self.sidebar.setToolTip(QCoreApplication.translate("selectImage", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.imageSelectionLabelSidebar.setText(QCoreApplication.translate("selectImage", u"Image Selection:", None))
        self.imageLabel.setText(QCoreApplication.translate("selectImage", u"Image:", None))
        self.imageFilenameDisplay.setText(QCoreApplication.translate("selectImage", u"Sample filename ", None))
        self.roiSidebarLabel.setText(QCoreApplication.translate("selectImage", u"Region of Interest (ROI) Selection", None))
        self.rfAnalysisLabel.setText(QCoreApplication.translate("selectImage", u"Export Results", None))
        self.ticAnalysisLabel.setText(QCoreApplication.translate("selectImage", u"Contrast-Enhanced Ultrasound\n"
"(CEUS) Analysis", None))
        self.analysisParamsLabel.setText(QCoreApplication.translate("selectImage", u"TIC Modification", None))
        self.backButton.setText(QCoreApplication.translate("selectImage", u"Back", None))
        self.findImagesButton.setText(QCoreApplication.translate("selectImage", u"Find Images", None))
        self.undoSpreadsheetButton.setText(QCoreApplication.translate("selectImage", u"Undo", None))
        ___qtablewidgetitem = self.imagesScrollArea.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("selectImage", u"Scan", None));
    # retranslateUi

