from UtcTool2d.analysisParamsSelection_ui import *
from UtcTool2d.rfAnalysis_ui_helper import *
import os
from Utils.roiFuncs import *

from PyQt5.QtWidgets import QWidget, QApplication

import platform
system = platform.system()


class AnalysisParamsGUI(Ui_analysisParams, QWidget):
    def __init__(self):
        # self.selectImage = QWidget()
        super().__init__()
        self.setupUi(self)

        if system == 'Windows':
            self.roiSidebarLabel.setStyleSheet("""QLabel { 
                font-size: 18px; 
                color: rgb(255, 255, 255); 
                background-color: rgba(255, 255, 255, 0); 
                border: 0px; 
                font-weight: bold; 
            }""")
            self.imageSelectionLabelSidebar.setStyleSheet("""QLabel {
                font-size: 18px;
                color: rgb(255, 255, 255);
                background-color: rgba(255, 255, 255, 0);
                border: 0px;
                font-weight: bold;
            }""")
            self.imageLabel.setStyleSheet("""QLabel {
                font-size: 13px;
                color: rgb(255, 255, 255);
                background-color: rgba(255, 255, 255, 0);
                border: 0px;
                font-weight: bold;
            }""")
            self.phantomLabel.setStyleSheet("""QLabel {
                font-size: 13px;
                color: rgb(255, 255, 255);
                background-color: rgba(255, 255, 255, 0);
                border: 0px;
                font-weight: bold;
            }""")
            self.imagePathInput.setStyleSheet("""QLabel {
                font-size: 11px;
                color: rgb(255, 255, 255);
                background-color: rgba(255, 255, 255, 0);
                border: 0px;
            }""")
            self.phantomPathInput.setStyleSheet("""QLabel {
                font-size: 11px;
                color: rgb(255, 255, 255);
                background-color: rgba(255, 255, 255, 0);
                border: 0px;
            }""")
            self.analysisParamsLabel.setStyleSheet("""QLabel {
                font-size: 18px;
                color: rgb(255, 255, 255);
                background-color: rgba(255, 255, 255, 0);
                border: 0px;
                font-weight:bold;
            }""")
            self.rfAnalysisLabel.setStyleSheet("""QLabel {
                font-size: 18px;
                color: rgb(255, 255, 255);
                background-color: rgba(255, 255, 255, 0);
                border: 0px;
                font-weight:bold;
            }""")
            self.exportResultsLabel.setStyleSheet("""QLabel {
                font-size: 18px;
                color: rgb(255, 255, 255);
                background-color: rgba(255, 255, 255, 0);
                border: 0px;
                font-weight:bold;
            }""")
            self.imageDepthLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.imageWidthLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.imageDepthVal.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.imageWidthVal.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.axWinSizeLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.latWinSizeLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.axOverlapLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.latOverlapLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.windowThresholdLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.minFreqLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.maxFreqLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.lowBandFreqLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.upBandFreqLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")
            self.samplingFreqLabel.setStyleSheet("""QLabel {
                color: white;
                background-color: rgba(0,0,0,0);
                font-size: 18px;
            }""")

        self.rfAnalysisGUI = None
        self.lastGui = None
        self.finalSplineX = None
        self.finalSplineY = None
        self.frame = None
        self.imArray = None
        self.dataFrame = None
        self.curPointsPlottedX = None
        self.curPointsPlottedY = None

        self.continueButton.clicked.connect(self.continueToRfAnalysis)
        self.backButton.clicked.connect(self.backToLastScreen)

    def backToLastScreen(self):
        self.lastGui.dataFrame = self.dataFrame
        self.lastGui.show()
        self.hide()

    def setFilenameDisplays(self, imageName, phantomName):
        self.imagePathInput.setHidden(False)
        self.phantomPathInput.setHidden(False)
        self.imagePathInput.setText(imageName)
        self.phantomPathInput.setText(phantomName)

    def continueToRfAnalysis(self):
        del self.rfAnalysisGUI
        self.rfAnalysisGUI = RfAnalysisGUI(self.finalSplineX, self.finalSplineY)
        self.rfAnalysisGUI.imgDataStruct = self.lastGui.imgDataStruct
        self.rfAnalysisGUI.imgInfoStruct = self.lastGui.imgInfoStruct
        self.rfAnalysisGUI.refDataStruct = self.lastGui.refDataStruct
        self.rfAnalysisGUI.refInfoStruct = self.lastGui.refInfoStruct
        self.rfAnalysisGUI.curPointsPlottedX = self.curPointsPlottedX
        self.rfAnalysisGUI.curPointsPlottedY = self.curPointsPlottedY
        self.rfAnalysisGUI.dataFrame = self.dataFrame
        self.rfAnalysisGUI.frame = self.frame
        self.rfAnalysisGUI.axialWinSize = self.axWinSizeVal.value()
        self.rfAnalysisGUI.lateralWinSize = self.latWinSizeVal.value()
        self.rfAnalysisGUI.axialOverlap = self.axOverlapVal.value()/100
        self.rfAnalysisGUI.lateralOverlap = self.latOverlapVal.value()/100
        self.rfAnalysisGUI.windowThreshold = self.windowThresholdVal.value()
        self.rfAnalysisGUI.minFrequency = self.minFreqVal.value()*1000000 #Hz
        self.rfAnalysisGUI.maxFrequency = self.maxFreqVal.value()*1000000 #Hz
        self.rfAnalysisGUI.samplingFreq = self.samplingFreqVal.value()*1000000 # Hz
        self.rfAnalysisGUI.upBandFreq = self.upBandFreqVal.value()*1000000 #Hz
        self.rfAnalysisGUI.lowBandFreq = self.lowBandFreqVal.value()*1000000 #Hz
        self.rfAnalysisGUI.setFilenameDisplays(self.imagePathInput.text().split('/')[-1], self.phantomPathInput.text().split('/')[-1])
        self.rfAnalysisGUI.displayROIWindows()
        self.rfAnalysisGUI.show()
        self.rfAnalysisGUI.lastGui = self
        self.hide()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # selectWindow = QWidget()
    ui = AnalysisParamsGUI()
    # ui.selectImage.show()
    ui.show()
    sys.exit(app.exec_())