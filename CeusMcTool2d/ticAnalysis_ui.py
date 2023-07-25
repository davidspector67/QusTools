# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ticAnalysis.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ticEditor(object):
    def setupUi(self, ticEditor):
        if not ticEditor.objectName():
            ticEditor.setObjectName(u"ticEditor")
        ticEditor.resize(1175, 749)
        ticEditor.setStyleSheet(u"QWidget {\n"
"	background: rgb(42, 42, 42);\n"
"}")
        self.analysisParamsLabel_2 = QLabel(ticEditor)
        self.analysisParamsLabel_2.setObjectName(u"analysisParamsLabel_2")
        self.analysisParamsLabel_2.setGeometry(QRect(470, -20, 571, 131))
        self.analysisParamsLabel_2.setStyleSheet(u"QLabel {\n"
"	font-size: 29px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.analysisParamsLabel_2.setTextFormat(Qt.AutoText)
        self.analysisParamsLabel_2.setScaledContents(False)
        self.analysisParamsLabel_2.setAlignment(Qt.AlignCenter)
        self.analysisParamsLabel_2.setWordWrap(True)
        self.selectT0Button = QPushButton(ticEditor)
        self.selectT0Button.setObjectName(u"selectT0Button")
        self.selectT0Button.setGeometry(QRect(680, 690, 171, 41))
        self.selectT0Button.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.sidebar = QWidget(ticEditor)
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
        self.analysisParamsSidebar = QFrame(ticEditor)
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
        self.ticFrame = QFrame(ticEditor)
        self.ticFrame.setObjectName(u"ticFrame")
        self.ticFrame.setGeometry(QRect(400, 360, 721, 311))
        self.ticFrame.setFrameShape(QFrame.StyledPanel)
        self.ticFrame.setFrameShadow(QFrame.Raised)
        self.t0Slider = QSlider(ticEditor)
        self.t0Slider.setObjectName(u"t0Slider")
        self.t0Slider.setGeometry(QRect(490, 690, 281, 41))
        self.t0Slider.setOrientation(Qt.Horizontal)
        self.acceptT0Button = QPushButton(ticEditor)
        self.acceptT0Button.setObjectName(u"acceptT0Button")
        self.acceptT0Button.setGeometry(QRect(870, 690, 171, 41))
        self.acceptT0Button.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.deSelectLastPointButton = QPushButton(ticEditor)
        self.deSelectLastPointButton.setObjectName(u"deSelectLastPointButton")
        self.deSelectLastPointButton.setGeometry(QRect(350, 690, 181, 41))
        self.deSelectLastPointButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.removeSelectedPointsButton = QPushButton(ticEditor)
        self.removeSelectedPointsButton.setObjectName(u"removeSelectedPointsButton")
        self.removeSelectedPointsButton.setGeometry(QRect(560, 690, 181, 41))
        self.removeSelectedPointsButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.restoreLastPointsButton = QPushButton(ticEditor)
        self.restoreLastPointsButton.setObjectName(u"restoreLastPointsButton")
        self.restoreLastPointsButton.setGeometry(QRect(770, 690, 181, 41))
        self.restoreLastPointsButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.acceptTicButton = QPushButton(ticEditor)
        self.acceptTicButton.setObjectName(u"acceptTicButton")
        self.acceptTicButton.setGeometry(QRect(980, 690, 181, 41))
        self.acceptTicButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.backButton = QPushButton(ticEditor)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 690, 131, 41))
        self.backButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.bmodeCoverLabel = QLabel(ticEditor)
        self.bmodeCoverLabel.setObjectName(u"bmodeCoverLabel")
        self.bmodeCoverLabel.setGeometry(QRect(440, 120, 231, 211))
        self.bmodeCoverLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.sagittalPlaneLabel = QLabel(ticEditor)
        self.sagittalPlaneLabel.setObjectName(u"sagittalPlaneLabel")
        self.sagittalPlaneLabel.setGeometry(QRect(420, 80, 271, 51))
        self.sagittalPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.sagittalPlaneLabel.setAlignment(Qt.AlignCenter)
        self.sagittalPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.mcBmodeDisplayLabel = QLabel(ticEditor)
        self.mcBmodeDisplayLabel.setObjectName(u"mcBmodeDisplayLabel")
        self.mcBmodeDisplayLabel.setGeometry(QRect(440, 120, 231, 211))
        self.mcCeDisplayLabel = QLabel(ticEditor)
        self.mcCeDisplayLabel.setObjectName(u"mcCeDisplayLabel")
        self.mcCeDisplayLabel.setGeometry(QRect(810, 120, 231, 211))
        self.ceCoverLabel = QLabel(ticEditor)
        self.ceCoverLabel.setObjectName(u"ceCoverLabel")
        self.ceCoverLabel.setGeometry(QRect(810, 120, 231, 211))
        self.ceCoverLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.coronalPlaneLabel = QLabel(ticEditor)
        self.coronalPlaneLabel.setObjectName(u"coronalPlaneLabel")
        self.coronalPlaneLabel.setGeometry(QRect(790, 80, 271, 51))
        self.coronalPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.coronalPlaneLabel.setAlignment(Qt.AlignCenter)
        self.coronalPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.mcBmodeDisplayLabel.raise_()
        self.analysisParamsLabel_2.raise_()
        self.selectT0Button.raise_()
        self.sidebar.raise_()
        self.analysisParamsSidebar.raise_()
        self.ticFrame.raise_()
        self.t0Slider.raise_()
        self.acceptT0Button.raise_()
        self.deSelectLastPointButton.raise_()
        self.removeSelectedPointsButton.raise_()
        self.restoreLastPointsButton.raise_()
        self.acceptTicButton.raise_()
        self.backButton.raise_()
        self.bmodeCoverLabel.raise_()
        self.sagittalPlaneLabel.raise_()
        self.mcCeDisplayLabel.raise_()
        self.ceCoverLabel.raise_()
        self.coronalPlaneLabel.raise_()

        self.retranslateUi(ticEditor)

        QMetaObject.connectSlotsByName(ticEditor)
    # setupUi

    def retranslateUi(self, ticEditor):
        ticEditor.setWindowTitle(QCoreApplication.translate("ticEditor", u"TIC Editor", None))
        self.analysisParamsLabel_2.setText(QCoreApplication.translate("ticEditor", u"Time Intensity Curve (TIC) Editor:", None))
        self.selectT0Button.setText(QCoreApplication.translate("ticEditor", u"Select Start Time (T0)", None))
