from UtcTool2d.analysisParamsSelection_ui import *
from UtcTool2d.rfAnalysis_ui_helper import *
import os
from Utils.roiFuncs import *

from PyQt5.QtWidgets import QWidget, QApplication


class AnalysisParamsGUI(Ui_analysisParams, QWidget):
    def __init__(self):
        # self.selectImage = QWidget()
        super().__init__()
        self.setupUi(self)

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
        self.rfAnalysisGUI.minFrequency = self.lastGui.imgInfoStruct.minFrequency #Hz
        self.rfAnalysisGUI.maxFrequency = self.lastGui.imgInfoStruct.maxFrequency #Hz
        self.rfAnalysisGUI.samplingFreq = self.lastGui.imgInfoStruct.samplingFrequency # Hz
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