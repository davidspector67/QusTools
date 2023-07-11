from CeusTool3d.ceusAnalysis_ui import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas




class CeusAnalysisGui(Ui_rfAnalysis, QWidget):
    def __init__(self):
        # self.selectImage = QWidget()
        super().__init__()
        self.setupUi(self)

        self.horizLayout = QHBoxLayout(self.ticDisplay)
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.horizLayout.addWidget(self.canvas)
        self.canvas.draw()
        
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # selectWindow = QWidget()
    ui = CeusAnalysisGui()
    # ui.selectImage.show()
    ui.show()
    sys.exit(app.exec_())