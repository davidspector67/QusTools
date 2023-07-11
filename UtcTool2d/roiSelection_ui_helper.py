from UtcTool2d.roiSelection_ui import *
from UtcTool2d.editImageDisplay_ui_helper import *
from UtcTool2d.analysisParamsSelection_ui_helper import *
from UtcTool2d.rfAnalysis_ui_helper import *
from Parsers.philipsMatParser import getImage
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

        global pointsPlottedX, pointsPlottedY
        pointsPlottedX = []
        pointsPlottedY = []
        self.imagePathInput.setHidden(True)
        self.phantomPathInput.setHidden(True)

        # Prepare B-Mode display plot
        self.horizontalLayout = QHBoxLayout(self.imDisplayFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.horizontalLayout.addWidget(self.canvas)

        self.editImageDisplayGUI = EditImageDisplayGUI()
        self.editImageDisplayGUI.contrastVal.valueChanged.connect(self.changeContrast)
        self.editImageDisplayGUI.brightnessVal.valueChanged.connect(self.changeBrightness)    
        self.editImageDisplayGUI.sharpnessVal.valueChanged.connect(self.changeSharpness)

        self.lastGui = None
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

        self.scatteredPoints = []

        self.redrawRoiButton.setHidden(True)
        
        self.editImageDisplayButton.clicked.connect(self.openImageEditor)
        self.drawRoiButton.clicked.connect(self.recordDrawROIClicked)
        self.undoLastPtButton.clicked.connect(self.undoLastPt)
        self.closeRoiButton.clicked.connect(self.closeInterpolation)
        self.redrawRoiButton.clicked.connect(self.restartROI)
        self.acceptRoiButton.clicked.connect(self.acceptROI)
        self.backButton.clicked.connect(self.backToLastScreen)

    def backToLastScreen(self):
        self.lastGui.show()
        self.hide()

    def changeContrast(self):
        self.editImageDisplayGUI.contrastValDisplay.setValue(int(self.editImageDisplayGUI.contrastVal.value()*10))
        self.updateBModeSettings()

    def changeBrightness(self):
        self.editImageDisplayGUI.brightnessValDisplay.setValue(int(self.editImageDisplayGUI.brightnessVal.value()*10))
        self.updateBModeSettings()

    def changeSharpness(self):
        self.editImageDisplayGUI.sharpnessValDisplay.setValue(int(self.editImageDisplayGUI.sharpnessVal.value()*10))
        self.updateBModeSettings()

    def openImageEditor(self):
        if self.editImageDisplayGUI.isVisible():
            self.editImageDisplayGUI.hide()
        else:
            self.editImageDisplayGUI.show()

    def setFilenameDisplays(self, imageName, phantomName):
        self.imagePathInput.setHidden(False)
        self.phantomPathInput.setHidden(False)
        self.imagePathInput.setText(imageName)
        self.phantomPathInput.setText(phantomName)
    
    def plotOnCanvas(self): # Plot current image on GUI
        self.ax = self.figure.add_subplot(111)
        im = plt.imread(os.path.join("imROIs", "bModeIm.png"))
        plt.imshow(im, cmap='Greys_r')

        if len(pointsPlottedX) > 0:
            self.scatteredPoints.append(self.ax.scatter(pointsPlottedX[-1], pointsPlottedY[-1], marker="o", s=0.5, c="red", zorder=500))
            if len(pointsPlottedX) > 1:
                xSpline, ySpline = calculateSpline(pointsPlottedX, pointsPlottedY)
                self.spline = self.ax.plot(xSpline, ySpline, color = "cyan", zorder=1, linewidth=0.75)
        self.figure.subplots_adjust(left=0,right=1, bottom=0,top=1, hspace=0.2,wspace=0.2)
        self.cursor = matplotlib.widgets.Cursor(self.ax, color="gold", linewidth=0.4, useblit=True)
        self.cursor.set_active(False)
        plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
        self.canvas.draw() # Refresh canvas


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
            imArray, self.imgDataStruct, self.imgInfoStruct, self.refDataStruct, self.refInfoStruct = getImage(dataFileName, dataFileLocation, phantFileName, phantFileLocation, self.frame)
            self.arHeight = imArray.shape[0]
            self.arWidth = imArray.shape[1]
            self.imData = np.array(imArray).reshape(self.arHeight, self.arWidth)
            self.imData = np.flipud(self.imData) #flipud
            self.imData = np.require(self.imData,np.uint8,'C')
            self.bytesLine = self.imData.strides[0]
            self.qIm = QImage(self.imData, self.arWidth, self.arHeight, self.bytesLine, QImage.Format_Grayscale8).scaled(721, 501)

            self.qIm.mirrored().save(os.path.join("imROIs", "bModeImRaw.png")) # Save as .png file

            self.pixSizeAx = self.imgDataStruct.bMode.shape[0] #were both scBmode
            self.pixSizeLat = self.imgDataStruct.bMode.shape[1]

            self.editImageDisplayGUI.contrastVal.setValue(4)
            self.editImageDisplayGUI.brightnessVal.setValue(0.75)
            self.editImageDisplayGUI.sharpnessVal.setValue(3)

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

        if imageFilePath.endswith(".dcm"):
            ds = pydicom.dcmread(imageFilePath)
            imArray = ds.pixel_array

            self.arHeight = imArray.shape[0]
            self.arWidth = imArray.shape[1]
            self.imData = np.array(imArray).reshape(self.arHeight, self.arWidth, 3)
            self.imData = np.flipud(self.imData) #flipud
            self.imData = np.require(self.imData,np.uint8,'C')
            self.bytesLine = self.imData.strides[0]
            self.qIm = QImage(self.imData, self.arWidth, self.arHeight, self.bytesLine, QImage.Format_RGB888) 

            self.qIm.mirrored().save(os.path.join("imROIs", "bModeImRaw.png")) # Save as .png file

            self.pixSizeAx = self.arHeight
            self.pixSizeLat = self.arWidth

            self.editImageDisplayGUI.contrastVal.setValue(1)
            self.editImageDisplayGUI.brightnessVal.setValue(1)
            self.editImageDisplayGUI.sharpnessVal.setValue(1)

        else:
            return

        # Implement correct previously assigned image display settings

        self.cvIm = Image.open(os.path.join("imROIs", "bModeImRaw.png"))
        enhancer = ImageEnhance.Contrast(self.cvIm)

        imOutput = enhancer.enhance(self.editImageDisplayGUI.contrastVal.value())
        bright = ImageEnhance.Brightness(imOutput)
        imOutput = bright.enhance(self.editImageDisplayGUI.brightnessVal.value())
        sharp = ImageEnhance.Sharpness(imOutput)
        imOutput = sharp.enhance(self.editImageDisplayGUI.sharpnessVal.value())
        imOutput.save(os.path.join("imROIs", "bModeIm.png"))

        self.plotOnCanvas()

    def recordDrawROIClicked(self):
        if self.drawRoiButton.isChecked(): # Set up b-mode to be drawn on
            # image, =self.ax.plot([], [], marker="o",markersize=3, markerfacecolor="red")
            # self.cid = image.figure.canvas.mpl_connect('button_press_event', self.interpolatePoints)
            self.cid = self.figure.canvas.mpl_connect('button_press_event', self.interpolatePoints)
            self.cursor.set_active(True)
        else: # No longer let b-mode be drawn on
            self.cid = self.figure.canvas.mpl_disconnect(self.cid)
            self.cursor.set_active(False)
        self.canvas.draw()

    def undoLastPt(self): # When drawing ROI, undo last point plotted
        if len(pointsPlottedX) > 0:
            self.scatteredPoints[-1].remove()
            self.scatteredPoints.pop()
            pointsPlottedX.pop()
            pointsPlottedY.pop()
            if len(pointsPlottedX) > 0:
                global finalSplineX
                global finalSplineY
                oldSpline = self.spline.pop(0)
                oldSpline.remove()
                if len(pointsPlottedX) > 1:
                    finalSplineX, finalSplineY = calculateSpline(pointsPlottedX, pointsPlottedY)
                    self.spline = self.ax.plot(finalSplineX, finalSplineY, color = "cyan", linewidth=0.75)
            self.canvas.draw()
            self.drawRoiButton.setChecked(True)
            self.recordDrawROIClicked()

    def closeInterpolation(self): # Finish drawing ROI
        if len(pointsPlottedX) > 2:
            self.ax.clear()
            im = plt.imread(os.path.join("imROIs", "bModeIm.png"))
            plt.imshow(im, cmap='Greys_r')
            pointsPlottedX.append(pointsPlottedX[0])
            pointsPlottedY.append(pointsPlottedY[0])
            global finalSplineX, finalSplineY
            finalSplineX, finalSplineY = calculateSpline(pointsPlottedX, pointsPlottedY)
            self.ax.plot(finalSplineX, finalSplineY, color = "cyan", linewidth=0.75)
            image, =self.ax.plot([], [], marker="o",markersize=3, markerfacecolor="red")
            image.figure.canvas.mpl_disconnect(self.cid)
            self.figure.subplots_adjust(left=0,right=1, bottom=0,top=1, hspace=0.2,wspace=0.2)
            plt.tick_params(bottom=False, left=False)
            self.canvas.draw()
            self.ROIDrawn = True
            self.drawRoiButton.setChecked(False)
            self.drawRoiButton.setCheckable(False)
            self.redrawRoiButton.setHidden(False)
            self.closeRoiButton.setHidden(True)
            self.cursor.set_active(False)
            self.undoLastPtButton.clicked.disconnect()
            self.canvas.draw()

    def restartROI(self): # Remove previously drawn roi and prepare user to draw a new one
        self.ax.clear()
        im = plt.imread(os.path.join("imROIs", "bModeIm.png"))
        self.ax.imshow(im, cmap='Greys_r')
        global pointsPlottedX, pointsPlottedY, finalSplineX, finalSplineY
        finalSplineX = []
        finalSplineY = []
        pointsPlottedX = []
        pointsPlottedY = []
        self.drawRoiButton.setChecked(False)
        image, = self.ax.plot([], [], marker="o", markersize=3, markerfacecolor="red")
        image.figure.canvas.mpl_disconnect(self.cid)
        self.figure.subplots_adjust(left=0,right=1, bottom=0,top=1, hspace=0.2,wspace=0.2)
        self.ax.tick_params(bottom=False, left=False)
        self.canvas.draw()
        self.drawRoiButton.setCheckable(True)
        self.closeRoiButton.setHidden(False)
        self.redrawRoiButton.setHidden(True)
        self.undoLastPtButton.clicked.connect(self.undoLastPt)

    def updateBModeSettings(self): # Updates background photo when image settings are modified
        self.cvIm = Image.open(os.path.join("imROIs", "bModeImRaw.png"))
        contrast = ImageEnhance.Contrast(self.cvIm)
        imOutput = contrast.enhance(self.editImageDisplayGUI.contrastVal.value())
        brightness = ImageEnhance.Brightness(imOutput)
        imOutput = brightness.enhance(self.editImageDisplayGUI.brightnessVal.value())
        sharpness = ImageEnhance.Sharpness(imOutput)
        imOutput = sharpness.enhance(self.editImageDisplayGUI.sharpnessVal.value())
        imOutput.save(os.path.join("imROIs", "bModeIm.png"))
        self.plotOnCanvas()
    
    def interpolatePoints(self, event): # Update ROI being drawn using spline using 2D interpolation
        pointsPlottedX.append(int(event.xdata))
        pointsPlottedY.append(int(event.ydata))
        plottedPoints = len(pointsPlottedX)

        if plottedPoints > 1:
            if plottedPoints > 2:
                oldSpline = self.spline.pop(0)
                oldSpline.remove()

            xSpline, ySpline = calculateSpline(pointsPlottedX, pointsPlottedY)
            self.spline = self.ax.plot(xSpline, ySpline, color = "cyan", zorder=1, linewidth=0.75)
            plt.subplots_adjust(left=0,right=1, bottom=0,top=1, hspace=0.2,wspace=0.2)
            plt.tick_params(bottom=False, left=False)
        self.scatteredPoints.append(self.ax.scatter(pointsPlottedX[-1], pointsPlottedY[-1], marker="o", s=0.5, c="red", zorder=500))
        self.canvas.draw()

    def acceptROI(self):
        if len(pointsPlottedX) > 1 and pointsPlottedX[0] == pointsPlottedX[-1]:
            del self.analysisParamsGUI
            self.analysisParamsGUI = AnalysisParamsGUI()
            self.analysisParamsGUI.axWinSizeVal.setValue(self.axWinSizeVal)
            self.analysisParamsGUI.latWinSizeVal.setValue(self.latWinSizeVal)
            self.analysisParamsGUI.axOverlapVal.setValue(self.axOverlapVal)
            self.analysisParamsGUI.latOverlapVal.setValue(self.latOverlapVal)
            self.analysisParamsGUI.minFreqVal.setValue(self.minFreqVal)
            self.analysisParamsGUI.maxFreqVal.setValue(self.maxFreqVal)
            self.analysisParamsGUI.startDepthVal.setValue(self.startDepthVal)
            self.analysisParamsGUI.endDepthVal.setValue(self.endDepthVal)
            self.analysisParamsGUI.clipFactorVal.setValue(self.clipFactorVal)
            self.analysisParamsGUI.samplingFreqVal.setValue(self.samplingFreqVal)
            self.analysisParamsGUI.finalSplineX = finalSplineX
            self.analysisParamsGUI.finalSplineY = finalSplineY
            self.analysisParamsGUI.setFilenameDisplays(self.imagePathInput.text().split('/')[-1], self.phantomPathInput.text().split('/')[-1])
            self.analysisParamsGUI.show()
            self.analysisParamsGUI.lastGui = self
            self.editImageDisplayGUI.hide()
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