from CeusTool3d.ticAnalysis_ui import *

import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class TicAnalysisGUI(Ui_ticEditor, QWidget):
    def __init__(self):
        # self.selectImage = QWidget()
        super().__init__()
        self.setupUi(self)
        self.deSelectLastPointButton.setHidden(True)
        self.removeSelectedPointsButton.setHidden(True)
        self.restoreLastPointsButton.setHidden(True)
        self.acceptTicButton.setHidden(True)
        self.acceptT0Button.setHidden(True)
        self.t0Slider.setHidden(True)

        self.t0Slider.setValue(0)

        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.horizLayout = QHBoxLayout(self.ticFrame)
        self.horizLayout.addWidget(self.canvas)
        self.canvas.draw()
        self.ax = self.fig.add_subplot(111)

        self.selectT0Button.clicked.connect(self.initT0)

        self.t0Index = -1
        self.selectedPoints = []
        self.frontPointsX = []
        self.frontPointsY = []
        self.removedPointsX = []
        self.removedPointsY = []
        self.ceusResultsGui = None
        self.lastGui = None
        self.backButton.clicked.connect(self.backToLastScreen)

    def backToLastScreen(self):
        self.lastGui.ticDisplay.setHidden(True)
        self.lastGui.resultsLabel.setHidden(True)
        self.lastGui.aucLabel.setHidden(True)
        self.lastGui.aucVal.setHidden(True)
        self.lastGui.peLabel.setHidden(True)
        self.lastGui.peVal.setHidden(True)
        self.lastGui.mttLabel.setHidden(True)
        self.lastGui.mttVal.setHidden(True)
        self.lastGui.tpLabel.setHidden(True)
        self.lastGui.tpVal.setHidden(True)
        self.lastGui.tmppvLabel.setHidden(True)
        self.lastGui.tmppvVal.setHidden(True)
        self.lastGui.voiVolumeLabel.setHidden(True)
        self.lastGui.voiVolumeVal.setHidden(True)

        self.lastGui.constructVoiLabel.setHidden(False)
        self.lastGui.drawRoiButton.setHidden(True)
        self.lastGui.undoLastPtButton.setHidden(True)
        self.lastGui.closeRoiButton.setHidden(True)
        self.lastGui.redrawRoiButton.setHidden(True)
        self.lastGui.continueButton.setHidden(False)
        self.lastGui.interpolateVoiButton.setHidden(True)
        self.lastGui.restartVoiButton.setHidden(False)

        self.analysisParamsSidebar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(49, 0, 124);\n"
"	border: 1px solid black;\n"
"}")

        self.ticAnalysisSidebar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(49, 0, 124);\n"
