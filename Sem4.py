# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SemesterPendekAugust2021v2.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import qdarkstyle
import webbrowser

f_date = date(2021, 8, 20)  # first date
l_date = date(2021, 10, 8)  # Last Date
A_date = date(2021, 7, 11)  # just to get 1 value. cannot use standart value because the date need to be in date
B_date = date(2021, 7, 10)  # just to get 1 value. cannot use standart value because the date need to be in date
one = A_date - B_date
today = date.today()
#print("Today's date:", today)
Total = l_date - f_date
#print(Total.days)
Current = l_date - today
#print(Current.days)
percentage = 100 - (( Current / Total ) * 100 )
weeks = (Current / one) / 7
#print (weeks)
#print (percentage)

def RELIABILITYCLASS():
    webbrowser.open('https://classroom.google.com/u/1/c/MzgzNDQwODQzODk5') #self.pushButton_2.clicked.connect(RELIABILITYCLASS)

def INTRUMENTATIONCLASS():
    webbrowser.open('https://classroom.google.com/u/1/c/Mzc5MDIwNTMwOTY5') #self.pushButton_3.clicked.connect(INTRUMENTATIONCLASS)

def RELIABILITYWASAP():
    webbrowser.open('https://chat.whatsapp.com/LbpOT4nrvg1BC9a32fgBtu') #self.pushButton.clicked.connect(RELIABILITYWASAP)

def INTRUMENTATIONWASAP():
    webbrowser.open('https://chat.whatsapp.com/GdbmUeAnfjX3v0gtixONMq') #self.pushButton_4.clicked.connect(INTRUMENTATIONWASAP)

def ONLINENOTES():
    webbrowser.open('https://docs.google.com/document/d/1XVbhW7EwnLS2vss4HNFtFDLS68msvZHC6T0OrRqkdCo/edit?usp=sharing') #self.pushButton_5.clicked.connect(ONLINENOTES)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(521, 567)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks)
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(20, 350, 481, 171))
        self.tableWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setMidLineWidth(-3)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAutoScrollMargin(23)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("EMT478 Instrumentation")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget.verticalHeader().setDefaultSectionSize(70)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(280, 300, 221, 21))
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setFormat("%p%")
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(percentage)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(280, 200, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display(weeks)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(350, 210, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(280, 250, 64, 23))
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_2.setLineWidth(0)
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.display(percentage)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(350, 250, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 30, 10)")
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 219, 95, 31))
        self.pushButton_2.clicked.connect(RELIABILITYCLASS)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(235, 52, 128);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 264, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(142, 298, 95, 28))
        self.pushButton_3.clicked.connect(INTRUMENTATIONCLASS)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(235, 52, 128);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 298, 95, 28))
        self.pushButton_4.clicked.connect(INTRUMENTATIONWASAP)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(245, 81, 66);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 219, 101, 31))
        self.pushButton.clicked.connect(RELIABILITYWASAP)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(245, 81, 66);\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 160, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 441, 111))
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 160, 191, 31))
        self.pushButton_5.clicked.connect(ONLINENOTES)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb74, 77, 82;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Semester Pendek August 2021"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sat"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sun"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "9.00am - 11.00am"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "11.30am - 12.30pm"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "12.30pm- 4.00pm"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "EMT 368 Reliability and Testability in\n"
"IC"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "EMT 368 Reliability and Testability in\n"
"IC"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "EMT 368 Reliability and Testability in\n"
"IC"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "EMT478 Instrumentation"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "EMT478 Instrumentation"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "Weeks left"))
        self.label_9.setText(_translate("MainWindow", "%"))
        self.pushButton_2.setText(_translate("MainWindow", "Classroom"))
        self.label_2.setText(_translate("MainWindow", "EMT478 Instrumentation"))
        self.pushButton_3.setText(_translate("MainWindow", "Classroom"))
        self.pushButton_4.setText(_translate("MainWindow", "whatsapp"))
        self.pushButton.setText(_translate("MainWindow", "whatsapp"))
        self.label.setText(_translate("MainWindow", "EMT 368 Reliability and \n"
"Testability in IC"))
        self.label_3.setText(_translate("MainWindow", "██╗░░░██╗███╗░░██╗██╗███╗░░░███╗░█████╗░██████╗░\n"
"██║░░░██║████╗░██║██║████╗░████║██╔══██╗██╔══██╗\n"
"██║░░░██║██╔██╗██║██║██╔████╔██║███████║██████╔╝\n"
"██║░░░██║██║╚████║██║██║╚██╔╝██║██╔══██║██╔═══╝░\n"
"╚██████╔╝██║░╚███║██║██║░╚═╝░██║██║░░██║██║░░░░░\n"
"░╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░"))
        self.pushButton_5.setText(_translate("MainWindow", "Classroom Notes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

