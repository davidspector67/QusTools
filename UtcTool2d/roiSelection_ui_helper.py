from UtcTool2d.roiSelection_ui import *
from UtcTool2d.editImageDisplay_ui_helper import *
from UtcTool2d.analysisParamsSelection_ui_helper import *
from UtcTool2d.rfAnalysis_ui_helper import *
import Parsers.philipsMatParser as matParser
import Parsers.siemensRfdParser as rfdParser
from Parsers.philipsRfParser import main_parser_stanford

import pydicom
import os
import numpy as np
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
import scipy.interpolate as interpolate


class RoiSelectionGUI(QWidget, Ui_constructRoi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.curPointsPlottedX = []
        self.curPointsPlottedY = []
        self.finalSplineX = []
        self.finalSplineY = []
        self.oldSpline = []
        self.imagePathInput.setHidden(True)
        self.phantomPathInput.setHidden(True)
        self.ofFramesLabel.setHidden(True)
        self.curFrameLabel.setHidden(True)
        self.totalFramesLabel.setHidden(True)
        self.curFrameSlider.setHidden(True)

        self.editImageDisplayButton.setHidden(True)

        self.imCoverPixmap = QPixmap(721, 501)
        self.imCoverPixmap.fill(Qt.transparent)
        self.imCoverFrame.setPixmap(self.imCoverPixmap)

        self.lastGui = None
        self.imArray = None
        self.axWinSizeVal = None
        self.latWinSizeVal = None
        self.axOverlapVal = None
        self.latOverlapVal = None
        self.minFreqVal = None
        self.maxFreqVal = None
        self.startDepthVal = None
        self.endDepthVal = None
        self.clipFactorVal = None
        self.samplingFreqVal = None
        self.analysisParamsGUI = None
        self.maskCoverImg = None
        self.dataFrame = None

        self.scatteredPoints = []

        self.redrawRoiButton.setHidden(True)
        
        self.undoLastPtButton.clicked.connect(self.undoLastPt)
        self.closeRoiButton.clicked.connect(self.closeInterpolation)
        self.redrawRoiButton.clicked.connect(self.undoLastRoi)
        self.acceptRoiButton.clicked.connect(self.acceptROI)
        self.backButton.clicked.connect(self.backToLastScreen)

    def backToLastScreen(self):
        self.lastGui.dataFrame = self.dataFrame
        self.lastGui.show()
        self.hide()

    def mousePressEvent(self,event):
        self.xCur = event.x()
        self.yCur = event.y()
        if self.drawRoiButton.isChecked():
            # Plot ROI points
            if self.xCur < 1121 and self.xCur > 400 and self.yCur < 671 and self.yCur > 170:
                self.actualX = int((self.xCur - 401)*(self.imData.shape[1])/721)
                self.actualY = int((self.yCur - 171)*(self.imData.shape[0])/501)
                plotY = self.xCur - 401
                plotX = self.yCur - 171
            else:
                return
            self.finalSplineX.append(self.actualX)
            self.finalSplineY.append(self.actualY)
            self.curPointsPlottedX.append(plotX)
            self.curPointsPlottedY.append(plotY)
            self.updateSpline()

    def updateSpline(self):
        self.maskCoverImg.fill(0)
        if len(self.curPointsPlottedX) > 0:            
            if len(self.curPointsPlottedX) > 1:
                xSpline, ySpline = calculateSpline(self.curPointsPlottedX, self.curPointsPlottedY)
                spline = [(int(xSpline[i]), int(ySpline[i])) for i in range(len(xSpline))]
                spline = np.array([*set(spline)])
                xSpline, ySpline = np.transpose(spline)
                xSpline = np.clip(xSpline, a_min=0, a_max=500)
                ySpline = np.clip(ySpline, a_min=0, a_max=720)
                for i in range(len(xSpline)):
                    self.maskCoverImg[xSpline[i]-1:xSpline[i]+2, ySpline[i]-1:ySpline[i]+2] = [255, 255, 0, 255]

            for i in range(len(self.curPointsPlottedX)):
                self.maskCoverImg[self.curPointsPlottedX[i]-2:self.curPointsPlottedX[i]+3, \
                                    self.curPointsPlottedY[i]-2:self.curPointsPlottedY[i]+3] = [0,0,255, 255]

        self.plotOnCanvas()
        self.updateCrosshair()

    def mouseMoveEvent(self, event):
        self.xCur = event.x()
        self.yCur = event.y()
        self.updateCrosshair()

    def updateCrosshair(self):
        if self.xCur < 1121 and self.xCur > 400 and self.yCur < 671 and self.yCur > 170:
            plotX = self.xCur - 401
        else:
            return
        
        plotY = self.yCur - 171
        self.imCoverFrame.pixmap().fill(Qt.transparent)
        painter = QPainter(self.imCoverFrame.pixmap())
        painter.setPen(Qt.yellow)
        bmodeVertLine = QLine(plotX, 0, plotX, 501)
        bmodeLatLine = QLine(0, plotY, 721, plotY)
        painter.drawLines([bmodeVertLine, bmodeLatLine])
        painter.end()
        self.update()

    def setFilenameDisplays(self, imageName, phantomName):
        self.imagePathInput.setHidden(False)
        self.phantomPathInput.setHidden(False)
        self.imagePathInput.setText(imageName)
        self.phantomPathInput.setText(phantomName)
    
    def plotOnCanvas(self): # Plot current image on GUI
        self.imData = np.array(self.imArray[self.frame]).reshape(self.arHeight, self.arWidth)
        self.imData = np.require(self.imData,np.uint8,'C')
        self.bytesLine = self.imData.strides[0]
        self.arHeight = self.imData.shape[0]
        self.arWidth = self.imData.shape[1]

        self.maskCoverImg = np.require(self.maskCoverImg, np.uint8, 'C')
        self.bytesLineMask, _ = self.maskCoverImg[:,:,0].strides
        self.qImgMask = QImage(self.maskCoverImg, self.maskCoverImg.shape[1], self.maskCoverImg.shape[0], self.bytesLineMask, QImage.Format_ARGB32)

        self.imMaskFrame.setPixmap(QPixmap.fromImage(self.qImgMask).scaled(721, 501))

        self.qIm = QImage(self.imData, self.arWidth, self.arHeight, self.bytesLine, QImage.Format_Grayscale8)
        self.imDisplayFrame.setPixmap(QPixmap.fromImage(self.qIm).scaled(721, 501))

    def openImage(self, imageFilePath, phantomFilePath): # Open initial image given data and phantom files previously inputted
        # Assume inputted files are correct 
        # TODO: implement this in image selection page
        # For now, Canon .bin files are not supported
        tmpLocation = imageFilePath.split("/")
        dataFileName = tmpLocation[-1]
        dataFileLocation = imageFilePath[:len(imageFilePath)-len(dataFileName)]
        tmpPhantLocation = phantomFilePath.split("/")
        phantFileName = tmpPhantLocation[-1]
        phantFileLocation = phantomFilePath[:len(phantomFilePath)-len(phantFileName)]
        if dataFileName[-3:] == ".rf": # Check binary signatures at start of .rf files
            dataFile = open(imageFilePath, 'rb')
            datasig = list(dataFile.read(8))
            if datasig != [0,0,0,0,255,255,0,0]: # Philips signature parameters
                # self.invalidPath.setText("Data and Phantom files are both invalid.\nPlease use Philips .rf files.")
                return
            elif datasig != [0,0,0,0,255,255,0,0]:
                # self.invalidPath.setText("Invalid phantom file.\nPlease use Philips .rf files.")
                return
            else: # Display Philips image and assign relevant default analysis
                main_parser_stanford(imageFilePath) # parse image filee

                dataFileName = str(dataFileName[:-3]+'.mat')

        if phantFileName[-3:] == ".rf": # Check binary signatures at start of .rf files
            phantFile = open(phantomFilePath, 'rb')
            phantsig = list(phantFile.read(8))
            if phantsig != [0,0,0,0,255,255,0,0]: # Philips signature parameters
                # self.invalidPath.setText("Data and Phantom files are both invalid.\nPlease use Philips .rf files.")
                return
            elif phantsig != [0,0,0,0,255,255,0,0]:
                # self.invalidPath.setText("Invalid phantom file.\nPlease use Philips .rf files.")
                return
            else: # Display Philips image and assign relevant default analysis
                main_parser_stanford(imageFilePath) # parse image filee

                phantFileName = str(phantFileName[:-3]+'.mat')

        if dataFileName[-4:] == ".mat" and phantFileName[-4:] == ".mat": # Display Philips image and assign relevant default analysis params
            self.frame = 0
            imArray, self.imgDataStruct, self.imgInfoStruct, self.refDataStruct, self.refInfoStruct = matParser.getImage(dataFileName, dataFileLocation, phantFileName, phantFileLocation, self.frame)
            self.arHeight = imArray.shape[0]
            self.arWidth = imArray.shape[1]
            self.imData = np.array(imArray).reshape(self.arHeight, self.arWidth)
            self.imData = np.flipud(self.imData) #flipud
            self.imData = np.require(self.imData,np.uint8,'C')
            self.bytesLine = self.imData.strides[0]
            self.qIm = QImage(self.imData, self.arWidth, self.arHeight, self.bytesLine, QImage.Format_Grayscale8).scaled(721, 501)

            self.qIm.mirrored().save(os.path.join("Junk", "bModeImRaw.png")) # Save as .png file

            self.pixSizeAx = self.imgDataStruct.bMode.shape[0] #were both scBmode
            self.pixSizeLat = self.imgDataStruct.bMode.shape[1]

            self.axWinSizeVal = 10#7#1#1480/20000000*10000 # must be at least 10 times wavelength
            self.latWinSizeVal = 10#7#1#1480/20000000*10000 # must be at least 10 times wavelength
            self.axOverlapVal = 50
            self.latOverlapVal = 50
            self.minFreqVal = 3
            self.maxFreqVal = 4.5
            self.startDepthVal = 0.04
            self.endDepthVal = 0.16
            self.clipFactorVal = 95
            self.samplingFreqVal = 20

        elif dataFileName[-4:] == ".rfd" and phantFileName[-4:] == ".rfd": # Display Philips image and assign relevant default analysis params
            self.imArray, self.imgDataStruct, self.imgInfoStruct, self.refDataStruct, self.refInfoStruct = rfdParser.getImage(dataFileName, dataFileLocation, phantFileName, phantFileLocation)
            self.frame = 0
            self.imData = np.array(self.imArray[self.frame]).reshape(self.imArray.shape[1], self.imArray.shape[2])
            self.imData = np.require(self.imData,np.uint8,'C')
            self.maskCoverImg = np.zeros([501, 721, 4])
            self.bytesLine = self.imData.strides[0]
            self.arHeight = self.imData.shape[0]
            self.arWidth = self.imData.shape[1]
            self.qIm = QImage(self.imData, self.arWidth, self.arHeight, self.bytesLine, QImage.Format_Grayscale8)

            self.imDisplayFrame.setPixmap(QPixmap.fromImage(self.qIm).scaled(721, 501))

            self.pixSizeAx = self.imgDataStruct.bMode.shape[0] #were both scBmode
            self.pixSizeLat = self.imgDataStruct.bMode.shape[1]

            self.ofFramesLabel.setHidden(False)
            self.curFrameLabel.setHidden(False)
            self.totalFramesLabel.setHidden(False)
            self.curFrameSlider.setHidden(False)
            self.curFrameSlider.setMaximum(self.imArray.shape[0]-1)
            self.totalFramesLabel.setText(str(self.imArray.shape[0]-1))
            self.curFrameSlider.valueChanged.connect(self.curFrameChanged)

            self.axOverlapVal = 50
            self.latOverlapVal = 50
            self.startDepthVal = 0.04
            self.endDepthVal = 0.16
            self.clipFactorVal = 95
            self.minFreqVal = 7
            self.maxFreqVal = 17
            self.axWinSizeVal = 3.5#1480/40000000*5000 # must be at least 10 times wavelength
            self.latWinSizeVal = 3.5#self.axialWinSize * 6 # must be at least 10 times wavelength
            self.samplingFreqVal = 40

        elif imageFilePath.endswith(".dcm"):
            ds = pydicom.dcmread(imageFilePath)
            imArray = ds.pixel_array

            self.arHeight = imArray.shape[0]
            self.arWidth = imArray.shape[1]
            self.imData = np.array(imArray).reshape(self.arHeight, self.arWidth, 3)
            self.imData = np.flipud(self.imData) #flipud
            self.imData = np.require(self.imData,np.uint8,'C')
            self.bytesLine = self.imData.strides[0]
            self.qIm = QImage(self.imData, self.arWidth, self.arHeight, self.bytesLine, QImage.Format_RGB888) 

            self.qIm.mirrored().save(os.path.join("Junk", "bModeImRaw.png")) # Save as .png file

            self.pixSizeAx = self.arHeight
            self.pixSizeLat = self.arWidth

            self.editImageDisplayGUI.contrastVal.setValue(1)
            self.editImageDisplayGUI.brightnessVal.setValue(1)
            self.editImageDisplayGUI.sharpnessVal.setValue(1)

        else:
            return
        
        self.plotOnCanvas()

    def curFrameChanged(self):
        self.frame = self.curFrameSlider.value()
        self.curFrameLabel.setText(str(self.frame))
        self.plotOnCanvas()

    def closeInterpolation(self): # Finish drawing ROI
        if len(self.curPointsPlottedX) > 2:
            self.drawRoiButton.setChecked(False)

            # remove duplicate points
            points = np.transpose(np.array([self.curPointsPlottedX, self.curPointsPlottedY]))
            points = removeDuplicates(points)
            [self.curPointsPlottedX, self.curPointsPlottedY] = np.transpose(points)
            points = np.transpose(np.array([self.finalSplineX, self.finalSplineY]))
            points = removeDuplicates(points)
            [self.finalSplineX, self.finalSplineY] = np.transpose(points)
            self.curPointsPlottedX = list(self.curPointsPlottedX)
            self.curPointsPlottedY = list(self.curPointsPlottedY)
            self.finalSplineX = list(self.finalSplineX)
            self.finalSplineY = list(self.finalSplineY)
            self.curPointsPlottedX.append(self.curPointsPlottedX[0])
            self.curPointsPlottedY.append(self.curPointsPlottedY[0])
            self.finalSplineX.append(self.finalSplineX[0])
            self.finalSplineY.append(self.finalSplineY[0])
            self.maskCoverImg.fill(0)

            xSpline, ySpline = calculateSpline(self.curPointsPlottedX, self.curPointsPlottedY)
            self.xSpline = xSpline
            self.ySpline = ySpline
            spline = [(int(xSpline[i]), int(ySpline[i])) for i in range(len(xSpline))]
            spline = np.array([*set(spline)])
            xSpline, ySpline = np.transpose(spline)
            xSpline = np.clip(xSpline, a_min=0, a_max=500)
            ySpline = np.clip(ySpline, a_min=0, a_max=720)
            for i in range(len(xSpline)):
                self.maskCoverImg[xSpline[i]-1:xSpline[i]+2, ySpline[i]-1:ySpline[i]+2] = [0, 0, 255, 255]
            self.curPointsPlottedX = []
            self.curPointsPlottedY = []
            self.drawRoiButton.setChecked(False)
            self.drawRoiButton.setCheckable(False)
            self.redrawRoiButton.setHidden(False)
            self.closeRoiButton.setHidden(True)
            self.plotOnCanvas()

    def undoLastPt(self):
        if len(self.curPointsPlottedX):
            self.maskCoverImg[self.curPointsPlottedX[-1]-2:self.curPointsPlottedX[-1]+3, \
                            self.curPointsPlottedY[-1]-2:self.curPointsPlottedY[-1]+3] = [0,0,0,0]
            self.curPointsPlottedX.pop()
            self.curPointsPlottedY.pop()
            self.finalSplineX.pop()
            self.finalSplineY.pop()
            self.updateSpline()

    def undoLastRoi(self):
        if not self.drawRoiButton.isCheckable():
            self.curPointsPlottedX = []
            self.curPointsPlottedY = []
            self.finalSplineX = []
            self.finalSplineY = []
            self.drawRoiButton.setCheckable(True)
            self.redrawRoiButton.setHidden(True)
            self.closeRoiButton.setHidden(False)
            self.maskCoverImg.fill(0)
            self.plotOnCanvas()
            self.update()

    def acceptROI(self):
        if len(self.finalSplineX):
            del self.analysisParamsGUI

            imData = np.array(self.imArray[self.frame]).reshape(self.arHeight, self.arWidth)
            imData = np.flipud(imData)
            imData = np.require(imData, np.uint8, 'C')
            bytesLine = imData.strides[0]
            arHeight = imData.shape[0]
            arWidth = imData.shape[1]
            savedIm = QImage(imData, arWidth, arHeight, bytesLine, QImage.Format_Grayscale8).scaled(721, 501)

            savedIm.mirrored().save(os.path.join("Junk", "bModeImRaw.png"))
            savedIm.mirrored().save(os.path.join("Junk", "bModeIm.png"))
            self.analysisParamsGUI = AnalysisParamsGUI()
            self.analysisParamsGUI.axWinSizeVal.setValue(self.axWinSizeVal)
            self.analysisParamsGUI.latWinSizeVal.setValue(self.latWinSizeVal)
            self.analysisParamsGUI.axOverlapVal.setValue(self.axOverlapVal)
            self.analysisParamsGUI.latOverlapVal.setValue(self.latOverlapVal)
            self.analysisParamsGUI.minFreqVal.setValue(self.minFreqVal)
            self.analysisParamsGUI.maxFreqVal.setValue(self.maxFreqVal)
            # self.analysisParamsGUI.startDepthVal.setValue(self.startDepthVal)
            # self.analysisParamsGUI.endDepthVal.setValue(self.endDepthVal)
            self.analysisParamsGUI.clipFactorVal.setValue(self.clipFactorVal)
            self.analysisParamsGUI.samplingFreqVal.setValue(self.samplingFreqVal)
            self.analysisParamsGUI.finalSplineX = self.ySpline
            self.analysisParamsGUI.finalSplineY = self.xSpline
            self.analysisParamsGUI.frame = self.frame
            self.analysisParamsGUI.imArray = self.imArray
            self.analysisParamsGUI.dataFrame = self.dataFrame
            self.analysisParamsGUI.setFilenameDisplays(self.imagePathInput.text().split('/')[-1], self.phantomPathInput.text().split('/')[-1])
            self.analysisParamsGUI.show()
            self.analysisParamsGUI.lastGui = self
            self.hide()

def calculateSpline(xpts, ypts): # 2D spline interpolation
    cv = []
    for i in range(len(xpts)):
        cv.append([xpts[i], ypts[i]])
    cv = np.array(cv)
    if len(xpts) == 2:
        tck, u_ = interpolate.splprep(cv.T, s=0.0, k=1)
    elif len(xpts) == 3:
        tck, u_ = interpolate.splprep(cv.T, s=0.0, k=2)
    else:
        tck, u_ = interpolate.splprep(cv.T, s=0.0, k=3)
    x,y = np.array(interpolate.splev(np.linspace(0, 1, 1000), tck))
    return x, y

def removeDuplicates(ar):
        # Credit: https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
        seen = set()
        seen_add = seen.add
        return [x for x in ar if not (tuple(x) in seen or seen_add(tuple(x)))]