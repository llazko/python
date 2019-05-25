import sys
from PyQt5 import QtCore, uic, QtWidgets
from matplotlib.pyplot import *
import serial.tools.list_ports

qtCreatorFile = "pr1.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def serial_ports():    
    return serial.tools.list_ports.comports()

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #.... you application continues here ....
        self.QuitButton.clicked.connect(self.GoQuit)
        self.PlotButton.clicked.connect(self.GoPlot)
        self.OpenButton.clicked.connect(self.GoOpen)
        self.CloseButton.clicked.connect(self.GoClose)
        self.SendButton.clicked.connect(self.GoSend)
        ports = serial_ports()
        COMs = ports[:]
        BAUDs = ["9600","115200"]

        for k in range(len(COMs)):
            self.comboBox_PORT.addItem(COMs[k][0])
        
        for k in range(len(BAUDs)):
            self.comboBox_BAUD.addItem(BAUDs[k])

        self.Port = self.comboBox_PORT.currentText()
        self.Baud = int(self.comboBox_BAUD.currentText())

        self.comboBox_BAUD.activated[str].connect(self.onBaud)      
        self.comboBox_PORT.activated[str].connect(self.onPort)      
        self.ser = serial.Serial()
 
    def GoPlot(self):
        while self.ser.in_waiting > 0:    
            print(self.ser.read())
#        self.graphicsView.plot(L)
            
    def GoQuit(self):
        self.ser.close()
        sys.exit(app.exec_())        

    def GoOpen(self):
        self.ser = serial.Serial(self.Port, self.Baud)
        print("Port " + self.Port +" is opened @" + str(self.Baud) + "bps")

    def GoClose(self):
        self.ser.close()
        print("Port is closed")

    def onBaud(self, text):
        print(text)
        self.Baud = int(text)

    def onPort(self, text):
        print(text)
        self.Port = text

    def GoSend(self):
        self.sendString = self.textEdit.toPlainText()
        print(self.sendString)
        self.ser.write(str.encode(self.sendString))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



