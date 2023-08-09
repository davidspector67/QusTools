from UtcTool2d.loadRoi_ui import *
import os
import csv

class LoadRoiGUI(Ui_loadRoi, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chooseRoiGUI = None

        self.chooseFileButton.clicked.connect(self.chooseFile)
        self.clearFileButton.clicked.connect(self.clearFile)
        self.openRoiButton.clicked.connect(self.getRoiPath)
        self.backButton.clicked.connect(self.backToChoice)

    def backToChoice(self):
        self.hide()
        self.chooseRoiGUI.show()

    def chooseFile(self):
        fileName, _ = QFileDialog.getOpenFileName(None, 'Open file', filter = '*.csv')
        if fileName != '':
            self.roiPathInput.setText(fileName)

    def clearFile(self):
        self.roiPathInput.clear()
    
    def getRoiPath(self):
        if os.path.exists(self.roiPathInput.text()):
            imageName = ''
            with open(self.roiPathInput.text(), mode='r') as csvfile:
                reader = csv.reader(csvfile)
                line_count = 0
                for row in reader:
                    if line_count == 1:
                        imageName = row[0]
                        self.chooseRoiGUI.curPointsPlottedX = row[1]
                        self.chooseRoiGUI.curPointsPlottedY = row[2]
                        break
                    line_count += 1
            if imageName != self.chooseRoiGUI.imagePathInput.text():
                self.chooseRoiGUI.curPointsPlottedX = []
                self.chooseRoiGUI.curPointsPlottedY = []
                print("Selected ROI for wrong image")
                return
            self.chooseRoiGUI.closeInterpolation()
            self.hide()
            self.chooseRoiGUI.show()
