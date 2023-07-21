# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ceusAnalysis.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_rfAnalysis(object):
    def setupUi(self, rfAnalysis):
        if not rfAnalysis.objectName():
            rfAnalysis.setObjectName(u"rfAnalysis")
        rfAnalysis.resize(1175, 749)
        rfAnalysis.setStyleSheet(u"QWidget {\n"
"	background: rgb(42, 42, 42);\n"
"}")
        self.resultsLabel = QLabel(rfAnalysis)
        self.resultsLabel.setObjectName(u"resultsLabel")
        self.resultsLabel.setGeometry(QRect(390, 540, 361, 51))
        self.resultsLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.resultsLabel.setTextFormat(Qt.AutoText)
        self.resultsLabel.setScaledContents(False)
        self.resultsLabel.setAlignment(Qt.AlignCenter)
        self.resultsLabel.setWordWrap(True)
        self.axialPlaneFrame = QFrame(rfAnalysis)
        self.axialPlaneFrame.setObjectName(u"axialPlaneFrame")
        self.axialPlaneFrame.setGeometry(QRect(400, 40, 321, 301))
        self.axialPlaneFrame.setFrameShape(QFrame.StyledPanel)
        self.axialPlaneFrame.setFrameShadow(QFrame.Raised)
        self.sidebar = QWidget(rfAnalysis)
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
"	background-color:  rgb(99, 0, 174);\n"
"	border: 1px solid black;\n"
"}")
        self.ticAnalysisSidebar.setFrameShape(QFrame.StyledPanel)
        self.ticAnalysisSidebar.setFrameShadow(QFrame.Raised)
        self.ticAnalysisLabel = QLabel(self.ticAnalysisSidebar)
        self.ticAnalysisLabel.setObjectName(u"ticAnalysisLabel")
        self.ticAnalysisLabel.setGeometry(QRect(0, 20, 341, 81))
        self.ticAnalysisLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 21px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: 0px;\n"
