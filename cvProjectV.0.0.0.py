# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComputerVisionProject.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 128))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.load = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.load.setObjectName("load")
        self.gridLayout.addWidget(self.load, 1, 0, 1, 1)
        self.save = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.filter = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.filter.setObjectName("filter")
        self.gridLayout.addWidget(self.filter, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 150, 281, 73))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.goruntuleme = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.goruntuleme.setObjectName("goruntuleme")
        self.gridLayout_2.addWidget(self.goruntuleme, 1, 0, 1, 1)
        self.esitleme = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.esitleme.setObjectName("esitleme")
        self.gridLayout_2.addWidget(self.esitleme, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 230, 281, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 350, 281, 61))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_3, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(320, 10, 571, 541))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 490, 281, 51))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(300, -10, 20, 551))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 290, 279, 51))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_2, 1, 0, 1, 1)
        self.esitleme_2 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.esitleme_2.setObjectName("esitleme_2")
        self.gridLayout_5.addWidget(self.esitleme_2, 0, 0, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(10, 420, 281, 61))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget_7)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_4, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load.setText(_translate("MainWindow", "Load"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Gaussian"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Hessian"))
        self.comboBox.setItemText(2, _translate("MainWindow", "İnverse"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Laplace"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Median"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Otsu"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Farid"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Roberts"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Sato"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Sobel"))
        self.filter.setText(_translate("MainWindow", "Run"))
        self.label.setText(_translate("MainWindow", "Filtreler"))
        self.goruntuleme.setText(_translate("MainWindow", "Histogram Görüntüleme"))
        self.esitleme.setText(_translate("MainWindow", "Histogram Eşikleme"))
        self.label_2.setText(_translate("MainWindow", "Histogram Görüntüleme Ve Eşikleme"))
        self.label_3.setText(_translate("MainWindow", "Yoğunluk Dönüşümü"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Resize"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Rotate"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Rescale"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Swirl"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Warp"))
        self.label_6.setText(_translate("MainWindow", "Uzaysal Dönüşüm İşlemleri"))
        self.pushButton.setText(_translate("MainWindow", "Video Seçme"))
        self.label_7.setText(_translate("MainWindow", "Kenar Belirleme"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Resize"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Rotate"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Rescale"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Swirl"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Warp"))
        self.esitleme_2.setText(_translate("MainWindow", "Histogram Eşikleme"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Resize"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Rotate"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Rescale"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Swirl"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Warp"))
        self.label_8.setText(_translate("MainWindow", "Morfolojik İşlemler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

