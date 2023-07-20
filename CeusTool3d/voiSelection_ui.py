# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'voiSelection.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_constructVoi(object):
    def setupUi(self, constructVoi):
        if not constructVoi.objectName():
            constructVoi.setObjectName(u"constructVoi")
        constructVoi.resize(1175, 749)
        constructVoi.setStyleSheet(u"QWidget {\n"
"	background: rgb(42, 42, 42);\n"
"}")
        self.constructVoiLabel = QLabel(constructVoi)
        self.constructVoiLabel.setObjectName(u"constructVoiLabel")
        self.constructVoiLabel.setGeometry(QRect(390, 570, 361, 51))
        self.constructVoiLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.constructVoiLabel.setTextFormat(Qt.AutoText)
        self.constructVoiLabel.setScaledContents(False)
        self.constructVoiLabel.setAlignment(Qt.AlignCenter)
        self.constructVoiLabel.setWordWrap(True)
        self.drawRoiButton = QPushButton(constructVoi)
        self.drawRoiButton.setObjectName(u"drawRoiButton")
        self.drawRoiButton.setGeometry(QRect(390, 630, 171, 41))
        self.drawRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:checked {\n"
"	color:white; \n"
"	font-size: 16px;\n"
"	background: rgb(45, 0, 110);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.drawRoiButton.setCheckable(True)
        self.drawRoiButton.setChecked(False)
        self.undoLastPtButton = QPushButton(constructVoi)
        self.undoLastPtButton.setObjectName(u"undoLastPtButton")
        self.undoLastPtButton.setGeometry(QRect(580, 630, 171, 41))
        self.undoLastPtButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.undoLastPtButton.setCheckable(False)
        self.interpolateVoiButton = QPushButton(constructVoi)
        self.interpolateVoiButton.setObjectName(u"interpolateVoiButton")
        self.interpolateVoiButton.setGeometry(QRect(580, 690, 171, 41))
        self.interpolateVoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.interpolateVoiButton.setCheckable(False)
        self.closeRoiButton = QPushButton(constructVoi)
        self.closeRoiButton.setObjectName(u"closeRoiButton")
        self.closeRoiButton.setGeometry(QRect(390, 690, 171, 41))
        self.closeRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.closeRoiButton.setCheckable(False)
        self.redrawRoiButton = QPushButton(constructVoi)
        self.redrawRoiButton.setObjectName(u"redrawRoiButton")
        self.redrawRoiButton.setGeometry(QRect(390, 690, 171, 41))
        self.redrawRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.redrawRoiButton.setCheckable(False)
        self.axialPlaneLabel = QLabel(constructVoi)
        self.axialPlaneLabel.setObjectName(u"axialPlaneLabel")
        self.axialPlaneLabel.setGeometry(QRect(420, 0, 271, 51))
        self.axialPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.axialPlaneLabel.setAlignment(Qt.AlignCenter)
        self.axialPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sagittalPlaneLabel = QLabel(constructVoi)
        self.sagittalPlaneLabel.setObjectName(u"sagittalPlaneLabel")
        self.sagittalPlaneLabel.setGeometry(QRect(840, 0, 271, 51))
        self.sagittalPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.sagittalPlaneLabel.setAlignment(Qt.AlignCenter)
        self.sagittalPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.coronalPlaneLabel = QLabel(constructVoi)
        self.coronalPlaneLabel.setObjectName(u"coronalPlaneLabel")
        self.coronalPlaneLabel.setGeometry(QRect(840, 370, 271, 51))
        self.coronalPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.coronalPlaneLabel.setAlignment(Qt.AlignCenter)
        self.coronalPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.axialFrameNum = QLabel(constructVoi)
        self.axialFrameNum.setObjectName(u"axialFrameNum")
        self.axialFrameNum.setGeometry(QRect(640, 350, 41, 31))
        self.axialFrameNum.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.axialFrameNum.setAlignment(Qt.AlignCenter)
        self.axialFrameNum.setTextInteractionFlags(Qt.NoTextInteraction)
        self.axialTotalFrames = QLabel(constructVoi)
        self.axialTotalFrames.setObjectName(u"axialTotalFrames")
        self.axialTotalFrames.setGeometry(QRect(700, 350, 61, 31))
        self.axialTotalFrames.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.axialTotalFrames.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.axialTotalFrames.setTextInteractionFlags(Qt.NoTextInteraction)
        self.axialOfLabel = QLabel(constructVoi)
        self.axialOfLabel.setObjectName(u"axialOfLabel")
        self.axialOfLabel.setGeometry(QRect(665, 350, 41, 31))
        self.axialOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.axialOfLabel.setAlignment(Qt.AlignCenter)
        self.axialOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sagittalFrameNum = QLabel(constructVoi)
        self.sagittalFrameNum.setObjectName(u"sagittalFrameNum")
        self.sagittalFrameNum.setGeometry(QRect(1050, 350, 41, 31))
        self.sagittalFrameNum.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.sagittalFrameNum.setAlignment(Qt.AlignCenter)
        self.sagittalFrameNum.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sagittalOfLabel = QLabel(constructVoi)
        self.sagittalOfLabel.setObjectName(u"sagittalOfLabel")
        self.sagittalOfLabel.setGeometry(QRect(1075, 350, 41, 31))
        self.sagittalOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.sagittalOfLabel.setAlignment(Qt.AlignCenter)
        self.sagittalOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sagittalTotalFrames = QLabel(constructVoi)
        self.sagittalTotalFrames.setObjectName(u"sagittalTotalFrames")
        self.sagittalTotalFrames.setGeometry(QRect(1110, 350, 61, 31))
        self.sagittalTotalFrames.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.sagittalTotalFrames.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.sagittalTotalFrames.setTextInteractionFlags(Qt.NoTextInteraction)
        self.coronalFrameNum = QLabel(constructVoi)
        self.coronalFrameNum.setObjectName(u"coronalFrameNum")
        self.coronalFrameNum.setGeometry(QRect(1050, 710, 41, 31))
        self.coronalFrameNum.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.coronalFrameNum.setAlignment(Qt.AlignCenter)
        self.coronalFrameNum.setTextInteractionFlags(Qt.NoTextInteraction)
        self.coronalOfLabel = QLabel(constructVoi)
        self.coronalOfLabel.setObjectName(u"coronalOfLabel")
        self.coronalOfLabel.setGeometry(QRect(1075, 710, 41, 31))
        self.coronalOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.coronalOfLabel.setAlignment(Qt.AlignCenter)
        self.coronalOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.coronalTotalFrames = QLabel(constructVoi)
        self.coronalTotalFrames.setObjectName(u"coronalTotalFrames")
        self.coronalTotalFrames.setGeometry(QRect(1110, 710, 61, 31))
        self.coronalTotalFrames.setStyleSheet(u"QLabel {\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.coronalTotalFrames.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.coronalTotalFrames.setTextInteractionFlags(Qt.NoTextInteraction)
        self.curSliceLabel = QLabel(constructVoi)
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
        self.curSliceSlider = QSlider(constructVoi)
        self.curSliceSlider.setObjectName(u"curSliceSlider")
        self.curSliceSlider.setGeometry(QRect(399, 420, 191, 41))
        self.curSliceSlider.setOrientation(Qt.Horizontal)
        self.curSliceOfLabel = QLabel(constructVoi)
        self.curSliceOfLabel.setObjectName(u"curSliceOfLabel")
        self.curSliceOfLabel.setGeometry(QRect(695, 425, 41, 31))
        self.curSliceOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceOfLabel.setAlignment(Qt.AlignCenter)
        self.curSliceOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.curSliceTotal = QLabel(constructVoi)
        self.curSliceTotal.setObjectName(u"curSliceTotal")
        self.curSliceTotal.setGeometry(QRect(730, 425, 61, 31))
        self.curSliceTotal.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceTotal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.curSliceTotal.setTextInteractionFlags(Qt.NoTextInteraction)
        self.voiAlphaLabel = QLabel(constructVoi)
        self.voiAlphaLabel.setObjectName(u"voiAlphaLabel")
        self.voiAlphaLabel.setGeometry(QRect(380, 475, 361, 51))
        self.voiAlphaLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.voiAlphaLabel.setTextFormat(Qt.AutoText)
        self.voiAlphaLabel.setScaledContents(False)
        self.voiAlphaLabel.setAlignment(Qt.AlignCenter)
        self.voiAlphaLabel.setWordWrap(True)
        self.voiAlphaSpinBox = QSpinBox(constructVoi)
        self.voiAlphaSpinBox.setObjectName(u"voiAlphaSpinBox")
        self.voiAlphaSpinBox.setGeometry(QRect(640, 525, 48, 24))
        font = QFont()
        font.setPointSize(13)
        self.voiAlphaSpinBox.setFont(font)
        self.voiAlphaSpinBox.setStyleSheet(u"QSpinBox{\n"
"	background-color: white,\n"
"}")
        self.voiAlphaTotal = QLabel(constructVoi)
        self.voiAlphaTotal.setObjectName(u"voiAlphaTotal")
        self.voiAlphaTotal.setGeometry(QRect(730, 520, 61, 31))
        self.voiAlphaTotal.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.voiAlphaTotal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.voiAlphaTotal.setTextInteractionFlags(Qt.NoTextInteraction)
        self.voiAlphaOfLabel = QLabel(constructVoi)
        self.voiAlphaOfLabel.setObjectName(u"voiAlphaOfLabel")
        self.voiAlphaOfLabel.setGeometry(QRect(695, 520, 41, 31))
        self.voiAlphaOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.voiAlphaOfLabel.setAlignment(Qt.AlignCenter)
        self.voiAlphaOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sidebar = QWidget(constructVoi)
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
        self.analysisParamsSidebar = QFrame(constructVoi)
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
        self.axialPlane = QLabel(constructVoi)
        self.axialPlane.setObjectName(u"axialPlane")
        self.axialPlane.setGeometry(QRect(400, 40, 321, 301))
        self.maskLayerAx = QLabel(constructVoi)
        self.maskLayerAx.setObjectName(u"maskLayerAx")
        self.maskLayerAx.setGeometry(QRect(400, 40, 321, 301))
        self.maskLayerAx.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.sagPlane = QLabel(constructVoi)
        self.sagPlane.setObjectName(u"sagPlane")
        self.sagPlane.setGeometry(QRect(810, 40, 321, 301))
        self.corPlane = QLabel(constructVoi)
        self.corPlane.setObjectName(u"corPlane")
        self.corPlane.setGeometry(QRect(810, 410, 321, 301))
        self.axCoverLabel = QLabel(constructVoi)
        self.axCoverLabel.setObjectName(u"axCoverLabel")
        self.axCoverLabel.setGeometry(QRect(400, 40, 321, 301))
        self.axCoverLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.maskLayerSag = QLabel(constructVoi)
        self.maskLayerSag.setObjectName(u"maskLayerSag")
        self.maskLayerSag.setGeometry(QRect(810, 40, 321, 301))
        self.maskLayerSag.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.maskLayerCor = QLabel(constructVoi)
        self.maskLayerCor.setObjectName(u"maskLayerCor")
        self.maskLayerCor.setGeometry(QRect(810, 410, 321, 301))
        self.maskLayerCor.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.sagCoverLabel = QLabel(constructVoi)
        self.sagCoverLabel.setObjectName(u"sagCoverLabel")
        self.sagCoverLabel.setGeometry(QRect(810, 40, 321, 301))
        self.sagCoverLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.corCoverLabel = QLabel(constructVoi)
        self.corCoverLabel.setObjectName(u"corCoverLabel")
        self.corCoverLabel.setGeometry(QRect(810, 410, 321, 301))
        self.corCoverLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.voiAlphaStatus = QProgressBar(constructVoi)
        self.voiAlphaStatus.setObjectName(u"voiAlphaStatus")
        self.voiAlphaStatus.setGeometry(QRect(399, 520, 191, 41))
        self.voiAlphaStatus.setValue(24)
        self.continueButton = QPushButton(constructVoi)
        self.continueButton.setObjectName(u"continueButton")
        self.continueButton.setGeometry(QRect(580, 650, 171, 41))
        self.continueButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.continueButton.setCheckable(False)
        self.aucVal = QLabel(constructVoi)
        self.aucVal.setObjectName(u"aucVal")
        self.aucVal.setGeometry(QRect(740, 570, 51, 51))
        font1 = QFont()
        font1.setPointSize(14)
        self.aucVal.setFont(font1)
        self.aucVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.aucVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.aucLabel = QLabel(constructVoi)
        self.aucLabel.setObjectName(u"aucLabel")
        self.aucLabel.setGeometry(QRect(680, 570, 81, 51))
        self.aucLabel.setFont(font1)
        self.aucLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.aucLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tpVal = QLabel(constructVoi)
        self.tpVal.setObjectName(u"tpVal")
        self.tpVal.setGeometry(QRect(740, 630, 51, 51))
        self.tpVal.setFont(font1)
        self.tpVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tpVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tmppvVal = QLabel(constructVoi)
        self.tmppvVal.setObjectName(u"tmppvVal")
        self.tmppvVal.setGeometry(QRect(740, 650, 71, 51))
        self.tmppvVal.setFont(font1)
        self.tmppvVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tmppvVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mttLabel = QLabel(constructVoi)
        self.mttLabel.setObjectName(u"mttLabel")
        self.mttLabel.setGeometry(QRect(680, 610, 81, 51))
        self.mttLabel.setFont(font1)
        self.mttLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.mttLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.peLabel = QLabel(constructVoi)
        self.peLabel.setObjectName(u"peLabel")
        self.peLabel.setGeometry(QRect(680, 590, 91, 51))
        self.peLabel.setFont(font1)
        self.peLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.peLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.voiVolumeLabel = QLabel(constructVoi)
        self.voiVolumeLabel.setObjectName(u"voiVolumeLabel")
        self.voiVolumeLabel.setGeometry(QRect(680, 700, 141, 51))
        self.voiVolumeLabel.setFont(font1)
        self.voiVolumeLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.voiVolumeLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.voiVolumeVal = QLabel(constructVoi)
        self.voiVolumeVal.setObjectName(u"voiVolumeVal")
        self.voiVolumeVal.setGeometry(QRect(790, 700, 51, 51))
        self.voiVolumeVal.setFont(font1)
        self.voiVolumeVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.voiVolumeVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mttVal = QLabel(constructVoi)
        self.mttVal.setObjectName(u"mttVal")
        self.mttVal.setGeometry(QRect(740, 610, 51, 51))
        self.mttVal.setFont(font1)
        self.mttVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.mttVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ticDisplay = QFrame(constructVoi)
        self.ticDisplay.setObjectName(u"ticDisplay")
        self.ticDisplay.setGeometry(QRect(350, 590, 321, 121))
        self.ticDisplay.setFrameShape(QFrame.StyledPanel)
        self.ticDisplay.setFrameShadow(QFrame.Raised)
        self.resultsLabel = QLabel(constructVoi)
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
        self.peVal = QLabel(constructVoi)
        self.peVal.setObjectName(u"peVal")
        self.peVal.setGeometry(QRect(740, 590, 51, 51))
        self.peVal.setFont(font1)
        self.peVal.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.peVal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tpLabel = QLabel(constructVoi)
        self.tpLabel.setObjectName(u"tpLabel")
        self.tpLabel.setGeometry(QRect(680, 630, 91, 51))
        self.tpLabel.setFont(font1)
        self.tpLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tpLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tmppvLabel = QLabel(constructVoi)
        self.tmppvLabel.setObjectName(u"tmppvLabel")
        self.tmppvLabel.setGeometry(QRect(680, 650, 71, 51))
        self.tmppvLabel.setFont(font1)
        self.tmppvLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.tmppvLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.backButton = QPushButton(constructVoi)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 690, 131, 41))
        self.backButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.restartVoiButton = QPushButton(constructVoi)
        self.restartVoiButton.setObjectName(u"restartVoiButton")
        self.restartVoiButton.setGeometry(QRect(390, 650, 171, 41))
        self.restartVoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.restartVoiButton.setCheckable(False)
        self.curSliceSpinBox = QDoubleSpinBox(constructVoi)
        self.curSliceSpinBox.setObjectName(u"curSliceSpinBox")
        self.curSliceSpinBox.setGeometry(QRect(630, 430, 68, 24))
        self.curSliceSpinBox.setStyleSheet(u"QDoubleSpinBox {\n"
"	background: white;\n"
"}")
        self.voiAdviceLabel = QLabel(constructVoi)
        self.voiAdviceLabel.setObjectName(u"voiAdviceLabel")
        self.voiAdviceLabel.setGeometry(QRect(380, 500, 361, 51))
        self.voiAdviceLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.voiAdviceLabel.setTextFormat(Qt.AutoText)
        self.voiAdviceLabel.setScaledContents(False)
        self.voiAdviceLabel.setAlignment(Qt.AlignCenter)
        self.voiAdviceLabel.setWordWrap(True)

        self.retranslateUi(constructVoi)

        QMetaObject.connectSlotsByName(constructVoi)
    # setupUi

    def retranslateUi(self, constructVoi):
        constructVoi.setWindowTitle(QCoreApplication.translate("constructVoi", u"Select Volume of Interest", None))
        self.constructVoiLabel.setText(QCoreApplication.translate("constructVoi", u"Construct Volume of Interest (VOI):", None))
        self.drawRoiButton.setText(QCoreApplication.translate("constructVoi", u"Draw ROI", None))
        self.undoLastPtButton.setText(QCoreApplication.translate("constructVoi", u"Undo Last Point", None))
        self.interpolateVoiButton.setText(QCoreApplication.translate("constructVoi", u"Interpolate VOI", None))
        self.closeRoiButton.setText(QCoreApplication.translate("constructVoi", u"Close ROI", None))
        self.redrawRoiButton.setText(QCoreApplication.translate("constructVoi", u"Undo Last ROI", None))
        self.axialPlaneLabel.setText(QCoreApplication.translate("constructVoi", u"Axial Plane", None))
        self.sagittalPlaneLabel.setText(QCoreApplication.translate("constructVoi", u"Sagittal Plane", None))
        self.coronalPlaneLabel.setText(QCoreApplication.translate("constructVoi", u"Coronal Plane", None))
        self.axialFrameNum.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.axialTotalFrames.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.axialOfLabel.setText(QCoreApplication.translate("constructVoi", u"of", None))
        self.sagittalFrameNum.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.sagittalOfLabel.setText(QCoreApplication.translate("constructVoi", u"of", None))
        self.sagittalTotalFrames.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.coronalFrameNum.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.coronalOfLabel.setText(QCoreApplication.translate("constructVoi", u"of", None))
        self.coronalTotalFrames.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.curSliceLabel.setText(QCoreApplication.translate("constructVoi", u"Current Slice (in seconds):", None))
        self.curSliceOfLabel.setText(QCoreApplication.translate("constructVoi", u"of", None))
        self.curSliceTotal.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.voiAlphaLabel.setText(QCoreApplication.translate("constructVoi", u"VOI Alpha:", None))
        self.voiAlphaTotal.setText(QCoreApplication.translate("constructVoi", u"255", None))
        self.voiAlphaOfLabel.setText(QCoreApplication.translate("constructVoi", u"of", None))
