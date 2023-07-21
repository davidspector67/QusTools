import sys
from PySide2.QtWidgets import QApplication
from CeusTool3d.selectImage_ui_helper import *
from UtcTool2d.selectImage_ui_helper import *
from CeusMcTool2d.selectImage_ui_helper import *
from welcome_ui import *

class QusGui(Ui_qusPage, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.utc2dButton.clicked.connect(self.moveToUtc2d)
        self.ceus3dButton.clicked.connect(self.moveToCeus3d)
        self.ceus2dButton.clicked.connect(self.moveToCeusMc2d)
        self.nextPage = None

    def moveToUtc2d(self):
        del self.nextPage
        self.nextPage = SelectImageGUI_UtcTool2d()
        self.nextPage.show()
        self.nextPage.welcomeGui = self
        self.hide()

    def moveToCeus3d(self):
        del self.nextPage
        self.nextPage = SelectImageGUI_CeusTool3d()
        self.nextPage.show()
        self.nextPage.welcomeGui = self
        self.hide()

    def moveToCeusMc2d(self):
        del self.nextPage
        self.nextPage = SelectImageGUI_CeusMcTool2d()
        self.nextPage.show()
        self.nextPage.welcomeGui = self
        self.hide()

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    welcomeApp = QApplication(sys.argv)
    welcomeUI = QusGui()
    welcomeUI.show()
    sys.exit(welcomeApp.exec_())