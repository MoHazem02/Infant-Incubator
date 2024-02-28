from PyQt5 import QtCore, QtGui, QtWidgets
from Assets import Resources_rc
import sys

class Ui_Monitor(object):
    def setupUi(self, Monitor):
        Monitor.setObjectName("Monitor")
        Monitor.resize(891, 631)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Incubator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Monitor.setWindowIcon(icon)
        Monitor.setMaximumSize(QtCore.QSize(900, 650))
        Monitor.setMinimumSize(QtCore.QSize(880, 550))
        Monitor.setStyleSheet("background-color:#3A3B3C;\n" "color: white;")
        self.centralwidget = QtWidgets.QWidget(Monitor)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.humidity_LCD = QtWidgets.QLCDNumber(self.groupBox_2)
        self.humidity_LCD.setGeometry(QtCore.QRect(40, 50, 151, 91))
        self.humidity_LCD.setObjectName("humidity_LCD")
        self.Humidity_Frame = QtWidgets.QFrame(self.groupBox_2)
        self.Humidity_Frame.setGeometry(QtCore.QRect(260, 60, 120, 80))
        self.Humidity_Frame.setStyleSheet("image: url(:/newPrefix/humidity.png);")
        self.Humidity_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Humidity_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Humidity_Frame.setObjectName("Humidity_Frame")
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.BPM_LCD = QtWidgets.QLCDNumber(self.groupBox)
        self.BPM_LCD.setGeometry(QtCore.QRect(180, 50, 151, 91))
        self.BPM_LCD.setObjectName("BPM_LCD")
        self.BPM_Frame = QtWidgets.QFrame(self.groupBox)
        self.BPM_Frame.setGeometry(QtCore.QRect(30, 60, 120, 80))
        self.BPM_Frame.setStyleSheet("image: url(:/newPrefix/heart.png);")
        self.BPM_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BPM_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BPM_Frame.setObjectName("BPM_Frame")
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.set_button = QtWidgets.QPushButton(self.groupBox_3)
        self.set_button.setGeometry(QtCore.QRect(230, 180, 181, 31))
        self.set_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.set_button.setStyleSheet("background-color: #784B84;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.set_button.setObjectName("set_button")
        self.temp_LCD = QtWidgets.QLCDNumber(self.groupBox_3)
        self.temp_LCD.setGeometry(QtCore.QRect(20, 70, 151, 91))
        self.temp_LCD.setObjectName("temp_LCD")
        self.increase_button = QtWidgets.QPushButton(self.groupBox_3)
        self.increase_button.setEnabled(True)
        self.increase_button.setGeometry(QtCore.QRect(330, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.increase_button.setFont(font)
        self.increase_button.setStyleSheet("background-color: #00A86B;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.increase_button.setObjectName("increase_button")
        self.decrease_button = QtWidgets.QPushButton(self.groupBox_3)
        self.decrease_button.setGeometry(QtCore.QRect(230, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.decrease_button.setFont(font)
        self.decrease_button.setStyleSheet("background-color: #E0115F;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"     border: 1.2px ;\n"
"border-style: outset;\n"
"border-radius: 8px;")
        self.decrease_button.setObjectName("decrease_button")
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 110, 111, 61))
        self.label.setStyleSheet("font-size: 38px;")
        self.label.setObjectName("label")
        self.Status_Frame = QtWidgets.QFrame(self.frame)
        self.Status_Frame.setGeometry(QtCore.QRect(190, 100, 120, 80))
        self.Status_Frame.setStyleSheet("image: url(:/newPrefix/checked.png);")
        self.Status_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Status_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Status_Frame.setObjectName("Status_Frame")
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        Monitor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Monitor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 26))
        self.menubar.setObjectName("menubar")
        Monitor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Monitor)
        self.statusbar.setObjectName("statusbar")
        Monitor.setStatusBar(self.statusbar)

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        _translate = QtCore.QCoreApplication.translate
        Monitor.setWindowTitle(_translate("Monitor", "Incubator Monitor"))
        self.groupBox_2.setTitle(_translate("Monitor", "Humidity"))
        self.groupBox.setTitle(_translate("Monitor", "Heart Rate"))
        self.groupBox_3.setTitle(_translate("Monitor", "Temperature"))
        self.set_button.setText(_translate("Monitor", "SET"))
        self.increase_button.setText(_translate("Monitor", "+"))
        self.decrease_button.setText(_translate("Monitor", "-"))
        self.label.setText(_translate("Monitor", "Status"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Monitor = QtWidgets.QMainWindow()
    ui = Ui_Monitor()
    ui.setupUi(Monitor)
    Monitor.show()
    sys.exit(app.exec_())
