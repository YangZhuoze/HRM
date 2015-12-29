# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui.Ui_main import Ui_MainWindow
from .message import message_event
from .clerk_query_list import clerk_query_list_event
from .clerk_create import clerk_create_event
from .clerk_update_list import clerk_update_list_event
from .clerk_confirm_list import clerk_confirm_list_event
from .salary_query_list import salary_query_list_event

from config import Permission
import currentApp

class main_event(QMainWindow, Ui_MainWindow):
    
    message = None
    clerk_query = None
    clerk_create = None
    clerk_update = None
    clerk_confirm = None
    salary_query = None
    
    def __init__(self, parent=None):
        super(main_event, self).__init__(parent)
        self.setupUi(self)
        self.label_currentUser_data.setText(currentApp.getCurrentUser().name)

    @pyqtSlot()
    def on_button_human_query_clicked(self):
        self.clerk_query = clerk_query_list_event()
        self.clerk_query.show()

    @pyqtSlot()
    def on_button_human_create_clicked(self):
        if (currentApp.getCurrentUser().role.permission &
                Permission.HUMAN_REGISTER == Permission.HUMAN_REGISTER):
            self.clerk_ = clerk_create_event()
            self.clerk_.show()
        else:
            self.message = message_event(msg = 'Permission Denied')
            self.message.show()
            
    @pyqtSlot()
    def on_button_human_update_clicked(self):
        if (currentApp.getCurrentUser().role.permission &
                Permission.HUMAN_UPDATE == Permission.HUMAN_UPDATE):
            self.clerk_update = clerk_update_list_event()
            self.clerk_update.show()
        else:
            self.message = message_event(msg = 'Permission Denied')
            self.message.show()
            
    @pyqtSlot()
    def on_button_human_confirm_clicked(self):
        if (currentApp.getCurrentUser().role.permission &
                Permission.HUMAN_COMFIRM == Permission.HUMAN_COMFIRM):
            self.clerk_confirm = clerk_confirm_list_event()
            self.clerk_confirm.show()
        else:
            self.message = message_event(msg = 'Permission Denied')
            self.message.show()
            
    @pyqtSlot()
    def on_button_salary_query_clicked(self):
        self.salary_query = salary_query_list_event()
        self.salary_query.show()
