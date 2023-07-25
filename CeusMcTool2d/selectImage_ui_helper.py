from CeusMcTool2d.selectImage_ui import *
from CeusMcTool2d.roiSelection_ui_helper import *

import os
from pathlib import Path
import Utils.utils as ut
import pandas as pd

def selectImageHelper(pathInput):
    if not os.path.exists(pathInput.text()): # check if file path is manually typed
        # NOTE: .bin is currently not supported
        fileName, _ = QFileDialog.getOpenFileName(None, 'Open File', filter = '*.rf *.mat')
        if fileName != '': # If valid file is chosen
            pathInput.setText(fileName)
        else:
            return


class SelectImageGUI_CeusMcTool2d(Ui_selectImage, QWidget):
    def __init__(self):
        # self.selectImage = QWidget()
        super().__init__()
        self.setupUi(self)
        self.imageFilenameDisplay.setHidden(True)
        self.selectImageErrorMsg.setHidden(True)
        self.imagesScrollArea.setHidden(True)
        self.undoSpreadsheetButton.setHidden(True)
        self.generateImageButton.setHidden(True)
        header = self.imagesScrollArea.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setStyleSheet("""
        QHeaderView::section{
            background-color: white;
            font-size: 15px;
            color: black;
        }""")
        self.imagesScrollArea.verticalHeader().setStyleSheet("""
        QHeaderView::section{
            background-color: white;
            font-size: 15px;
            color: black;
        }
        QHeaderView::section::selected{
            background-color: pink;
            font-size: 14px;
            color: black
            font-weight: bold;
        }""")

        self.imageNifti = 0

        self.roiSelectionGui = None
        self.welcomeGui = None

        self.generateImageButton.clicked.connect(self.moveToRoiSelection)
        self.chooseSpreadsheetFileButton.clicked.connect(self.getSpreadsheetPath)
        self.clearSpreadsheetFileButton.clicked.connect(self.clearSpreadsheetPath)
        self.findImagesButton.clicked.connect(self.listImages)
        self.backButton.clicked.connect(self.backToWelcomeScreen)
        self.undoSpreadsheetButton.clicked.connect(self.undoSpreadsheetEntry)

    def undoSpreadsheetEntry(self):
        self.imagesScrollArea.clearContents()
        self.imagesScrollArea.setHidden(True)
        self.spreadsheetPath.clear()
        self.spreadsheetPath.setHidden(False)
        self.chooseSpreadsheetFileButton.setHidden(False)
        self.clearSpreadsheetFileButton.setHidden(False)
        self.findImagesButton.setHidden(False)
        self.generateImageButton.setHidden(True)
        self.undoSpreadsheetButton.setHidden(True)
        self.selectSpreadsheeetLabel.setHidden(False)

    def listImages(self):
        if len(self.spreadsheetPath.text()):
            self.df = pd.read_excel(self.spreadsheetPath.text())
            patients = self.df['patient_code'].to_string(index=False)
            scans = self.df['cleaned_path']
            self.patients = patients.splitlines()
            self.scans = [scan.split('/')[-1][:-4] for scan in scans]

            self.imagesScrollArea.setHidden(False)
            self.selectSpreadsheeetLabel.setHidden(True)
            self.spreadsheetPath.setHidden(True)
            self.chooseSpreadsheetFileButton.setHidden(True)
            self.clearSpreadsheetFileButton.setHidden(True)
            self.findImagesButton.setHidden(True)
            self.undoSpreadsheetButton.setHidden(False)
            self.generateImageButton.setHidden(False)

            self.imagesScrollArea.setRowCount(len(self.patients))
            self.imagesScrollArea.setVerticalHeaderLabels(self.patients)

            for i in range(len(self.patients)):
                item = QTableWidgetItem(self.scans[i])
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.imagesScrollArea.setItem(i, 0, item)


    def backToWelcomeScreen(self):
        self.welcomeGui.show()
        self.hide()

    def getSpreadsheetPath(self):
        fileName, _ = QFileDialog.getOpenFileName(None, 'Open File', filter = '*.xlsx')
        if fileName != '':
            self.spreadsheetPath.setText(fileName)

    def clearSpreadsheetPath(self):
        self.spreadsheetPath.setText('')

    def moveToRoiSelection(self):
        selected = self.imagesScrollArea.selectedIndexes()
        if len(selected) == 1:
            index = selected[0].row()
            del self.roiSelectionGui
            self.roiSelectionGui = RoiSelectionGUI()
            self.roiSelectionGui.setFilenameDisplays(self.scans[index])
            self.roiSelectionGui.df = self.df
            xcel_dir = Path(self.spreadsheetPath.text())
            xcel_dir = xcel_dir.parent.absolute()
            self.roiSelectionGui.openImage(index, xcel_dir)
            self.roiSelectionGui.lastGui = self
            self.roiSelectionGui.show()
            self.hide()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # selectWindow = QWidget()
    ui = SelectImageGUI_CeusMcTool2d()
    # ui.selectImage.show()
    ui.show()
    sys.exit(app.exec_())