"	border: 1px solid black;\n"
"}")

        self.lastGui.show()
        self.hide()
        

    def initT0(self):
        self.acceptT0Button.setHidden(False)
        self.selectT0Button.setHidden(True)
        self.t0Slider.setHidden(False)

        self.t0Slider.setMinimum(int(min(self.ticX[:,0])))
        self.t0Slider.setMaximum(int(max(self.ticX[:,0])))
        self.t0Slider.valueChanged.connect(self.t0ScrollValueChanged)
        self.t0Slider.setValue(0)
        self.prevLine = self.ax.axvline(x = self.t0Slider.value(), color = 'green', label = 'axvline - full height')
        self.canvas.draw()

        self.acceptT0Button.clicked.connect(self.acceptT0)

    def graph(self,x,y):
        global ticX, ticY
        y -= min(y)
        self.ticX = x
        self.ticY = y
        ticX = self.ticX
        ticY = self.ticY
        self.ax.plot(x[:,0],y)
        self.ax.scatter(x[:,0],y,color='r')
        self.ax.set_xlabel("Time (s)", fontsize=11, labelpad=1)
        self.ax.set_ylabel("Signal Amplitude", fontsize=11, labelpad=1)
        self.ax.set_title("Time Intensity Curve (TIC)", fontsize=14, pad=1.5)
        self.ax.tick_params('both', pad=0.3, labelsize=7.2)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.xticks(np.arange(0, int(max(self.ticX[:,0]))+10, 10))
        self.fig.subplots_adjust(left=0.1, right=0.97, top=0.9, bottom=0.1)

        if self.t0Index > -1:
            self.mask = np.zeros(self.ticX[:,0].shape, dtype=bool)
            self.selector = RectangleSelector(self.ax, self.rect_highlight, useblit=True, props = dict(facecolor='cyan', alpha=0.2))

        self.canvas.draw()

    def t0ScrollValueChanged(self):
        self.prevLine.remove()
        self.prevLine = self.ax.axvline(x = self.t0Slider.value(), color = 'green', label = 'axvline - full height')
        self.canvas.draw()

    def removeSelectedPoints(self):
        if len(self.selectedPoints):
            self.selectedPoints.sort()
            j = 0
            curRemovedX = []
            curRemovedY = []
            for i in range(len(self.ticX)):
                if i == self.selectedPoints[j]:
                    curRemovedX.append(self.ticX[i])
                    curRemovedY.append(self.ticY[i])
                    j += 1
                    if j == len(self.selectedPoints):
                        break
            self.ticX = np.delete(self.ticX, self.selectedPoints, axis=0)
            self.ticY = np.delete(self.ticY, self.selectedPoints)
            self.ax.clear()
            self.graph(self.ticX,self.ticY)
            self.removedPointsX.append(curRemovedX)
            self.removedPointsY.append(curRemovedY)
            self.selectedPoints = []


    def acceptT0(self):
        self.t0Slider.setHidden(True)
        self.t0Slider.setHidden(True)
        self.acceptT0Button.setHidden(True)
        self.deSelectLastPointButton.setHidden(False)
        self.deSelectLastPointButton.clicked.connect(self.deselectLast)
        self.removeSelectedPointsButton.setHidden(False)
        self.removeSelectedPointsButton.clicked.connect(self.removeSelectedPoints)
        self.restoreLastPointsButton.setHidden(False)
        self.restoreLastPointsButton.clicked.connect(self.restoreLastPoints)
        self.acceptTicButton.setHidden(False)

        if self.t0Index == -1:
            for i in range(len(self.ticX[:,0])):
                if self.ticX[:,0][i] > self.t0Slider.value():
                    break
            self.t0Index = i

        self.selectedPoints = list(range(self.t0Index))
        if len(self.selectedPoints):
            self.removeSelectedPoints()
            self.frontPointsX = self.removedPointsX[-1]
            self.frontPointsY = self.removedPointsY[-1]
            self.removedPointsX.pop()
            self.removedPointsY.pop()
        self.ticX[:,0] -= (min(self.ticX[:,0]) - 1)
        self.ax.clear()
        self.graph(self.ticX, self.ticY)

    def rect_highlight(self, event1, event2):
        self.mask |= self.inside(event1, event2)
        x = self.ticX[:,0][self.mask]
        y = self.ticY[self.mask]
        addedIndices = np.sort(np.array(list(range(len(self.ticY))))[self.mask])
        for index in addedIndices:
            self.selectedPoints.append(index) 
        self.ax.scatter(x, y, color='orange')
        self.canvas.draw()

    def inside(self, event1, event2):
        # Returns a boolean mask of the points inside the rectangle defined by
        # event1 and event2
        x0, x1 = sorted([event1.xdata, event2.xdata])
        y0, y1 = sorted([event1.ydata, event2.ydata])
        mask = ((self.ticX[:,0] > x0) & (self.ticX[:,0] < x1) &
                (self.ticY > y0) & (self.ticY < y1))
        return mask
    
    def deselectLast(self):
        if len(self.selectedPoints):
            lastPt = self.selectedPoints[-1]
            self.selectedPoints.pop()
            self.ax.scatter(self.ticX[lastPt][0],self.ticY[lastPt],color='red')
            self.canvas.draw()
            self.mask = np.zeros(self.ticX[:,0].shape, dtype=bool)

    def restoreLastPoints(self):
        if len(self.removedPointsX) > 0:
            for i in range(len(self.selectedPoints)):
                self.deselectLast()
            self.selectedPoints = []
            j = 0
            i = 0
            max = self.ticX.shape[0] + len(self.removedPointsX[-1])
            while i < self.ticX.shape[0]-1:
                if self.ticX[i][0] < self.removedPointsX[-1][j][0] and self.removedPointsX[-1][j][0] < self.ticX[i+1][0]:
                    self.ticX = np.insert(self.ticX, i+1, self.removedPointsX[-1][j], axis=0)
                    self.ticY = np.insert(self.ticY, i+1, self.removedPointsY[-1][j])
                    j += 1
                    if j == len(self.removedPointsX[-1]):
                        break
                i += 1
            if i < max and j < len(self.removedPointsX[-1]):
                while j < len(self.removedPointsX[-1]):
                    self.ticX = np.insert(self.ticX, i+1, self.removedPointsX[-1][j], axis=0)
                    self.ticY = np.append(self.ticY, self.removedPointsY[-1][j])
                    j += 1
                    i += 1
            self.removedPointsX.pop()
            self.removedPointsY.pop()
            self.ax.clear()
            ticX = self.ticX
            ticY = self.ticY
            self.graph(ticX, ticY)

    

    # def moveToRfAnalysis(self):
    #     self.rfAnalysisGui.show()
    #     self.hide()
        
        

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     # selectWindow = QWidget()
#     ui = TicAnalysisGUI()
#     # ui.selectImage.show()
#     ui.show()
#     sys.exit(app.exec_())
if __name__ == "__main__":
    import sys
    from numpy import genfromtxt
    # my_data = genfromtxt('/Users/davidspector/Home/Stanford/USImgAnalysisGui_v2/Data/newest_test_tic.csv', delimiter=',')[1:]
    my_data = genfromtxt('/Users/davidspector/Home/Stanford/USImgAnalysisGui_v2/Data/C3P13_original_tic.csv', delimiter=',')[1:]
    # my_data = genfromtxt('/Users/davidspector/Home/Stanford/USImgAnalysisGui_v2/Data/C3P13_original_tic.csv', delimiter=',')

    test_ticX = np.array([[my_data[i,0],i] for i in range(len(my_data[:,0]))])
    # test_ticY = my_data[:,1]
    test_ticY = my_data[:,1] - min(my_data[:,1])

    normalizer = max(test_ticY)

    print(np.average(my_data[:,1]))


    app = QApplication(sys.argv)
    ui = TicAnalysisGUI()
    ui.show()
    ui.graph(test_ticX, test_ticY)
    sys.exit(app.exec_())
