from UtcTool2dIQ.editWindowDisplay_ui import *

from PyQt5.QtWidgets import QWidget

class EditWindowDisplayGUI(Ui_editBmode, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.p1xDisplay.setTextVisible(False)
        self.p1yDisplay.setTextVisible(False)
        self.p2xDisplay.setTextVisible(False)
        self.p2yDisplay.setTextVisible(False)
    