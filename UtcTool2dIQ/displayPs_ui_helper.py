from UtcTool2dIQ.displayPs_ui import *
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class PsPlotterGUI(Ui_psPlotter, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Prepare PS display plot
        self.horizontalLayout = QHBoxLayout(self.plotFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.horizontalLayout.addWidget(self.canvas)

        


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # selectWindow = QWidget()
    ui = PsPlotterGUI()
    # ui.selectImage.show()
    ui.show()
    sys.exit(app.exec_())