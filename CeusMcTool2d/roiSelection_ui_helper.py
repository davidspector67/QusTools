from CeusMcTool2d.roiSelection_ui import *
from CeusMcTool2d.ticAnalysis_ui_helper import *


import nibabel as nib
import numpy as np
from scipy.ndimage import binary_fill_holes

from itertools import chain
import os
import scipy.interpolate as interpolate
import numpy as np
import nibabel as nib
from scipy.spatial import ConvexHull
import pyvista as pv
import Utils.utils as ut
import Utils.lognormalFunctions as lf
import Utils.motionCorrection as mc


class RoiSelectionGUI(Ui_constructRoi, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.acceptGeneratedRoiButton.setHidden(True)

        self.sliceSpinBoxChanged = False
        self.sliceSliderChanged = False
        self.df = None

        self.curSliceIndex= 0
        self.curAlpha = 255
        self.curPointsPlottedX = []
        self.curPointsPlottedY = []
        self.pointsPlotted = []
        self.xCur = 0
        self.yCur = 0
        self.planesDrawn = []
        self.painted = "none"
        self.lastGui = None

        self.bmodeCoverPixmap = QPixmap(381, 351)
        self.bmodeCoverPixmap.fill(Qt.transparent)
        self.bmodeCoverLabel.setPixmap(self.bmodeCoverPixmap)

        self.ceCoverPixmap = QPixmap(381, 351)
        self.ceCoverPixmap.fill(Qt.transparent)
        self.ceCoverLabel.setPixmap(self.ceCoverPixmap)

        self.setMouseTracking(True)

        self.backButton.clicked.connect(self.backToLastScreen)

    def backToLastScreen(self):
        if not self.tpVal.isHidden():
            self.ticAnalysisGui.show()
        else:
            self.lastGui.show()
        self.hide()

    def restartVoi(self):
        self.pointsPlotted = []
        self.planesDrawn = []
        self.maskCoverImg.fill(0)

        self.voiAlphaLabel.setHidden(True)
        self.voiAlphaOfLabel.setHidden(True)
        self.voiAlphaSpinBox.setHidden(True)
        self.voiAlphaStatus.setHidden(True)
        self.voiAlphaTotal.setHidden(True)
        self.restartVoiButton.setHidden(True)
        self.continueButton.setHidden(True)

        self.drawRoiButton.setHidden(False)
        self.undoLastPtButton.setHidden(False)
        self.redrawRoiButton.setHidden(False)
        self.interpolateVoiButton.setHidden(False)
        self.voiAdviceLabel.setHidden(False)
        
        self.changeAxialSlices()
        self.changeSagSlices()
        self.changeCorSlices()
        self.update()
        
    def computeTic(self):
        times = [i*self.header[4] for i in range(1, self.OGData4dImg.shape[3]+1)]
        self.voxelScale = self.header[1]*self.header[2]*self.header[3] #/1000/1000/1000 # mm^3
        self.pointsPlotted = [*set(self.pointsPlotted)]
        print("Voxel volume:", self.voxelScale)
        self.voxelScale *= len(self.pointsPlotted)
        print("Num voxels:", len(self.pointsPlotted))
        simplifiedMask = self.maskCoverImg[:,:,:,2]
        TIC = ut.generate_TIC(self.OGData4dImg, simplifiedMask, times, 24.09,  self.voxelScale)

        # Bunch of checks
        if np.isnan(np.sum(TIC[:,1])):
            print('STOPPED:NaNs in the VOI')
            return;
        if np.isinf(np.sum(TIC[:,1])):
            print('STOPPED:InFs in the VOI')
            return;

        self.ticX = np.array([[TIC[i,0],i] for i in range(len(TIC[:,0]))])
        self.ticY = TIC[:,1]
        self.ticAnalysisGui.ax.clear()
        self.ticAnalysisGui.ticX = []
        self.ticAnalysisGui.ticY = []
        self.ticAnalysisGui.removedPointsX = []
        self.ticAnalysisGui.removedPointsY = []
        self.ticAnalysisGui.selectedPoints = []
        self.ticAnalysisGui.t0Index = -1
        self.ticAnalysisGui.graph(self.ticX, self.ticY)


    def setFilenameDisplays(self, imageName):
        self.imagePathInput.setHidden(False)
        
        imFile = imageName.split('/')[-1]

        self.imagePathInput.setText(imFile)
        self.inputTextPath = imageName

    def curSliceSpinBoxValueChanged(self):
        if not self.sliceSliderChanged:
            self.sliceSpinBoxChanged = True
            self.sliceValueChanged()

    def curSliceSliderValueChanged(self):
        if not self.sliceSpinBoxChanged:
            self.sliceSliderChanged = True
            self.sliceValueChanged()

    def sliceValueChanged(self):
        if self.sliceSpinBoxChanged and self.sliceSliderChanged:
            self.sliceSpinBoxChanged = False
            self.sliceSliderChanged = False
            print("Error tracking slices")
            return
        if self.sliceSpinBoxChanged:
            self.curSliceIndex = int(self.curSliceSpinBox.value())
            self.curSliceSlider.setValue(self.curSliceIndex)
            self.sliceSpinBoxChanged = False
        if self.sliceSliderChanged:
            self.curSliceIndex= int(self.curSliceSlider.value())
            self.curSliceSpinBox.setValue(self.curSliceIndex)
            self.sliceSliderChanged = False
        self.changeAxialSlices()
        self.changeSagSlices()
        self.changeCorSlices()

    def alphaValueChanged(self):
        self.curAlpha = int(self.voiAlphaSpinBox.value())
        self.voiAlphaSpinBoxChanged = False
        self.voiAlphaStatus.setValue(self.curAlpha)
        for i in range(len(self.pointsPlotted)):
            self.maskCoverImg[self.pointsPlotted[i][0], self.pointsPlotted[i][1], self.pointsPlotted[i][2],3] = self.curAlpha
        self.changeAxialSlices()
        self.changeSagSlices()
        self.changeCorSlices()

    def openImage(self, index, xcel_dir):  
        # WARNING: Currently running under assumption CE and bmode have same dims

        self.x0_bmode = int(self.df.loc[index, 'x0_bmode'])     
        self.y0_bmode = int(self.df.loc[index, 'y0_bmode']) 
        self.w_bmode = int(self.df.loc[index, 'w_bmode'])
        self.h_bmode = int(self.df.loc[index, 'h_bmode'])
        self.x0_CE = int(self.df.loc[index, 'x0_CE'])
        self.y0_CE = int(self.df.loc[index, 'y0_CE'])
        self.w_CE = int(self.df.loc[index, 'w_CE'])
        self.h_CE = int(self.df.loc[index, 'h_CE'])
        self.CE_side = self.df.loc[index, 'CE_window_left(l)_or_right(r)']
        self.cineRate = self.df.loc[index, 'CineRate']
        
        pickle_full_path = os.path.join(xcel_dir, self.df.loc[index, 'pickle_bmode_CE_gray_path'])

        self.full_array = mc.load_pickle(pickle_full_path).astype(np.uint8)

        self.bmode = self.full_array[:,self.y0_bmode:self.y0_bmode+self.h_bmode, \
                                     self.x0_bmode:self.x0_bmode+self.w_bmode]
        
        self.contrastEnhanced = self.full_array[:, self.y0_CE:self.y0_CE+self.h_CE, \
                                                self.x0_CE:self.x0_CE+self.w_CE]
        

        self.numSlices = self.bmode.shape[0]
        self.x = self.w_bmode
        self.y = self.h_bmode

        self.curSliceSlider.setMaximum(self.numSlices-1)

        self.sliceArray = np.round([i*(1/self.cineRate) for i in range(1, self.numSlices+1)], decimals=2)
        self.totalSecondsLabel.setText(str(self.sliceArray[-1]))

        self.curSliceTotal.setText(str(self.numSlices-1))

        self.curSliceSpinBox.setValue(self.sliceArray[self.curSliceIndex])
        self.curSliceSlider.setValue(self.curSliceIndex)
        self.curSliceSlider.valueChanged.connect(self.curSliceSliderValueChanged)
        self.curSliceSpinBox.valueChanged.connect(self.curSliceSpinBoxValueChanged)

        self.drawRoiButton.setCheckable(True)

        #getting initial image data for bmode and CE
        self.dataBmode = self.bmode[self.curSliceIndex]
        self.dataBmode = np.require(self.dataBmode, np.uint8, 'C')
        self.dataCE = self.contrastEnhanced[self.curSliceIndex]
        self.dataCE = np.require(self.dataCE, np.uint8, 'C')

        self.bytesLineBmode, _ = self.dataBmode.strides #in order to create proper QImage, need to know bytes/line
        self.bytesLineCE, _ = self.dataCE.strides

        self.qImgBmode = QImage(self.dataBmode, self.w_bmode, self.h_bmode, self.bytesLineBmode, QImage.Format_Grayscale8) #creating QImage
        self.qImgCE = QImage(self.dataCE, self.w_CE, self.h_CE, self.bytesLineCE, QImage.Format_Grayscale8)

        self.bmodePlane.setPixmap(QPixmap.fromImage(self.qImgBmode).scaled(381, 351))
        self.cePlane.setPixmap(QPixmap.fromImage(self.qImgCE).scaled(381, 351))

        self.closeRoiButton.clicked.connect(self.acceptPolygon) #called to exit the paint function
        self.undoLastPtButton.clicked.connect(self.undoLastPoint) #deletes last drawn rectangle if on sag or cor slices

        self.redrawRoiButton.clicked.connect(self.undoLastRoi)
        self.drawRoiButton.clicked.connect(self.startRoiDraw)

    def changeAxialSlices(self):

        self.axialFrameNum.setText(str(self.newZVal+1))

        self.data2dAx = self.data4dImg[:,:,self.newZVal, self.curSliceIndex]#, self.curSliceIndex #defining 2D data for axial
        self.data2dAx = np.flipud(self.data2dAx) #flipud
        self.data2dAx = np.rot90(self.data2dAx,3) #rotate
        self.data2dAx = np.require(self.data2dAx,np.uint8,'C')

        self.bytesLineAx, _ = self.data2dAx.strides
        self.qImgAx = QImage(self.data2dAx,self.widthAx, self.heightAx, self.bytesLineAx, QImage.Format_Grayscale8)

        tempAx = self.maskCoverImg[:,:,self.newZVal,:] #2D data for axial
        tempAx = np.flipud(tempAx) #flipud
        tempAx = np.rot90(tempAx,3) #rotate ccw 270
        tempAx = np.require(tempAx,np.uint8, 'C')

        self.curMaskAxIm = QImage(tempAx, self.maskAxW, self.maskAxH, self.maskBytesLineAx, QImage.Format_ARGB32) #creating QImage

        self.maskLayerAx.setPixmap(QPixmap.fromImage(self.curMaskAxIm).scaled(381,351)) #displaying QPixmap in the QLabels
        self.axialPlane.setPixmap(QPixmap.fromImage(self.qImgAx).scaled(381,351)) #otherwise, would just display the normal unmodified q_img


    def changeSagSlices(self):

        self.sagittalFrameNum.setText(str(self.newXVal+1))

        self.data2dSag = self.data4dImg[self.newXVal,:,:, self.curSliceIndex]#, self.curSliceIndex
        self.data2dSag = np.flipud(self.data2dSag) #flipud
        self.data2dSag = np.rot90(self.data2dSag,2) #rotate
        self.data2dSag = np.fliplr(self.data2dSag)
        self.data2dSag = np.require(self.data2dSag,np.uint8,'C')

        self.bytesLineSag, _ = self.data2dSag.strides
        self.qImgSag = QImage(self.data2dSag,self.widthSag, self.heightSag, self.bytesLineSag, QImage.Format_Grayscale8)

        tempSag = self.maskCoverImg[self.newXVal,:,:,:] #2D data for sagittal
        tempSag = np.flipud(tempSag) #flipud
        tempSag = np.rot90(tempSag,2) #rotate ccw 180
        tempSag = np.fliplr(tempSag)
        tempSag = np.require(tempSag,np.uint8,'C')
        
        self.curMaskSagIm = QImage(tempSag, self.maskSagW, self.maskSagH, self.maskBytesLineSag, QImage.Format_ARGB32)

        self.maskLayerSag.setPixmap(QPixmap.fromImage(self.curMaskSagIm).scaled(381,351))
        self.sagPlane.setPixmap(QPixmap.fromImage(self.qImgSag).scaled(381,351))


    def changeCorSlices(self):

        self.coronalFrameNum.setText(str(self.newYVal+1))

        self.data2dCor = self.data4dImg[:,self.newYVal,:, self.curSliceIndex]#, self.curSliceIndex
        self.data2dCor = np.rot90(self.data2dCor,1) #rotate
        self.data2dCor = np.flipud(self.data2dCor) #flipud
        self.data2dCor = np.require(self.data2dCor, np.uint8,'C')

        self.bytesLineCor, _ = self.data2dCor.strides
        self.qImgCor = QImage(self.data2dCor,self.widthCor,self.heightCor, self.bytesLineCor, QImage.Format_Grayscale8)

        tempCor = self.maskCoverImg[:,self.newYVal,:,:] #2D data for coronal
        tempCor = np.rot90(tempCor,1) #rotate ccw 90
        tempCor = np.flipud(tempCor) #flipud
        tempCor = np.require(tempCor,np.uint8,'C')

        self.curMaskCorIm = QImage(tempCor, self.maskCorW, self.maskCorH, self.maskBytesLineCor, QImage.Format_ARGB32)

        self.maskLayerCor.setPixmap(QPixmap.fromImage(self.curMaskCorIm).scaled(381,351))
        self.corPlane.setPixmap(QPixmap.fromImage(self.qImgCor).scaled(381,351))

    def updateCrosshair(self):
        if self.xCur < 741 and self.xCur > 360 and self.yCur < 501 and self.yCur > 150:
            self.actualX = int((self.xCur - 361)*(self.h_bmode-1)/381)
            self.actualY = int((self.yCur - 151)*(self.w_bmode-1)/351)
            plotX = self.xCur - 361
        elif self.xCur < 1151 and self.xCur > 770 and self.yCur < 501 and self.yCur > 150:
            self.actualX = int((self.xCur-771)*(self.h_CE-1)/381)
            self.actualY = int((self.yCur-151)*(self.w_CE-1)/351)
            plotX = self.xCur - 771
        else:
            return
        
        plotY = self.yCur - 151

        self.bmodeCoverLabel.pixmap().fill(Qt.transparent)
        painter = QPainter(self.bmodeCoverLabel.pixmap())
        painter.setPen(Qt.yellow)
        bmodeVertLine = QLine(plotX, 0, plotX, 351)
        bmodeLatLine = QLine(0, plotY, 381, plotY)
        painter.drawLines([bmodeVertLine, bmodeLatLine])
        painter.end()
            
        self.ceCoverLabel.pixmap().fill(Qt.transparent)
        painter = QPainter(self.ceCoverLabel.pixmap())
        painter.setPen(Qt.yellow)
        ceVertLine = QLine(plotX, 0, plotX, 351)
        ceLatLine = QLine(0, plotY, 381, plotY)
        painter.drawLines([ceVertLine, ceLatLine])
        painter.end()
        self.update()

    def mousePressEvent(self,event):
        self.xCur = event.x()
        self.yCur = event.y()
        self.newPointPlotted = False
        if self.drawRoiButton.isChecked():
            # Plot ROI points
            if (self.xCur < 721 and self.xCur > 400 and self.yCur < 341 and self.yCur > 40) and (self.painted == "none" or self.painted == "ax"):
                self.actualX = int((self.xCur - 401)*(self.widthAx-1)/381)
                self.actualY = int((self.yCur - 41)*(self.heightAx-1)/351)
                self.maskCoverImg[self.actualX, self.actualY, self.newZVal] = [0, 0, 255,int(self.curAlpha)]
                self.curPointsPlottedX.append(self.actualX)
                self.curPointsPlottedY.append(self.actualY)
                self.newPointPlotted = True
                self.painted = "ax"
                self.curROIDrawn = False
            elif (event.x() < 1131 and event.x() > 810 and event.y() < 341 and event.y() > 40) and (self.painted == "none" or self.painted == "sag"):
                self.actualX = int((self.xCur-811)*(self.widthSag-1)/381)
                self.actualY = int((self.yCur-41)*(self.heightSag-1)/351)
                self.maskCoverImg[self.newXVal, self.actualY, self.actualX] = [0,0,255,int(self.curAlpha)]
                self.curPointsPlottedX.append(self.actualX)
                self.curPointsPlottedY.append(self.actualY)
                self.newPointPlotted = True
                self.painted = "sag"
                self.curROIDrawn = False
            elif (event.x() < 1131 and event.x() > 810 and event.y() < 711 and event.y() > 410) and (self.painted == "none" or self.painted == "cor"):
                self.actualX = int((self.xCur-811)*(self.widthCor-1)/381)
                self.actualY = int((self.yCur-411)*(self.heightCor-1)/351)
                self.maskCoverImg[self.actualX, self.newYVal, self.actualY] = [0,0,255,int(self.curAlpha)]
                self.curPointsPlottedX.append(self.actualX)
                self.curPointsPlottedY.append(self.actualY)
                self.newPointPlotted = True
                self.painted = "cor"
                self.curROIDrawn = False
            self.changeSagSlices()
            self.changeCorSlices()
            self.changeAxialSlices()
            self.updateCrosshair()

    def mouseMoveEvent(self, event):
        self.xCur = event.x()
        self.yCur = event.y()
        self.updateCrosshair()

    
    def acceptPolygon(self):
        # 2d interpolation
        if len(self.curPointsPlottedX):
            self.drawRoiButton.setChecked(False)

            # remove duplicate points
            points = np.transpose(np.array([self.curPointsPlottedX, self.curPointsPlottedY]))
            points = removeDuplicates(points)
            [self.curPointsPlottedX, self.curPointsPlottedY] = np.transpose(points)
            self.curPointsPlottedX = list(self.curPointsPlottedX)
            self.curPointsPlottedY = list(self.curPointsPlottedY)

            self.curPointsPlottedX.append(self.curPointsPlottedX[0])
            self.curPointsPlottedY.append(self.curPointsPlottedY[0])
            self.maskCoverImg.fill(0)
            x, y = calculateSpline(self.curPointsPlottedX, self.curPointsPlottedY)
            newROI = []
            for i in range(len(x)):
                if self.painted == "ax":
                    if len(newROI) == 0 or newROI[-1] != (int(x[i]), int(y[i]), self.newZVal):
                        newROI.append((int(x[i]), int(y[i]), self.newZVal))
                elif self.painted == "sag":
                    if len(newROI) == 0 or newROI[-1] != (self.newXVal, int(y[i]), int (x[i])):
                        newROI.append((self.newXVal, int(y[i]), int(x[i])))
                elif self.painted == "cor":
                    if len(newROI) == 0 or newROI[-1] != (int(x[i]), self.newYVal, int(y[i])):
                        newROI.append((int(x[i]), self.newYVal, int(y[i])))
            self.pointsPlotted.append(newROI)
            for i in range(len(self.pointsPlotted)):
                for j in range(len(self.pointsPlotted[i])):
                    self.maskCoverImg[self.pointsPlotted[i][j][0], self.pointsPlotted[i][j][1], self.pointsPlotted[i][j][2]] = [0,0,255,int(self.curAlpha)]
            self.changeAxialSlices()
            self.changeSagSlices()
            self.changeCorSlices()
            self.curPointsPlottedX = []
            self.curPointsPlottedY = []
            self.planesDrawn.append(self.painted)
            self.painted = "none"
            self.curROIDrawn = True
            self.redrawRoiButton.setHidden(False)
            self.closeRoiButton.setHidden(True)
            # if (len(self.planesDrawn) == 1) or (len(self.planesDrawn) >= 3 and ((self.planesDrawn[0]!=self.planesDrawn[1]) and (self.planesDrawn[1]!=self.planesDrawn[2]) and (self.planesDrawn[2]!=self.planesDrawn[0]))):
            if len(self.planesDrawn):
                self.interpolateVoiButton.clicked.connect(self.voi3dInterpolation)

    def undoLastPoint(self):
        if len(self.curPointsPlottedX) != 0:
            self.maskCoverImg[self.curPointsPlottedX[-1]]
            self.curPointsPlottedX.pop()
            self.curPointsPlottedY.pop()
            self.maskCoverImg.fill(0)
            for i in range(len(self.pointsPlotted)):
                for j in range(len(self.pointsPlotted[i])):
                    self.maskCoverImg[self.pointsPlotted[i][j][0], self.pointsPlotted[i][j][1], self.pointsPlotted[i][j][2]] = [0,0,255, int(self.curAlpha)]
            for i in range(len(self.curPointsPlottedX)):
                if self.painted == "ax":
                    self.maskCoverImg[int(self.curPointsPlottedX[i]), int(self.curPointsPlottedY[i]), self.newZVal] = [0,0,255,int(self.curAlpha)]
                elif self.painted == "sag":
                    self.maskCoverImg[self.newXVal, int(self.curPointsPlottedY[i]), int(self.curPointsPlottedX[i])] = [0,0,255,int(self.curAlpha)]
                elif self.painted == "cor":
                    self.maskCoverImg[int(self.curPointsPlottedX[i]), self.newYVal, int(self.curPointsPlottedY[i])] = [0,0,255,int(self.curAlpha)]

            self.changeAxialSlices()
            self.changeSagSlices()
            self.changeCorSlices()
        if len(self.curPointsPlottedX) == 0:
            self.painted == "none"

    def moveToTic(self):
        self.ticAnalysisGui.timeLine = None
        self.computeTic()
        self.ticAnalysisGui.data4dImg = self.data4dImg
        self.ticAnalysisGui.curSliceIndex = self.curSliceIndex
        self.ticAnalysisGui.newXVal = self.newXVal
        self.ticAnalysisGui.newYVal = self.newYVal
        self.ticAnalysisGui.newZVal = self.newZVal
        self.ticAnalysisGui.x = self.x
        self.ticAnalysisGui.y = self.y
        self.ticAnalysisGui.z = self.z
        self.ticAnalysisGui.maskCoverImg = self.maskCoverImg
        self.ticAnalysisGui.widthAx = self.widthAx
        self.ticAnalysisGui.heightAx = self.heightAx
        self.ticAnalysisGui.bytesLineAx = self.bytesLineAx
        self.ticAnalysisGui.maskAxW = self.maskAxW
        self.ticAnalysisGui.maskAxH = self.maskAxH
        self.ticAnalysisGui.maskBytesLineAx = self.maskBytesLineAx
        self.ticAnalysisGui.widthSag = self.widthSag
        self.ticAnalysisGui.heightSag = self.heightSag
        self.ticAnalysisGui.bytesLineSag = self.bytesLineSag
        self.ticAnalysisGui.maskSagW = self.maskSagW
        self.ticAnalysisGui.maskSagH = self.maskSagH
        self.ticAnalysisGui.maskBytesLineSag = self.maskBytesLineSag
        self.ticAnalysisGui.widthCor = self.widthCor
        self.ticAnalysisGui.heightCor = self.heightCor
        self.ticAnalysisGui.bytesLineCor = self.bytesLineCor
        self.ticAnalysisGui.maskCorW = self.maskCorW
        self.ticAnalysisGui.maskCorH = self.maskCorH
        self.ticAnalysisGui.maskBytesLineCor = self.maskBytesLineCor
        self.ticAnalysisGui.sliceArray = self.sliceArray
        self.voiAlphaSpinBox.setValue(100)
        self.alphaValueChanged()
        self.ticAnalysisGui.changeAxialSlices()
        self.ticAnalysisGui.changeSagSlices()
        self.ticAnalysisGui.changeCorSlices()
        self.ticAnalysisGui.deSelectLastPointButton.setHidden(True)
        self.ticAnalysisGui.removeSelectedPointsButton.setHidden(True)
        self.ticAnalysisGui.restoreLastPointsButton.setHidden(True)
        self.ticAnalysisGui.acceptTicButton.setHidden(True)
        self.ticAnalysisGui.acceptT0Button.setHidden(True)
        self.ticAnalysisGui.t0Slider.setHidden(True)
        self.ticAnalysisGui.selectT0Button.setHidden(False)
        self.ticAnalysisGui.show()
        self.ticAnalysisGui.lastGui = self
        self.ticAnalysisGui.ceusResultsGui = self
        self.ticAnalysisGui.acceptTicButton.clicked.connect(self.acceptTIC)
        self.ticAnalysisGui.imagePathInput.setText(self.imagePathInput.text())
        self.hide()   


    def startRoiDraw(self):
        if self.drawRoiButton.isChecked():
            self.closeRoiButton.setHidden(False)
            self.redrawRoiButton.setHidden(True)
        elif not len(self.curPointsPlottedX):
            self.closeRoiButton.setHidden(True)
            self.redrawRoiButton.setHidden(False)

    def undoLastRoi(self):
        if len(self.planesDrawn):

            if len(self.pointsPlotted) > 0:
                self.pointsPlotted.pop()
                self.planesDrawn.pop()
                self.maskCoverImg.fill(0)
                for i in range(len(self.pointsPlotted)):
                    for j in range(len(self.pointsPlotted[i])):
                        self.maskCoverImg[self.pointsPlotted[i][j][0], self.pointsPlotted[i][j][1], self.pointsPlotted[i][j][2]] = [0,0,255,int(self.curAlpha)]
                self.changeAxialSlices()
                self.changeSagSlices()
                self.changeCorSlices()
            self.update()

    def voi3dInterpolation(self):
        if len(self.planesDrawn):
            if len(self.planesDrawn) >= 3:
                points = calculateSpline3D(list(chain.from_iterable(self.pointsPlotted)))
            else:
                points = set()
                for group in np.array(self.pointsPlotted):
                    for point in group:
                        points.add(tuple(point))

            self.pointsPlotted = []
            self.maskCoverImg.fill(0)
            
            for point in points:
                if max(self.data4dImg[tuple(point)]) != 0:
                    self.maskCoverImg[tuple(point)] = [0,0,255,int(self.curAlpha)]
                    self.pointsPlotted.append(tuple(point))
            if len(self.pointsPlotted) == 0:
                print("VOI not in US image.\nDraw new VOI over US image")
                self.maskCoverImg.fill(0)
                self.changeAxialSlices()
                self.changeSagSlices()
                self.changeCorSlices()
                return
        
        mask = np.zeros((self.maskCoverImg.shape[0], self.maskCoverImg.shape[1], self.maskCoverImg.shape[2]))

        for point in self.pointsPlotted:
            mask[point] = 1
        for i in range(mask.shape[2]):
            border = np.where(mask[:,:,i] == 1)
            if (not len(border[0])) or (max(border[0]) == min(border[0])) or (max(border[1]) == min(border[1])):
                continue
            border = np.array(border).T
            hull = ConvexHull(border)
            vertices = border[hull.vertices]
            shape = vertices.shape
            vertices = np.reshape(np.append(vertices, vertices[0]), (shape[0]+1, shape[1]))

            # Linear interpolation of 2d convex hull
            tck, u_ = interpolate.splprep(vertices.T, s=0.0, k=1)
            splineX, splineY = np.array(interpolate.splev(np.linspace(0, 1, 1000), tck))

            mask[:,:,i] = np.zeros((mask.shape[0], mask.shape[1]))
            for j in range(len(splineX)):
                mask[int(splineX[j]), int(splineY[j]), i] = 1
            filledMask = binary_fill_holes(mask[:,:,i])
            maskPoints = np.array(np.where(filledMask == True))
            for j in range(len(maskPoints[0])):
                self.maskCoverImg[maskPoints[0][j], maskPoints[1][j], i] = [0,0,255,int(self.curAlpha)]
                self.pointsPlotted.append((maskPoints[0][j], maskPoints[1][j], i))
        self.changeAxialSlices()
        self.changeSagSlices()
        self.changeCorSlices()
        self.interpolateVoiButton.setHidden(True)
        self.continueButton.setHidden(False)
        
        self.drawRoiButton.setHidden(True)
        self.undoLastPtButton.setHidden(True)
        self.redrawRoiButton.setHidden(True)
        self.voiAdviceLabel.setHidden(True)

        self.voiAlphaLabel.setHidden(False)
        self.voiAlphaOfLabel.setHidden(False)
        self.voiAlphaSpinBox.setHidden(False)
        self.voiAlphaStatus.setHidden(False)
        self.voiAlphaTotal.setHidden(False)
        self.restartVoiButton.setHidden(False)
        self.restartVoiButton.clicked.connect(self.restartVoi)

    def acceptTIC(self):
        self.ticDisplay.setHidden(False)
        self.resultsLabel.setHidden(False)
        self.aucLabel.setHidden(False)
        self.aucVal.setHidden(False)
        self.peLabel.setHidden(False)
        self.peVal.setHidden(False)
        self.mttLabel.setHidden(False)
        self.mttVal.setHidden(False)
        self.tpLabel.setHidden(False)
        self.tpVal.setHidden(False)
        self.tmppvLabel.setHidden(False)
        self.tmppvVal.setHidden(False)
        self.voiVolumeLabel.setHidden(False)
        self.voiVolumeVal.setHidden(False)

        self.analysisParamsSidebar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(99, 0, 174);\n"
"	border: 1px solid black;\n"
"}")

        self.ticAnalysisSidebar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(99, 0, 174);\n"
