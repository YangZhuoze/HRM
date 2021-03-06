# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Python\HRM\main\Ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setMaximumSize(QtCore.QSize(16777215, 121))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 2, 3)
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_human = QtWidgets.QWidget()
        self.tab_human.setObjectName("tab_human")
        self.frame_human_query = QtWidgets.QFrame(self.tab_human)
        self.frame_human_query.setGeometry(QtCore.QRect(70, 40, 131, 171))
        self.frame_human_query.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_human_query.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_human_query.setObjectName("frame_human_query")
        self.graphics_human_query = QtWidgets.QGraphicsView(self.frame_human_query)
        self.graphics_human_query.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_human_query.setStyleSheet("border-image: url(:/images/human_query.jpg);\n"
"")
        self.graphics_human_query.setResizeAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.graphics_human_query.setObjectName("graphics_human_query")
        self.button_human_query = QtWidgets.QPushButton(self.frame_human_query)
        self.button_human_query.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_human_query.setObjectName("button_human_query")
        self.frame_human_create = QtWidgets.QFrame(self.tab_human)
        self.frame_human_create.setGeometry(QtCore.QRect(230, 40, 131, 171))
        self.frame_human_create.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_human_create.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_human_create.setObjectName("frame_human_create")
        self.graphics_human_create = QtWidgets.QGraphicsView(self.frame_human_create)
        self.graphics_human_create.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_human_create.setStyleSheet("border-image: url(:/images/human_create.jpg);")
        self.graphics_human_create.setObjectName("graphics_human_create")
        self.button_human_create = QtWidgets.QPushButton(self.frame_human_create)
        self.button_human_create.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_human_create.setObjectName("button_human_create")
        self.frame_human_update = QtWidgets.QFrame(self.tab_human)
        self.frame_human_update.setGeometry(QtCore.QRect(390, 40, 131, 171))
        self.frame_human_update.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_human_update.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_human_update.setObjectName("frame_human_update")
        self.graphics_human_update = QtWidgets.QGraphicsView(self.frame_human_update)
        self.graphics_human_update.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_human_update.setStyleSheet("border-image: url(:/images/human_update.jpg);\n"
"")
        self.graphics_human_update.setObjectName("graphics_human_update")
        self.button_human_update = QtWidgets.QPushButton(self.frame_human_update)
        self.button_human_update.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_human_update.setObjectName("button_human_update")
        self.frame_human_confirm = QtWidgets.QFrame(self.tab_human)
        self.frame_human_confirm.setGeometry(QtCore.QRect(550, 40, 131, 171))
        self.frame_human_confirm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_human_confirm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_human_confirm.setObjectName("frame_human_confirm")
        self.graphics_human_confirm = QtWidgets.QGraphicsView(self.frame_human_confirm)
        self.graphics_human_confirm.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_human_confirm.setStyleSheet("border-image: url(:/images/human_confirm.jpg);\n"
"")
        self.graphics_human_confirm.setObjectName("graphics_human_confirm")
        self.button_human_confirm = QtWidgets.QPushButton(self.frame_human_confirm)
        self.button_human_confirm.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_human_confirm.setObjectName("button_human_confirm")
        self.frame_position_query = QtWidgets.QFrame(self.tab_human)
        self.frame_position_query.setGeometry(QtCore.QRect(70, 240, 131, 171))
        self.frame_position_query.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_position_query.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_position_query.setObjectName("frame_position_query")
        self.graphics_position_query = QtWidgets.QGraphicsView(self.frame_position_query)
        self.graphics_position_query.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_position_query.setStyleSheet("border-image: url(:/images/position_query.jpg);\n"
"")
        self.graphics_position_query.setObjectName("graphics_position_query")
        self.button_position_query = QtWidgets.QPushButton(self.frame_position_query)
        self.button_position_query.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_position_query.setObjectName("button_position_query")
        self.frame_human_xx = QtWidgets.QFrame(self.tab_human)
        self.frame_human_xx.setGeometry(QtCore.QRect(230, 240, 131, 171))
        self.frame_human_xx.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_human_xx.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_human_xx.setObjectName("frame_human_xx")
        self.graphics_position_list = QtWidgets.QGraphicsView(self.frame_human_xx)
        self.graphics_position_list.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_position_list.setStyleSheet("border-image: url(:/images/position_list.jpg);\n"
"")
        self.graphics_position_list.setObjectName("graphics_position_list")
        self.button_position_list = QtWidgets.QPushButton(self.frame_human_xx)
        self.button_position_list.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_position_list.setObjectName("button_position_list")
        self.frame_role = QtWidgets.QFrame(self.tab_human)
        self.frame_role.setGeometry(QtCore.QRect(390, 240, 131, 171))
        self.frame_role.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_role.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_role.setObjectName("frame_role")
        self.graphics_role = QtWidgets.QGraphicsView(self.frame_role)
        self.graphics_role.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_role.setStyleSheet("border-image: url(:/images/role_list.jpg);\n"
"")
        self.graphics_role.setObjectName("graphics_role")
        self.button_role = QtWidgets.QPushButton(self.frame_role)
        self.button_role.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_role.setObjectName("button_role")
        self.frame_role_link_list = QtWidgets.QFrame(self.tab_human)
        self.frame_role_link_list.setGeometry(QtCore.QRect(550, 240, 131, 171))
        self.frame_role_link_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_role_link_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_role_link_list.setObjectName("frame_role_link_list")
        self.graphics_role_link_list = QtWidgets.QGraphicsView(self.frame_role_link_list)
        self.graphics_role_link_list.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_role_link_list.setStyleSheet("border-image: url(:/images/role.jpg);\n"
"")
        self.graphics_role_link_list.setObjectName("graphics_role_link_list")
        self.button_role_link_list = QtWidgets.QPushButton(self.frame_role_link_list)
        self.button_role_link_list.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_role_link_list.setObjectName("button_role_link_list")
        self.tabWidget.addTab(self.tab_human, "")
        self.tab_institute = QtWidgets.QWidget()
        self.tab_institute.setObjectName("tab_institute")
        self.frame_institute_query = QtWidgets.QFrame(self.tab_institute)
        self.frame_institute_query.setGeometry(QtCore.QRect(70, 40, 131, 171))
        self.frame_institute_query.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_institute_query.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_institute_query.setObjectName("frame_institute_query")
        self.graphics_institute_query = QtWidgets.QGraphicsView(self.frame_institute_query)
        self.graphics_institute_query.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_institute_query.setStyleSheet("border-image: url(:/images/ins_query.jpg);")
        self.graphics_institute_query.setObjectName("graphics_institute_query")
        self.button_institute_query = QtWidgets.QPushButton(self.frame_institute_query)
        self.button_institute_query.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_institute_query.setObjectName("button_institute_query")
        self.frame_institute_create = QtWidgets.QFrame(self.tab_institute)
        self.frame_institute_create.setGeometry(QtCore.QRect(230, 40, 131, 171))
        self.frame_institute_create.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_institute_create.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_institute_create.setObjectName("frame_institute_create")
        self.graphics_institute_create = QtWidgets.QGraphicsView(self.frame_institute_create)
        self.graphics_institute_create.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_institute_create.setStyleSheet("border-image: url(:/images/ins_create.jpg);")
        self.graphics_institute_create.setObjectName("graphics_institute_create")
        self.button_institute_create = QtWidgets.QPushButton(self.frame_institute_create)
        self.button_institute_create.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_institute_create.setObjectName("button_institute_create")
        self.frame_institute_update = QtWidgets.QFrame(self.tab_institute)
        self.frame_institute_update.setGeometry(QtCore.QRect(390, 40, 131, 171))
        self.frame_institute_update.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_institute_update.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_institute_update.setObjectName("frame_institute_update")
        self.graphics_institute_update = QtWidgets.QGraphicsView(self.frame_institute_update)
        self.graphics_institute_update.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_institute_update.setStyleSheet("border-image: url(:/images/ins_update.jpg);")
        self.graphics_institute_update.setObjectName("graphics_institute_update")
        self.button_institute_update = QtWidgets.QPushButton(self.frame_institute_update)
        self.button_institute_update.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_institute_update.setObjectName("button_institute_update")
        self.tabWidget.addTab(self.tab_institute, "")
        self.tab_salary = QtWidgets.QWidget()
        self.tab_salary.setObjectName("tab_salary")
        self.frame_salary_query = QtWidgets.QFrame(self.tab_salary)
        self.frame_salary_query.setGeometry(QtCore.QRect(70, 40, 131, 171))
        self.frame_salary_query.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salary_query.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salary_query.setObjectName("frame_salary_query")
        self.graphics_salary_query = QtWidgets.QGraphicsView(self.frame_salary_query)
        self.graphics_salary_query.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_salary_query.setStyleSheet("border-image: url(:/images/salary_query.jpg);")
        self.graphics_salary_query.setObjectName("graphics_salary_query")
        self.button_salary_query = QtWidgets.QPushButton(self.frame_salary_query)
        self.button_salary_query.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_salary_query.setObjectName("button_salary_query")
        self.frame_salary_create = QtWidgets.QFrame(self.tab_salary)
        self.frame_salary_create.setGeometry(QtCore.QRect(230, 40, 131, 171))
        self.frame_salary_create.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salary_create.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salary_create.setObjectName("frame_salary_create")
        self.graphics_salary_create = QtWidgets.QGraphicsView(self.frame_salary_create)
        self.graphics_salary_create.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_salary_create.setStyleSheet("border-image: url(:/images/salary_create.jpg);")
        self.graphics_salary_create.setObjectName("graphics_salary_create")
        self.button_salary_create = QtWidgets.QPushButton(self.frame_salary_create)
        self.button_salary_create.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_salary_create.setObjectName("button_salary_create")
        self.frame_salary_update = QtWidgets.QFrame(self.tab_salary)
        self.frame_salary_update.setGeometry(QtCore.QRect(390, 40, 131, 171))
        self.frame_salary_update.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salary_update.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salary_update.setObjectName("frame_salary_update")
        self.graphics_salary_update = QtWidgets.QGraphicsView(self.frame_salary_update)
        self.graphics_salary_update.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_salary_update.setStyleSheet("border-image: url(:/images/salary_update.jpg);")
        self.graphics_salary_update.setObjectName("graphics_salary_update")
        self.button_salary_update = QtWidgets.QPushButton(self.frame_salary_update)
        self.button_salary_update.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_salary_update.setObjectName("button_salary_update")
        self.frame_salary_confirm = QtWidgets.QFrame(self.tab_salary)
        self.frame_salary_confirm.setGeometry(QtCore.QRect(550, 40, 131, 171))
        self.frame_salary_confirm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salary_confirm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salary_confirm.setObjectName("frame_salary_confirm")
        self.graphics_salary_confirm = QtWidgets.QGraphicsView(self.frame_salary_confirm)
        self.graphics_salary_confirm.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_salary_confirm.setStyleSheet("border-image: url(:/images/salary_confirm.jpg);")
        self.graphics_salary_confirm.setObjectName("graphics_salary_confirm")
        self.button_salary_confirm = QtWidgets.QPushButton(self.frame_salary_confirm)
        self.button_salary_confirm.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_salary_confirm.setObjectName("button_salary_confirm")
        self.frame_salary_pay = QtWidgets.QFrame(self.tab_salary)
        self.frame_salary_pay.setGeometry(QtCore.QRect(70, 240, 131, 171))
        self.frame_salary_pay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salary_pay.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salary_pay.setObjectName("frame_salary_pay")
        self.graphics_salary_pay = QtWidgets.QGraphicsView(self.frame_salary_pay)
        self.graphics_salary_pay.setGeometry(QtCore.QRect(0, 0, 131, 121))
        self.graphics_salary_pay.setStyleSheet("border-image: url(:/images/salary_pay.jpg);")
        self.graphics_salary_pay.setObjectName("graphics_salary_pay")
        self.button_salary_pay = QtWidgets.QPushButton(self.frame_salary_pay)
        self.button_salary_pay.setGeometry(QtCore.QRect(20, 130, 91, 31))
        self.button_salary_pay.setObjectName("button_salary_pay")
        self.tabWidget.addTab(self.tab_salary, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 2, 1, 1)
        self.label_currentUser = QtWidgets.QLabel(self.centralWidget)
        self.label_currentUser.setGeometry(QtCore.QRect(592, 70, 105, 60))
        self.label_currentUser.setObjectName("label_currentUser")
        self.label_currentUser_data = QtWidgets.QLabel(self.centralWidget)
        self.label_currentUser_data.setGeometry(QtCore.QRect(703, 70, 88, 60))
        self.label_currentUser_data.setObjectName("label_currentUser_data")
        self.graphicsView.raise_()
        self.tabWidget.raise_()
        self.label_currentUser.raise_()
        self.label_currentUser_data.raise_()
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_human_query.setText(_translate("MainWindow", "人事查询"))
        self.button_human_create.setText(_translate("MainWindow", "人事登记"))
        self.button_human_update.setText(_translate("MainWindow", "人事变更"))
        self.button_human_confirm.setText(_translate("MainWindow", "人事复核"))
        self.button_position_query.setText(_translate("MainWindow", "职位查询"))
        self.button_position_list.setText(_translate("MainWindow", "职位操作"))
        self.button_role.setText(_translate("MainWindow", "权限管理"))
        self.button_role_link_list.setText(_translate("MainWindow", "权限关联"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_human), _translate("MainWindow", "人事管理"))
        self.button_institute_query.setText(_translate("MainWindow", "机构查询"))
        self.button_institute_create.setText(_translate("MainWindow", "机构登记"))
        self.button_institute_update.setText(_translate("MainWindow", "机构变更"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_institute), _translate("MainWindow", "机构管理"))
        self.button_salary_query.setText(_translate("MainWindow", "薪酬查询"))
        self.button_salary_create.setText(_translate("MainWindow", "薪酬登记"))
        self.button_salary_update.setText(_translate("MainWindow", "薪酬变更"))
        self.button_salary_confirm.setText(_translate("MainWindow", "薪酬复核"))
        self.button_salary_pay.setText(_translate("MainWindow", "薪酬发放"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_salary), _translate("MainWindow", "薪酬管理"))
        self.label_currentUser.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">当前登陆用户：</span></p></body></html>"))
        self.label_currentUser_data.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">currentUser</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