"	font-weight: bold;\n"
"}")
        self.ticAnalysisLabel.setAlignment(Qt.AlignCenter)
        self.analysisParamsSidebar = QFrame(rfAnalysis)
        self.analysisParamsSidebar.setObjectName(u"analysisParamsSidebar")
        self.analysisParamsSidebar.setGeometry(QRect(0, 240, 341, 121))
        self.analysisParamsSidebar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(99, 0, 174);\n"
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
        self.axialPlaneLabel = QLabel(rfAnalysis)
        self.axialPlaneLabel.setObjectName(u"axialPlaneLabel")
        self.axialPlaneLabel.setGeometry(QRect(420, 0, 271, 51))
        self.axialPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.axialPlaneLabel.setAlignment(Qt.AlignCenter)
        self.axialPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sagittalPlaneLabel = QLabel(rfAnalysis)
        self.sagittalPlaneLabel.setObjectName(u"sagittalPlaneLabel")
        self.sagittalPlaneLabel.setGeometry(QRect(840, 0, 271, 51))
        self.sagittalPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.sagittalPlaneLabel.setAlignment(Qt.AlignCenter)
        self.sagittalPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sagittalPlaneFrame = QFrame(rfAnalysis)
        self.sagittalPlaneFrame.setObjectName(u"sagittalPlaneFrame")
        self.sagittalPlaneFrame.setGeometry(QRect(810, 40, 321, 301))
        self.sagittalPlaneFrame.setFrameShape(QFrame.StyledPanel)
        self.sagittalPlaneFrame.setFrameShadow(QFrame.Raised)
        self.coronalPlaneLabel = QLabel(rfAnalysis)
        self.coronalPlaneLabel.setObjectName(u"coronalPlaneLabel")
        self.coronalPlaneLabel.setGeometry(QRect(840, 370, 271, 51))
        self.coronalPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.coronalPlaneLabel.setAlignment(Qt.AlignCenter)
        self.coronalPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.coronalPlaneFrame = QFrame(rfAnalysis)
        self.coronalPlaneFrame.setObjectName(u"coronalPlaneFrame")
        self.coronalPlaneFrame.setGeometry(QRect(810, 410, 321, 301))
        self.coronalPlaneFrame.setFrameShape(QFrame.StyledPanel)
        self.coronalPlaneFrame.setFrameShadow(QFrame.Raised)
        self.axialSliceNum = QLabel(rfAnalysis)
        self.axialSliceNum.setObjectName(u"axialSliceNum")
        self.axialSliceNum.setGeometry(QRect(640, 350, 41, 31))
        self.axialSliceNum.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.axialSliceNum.setAlignment(Qt.AlignCenter)
        self.axialSliceNum.setTextInteractionFlags(Qt.NoTextInteraction)
        self.axialTotalSlices = QLabel(rfAnalysis)
        self.axialTotalSlices.setObjectName(u"axialTotalSlices")
        self.axialTotalSlices.setGeometry(QRect(700, 350, 61, 31))
        self.axialTotalSlices.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.axialTotalSlices.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.axialTotalSlices.setTextInteractionFlags(Qt.NoTextInteraction)
        self.axialOfLabel = QLabel(rfAnalysis)
        self.axialOfLabel.setObjectName(u"axialOfLabel")
        self.axialOfLabel.setGeometry(QRect(665, 350, 41, 31))
        self.axialOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.axialOfLabel.setAlignment(Qt.AlignCenter)
        self.axialOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sagittalSliceNum = QLabel(rfAnalysis)
        self.sagittalSliceNum.setObjectName(u"sagittalSliceNum")
        self.sagittalSliceNum.setGeometry(QRect(1050, 350, 41, 31))
        self.sagittalSliceNum.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.sagittalSliceNum.setAlignment(Qt.AlignCenter)
        self.sagittalSliceNum.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sagittalOfLabel = QLabel(rfAnalysis)
        self.sagittalOfLabel.setObjectName(u"sagittalOfLabel")
        self.sagittalOfLabel.setGeometry(QRect(1075, 350, 41, 31))
        self.sagittalOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.sagittalOfLabel.setAlignment(Qt.AlignCenter)
        self.sagittalOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sagittalTotalSlices = QLabel(rfAnalysis)
        self.sagittalTotalSlices.setObjectName(u"sagittalTotalSlices")
        self.sagittalTotalSlices.setGeometry(QRect(1110, 350, 61, 31))
        self.sagittalTotalSlices.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.sagittalTotalSlices.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.sagittalTotalSlices.setTextInteractionFlags(Qt.NoTextInteraction)
        self.coronalSliceNum = QLabel(rfAnalysis)
        self.coronalSliceNum.setObjectName(u"coronalSliceNum")
        self.coronalSliceNum.setGeometry(QRect(1050, 710, 41, 31))
        self.coronalSliceNum.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.coronalSliceNum.setAlignment(Qt.AlignCenter)
        self.coronalSliceNum.setTextInteractionFlags(Qt.NoTextInteraction)
        self.coronalOfLabel = QLabel(rfAnalysis)
        self.coronalOfLabel.setObjectName(u"coronalOfLabel")
        self.coronalOfLabel.setGeometry(QRect(1075, 710, 41, 31))
        self.coronalOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.coronalOfLabel.setAlignment(Qt.AlignCenter)
        self.coronalOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.coronalTotalSlices = QLabel(rfAnalysis)
        self.coronalTotalSlices.setObjectName(u"coronalTotalSlices")
        self.coronalTotalSlices.setGeometry(QRect(1110, 710, 61, 31))
        self.coronalTotalSlices.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.coronalTotalSlices.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.coronalTotalSlices.setTextInteractionFlags(Qt.NoTextInteraction)
        self.curSliceLabel = QLabel(rfAnalysis)
        self.curSliceLabel.setObjectName(u"curSliceLabel")
        self.curSliceLabel.setGeometry(QRect(380, 370, 361, 51))
        self.curSliceLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceLabel.setTextFormat(Qt.AutoText)
        self.curSliceLabel.setScaledContents(False)
        self.curSliceLabel.setAlignment(Qt.AlignCenter)
        self.curSliceLabel.setWordWrap(True)
        self.curSliceSlider = QSlider(rfAnalysis)
        self.curSliceSlider.setObjectName(u"curSliceSlider")
        self.curSliceSlider.setGeometry(QRect(399, 430, 191, 22))
        self.curSliceSlider.setOrientation(Qt.Horizontal)
        self.curSliceOfLabel = QLabel(rfAnalysis)
        self.curSliceOfLabel.setObjectName(u"curSliceOfLabel")
        self.curSliceOfLabel.setGeometry(QRect(695, 425, 41, 31))
        self.curSliceOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceOfLabel.setAlignment(Qt.AlignCenter)
        self.curSliceOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.curSliceTotal = QLabel(rfAnalysis)
        self.curSliceTotal.setObjectName(u"curSliceTotal")
        self.curSliceTotal.setGeometry(QRect(730, 425, 61, 31))
        self.curSliceTotal.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceTotal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.curSliceTotal.setTextInteractionFlags(Qt.NoTextInteraction)
        self.curSliceSpinBox = QSpinBox(rfAnalysis)
        self.curSliceSpinBox.setObjectName(u"curSliceSpinBox")
        self.curSliceSpinBox.setGeometry(QRect(640, 430, 48, 24))
        font = QFont()
        font.setPointSize(13)
        self.curSliceSpinBox.setFont(font)
        self.curSliceSpinBox.setStyleSheet(u"QSpinBox{\n"
"	background-color: white,\n"
"}")
        self.voiAlphaLabel = QLabel(rfAnalysis)
        self.voiAlphaLabel.setObjectName(u"voiAlphaLabel")
        self.voiAlphaLabel.setGeometry(QRect(380, 465, 361, 51))
        self.voiAlphaLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.voiAlphaLabel.setTextFormat(Qt.AutoText)
        self.voiAlphaLabel.setScaledContents(False)
        self.voiAlphaLabel.setAlignment(Qt.AlignCenter)
        self.voiAlphaLabel.setWordWrap(True)
        self.voiAlphaSpinBox = QSpinBox(rfAnalysis)
        self.voiAlphaSpinBox.setObjectName(u"voiAlphaSpinBox")
        self.voiAlphaSpinBox.setGeometry(QRect(640, 515, 48, 24))
        self.voiAlphaSpinBox.setFont(font)
        self.voiAlphaSpinBox.setStyleSheet(u"QSpinBox{\n"
"	background-color: white,\n"
"}")
        self.voiAlphaTotal = QLabel(rfAnalysis)
        self.voiAlphaTotal.setObjectName(u"voiAlphaTotal")
        self.voiAlphaTotal.setGeometry(QRect(730, 510, 61, 31))
        self.voiAlphaTotal.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.voiAlphaTotal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.voiAlphaTotal.setTextInteractionFlags(Qt.NoTextInteraction)
        self.voiAlphaOfLabel = QLabel(rfAnalysis)
        self.voiAlphaOfLabel.setObjectName(u"voiAlphaOfLabel")
        self.voiAlphaOfLabel.setGeometry(QRect(695, 510, 41, 31))
        self.voiAlphaOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.voiAlphaOfLabel.setAlignment(Qt.AlignCenter)
        self.voiAlphaOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.aucVal = QLabel(rfAnalysis)
        self.aucVal.setObjectName(u"aucVal")
        self.aucVal.setGeometry(QRect(760, 570, 51, 51))
        font1 = QFont()
        font1.setPointSize(14)
        self.aucVal.setFont(font1)
        self.aucVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.aucVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.aucLabel = QLabel(rfAnalysis)
        self.aucLabel.setObjectName(u"aucLabel")
        self.aucLabel.setGeometry(QRect(700, 570, 81, 51))
        self.aucLabel.setFont(font1)
        self.aucLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.aucLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.peLabel = QLabel(rfAnalysis)
        self.peLabel.setObjectName(u"peLabel")
        self.peLabel.setGeometry(QRect(700, 590, 91, 51))
        self.peLabel.setFont(font1)
        self.peLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.peLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.peVal = QLabel(rfAnalysis)
        self.peVal.setObjectName(u"peVal")
        self.peVal.setGeometry(QRect(760, 590, 51, 51))
        self.peVal.setFont(font1)
        self.peVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.peVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.voiVolumeLabel = QLabel(rfAnalysis)
        self.voiVolumeLabel.setObjectName(u"voiVolumeLabel")
        self.voiVolumeLabel.setGeometry(QRect(680, 700, 141, 51))
        self.voiVolumeLabel.setFont(font1)
        self.voiVolumeLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.voiVolumeLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tmmpVal = QLabel(rfAnalysis)
        self.tmmpVal.setObjectName(u"tmmpVal")
        self.tmmpVal.setGeometry(QRect(760, 650, 71, 51))
        self.tmmpVal.setFont(font1)
        self.tmmpVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tmmpVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.voiVolumeVal = QLabel(rfAnalysis)
        self.voiVolumeVal.setObjectName(u"voiVolumeVal")
        self.voiVolumeVal.setGeometry(QRect(790, 700, 151, 51))
        self.voiVolumeVal.setFont(font1)
        self.voiVolumeVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.voiVolumeVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tmppvLabel = QLabel(rfAnalysis)
        self.tmppvLabel.setObjectName(u"tmppvLabel")
        self.tmppvLabel.setGeometry(QRect(700, 650, 71, 51))
        self.tmppvLabel.setFont(font1)
        self.tmppvLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tmppvLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tpLabel = QLabel(rfAnalysis)
        self.tpLabel.setObjectName(u"tpLabel")
        self.tpLabel.setGeometry(QRect(700, 630, 91, 51))
        self.tpLabel.setFont(font1)
        self.tpLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tpLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tpVal = QLabel(rfAnalysis)
        self.tpVal.setObjectName(u"tpVal")
        self.tpVal.setGeometry(QRect(760, 630, 51, 51))
        self.tpVal.setFont(font1)
        self.tpVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tpVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mttVal = QLabel(rfAnalysis)
        self.mttVal.setObjectName(u"mttVal")
        self.mttVal.setGeometry(QRect(760, 610, 51, 51))
        self.mttVal.setFont(font1)
        self.mttVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.mttVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mttLabel = QLabel(rfAnalysis)
        self.mttLabel.setObjectName(u"mttLabel")
        self.mttLabel.setGeometry(QRect(700, 610, 81, 51))
        self.mttLabel.setFont(font1)
        self.mttLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.mttLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ticDisplay = QFrame(rfAnalysis)
        self.ticDisplay.setObjectName(u"ticDisplay")
        self.ticDisplay.setGeometry(QRect(350, 590, 321, 121))
        self.ticDisplay.setFrameShape(QFrame.StyledPanel)
        self.ticDisplay.setFrameShadow(QFrame.Raised)
        self.voiAlphaStatus = QProgressBar(rfAnalysis)
        self.voiAlphaStatus.setObjectName(u"voiAlphaStatus")
        self.voiAlphaStatus.setGeometry(QRect(399, 510, 191, 22))
        self.voiAlphaStatus.setValue(24)
        self.backButton = QPushButton(rfAnalysis)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 690, 131, 41))
        self.backButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")

        self.retranslateUi(rfAnalysis)

        QMetaObject.connectSlotsByName(rfAnalysis)
    # setupUi

    def retranslateUi(self, rfAnalysis):
        rfAnalysis.setWindowTitle(QCoreApplication.translate("rfAnalysis", u"Analysis Results", None))
        self.resultsLabel.setText(QCoreApplication.translate("rfAnalysis", u"Results:", None))
