# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CeusMcTool2d/selectImage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_selectImage(object):
    def setupUi(self, selectImage):
        selectImage.setObjectName("selectImage")
        selectImage.resize(1175, 749)
        selectImage.setStyleSheet("QWidget {\n"
"    background: rgb(42, 42, 42);\n"
"}")
        self.selectDataLabel = QtWidgets.QLabel(selectImage)
        self.selectDataLabel.setGeometry(QtCore.QRect(540, 70, 431, 131))
        self.selectDataLabel.setStyleSheet("QLabel {\n"
"    font-size: 29px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectDataLabel.setTextFormat(QtCore.Qt.AutoText)
        self.selectDataLabel.setScaledContents(False)
        self.selectDataLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectDataLabel.setWordWrap(True)
        self.selectDataLabel.setObjectName("selectDataLabel")
        self.chooseSpreadsheetFileButton = QtWidgets.QPushButton(selectImage)
        self.chooseSpreadsheetFileButton.setGeometry(QtCore.QRect(622, 380, 131, 41))
        self.chooseSpreadsheetFileButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    background: rgb(90, 37, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.chooseSpreadsheetFileButton.setObjectName("chooseSpreadsheetFileButton")
        self.spreadsheetPath = QtWidgets.QLineEdit(selectImage)
        self.spreadsheetPath.setGeometry(QtCore.QRect(650, 330, 201, 31))
        self.spreadsheetPath.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(249, 249, 249);\n"
"    color: black;\n"
"}")
        self.spreadsheetPath.setObjectName("spreadsheetPath")
        self.clearSpreadsheetFileButton = QtWidgets.QPushButton(selectImage)
        self.clearSpreadsheetFileButton.setGeometry(QtCore.QRect(760, 380, 131, 41))
        self.clearSpreadsheetFileButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    background: rgb(90, 37, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.clearSpreadsheetFileButton.setObjectName("clearSpreadsheetFileButton")
        self.generateImageButton = QtWidgets.QPushButton(selectImage)
        self.generateImageButton.setGeometry(QtCore.QRect(760, 600, 131, 41))
        self.generateImageButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    background: rgb(90, 37, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.generateImageButton.setObjectName("generateImageButton")
        self.selectImageErrorMsg = QtWidgets.QLabel(selectImage)
        self.selectImageErrorMsg.setGeometry(QtCore.QRect(700, 660, 111, 41))
        self.selectImageErrorMsg.setStyleSheet("QLabel {\n"
"    color: rgb(255, 0, 23);\n"
"    font-size: 25px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectImageErrorMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.selectImageErrorMsg.setObjectName("selectImageErrorMsg")
        self.selectSpreadsheeetLabel = QtWidgets.QLabel(selectImage)
        self.selectSpreadsheeetLabel.setGeometry(QtCore.QRect(610, 250, 271, 51))
        self.selectSpreadsheeetLabel.setStyleSheet("QLabel {\n"
"    font-size: 18px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.selectSpreadsheeetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectSpreadsheeetLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.selectSpreadsheeetLabel.setObjectName("selectSpreadsheeetLabel")
        self.sidebar = QtWidgets.QWidget(selectImage)
        self.sidebar.setGeometry(QtCore.QRect(0, 0, 341, 751))
        self.sidebar.setStyleSheet("QWidget {\n"
"    background-color: rgb(28, 0, 101);\n"
"}")
        self.sidebar.setObjectName("sidebar")
        self.imageSelectionSidebar = QtWidgets.QFrame(self.sidebar)
        self.imageSelectionSidebar.setGeometry(QtCore.QRect(0, 0, 341, 121))
        self.imageSelectionSidebar.setStyleSheet("QFrame {\n"
"    background-color: rgb(99, 0, 174);\n"
"    border: 1px solid black;\n"
"}")
        self.imageSelectionSidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageSelectionSidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageSelectionSidebar.setObjectName("imageSelectionSidebar")
        self.imageSelectionLabelSidebar = QtWidgets.QLabel(self.imageSelectionSidebar)
        self.imageSelectionLabelSidebar.setGeometry(QtCore.QRect(70, 0, 191, 51))
        self.imageSelectionLabelSidebar.setStyleSheet("QLabel {\n"
"    font-size: 21px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 0px;\n"
"    font-weight: bold;\n"
"}")
        self.imageSelectionLabelSidebar.setAlignment(QtCore.Qt.AlignCenter)
        self.imageSelectionLabelSidebar.setObjectName("imageSelectionLabelSidebar")
        self.imageLabel = QtWidgets.QLabel(self.imageSelectionSidebar)
        self.imageLabel.setGeometry(QtCore.QRect(-60, 50, 191, 51))
        self.imageLabel.setStyleSheet("QLabel {\n"
"    font-size: 16px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 0px;\n"
"    font-weight: bold;\n"
"}")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.imageFilenameDisplay = QtWidgets.QLabel(self.imageSelectionSidebar)
        self.imageFilenameDisplay.setGeometry(QtCore.QRect(100, 50, 241, 51))
        self.imageFilenameDisplay.setStyleSheet("QLabel {\n"
"    font-size: 14px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 0px;\n"
"}")
        self.imageFilenameDisplay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.imageFilenameDisplay.setObjectName("imageFilenameDisplay")
        self.roiSidebar = QtWidgets.QFrame(self.sidebar)
        self.roiSidebar.setGeometry(QtCore.QRect(0, 120, 341, 121))
        self.roiSidebar.setStyleSheet("QFrame {\n"
"    background-color: rgb(49, 0, 124);\n"
"    border: 1px solid black;\n"
"}")
        self.roiSidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roiSidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roiSidebar.setObjectName("roiSidebar")
        self.roiSidebarLabel = QtWidgets.QLabel(self.roiSidebar)
        self.roiSidebarLabel.setGeometry(QtCore.QRect(0, 30, 341, 51))
        self.roiSidebarLabel.setStyleSheet("QLabel {\n"
"    font-size: 21px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 0px;\n"
"    font-weight: bold;\n"
"}")
        self.roiSidebarLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.roiSidebarLabel.setObjectName("roiSidebarLabel")
        self.rfAnalysisSidebar = QtWidgets.QFrame(self.sidebar)
        self.rfAnalysisSidebar.setGeometry(QtCore.QRect(0, 480, 341, 121))
        self.rfAnalysisSidebar.setStyleSheet("QFrame {\n"
"    background-color:  rgb(49, 0, 124);\n"
"    border: 1px solid black;\n"
"}")
        self.rfAnalysisSidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rfAnalysisSidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rfAnalysisSidebar.setObjectName("rfAnalysisSidebar")
        self.rfAnalysisLabel = QtWidgets.QLabel(self.rfAnalysisSidebar)
        self.rfAnalysisLabel.setGeometry(QtCore.QRect(0, 30, 341, 51))
        self.rfAnalysisLabel.setStyleSheet("QLabel {\n"
"    font-size: 21px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 0px;\n"
"    font-weight: bold;\n"
"}")
        self.rfAnalysisLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rfAnalysisLabel.setObjectName("rfAnalysisLabel")
        self.ticAnalysisSidebar = QtWidgets.QFrame(self.sidebar)
        self.ticAnalysisSidebar.setGeometry(QtCore.QRect(0, 360, 341, 121))
        self.ticAnalysisSidebar.setStyleSheet("QFrame {\n"
"    background-color:  rgb(49, 0, 124);\n"
"    border: 1px solid black;\n"
"}")
        self.ticAnalysisSidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ticAnalysisSidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ticAnalysisSidebar.setObjectName("ticAnalysisSidebar")
        self.ticAnalysisLabel = QtWidgets.QLabel(self.ticAnalysisSidebar)
        self.ticAnalysisLabel.setGeometry(QtCore.QRect(0, 30, 341, 51))
        self.ticAnalysisLabel.setStyleSheet("QLabel {\n"
"    font-size: 21px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 0px;\n"
"    font-weight: bold;\n"
"}")
        self.ticAnalysisLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ticAnalysisLabel.setObjectName("ticAnalysisLabel")
        self.analysisParamsSidebar = QtWidgets.QFrame(selectImage)
        self.analysisParamsSidebar.setGeometry(QtCore.QRect(0, 240, 341, 121))
        self.analysisParamsSidebar.setStyleSheet("QFrame {\n"
"    background-color: rgb(49, 0, 124);\n"
"    border: 1px solid black;\n"
"}")
        self.analysisParamsSidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analysisParamsSidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analysisParamsSidebar.setObjectName("analysisParamsSidebar")
        self.analysisParamsLabel = QtWidgets.QLabel(self.analysisParamsSidebar)
        self.analysisParamsLabel.setGeometry(QtCore.QRect(0, 30, 341, 51))
        self.analysisParamsLabel.setStyleSheet("QLabel {\n"
"    font-size: 21px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 0px;\n"
"    font-weight:bold;\n"
"}")
        self.analysisParamsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.analysisParamsLabel.setObjectName("analysisParamsLabel")
        self.backButton = QtWidgets.QPushButton(selectImage)
        self.backButton.setGeometry(QtCore.QRect(10, 690, 131, 41))
        self.backButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    background: rgb(90, 37, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.backButton.setObjectName("backButton")
        self.findImagesButton = QtWidgets.QPushButton(selectImage)
        self.findImagesButton.setGeometry(QtCore.QRect(690, 500, 131, 41))
        self.findImagesButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    background: rgb(90, 37, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.findImagesButton.setObjectName("findImagesButton")
        self.undoSpreadsheetButton = QtWidgets.QPushButton(selectImage)
        self.undoSpreadsheetButton.setGeometry(QtCore.QRect(610, 600, 131, 41))
        self.undoSpreadsheetButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    background: rgb(90, 37, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.undoSpreadsheetButton.setObjectName("undoSpreadsheetButton")
        self.imagesScrollArea = QtWidgets.QTableWidget(selectImage)
        self.imagesScrollArea.setGeometry(QtCore.QRect(550, 210, 421, 331))
        self.imagesScrollArea.setStyleSheet(" QTableWidget {\n"
"        background-color: black; \n"
"        border-radius: 10px;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"    Background-color:white;\n"
"    font-size: 15px;\n"
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
        self.imagesScrollArea.setObjectName("imagesScrollArea")
        item = QtWidgets.QTableWidgetItem()
        self.imagesScrollArea.setHorizontalHeaderItem(0, item)
        self.imagesScrollArea.horizontalHeader().setCascadingSectionResizes(False)

        self.retranslateUi(selectImage)
        QtCore.QMetaObject.connectSlotsByName(selectImage)

    def retranslateUi(self, selectImage):
        _translate = QtCore.QCoreApplication.translate
        selectImage.setWindowTitle(_translate("selectImage", "Select Ultrasound Image"))
        self.selectDataLabel.setText(_translate("selectImage", "Select set of 2D Images to Analyze:"))
        self.chooseSpreadsheetFileButton.setText(_translate("selectImage", "Choose File"))
        self.clearSpreadsheetFileButton.setText(_translate("selectImage", "Clear Path"))
        self.generateImageButton.setText(_translate("selectImage", "Generate Image"))
        self.selectImageErrorMsg.setText(_translate("selectImage", "Error Msg"))
        self.selectSpreadsheeetLabel.setText(_translate("selectImage", "Select Excel Spreadsheet: (.xlsx)"))
        self.sidebar.setToolTip(_translate("selectImage", "<html><head/><body><p><br/></p></body></html>"))
        self.imageSelectionLabelSidebar.setText(_translate("selectImage", "Image Selection:"))
        self.imageLabel.setText(_translate("selectImage", "Image:"))
        self.imageFilenameDisplay.setText(_translate("selectImage", "Sample filename "))
        self.roiSidebarLabel.setText(_translate("selectImage", "Region of Interest (ROI) Selection"))
        self.rfAnalysisLabel.setText(_translate("selectImage", "Export Results"))
        self.ticAnalysisLabel.setText(_translate("selectImage", "Contrast-Enhanced Ultrasound\n"
"(CEUS) Analysis"))
        self.analysisParamsLabel.setText(_translate("selectImage", "TIC Modification"))
        self.backButton.setText(_translate("selectImage", "Back"))
        self.findImagesButton.setText(_translate("selectImage", "Find Images"))
        self.undoSpreadsheetButton.setText(_translate("selectImage", "Undo"))
        item = self.imagesScrollArea.horizontalHeaderItem(0)
        item.setText(_translate("selectImage", "Scan"))