#if QT_CONFIG(tooltip)
        self.sidebar.setToolTip(QCoreApplication.translate("constructVoi", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.imageSelectionLabelSidebar.setText(QCoreApplication.translate("constructVoi", u"Image Selection:", None))
        self.imageLabel.setText(QCoreApplication.translate("constructVoi", u"Image:", None))
        self.imagePathInput.setText(QCoreApplication.translate("constructVoi", u"Sample filename ", None))
        self.roiSidebarLabel.setText(QCoreApplication.translate("constructVoi", u"Volume of Interest (VOI) Selection", None))
        self.rfAnalysisLabel.setText(QCoreApplication.translate("constructVoi", u"Export Results", None))
        self.ticAnalysisLabel.setText(QCoreApplication.translate("constructVoi", u"Contrast-Enhanced Ultrasound\n"
"(CEUS) Analysis", None))
        self.analysisParamsLabel.setText(QCoreApplication.translate("constructVoi", u"TIC Modification", None))
        self.axialPlane.setText("")
        self.maskLayerAx.setText("")
        self.sagPlane.setText("")
        self.corPlane.setText("")
        self.axCoverLabel.setText("")
        self.maskLayerSag.setText("")
        self.maskLayerCor.setText("")
        self.sagCoverLabel.setText("")
        self.corCoverLabel.setText("")
        self.continueButton.setText(QCoreApplication.translate("constructVoi", u"Continue", None))
        self.aucVal.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.aucLabel.setText(QCoreApplication.translate("constructVoi", u"AUC:", None))
        self.tpVal.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.tmppvVal.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.mttLabel.setText(QCoreApplication.translate("constructVoi", u"MTT:", None))
        self.peLabel.setText(QCoreApplication.translate("constructVoi", u"PE:", None))
        self.voiVolumeLabel.setText(QCoreApplication.translate("constructVoi", u"VOI Vol (mm^3):", None))
        self.voiVolumeVal.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.mttVal.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.resultsLabel.setText(QCoreApplication.translate("constructVoi", u"Results:", None))
        self.peVal.setText(QCoreApplication.translate("constructVoi", u"0", None))
        self.tpLabel.setText(QCoreApplication.translate("constructVoi", u"TP:", None))
        self.tmppvLabel.setText(QCoreApplication.translate("constructVoi", u"TMPPV:", None))
        self.backButton.setText(QCoreApplication.translate("constructVoi", u"Back", None))
        self.restartVoiButton.setText(QCoreApplication.translate("constructVoi", u"Restart VOI", None))
        self.voiAdviceLabel.setText(QCoreApplication.translate("constructVoi", u"For best results, draw 1 ROI in each plane before interpolating", None))
    # retranslateUi

