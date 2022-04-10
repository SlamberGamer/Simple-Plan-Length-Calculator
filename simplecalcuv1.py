# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simplecalcuv1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 547)

        def Calcu():
            num1 = float(self.textEdit.toPlainText())
            num2 = float(self.textEdit_2.toPlainText())
            # ans = multipy(num1 , num2)
            print(num2)
            # self.label_4.setText(ans)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 431, 221))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Nasalization Rg")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 30, 10)")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 360, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Nasalization Rg")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 30, 10)")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 430, 271, 61))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(152,251,152)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 280, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 350, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 300, 93, 71))
        self.pushButton.setStyleSheet("border-radius : 100; border : 2px solid black\n"
"setGeometry(200, 150, 100, 100)")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(Calcu)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SimpleCalcu"))
        self.label.setText(_translate("MainWindow", "░██████╗██╗███╗░░░███╗██████╗░██╗░░░░░███████╗\n"
"██╔════╝██║████╗░████║██╔══██╗██║░░░░░██╔════╝\n"
"╚█████╗░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░\n"
"░╚═══██╗██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░\n"
"██████╔╝██║██║░╚═╝░██║██║░░░░░███████╗███████╗\n"
"╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝\n"
"\n"
"░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗\n"
"██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║\n"
"██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║\n"
"██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║\n"
"╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝\n"
"░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░"))
        self.label_2.setText(_translate("MainWindow", "Value 1 :"))
        self.label_4.setText(_translate("MainWindow", "Value 2 :"))
        self.label_3.setText(_translate("MainWindow", "Answer"))
        self.pushButton.setText(_translate("MainWindow", "CalCu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