"	border: 1px solid black;\n"
"}")

        self.constructVoiLabel.setHidden(True)
        self.drawRoiButton.setHidden(True)
        self.undoLastPtButton.setHidden(True)
        self.closeRoiButton.setHidden(True)
        self.redrawRoiButton.setHidden(True)
        self.continueButton.setHidden(True)
        self.interpolateVoiButton.setHidden(True)
        self.restartVoiButton.setHidden(True)
        self.voiAdviceLabel.setHidden(True)

        self.ax.clear()
        self.ax.plot(self.ticAnalysisGui.ticX[:,0], self.ticAnalysisGui.ticY)

        # self.sliceArray = self.ticEditor.ticX[:,1]
        # if self.curSliceIndex>= len(self.sliceArray):
        #     self.curSliceSlider.setValue(len(self.sliceArray)-1)
        #     self.curSliceSliderValueChanged()
        # self.curSliceSlider.setMaximum(len(self.sliceArray)-1)
        # self.curSliceSpinBox.setMaximum(len(self.sliceArray)-1)

        tmppv = np.max(self.ticAnalysisGui.ticY)
        self.ticAnalysisGui.ticY = self.ticAnalysisGui.ticY/tmppv;
        x = self.ticAnalysisGui.ticX[:,0] - np.min(self.ticAnalysisGui.ticX[:,0])

        # Bunch of checks
        if np.isnan(np.sum(self.ticAnalysisGui.ticY)):
            print('STOPPED:NaNs in the VOI')
            return;
        if np.isinf(np.sum(self.ticAnalysisGui.ticY)):
            print('STOPPED:InFs in the VOI')
            return;

        # Do the fitting
        try:
            params, popt, wholecurve = lf.data_fit([x, self.ticAnalysisGui.ticY], tmppv);
            self.ax.plot(self.ticAnalysisGui.ticX[:,0], wholecurve)
            range = max(self.ticAnalysisGui.ticX[:,0]) - min(self.ticAnalysisGui.ticX[:,0])
            self.ax.set_xlim(xmin=min(self.ticAnalysisGui.ticX[:,0])-(0.05*range), xmax=max(self.ticAnalysisGui.ticX[:,0])+(0.05*range))
        except RuntimeError:
            print('RunTimeError')
            params = np.array([np.max(self.ticAnalysisGui.ticY)*tmppv, np.trapz(self.ticAnalysisGui.ticY*tmppv, x=self.ticAnalysisGui.ticX[:,0]), self.ticAnalysisGui.ticX[-1,0], np.argmax(self.ticAnalysisGui.ticY), np.max(self.ticAnalysisGui.ticX[:,0])*2, 0]);
        self.fig.subplots_adjust(left=0.1, right=0.97, top=0.85, bottom=0.25)
        self.canvas.draw()
        self.ticAnalysisGui.ticY *= tmppv

        self.aucVal.setText(str(np.around(params[1], decimals=3)))
        self.peVal.setText(str(np.around(params[0], decimals=3)))
        self.tpVal.setText(str(np.around(params[2], decimals=2)))
        self.mttVal.setText(str(np.around(params[3], decimals=2)))
        self.tmppvVal.setText(str(np.around(tmppv, decimals=1)))
        self.voiVolumeVal.setText(str(np.around(self.voxelScale, decimals=1)))

        self.ticAnalysisGui.hide()
        self.curSliceSlider.setValue(self.ticAnalysisGui.curSliceIndex)
        self.curSliceSliderValueChanged()
        self.show()




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

