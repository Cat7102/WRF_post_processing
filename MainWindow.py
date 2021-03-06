# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import OtherParameter_interpolate,Windspeed_interpolate,Windspeed_interpolate_time,Draw_plan_graph,Get_data,Draw_vertical_graph


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 189)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WRF后处理"))
        self.pushButton.setText(_translate("MainWindow", "风速插值（高度）"))
        self.pushButton_3.setText(_translate("MainWindow", "气象参数插值计算（除风速）"))
        self.pushButton_2.setText(_translate("MainWindow", "风速插值（时间）"))
        self.pushButton_4.setText(_translate("MainWindow", "绘制平面图"))
        self.pushButton_5.setText(_translate("MainWindow", "提取参数"))
        self.pushButton_6.setText(_translate("MainWindow", "绘制立面图"))

        '''以下是自己编辑的内容'''
        self.pushButton.clicked.connect(self.show_dialog_1)
        self.pushButton_2.clicked.connect(self.show_dialog_2)
        self.pushButton_3.clicked.connect(self.show_dialog_3)
        self.pushButton_4.clicked.connect(self.show_dialog_4)
        self.pushButton_5.clicked.connect(self.show_dialog_5)
        self.pushButton_6.clicked.connect(self.show_dialog_6)

    def show_dialog_1(self):
        MainWindow = QtWidgets.QDialog()
        ui = Windspeed_interpolate.Ui_Dialog()
        ui.setupUi(MainWindow)
        MainWindow.exec_()

    def show_dialog_2(self):
        MainWindow = QtWidgets.QDialog()
        ui = Windspeed_interpolate_time.Ui_Dialog()
        ui.setupUi(MainWindow)
        MainWindow.exec_()

    def show_dialog_3(self):
        MainWindow = QtWidgets.QDialog()
        ui = OtherParameter_interpolate.Ui_Dialog()
        ui.setupUi(MainWindow)
        MainWindow.exec_()

    def show_dialog_4(self):
        MainWindow = QtWidgets.QDialog()
        ui = Draw_plan_graph.Ui_Dialog()
        ui.setupUi(MainWindow)
        MainWindow.exec_()

    def show_dialog_5(self):
        MainWindow = QtWidgets.QDialog()
        ui = Get_data.Ui_Dialog()
        ui.setupUi(MainWindow)
        MainWindow.exec_()

    def show_dialog_6(self):
        MainWindow = QtWidgets.QDialog()
        ui = Draw_vertical_graph.Ui_Dialog()
        ui.setupUi(MainWindow)
        MainWindow.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())