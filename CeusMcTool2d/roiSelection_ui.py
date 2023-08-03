# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'roiSelection.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_constructRoi(object):
    def setupUi(self, constructRoi):
        if not constructRoi.objectName():
            constructRoi.setObjectName(u"constructRoi")
        constructRoi.resize(1175, 749)
        constructRoi.setStyleSheet(u"QWidget {\n"
"	background: rgb(42, 42, 42);\n"
"}")
        self.axialPlaneLabel = QLabel(constructRoi)
        self.axialPlaneLabel.setObjectName(u"axialPlaneLabel")
        self.axialPlaneLabel.setGeometry(QRect(410, 100, 271, 51))
        self.axialPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.axialPlaneLabel.setAlignment(Qt.AlignCenter)
        self.axialPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sagittalPlaneLabel = QLabel(constructRoi)
        self.sagittalPlaneLabel.setObjectName(u"sagittalPlaneLabel")
        self.sagittalPlaneLabel.setGeometry(QRect(830, 100, 271, 51))
        self.sagittalPlaneLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 18px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.sagittalPlaneLabel.setAlignment(Qt.AlignCenter)
        self.sagittalPlaneLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.curSliceLabel = QLabel(constructRoi)
        self.curSliceLabel.setObjectName(u"curSliceLabel")
        self.curSliceLabel.setGeometry(QRect(350, 530, 361, 51))
        self.curSliceLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceLabel.setTextFormat(Qt.AutoText)
        self.curSliceLabel.setScaledContents(False)
        self.curSliceLabel.setAlignment(Qt.AlignCenter)
        self.curSliceLabel.setWordWrap(True)
        self.curSliceSlider = QSlider(constructRoi)
        self.curSliceSlider.setObjectName(u"curSliceSlider")
        self.curSliceSlider.setGeometry(QRect(369, 590, 191, 41))
        self.curSliceSlider.setOrientation(Qt.Horizontal)
        self.curSliceOfLabel = QLabel(constructRoi)
        self.curSliceOfLabel.setObjectName(u"curSliceOfLabel")
        self.curSliceOfLabel.setGeometry(QRect(665, 595, 41, 31))
        self.curSliceOfLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceOfLabel.setAlignment(Qt.AlignCenter)
        self.curSliceOfLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.curSliceTotal = QLabel(constructRoi)
        self.curSliceTotal.setObjectName(u"curSliceTotal")
        self.curSliceTotal.setGeometry(QRect(700, 595, 61, 31))
        self.curSliceTotal.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceTotal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.curSliceTotal.setTextInteractionFlags(Qt.NoTextInteraction)
        self.sidebar = QWidget(constructRoi)
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
        self.analysisParamsSidebar = QFrame(constructRoi)
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
        self.bmodePlane = QLabel(constructRoi)
        self.bmodePlane.setObjectName(u"bmodePlane")
        self.bmodePlane.setGeometry(QRect(360, 150, 381, 351))
        self.bmodeMaskLayer = QLabel(constructRoi)
        self.bmodeMaskLayer.setObjectName(u"bmodeMaskLayer")
        self.bmodeMaskLayer.setGeometry(QRect(360, 150, 381, 351))
        self.bmodeMaskLayer.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.cePlane = QLabel(constructRoi)
        self.cePlane.setObjectName(u"cePlane")
        self.cePlane.setGeometry(QRect(770, 150, 381, 351))
        self.mcBmodeDisplayLabel = QLabel(constructRoi)
        self.mcBmodeDisplayLabel.setObjectName(u"mcBmodeDisplayLabel")
        self.mcBmodeDisplayLabel.setGeometry(QRect(360, 150, 381, 351))
        self.mcBmodeDisplayLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.ceMaskLayer = QLabel(constructRoi)
        self.ceMaskLayer.setObjectName(u"ceMaskLayer")
        self.ceMaskLayer.setGeometry(QRect(770, 150, 381, 351))
        self.ceMaskLayer.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.mcCeDisplayLabel = QLabel(constructRoi)
        self.mcCeDisplayLabel.setObjectName(u"mcCeDisplayLabel")
        self.mcCeDisplayLabel.setGeometry(QRect(770, 150, 381, 351))
        self.mcCeDisplayLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.backButton = QPushButton(constructRoi)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 690, 131, 41))
        self.backButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.curSliceSpinBox = QSpinBox(constructRoi)
        self.curSliceSpinBox.setObjectName(u"curSliceSpinBox")
        self.curSliceSpinBox.setGeometry(QRect(620, 600, 48, 24))
        self.curSliceSpinBox.setStyleSheet(u"QSpinBox {\n"
"	background: white;\n"
"	color: black;\n"
"}")
        self.curSliceOfLabel_2 = QLabel(constructRoi)
        self.curSliceOfLabel_2.setObjectName(u"curSliceOfLabel_2")
        self.curSliceOfLabel_2.setGeometry(QRect(480, 660, 41, 31))
        self.curSliceOfLabel_2.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSliceOfLabel_2.setAlignment(Qt.AlignCenter)
        self.curSliceOfLabel_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.totalSecondsLabel = QLabel(constructRoi)
        self.totalSecondsLabel.setObjectName(u"totalSecondsLabel")
        self.totalSecondsLabel.setGeometry(QRect(515, 660, 61, 31))
        self.totalSecondsLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.totalSecondsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.totalSecondsLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.curSecondLabel = QLabel(constructRoi)
        self.curSecondLabel.setObjectName(u"curSecondLabel")
        self.curSecondLabel.setGeometry(QRect(420, 660, 61, 31))
        self.curSecondLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.curSecondLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.curSecondLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.secondsLabel = QLabel(constructRoi)
        self.secondsLabel.setObjectName(u"secondsLabel")
        self.secondsLabel.setGeometry(QRect(580, 660, 81, 31))
        self.secondsLabel.setStyleSheet(u"QLabel {\n"
"	font-size: 17px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.secondsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.secondsLabel.setTextInteractionFlags(Qt.NoTextInteraction)
        self.constructRoiLabel = QLabel(constructRoi)
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
        self.undoLastPtButton = QPushButton(constructRoi)
        self.undoLastPtButton.setObjectName(u"undoLastPtButton")
        self.undoLastPtButton.setGeometry(QRect(970, 570, 171, 41))
        self.undoLastPtButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.undoLastPtButton.setCheckable(False)
        self.closeRoiButton = QPushButton(constructRoi)
        self.closeRoiButton.setObjectName(u"closeRoiButton")
        self.closeRoiButton.setGeometry(QRect(780, 630, 171, 41))
        self.closeRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.closeRoiButton.setCheckable(False)
        self.redrawRoiButton = QPushButton(constructRoi)
        self.redrawRoiButton.setObjectName(u"redrawRoiButton")
        self.redrawRoiButton.setGeometry(QRect(780, 630, 171, 41))
        self.redrawRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.redrawRoiButton.setCheckable(False)
        self.drawRoiButton = QPushButton(constructRoi)
        self.drawRoiButton.setObjectName(u"drawRoiButton")
        self.drawRoiButton.setGeometry(QRect(780, 570, 171, 41))
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
        self.fitToRoiButton = QPushButton(constructRoi)
        self.fitToRoiButton.setObjectName(u"fitToRoiButton")
        self.fitToRoiButton.setGeometry(QRect(970, 630, 171, 41))
        self.fitToRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.fitToRoiButton.setCheckable(False)
        self.acceptGeneratedRoiButton = QPushButton(constructRoi)
        self.acceptGeneratedRoiButton.setObjectName(u"acceptGeneratedRoiButton")
        self.acceptGeneratedRoiButton.setGeometry(QRect(970, 600, 171, 41))
        self.acceptGeneratedRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.acceptGeneratedRoiButton.setCheckable(True)
        self.acceptGeneratedRoiButton.setChecked(False)
        self.roiFitNoteLabel = QLabel(constructRoi)
        self.roiFitNoteLabel.setObjectName(u"roiFitNoteLabel")
        self.roiFitNoteLabel.setGeometry(QRect(780, 690, 341, 41))
        self.roiFitNoteLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 0, 23);\n"
