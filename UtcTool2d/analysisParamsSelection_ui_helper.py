from UtcTool2d.analysisParamsSelection_ui import *
from UtcTool2d.rfAnalysis_ui_helper import *
import os
from Utils.roiFuncs import *

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

        self.continueButton.clicked.connect(self.continueToRfAnalysis)
        self.backButton.clicked.connect(self.backToLastScreen)

    def backToLastScreen(self):
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
        self.rfAnalysisGUI.frame = self.frame
        # self.rfAnalysisGUI.imArray = self.imArray
        self.rfAnalysisGUI.editImageDisplayButton.setHidden(True)
        self.rfAnalysisGUI.axialWinSize = self.axWinSizeVal.value()
        self.rfAnalysisGUI.lateralWinSize = self.latWinSizeVal.value()
        self.rfAnalysisGUI.axialOverlap = self.axOverlapVal.value()/100
        self.rfAnalysisGUI.lateralOverlap = self.latOverlapVal.value()/100
        self.rfAnalysisGUI.threshold = self.clipFactorVal.value()
        self.rfAnalysisGUI.minFrequency = self.minFreqVal.value()*1000000 # MHz -> Hz
        self.rfAnalysisGUI.maxFrequency = self.maxFreqVal.value()*1000000 # MHz -> Hz
        self.rfAnalysisGUI.samplingFreq = self.samplingFreqVal.value()*1000000 # MHz -> Hz
        self.rfAnalysisGUI.setFilenameDisplays(self.imagePathInput.text().split('/')[-1], self.phantomPathInput.text().split('/')[-1])
        # self.rfAnalysisGUI.paramapCoverImg = np.zeros([self.imArray.shape[1], self.imArray.shape[2], 4])
        # self.rfAnalysisGUI.maskCoverImg = np.zeros([501, 721, 4])
        # self.rfAnalysisGUI.xSpline = self.finalSplineX
        # self.rfAnalysisGUI.ySpline = self.finalSplineY
        self.rfAnalysisGUI.displayROIWindows()
        self.rfAnalysisGUI.show()
        self.rfAnalysisGUI.lastGui = self
        self.hide()

            #      self.analysisParamsGUI.axWinSizeVal.setValue(10)#7#1#1480/20000000*10000 # must be at least 10 times wavelength
            # self.analysisParamsGUI.latWinSizeVal.setValue(10)#7#1#1480/20000000*10000 # must be at least 10 times wavelength
            # self.analysisParamsGUI.axOverlapVal.setValue(5)
            # self.analysisParamsGUI.latOverlapVal.setValue(5)
            # self.analysisParamsGUI.minFreqVal.setValue(3)
            # self.analysisParamsGUI.maxFreqVal.setValue(4.5)
            # self.analysisParamsGUI.startDepthVal.setValue(0.04)
            # self.analysisParamsGUI.endDepthVal.setValue(0.16)
            # self.analysisParamsGUI.clipFactorVal.setValue(95)
            # self.analysisParamsGUI.samplingFreqVal.setValue(20)
            # self.analysisParamsGUI.frameVal.setValue(self.frame)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # selectWindow = QWidget()
    ui = AnalysisParamsGUI()
    # ui.selectImage.show()
    ui.show()
    sys.exit(app.exec_())