def ellipsoidFitLS(pos):

    # centre coordinates on origin
    pos = pos - np.mean(pos, axis=0)

    # build our regression matrix
    A = pos**2

    # vector of ones
    O = np.ones(len(A))

    # least squares solver
    B, resids, rank, s = np.linalg.lstsq(A, O, rcond=None)

    # solving for a, b, c
    a_ls = np.sqrt(1.0/B[0])
    b_ls = np.sqrt(1.0/B[1])
    c_ls = np.sqrt(1.0/B[2])

    return (a_ls, b_ls, c_ls)

def calculateSpline3D(points):
    # Calculate ellipsoid of best fit
    # points = np.array(points)
    # a,b,c = ellipsoidFitLS(points)
    # output = set()


    # u = np.linspace(0., np.pi*2., 1000)
    # v = np.linspace(0., np.pi, 1000)
    # u, v = np.meshgrid(u,v)

    # x = a*np.cos(u)*np.sin(v)
    # y = b*np.sin(u)*np.sin(v)
    # z = c*np.cos(v)

    # # turn this data into 1d arrays
    # x = x.flatten()
    # y = y.flatten()
    # z = z.flatten()
    # x += np.mean(points, axis=0)[0]
    # y += np.mean(points, axis=0)[1]
    # z += np.mean(points, axis=0)[2]

    # for i in range(len(x)):
    #     output.add((int(x[i]), int(y[i]), int(z[i])))
    # return output

    cloud = pv.PolyData(points, force_float=False)
    volume = cloud.delaunay_3d(alpha=100.)
    shell = volume.extract_geometry()
    final = shell.triangulate()
    final.smooth(n_iter=1000)
    faces = final.faces.reshape((-1, 4))
    faces = faces[:, 1:]
    arr = final.points[faces]

    arr = np.array(arr)

    output = set()
    for tri in arr:
        slope_2 = (tri[2]-tri[1])
        start_2 = tri[1]
        slope_3 = (tri[0]-tri[1])
        start_3 = tri[1]
        for i in range(100, -1, -1):
            bound_one = start_2 + ((i/100)*slope_2)
            bound_two = start_3 + ((i/100)*slope_3)
            cur_slope = bound_one-bound_two
            cur_start = bound_two
            for j in range(100, -1, -1):
                cur_pos = cur_start + ((j/100)*cur_slope)
                output.add((int(cur_pos[0]), int(cur_pos[1]), int(cur_pos[2])))
    
    return output

def removeDuplicates(ar):
        # Credit: https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
        seen = set()
        seen_add = seen.add
        return [x for x in ar if not (tuple(x) in seen or seen_add(tuple(x)))]
         



if __name__ == "__main__":
    pickle_full_path = "/Users/davidspector/Home/Stanford/MC_Sample_Code/data/P_005_021/pickle_bmode_CE_gray/ceus_inj1_wi_000000.000000.pkl"
    x0_bmode = 0
    x0_CE = 721
    y0_bmode = 40
    y0_CE = 40
    w_bmode = 721
    h_bmode = 697
    w_CE = 721
    h_CE = 697

    import sys
    app = QApplication(sys.argv)
    # selectWindow = QWidget()
    ui = RoiSelectionGUI()
    # ui.selectImage.show()
    ui.show()
    sys.exit(app.exec_())