"	font-size: 20px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.roiFitNoteLabel.setAlignment(Qt.AlignCenter)
        self.bmodeCoverLabel = QLabel(constructRoi)
        self.bmodeCoverLabel.setObjectName(u"bmodeCoverLabel")
        self.bmodeCoverLabel.setGeometry(QRect(360, 150, 381, 351))
        self.bmodeCoverLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.ceCoverLabel = QLabel(constructRoi)
        self.ceCoverLabel.setObjectName(u"ceCoverLabel")
        self.ceCoverLabel.setGeometry(QRect(770, 150, 381, 351))
        self.ceCoverLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"}")
        self.undoRoiButton = QPushButton(constructRoi)
        self.undoRoiButton.setObjectName(u"undoRoiButton")
        self.undoRoiButton.setGeometry(QRect(780, 600, 171, 41))
        self.undoRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.undoRoiButton.setCheckable(True)
        self.undoRoiButton.setChecked(False)
        self.newRoiButton = QPushButton(constructRoi)
        self.newRoiButton.setObjectName(u"newRoiButton")
        self.newRoiButton.setGeometry(QRect(780, 600, 171, 41))
        self.newRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.newRoiButton.setCheckable(True)
        self.newRoiButton.setChecked(False)
        self.loadRoiButton = QPushButton(constructRoi)
        self.loadRoiButton.setObjectName(u"loadRoiButton")
        self.loadRoiButton.setGeometry(QRect(970, 600, 171, 41))
        self.loadRoiButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	background: rgb(90, 37, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.loadRoiButton.setCheckable(True)
        self.loadRoiButton.setChecked(False)

        self.retranslateUi(constructRoi)

        QMetaObject.connectSlotsByName(constructRoi)
    # setupUi

    def retranslateUi(self, constructRoi):
        constructRoi.setWindowTitle(QCoreApplication.translate("constructRoi", u"Select Region of Interest", None))
        self.axialPlaneLabel.setText(QCoreApplication.translate("constructRoi", u"B-Mode", None))
        self.sagittalPlaneLabel.setText(QCoreApplication.translate("constructRoi", u"Contrast-Enhanced Image", None))
        self.curSliceLabel.setText(QCoreApplication.translate("constructRoi", u"Current Frame:", None))
        self.curSliceOfLabel.setText(QCoreApplication.translate("constructRoi", u"of", None))
        self.curSliceTotal.setText(QCoreApplication.translate("constructRoi", u"0", None))
#if QT_CONFIG(tooltip)
        self.sidebar.setToolTip(QCoreApplication.translate("constructRoi", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.imageSelectionLabelSidebar.setText(QCoreApplication.translate("constructRoi", u"Image Selection:", None))
        self.imageLabel.setText(QCoreApplication.translate("constructRoi", u"Image:", None))
        self.imagePathInput.setText(QCoreApplication.translate("constructRoi", u"Sample filename ", None))
        self.roiSidebarLabel.setText(QCoreApplication.translate("constructRoi", u"Region of Interest (ROI) Selection", None))
        self.rfAnalysisLabel.setText(QCoreApplication.translate("constructRoi", u"Export Results", None))
        self.ticAnalysisLabel.setText(QCoreApplication.translate("constructRoi", u"Contrast-Enhanced Ultrasound\n"
"(CEUS) Analysis", None))
        self.analysisParamsLabel.setText(QCoreApplication.translate("constructRoi", u"TIC Modification", None))
        self.bmodePlane.setText("")
        self.bmodeMaskLayer.setText("")
        self.cePlane.setText("")
        self.mcBmodeDisplayLabel.setText("")
        self.ceMaskLayer.setText("")
        self.mcCeDisplayLabel.setText("")
        self.backButton.setText(QCoreApplication.translate("constructRoi", u"Back", None))
        self.curSliceOfLabel_2.setText(QCoreApplication.translate("constructRoi", u"of", None))
        self.totalSecondsLabel.setText(QCoreApplication.translate("constructRoi", u"0", None))
        self.curSecondLabel.setText(QCoreApplication.translate("constructRoi", u"0", None))
        self.secondsLabel.setText(QCoreApplication.translate("constructRoi", u"seconds", None))
        self.constructRoiLabel.setText(QCoreApplication.translate("constructRoi", u"Construct Region of Interest (ROI):", None))
        self.undoLastPtButton.setText(QCoreApplication.translate("constructRoi", u"Undo Last Point", None))
        self.closeRoiButton.setText(QCoreApplication.translate("constructRoi", u"Close ROI", None))
        self.redrawRoiButton.setText(QCoreApplication.translate("constructRoi", u"Redraw ROI", None))
        self.drawRoiButton.setText(QCoreApplication.translate("constructRoi", u"Draw ROI", None))
        self.fitToRoiButton.setText(QCoreApplication.translate("constructRoi", u"Fit to ROI", None))
        self.acceptGeneratedRoiButton.setText(QCoreApplication.translate("constructRoi", u"Accept Generated ROI", None))
        self.roiFitNoteLabel.setText(QCoreApplication.translate("constructRoi", u"NOTE: Will fit to ROI using current\n"
"frame as reference", None))
        self.bmodeCoverLabel.setText("")
        self.ceCoverLabel.setText("")
        self.undoRoiButton.setText(QCoreApplication.translate("constructRoi", u"Undo", None))
        self.newRoiButton.setText(QCoreApplication.translate("constructRoi", u"New ROI", None))
        self.loadRoiButton.setText(QCoreApplication.translate("constructRoi", u"Load ROI", None))
    # retranslateUi

