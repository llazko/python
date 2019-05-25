import sys
from PyQt5 import QtCore, uic, QtWidgets
from matplotlib.pyplot import *

qtCreatorFile = "pr1.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #.... you application continues here ....
        self.QuitButton.clicked.connect(self.GoQuit)
        self.PlotButton.clicked.connect(self.GoPlot)
    def GoPlot(self):
        L = [1,2,3,4,5]
        self.graphicsView.plot(L)
    def GoQuit(self):
        sys.exit(app.exec_())        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



