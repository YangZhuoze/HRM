# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui.Ui_main import Ui_MainWindow
from .create import create_event

import main.currentUser as currentUser

class main_event(QMainWindow, Ui_MainWindow):
    
    create = create_event()
    
    def __init__(self, parent=None):
        super(main_event, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_button_query_clicked(self):
        self.create.show()