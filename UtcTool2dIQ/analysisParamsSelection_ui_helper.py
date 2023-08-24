from UtcTool2dIQ.analysisParamsSelection_ui import *
from UtcTool2dIQ.rfAnalysis_ui_helper import *
import os
from Utils.roiFuncs import *

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog

def selectImageHelper(pathInput):
    if not os.path.exists(pathInput.text()): # check if file path is manually typed
        # NOTE: .bin is currently not supported
        fileName, _ = QFileDialog.getOpenFileName(None, 'Open File', filter = '*.rf *.mat')
        if fileName != '': # If valid file is chosen
            pathInput.setText(fileName)
        else:
            return


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
        self.rfAnalysisGUI.axialWinSize = self.axWinSizeVal.value()
        self.rfAnalysisGUI.lateralWinSize = self.latWinSizeVal.value()
        self.rfAnalysisGUI.axialOverlap = self.axOverlapVal.value()/100
        self.rfAnalysisGUI.lateralOverlap = self.latOverlapVal.value()/100
        self.rfAnalysisGUI.threshold = self.windowThresholdVal.value()
        self.rfAnalysisGUI.editImageDisplayGUI.contrastVal.setValue(self.lastGui.editImageDisplayGUI.contrastVal.value())
        self.rfAnalysisGUI.editImageDisplayGUI.brightnessVal.setValue(self.lastGui.editImageDisplayGUI.brightnessVal.value())
        self.rfAnalysisGUI.editImageDisplayGUI.sharpnessVal.setValue(self.lastGui.editImageDisplayGUI.sharpnessVal.value())
        self.rfAnalysisGUI.editImageDisplayGUI.contrastVal.valueChanged.connect(self.lastGui.analysisParamsGUI.rfAnalysisGUI.changeContrast)
        self.rfAnalysisGUI.editImageDisplayGUI.brightnessVal.valueChanged.connect(self.rfAnalysisGUI.changeBrightness)    
        self.rfAnalysisGUI.editImageDisplayGUI.sharpnessVal.valueChanged.connect(self.rfAnalysisGUI.changeSharpness)
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