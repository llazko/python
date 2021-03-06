import sys
import datetime
import requests
from PyQt5 import QtCore, uic, QtWidgets
 
qtCreatorFile = "btc.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		today = datetime.datetime.now()
		res = today.strftime("%Y-%m-%d")
		url = "https://api.coindesk.com/v1/bpi/currentprice.json"
		resp = requests.get(url)
		self.label.setText(str(resp.json()['bpi']['USD']['rate']) + " today")

		self.prev_button.clicked.connect(self.GoPrev)
		self.next_button.clicked.connect(self.GoNext)
		self.quit_button.clicked.connect(self.GoQuit)

	def GoNext(self):
		global daynumber
		if daynumber < -1:
			daynumber += 1
		today = datetime.datetime.now()
		day = datetime.timedelta(days=daynumber)
		res = (today + day).strftime("%Y-%m-%d")
		url = "https://api.coindesk.com/v1/bpi/historical/close.json"
		
		resp = requests.get(url, params={'start' : res , 'end' : res})
		self.label.setText(str(resp.json()['bpi'][res]) + " on {}" .format(res))


	def GoPrev(self):
		global daynumber
		daynumber -= 1
		today = datetime.datetime.now()
		day = datetime.timedelta(days=daynumber)
		res = (today + day).strftime("%Y-%m-%d")
		url = "https://api.coindesk.com/v1/bpi/historical/close.json"
		
		resp = requests.get(url, params={'start' : res , 'end' : res})
		self.label.setText(str(resp.json()['bpi'][res])+ " on {}" .format(res))

	def GoQuit(self):
		sys.exit(app.exec_())
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    daynumber = 0
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