#if QT_CONFIG(tooltip)
        self.sidebar.setToolTip(QCoreApplication.translate("ticEditor", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.imageSelectionLabelSidebar.setText(QCoreApplication.translate("ticEditor", u"Image Selection:", None))
        self.imageLabel.setText(QCoreApplication.translate("ticEditor", u"Image:", None))
        self.imagePathInput.setText(QCoreApplication.translate("ticEditor", u"Sample filename ", None))
        self.roiSidebarLabel.setText(QCoreApplication.translate("ticEditor", u"Volume of Interest (VOI) Selection", None))
        self.rfAnalysisLabel.setText(QCoreApplication.translate("ticEditor", u"Export Results", None))
        self.ticAnalysisLabel.setText(QCoreApplication.translate("ticEditor", u"Contrast-Enhanced Ultrasound\n"
"(CEUS) Analysis", None))
        self.analysisParamsLabel.setText(QCoreApplication.translate("ticEditor", u"TIC Modification", None))
        self.acceptT0Button.setText(QCoreApplication.translate("ticEditor", u"Accept T0", None))
        self.deSelectLastPointButton.setText(QCoreApplication.translate("ticEditor", u"De-Select Last Point", None))
        self.removeSelectedPointsButton.setText(QCoreApplication.translate("ticEditor", u"Remove Selected Points", None))
        self.restoreLastPointsButton.setText(QCoreApplication.translate("ticEditor", u"Restore Last Points", None))
        self.acceptTicButton.setText(QCoreApplication.translate("ticEditor", u"Accept TIC", None))
        self.backButton.setText(QCoreApplication.translate("ticEditor", u"Back", None))
        self.bmodeCoverLabel.setText("")
        self.sagittalPlaneLabel.setText(QCoreApplication.translate("ticEditor", u"B-Mode Image", None))
        self.mcBmodeDisplayLabel.setText("")
        self.mcCeDisplayLabel.setText("")
        self.ceCoverLabel.setText("")
        self.coronalPlaneLabel.setText(QCoreApplication.translate("ticEditor", u"Contrast-Enhanced Image", None))
    # retranslateUi