#if QT_CONFIG(tooltip)
        self.sidebar.setToolTip(QCoreApplication.translate("rfAnalysis", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.imageSelectionLabelSidebar.setText(QCoreApplication.translate("rfAnalysis", u"Image Selection:", None))
        self.imageLabel.setText(QCoreApplication.translate("rfAnalysis", u"Image:", None))
        self.imagePathInput.setText(QCoreApplication.translate("rfAnalysis", u"Sample filename ", None))
        self.roiSidebarLabel.setText(QCoreApplication.translate("rfAnalysis", u"Volume of Interest (VOI) Selection", None))
        self.rfAnalysisLabel.setText(QCoreApplication.translate("rfAnalysis", u"Export Results", None))
        self.ticAnalysisLabel.setText(QCoreApplication.translate("rfAnalysis", u"Contrast-Enhanced Ultrasound\n"
"(CEUS) Analysis", None))
        self.analysisParamsLabel.setText(QCoreApplication.translate("rfAnalysis", u"TIC Modification", None))
        self.axialPlaneLabel.setText(QCoreApplication.translate("rfAnalysis", u"Axial Plane", None))
        self.sagittalPlaneLabel.setText(QCoreApplication.translate("rfAnalysis", u"Sagittal Plane", None))
        self.coronalPlaneLabel.setText(QCoreApplication.translate("rfAnalysis", u"Coronal Plane", None))
        self.axialSliceNum.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.axialTotalSlices.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.axialOfLabel.setText(QCoreApplication.translate("rfAnalysis", u"of", None))
        self.sagittalSliceNum.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.sagittalOfLabel.setText(QCoreApplication.translate("rfAnalysis", u"of", None))
        self.sagittalTotalSlices.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.coronalSliceNum.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.coronalOfLabel.setText(QCoreApplication.translate("rfAnalysis", u"of", None))
        self.coronalTotalSlices.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.curSliceLabel.setText(QCoreApplication.translate("rfAnalysis", u"Current Slice:", None))
        self.curSliceOfLabel.setText(QCoreApplication.translate("rfAnalysis", u"of", None))
        self.curSliceTotal.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.voiAlphaLabel.setText(QCoreApplication.translate("rfAnalysis", u"VOI Alpha:", None))
        self.voiAlphaTotal.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.voiAlphaOfLabel.setText(QCoreApplication.translate("rfAnalysis", u"of", None))
        self.aucVal.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.aucLabel.setText(QCoreApplication.translate("rfAnalysis", u"AUC", None))
        self.peLabel.setText(QCoreApplication.translate("rfAnalysis", u"PE", None))
        self.peVal.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.voiVolumeLabel.setText(QCoreApplication.translate("rfAnalysis", u"VOI Vol (mm^3)", None))
        self.tmmpVal.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.voiVolumeVal.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.tmppvLabel.setText(QCoreApplication.translate("rfAnalysis", u"TMPPV", None))
        self.tpLabel.setText(QCoreApplication.translate("rfAnalysis", u"TP", None))
        self.tpVal.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.mttVal.setText(QCoreApplication.translate("rfAnalysis", u"0", None))
        self.mttLabel.setText(QCoreApplication.translate("rfAnalysis", u"MTT", None))
        self.backButton.setText(QCoreApplication.translate("rfAnalysis", u"Back", None))
    # retranslateUi

