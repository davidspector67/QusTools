# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'roiSelection copy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ceusAnalysis(object):
    def setupUi(self, ceusAnalysis):
        if not ceusAnalysis.objectName():
            ceusAnalysis.setObjectName(u"ceusAnalysis")
        ceusAnalysis.resize(1175, 749)
        ceusAnalysis.setStyleSheet(u"QWidget {\n"
"	background: rgb(42, 42, 42);\n"
"}")
        self.axialPlaneLabel = QLabel(ceusAnalysis)
        self.axialPlaneLabel.setObjectName(u"axialPlaneLabel")
        self.axialPlaneLabel.setGeometry(QRect(410, 100, 271, 51))
        self.axialPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.axialPlaneLabel.setAlignment(Qt.AlignCenter)
        self.axialPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sagittalPlaneLabel = QLabel(ceusAnalysis)
        self.sagittalPlaneLabel.setObjectName(u"sagittalPlaneLabel")
        self.sagittalPlaneLabel.setGeometry(QRect(830, 100, 271, 51))
        self.sagittalPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.sagittalPlaneLabel.setAlignment(Qt.AlignCenter)
        self.sagittalPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.curSliceLabel = QLabel(ceusAnalysis)
        self.curSliceLabel.setObjectName(u"curSliceLabel")
        self.curSliceLabel.setGeometry(QRect(300, 530, 361, 51))
        self.curSliceLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceLabel.setTextFormat(Qt.AutoText)
        self.curSliceLabel.setScaledContents(False)
        self.curSliceLabel.setAlignment(Qt.AlignCenter)
        self.curSliceLabel.setWordWrap(True)
        self.curSliceSlider = QSlider(ceusAnalysis)
        self.curSliceSlider.setObjectName(u"curSliceSlider")
        self.curSliceSlider.setGeometry(QRect(380, 590, 191, 41))
        self.curSliceSlider.setOrientation(Qt.Horizontal)
        self.curSliceOfLabel = QLabel(ceusAnalysis)
        self.curSliceOfLabel.setObjectName(u"curSliceOfLabel")
        self.curSliceOfLabel.setGeometry(QRect(455, 650, 41, 31))
        self.curSliceOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceOfLabel.setAlignment(Qt.AlignCenter)
        self.curSliceOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sidebar = QWidget(ceusAnalysis)
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
        self.imagePathInput = QLabel(self.imageSelectionSidebar)
        self.imagePathInput.setObjectName(u"imagePathInput")
        self.imagePathInput.setGeometry(QRect(100, 50, 241, 51))
        self.imagePathInput.setStyleSheet(u"QLabel {\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"}")
        self.imagePathInput.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.roiSidebar = QFrame(self.sidebar)
        self.roiSidebar.setObjectName(u"roiSidebar")
        self.roiSidebar.setGeometry(QRect(0, 120, 341, 121))
        self.roiSidebar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(99, 0, 174);\n"
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
        self.analysisParamsSidebar = QFrame(ceusAnalysis)
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
        self.bmodePlane = QLabel(ceusAnalysis)
        self.bmodePlane.setObjectName(u"bmodePlane")
        self.bmodePlane.setGeometry(QRect(360, 150, 381, 351))
        self.bmodeMaskLayer = QLabel(ceusAnalysis)
        self.bmodeMaskLayer.setObjectName(u"bmodeMaskLayer")
        self.bmodeMaskLayer.setGeometry(QRect(360, 150, 381, 351))
        self.bmodeMaskLayer.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.cePlane = QLabel(ceusAnalysis)
        self.cePlane.setObjectName(u"cePlane")
        self.cePlane.setGeometry(QRect(770, 150, 381, 351))
        self.mcBmodeDisplayLabel = QLabel(ceusAnalysis)
        self.mcBmodeDisplayLabel.setObjectName(u"mcBmodeDisplayLabel")
        self.mcBmodeDisplayLabel.setGeometry(QRect(360, 150, 381, 351))
        self.mcBmodeDisplayLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.ceMaskLayer = QLabel(ceusAnalysis)
        self.ceMaskLayer.setObjectName(u"ceMaskLayer")
        self.ceMaskLayer.setGeometry(QRect(770, 150, 381, 351))
        self.ceMaskLayer.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.mcCeDisplayLabel = QLabel(ceusAnalysis)
        self.mcCeDisplayLabel.setObjectName(u"mcCeDisplayLabel")
        self.mcCeDisplayLabel.setGeometry(QRect(770, 150, 381, 351))
        self.mcCeDisplayLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.backButton = QPushButton(ceusAnalysis)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 690, 131, 41))
        self.backButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.curSliceSpinBox = QSpinBox(ceusAnalysis)
        self.curSliceSpinBox.setObjectName(u"curSliceSpinBox")
        self.curSliceSpinBox.setGeometry(QRect(410, 655, 48, 24))
        self.curSliceSpinBox.setStyleSheet(u"QSpinBox {\n"
"	background: white;\n"
"	color: black;\n"
"}")
        self.curSliceOfLabel_2 = QLabel(ceusAnalysis)
        self.curSliceOfLabel_2.setObjectName(u"curSliceOfLabel_2")
        self.curSliceOfLabel_2.setGeometry(QRect(410, 700, 41, 31))
        self.curSliceOfLabel_2.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceOfLabel_2.setAlignment(Qt.AlignCenter)
        self.curSliceOfLabel_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.totalSecondsLabel = QLabel(ceusAnalysis)
        self.totalSecondsLabel.setObjectName(u"totalSecondsLabel")
        self.totalSecondsLabel.setGeometry(QRect(445, 700, 61, 31))
        self.totalSecondsLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.totalSecondsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.totalSecondsLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.curSecondLabel = QLabel(ceusAnalysis)
        self.curSecondLabel.setObjectName(u"curSecondLabel")
        self.curSecondLabel.setGeometry(QRect(350, 700, 61, 31))
        self.curSecondLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSecondLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.curSecondLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.secondsLabel = QLabel(ceusAnalysis)
        self.secondsLabel.setObjectName(u"secondsLabel")
        self.secondsLabel.setGeometry(QRect(510, 700, 81, 31))
        self.secondsLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.secondsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.secondsLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.constructRoiLabel = QLabel(ceusAnalysis)
        self.constructRoiLabel.setObjectName(u"constructRoiLabel")
        self.constructRoiLabel.setGeometry(QRect(540, -10, 431, 131))
        self.constructRoiLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 29px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.constructRoiLabel.setTextFormat(Qt.AutoText)
        self.constructRoiLabel.setScaledContents(False)
        self.constructRoiLabel.setAlignment(Qt.AlignCenter)
        self.constructRoiLabel.setWordWrap(True)
        self.bmodeCoverLabel = QLabel(ceusAnalysis)
        self.bmodeCoverLabel.setObjectName(u"bmodeCoverLabel")
        self.bmodeCoverLabel.setGeometry(QRect(360, 150, 381, 351))
        self.bmodeCoverLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.ceCoverLabel = QLabel(ceusAnalysis)
        self.ceCoverLabel.setObjectName(u"ceCoverLabel")
        self.ceCoverLabel.setGeometry(QRect(770, 150, 381, 351))
        self.ceCoverLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.peVal = QLabel(ceusAnalysis)
        self.peVal.setObjectName(u"peVal")
        self.peVal.setGeometry(QRect(1100, 560, 51, 51))
        font = QFont()
        font.setPointSize(14)
        self.peVal.setFont(font)
        self.peVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.peVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tpLabel = QLabel(ceusAnalysis)
        self.tpLabel.setObjectName(u"tpLabel")
        self.tpLabel.setGeometry(QRect(1040, 600, 91, 51))
        self.tpLabel.setFont(font)
        self.tpLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tpLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.voiVolumeVal = QLabel(ceusAnalysis)
        self.voiVolumeVal.setObjectName(u"voiVolumeVal")
        self.voiVolumeVal.setGeometry(QRect(1100, 650, 151, 51))
        self.voiVolumeVal.setFont(font)
        self.voiVolumeVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.voiVolumeVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mttLabel = QLabel(ceusAnalysis)
        self.mttLabel.setObjectName(u"mttLabel")
        self.mttLabel.setGeometry(QRect(1040, 580, 81, 51))
        self.mttLabel.setFont(font)
        self.mttLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.mttLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tpVal = QLabel(ceusAnalysis)
        self.tpVal.setObjectName(u"tpVal")
        self.tpVal.setGeometry(QRect(1100, 600, 51, 51))
        self.tpVal.setFont(font)
        self.tpVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tpVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.voiVolumeLabel = QLabel(ceusAnalysis)
        self.voiVolumeLabel.setObjectName(u"voiVolumeLabel")
        self.voiVolumeLabel.setGeometry(QRect(1040, 640, 71, 71))
        self.voiVolumeLabel.setFont(font)
        self.voiVolumeLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.voiVolumeLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tmppvLabel = QLabel(ceusAnalysis)
        self.tmppvLabel.setObjectName(u"tmppvLabel")
        self.tmppvLabel.setGeometry(QRect(1040, 620, 71, 51))
        self.tmppvLabel.setFont(font)
        self.tmppvLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tmppvLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ticDisplay = QFrame(ceusAnalysis)
        self.ticDisplay.setObjectName(u"ticDisplay")
        self.ticDisplay.setGeometry(QRect(620, 560, 401, 171))
        self.ticDisplay.setFrameShape(QFrame.StyledPanel)
        self.ticDisplay.setFrameShadow(QFrame.Raised)
        self.aucVal = QLabel(ceusAnalysis)
        self.aucVal.setObjectName(u"aucVal")
        self.aucVal.setGeometry(QRect(1100, 540, 51, 51))
        self.aucVal.setFont(font)
        self.aucVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.aucVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.peLabel = QLabel(ceusAnalysis)
        self.peLabel.setObjectName(u"peLabel")
        self.peLabel.setGeometry(QRect(1040, 560, 91, 51))
        self.peLabel.setFont(font)
        self.peLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.peLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.resultsLabel = QLabel(ceusAnalysis)
        self.resultsLabel.setObjectName(u"resultsLabel")
        self.resultsLabel.setGeometry(QRect(670, 510, 361, 51))
        self.resultsLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.resultsLabel.setTextFormat(Qt.AutoText)
        self.resultsLabel.setScaledContents(False)
        self.resultsLabel.setAlignment(Qt.AlignCenter)
        self.resultsLabel.setWordWrap(True)
        self.tmmpVal = QLabel(ceusAnalysis)
        self.tmmpVal.setObjectName(u"tmmpVal")
        self.tmmpVal.setGeometry(QRect(1100, 620, 71, 51))
        self.tmmpVal.setFont(font)
        self.tmmpVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tmmpVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mttVal = QLabel(ceusAnalysis)
        self.mttVal.setObjectName(u"mttVal")
        self.mttVal.setGeometry(QRect(1100, 580, 51, 51))
        self.mttVal.setFont(font)
        self.mttVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.mttVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.aucLabel = QLabel(ceusAnalysis)
        self.aucLabel.setObjectName(u"aucLabel")
        self.aucLabel.setGeometry(QRect(1040, 540, 81, 51))
        self.aucLabel.setFont(font)
        self.aucLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.aucLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.curSliceTotal = QLabel(ceusAnalysis)
        self.curSliceTotal.setObjectName(u"curSliceTotal")
        self.curSliceTotal.setGeometry(QRect(490, 650, 61, 31))
        self.curSliceTotal.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceTotal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.curSliceTotal.setTextInteractionFlags(Qt.NoTextInteraction)

        self.retranslateUi(ceusAnalysis)

        QMetaObject.connectSlotsByName(ceusAnalysis)
    # setupUi

    def retranslateUi(self, ceusAnalysis):
        ceusAnalysis.setWindowTitle(QCoreApplication.translate("ceusAnalysis", u"Select Region of Interest", None))
        self.axialPlaneLabel.setText(QCoreApplication.translate("ceusAnalysis", u"B-Mode", None))
        self.sagittalPlaneLabel.setText(QCoreApplication.translate("ceusAnalysis", u"Contrast-Enhanced Image", None))
        self.curSliceLabel.setText(QCoreApplication.translate("ceusAnalysis", u"Current Frame:", None))
        self.curSliceOfLabel.setText(QCoreApplication.translate("ceusAnalysis", u"of", None))
#if QT_CONFIG(tooltip)
        self.sidebar.setToolTip(QCoreApplication.translate("ceusAnalysis", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.imageSelectionLabelSidebar.setText(QCoreApplication.translate("ceusAnalysis", u"Image Selection:", None))
        self.imageLabel.setText(QCoreApplication.translate("ceusAnalysis", u"Image:", None))
        self.imagePathInput.setText(QCoreApplication.translate("ceusAnalysis", u"Sample filename ", None))
        self.roiSidebarLabel.setText(QCoreApplication.translate("ceusAnalysis", u"Region of Interest (ROI) Selection", None))
        self.rfAnalysisLabel.setText(QCoreApplication.translate("ceusAnalysis", u"Export Results", None))
        self.ticAnalysisLabel.setText(QCoreApplication.translate("ceusAnalysis", u"Contrast-Enhanced Ultrasound\n"
"(CEUS) Analysis", None))
        self.analysisParamsLabel.setText(QCoreApplication.translate("ceusAnalysis", u"TIC Modification", None))
        self.bmodePlane.setText("")
        self.bmodeMaskLayer.setText("")
        self.cePlane.setText("")
        self.mcBmodeDisplayLabel.setText("")
        self.ceMaskLayer.setText("")
        self.mcCeDisplayLabel.setText("")
        self.backButton.setText(QCoreApplication.translate("ceusAnalysis", u"Back", None))
        self.curSliceOfLabel_2.setText(QCoreApplication.translate("ceusAnalysis", u"of", None))
        self.totalSecondsLabel.setText(QCoreApplication.translate("ceusAnalysis", u"0", None))
        self.curSecondLabel.setText(QCoreApplication.translate("ceusAnalysis", u"0", None))
        self.secondsLabel.setText(QCoreApplication.translate("ceusAnalysis", u"seconds", None))
        self.constructRoiLabel.setText(QCoreApplication.translate("ceusAnalysis", u"Construct Region of Interest (ROI):", None))
        self.bmodeCoverLabel.setText("")
        self.ceCoverLabel.setText("")
        self.peVal.setText(QCoreApplication.translate("ceusAnalysis", u"0", None))
        self.tpLabel.setText(QCoreApplication.translate("ceusAnalysis", u"TP", None))
        self.voiVolumeVal.setText(QCoreApplication.translate("ceusAnalysis", u"0", None))
        self.mttLabel.setText(QCoreApplication.translate("ceusAnalysis", u"MTT", None))
        self.tpVal.setText(QCoreApplication.translate("ceusAnalysis", u"0", None))
        self.voiVolumeLabel.setText(QCoreApplication.translate("ceusAnalysis", u"ROI Area\n"
"(mm^2)", None))
        self.tmppvLabel.setText(QCoreApplication.translate("ceusAnalysis", u"TMPPV", None))
        self.aucVal.setText(QCoreApplication.translate("ceusAnalysis", u"0", None))
        self.peLabel.setText(QCoreApplication.translate("ceusAnalysis", u"PE", None))
        self.resultsLabel.setText(QCoreApplication.translate("ceusAnalysis", u"Results:", None))
        self.tmmpVal.setText(QCoreApplication.translate("ceusAnalysis", u"0", None))
        self.mttVal.setText(QCoreApplication.translate("ceusAnalysis", u"0", None))
        self.aucLabel.setText(QCoreApplication.translate("ceusAnalysis", u"AUC", None))
        self.curSliceTotal.setText(QCoreApplication.translate("ceusAnalysis", u"0", None))
    # retranslateUi

