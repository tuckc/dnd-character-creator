from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

class BackgroundWindow(QWidget):
	def __init__(self, parent):	
		QTabWidget.__init__(self)
		self.tab_window = parent
		self.setup()	

	def setup(self):
		self.vbox = QVBoxLayout()
		self.picbox = QHBoxLayout()
		self.buttonbox = QHBoxLayout()

		self.buttonbox.addWidget(QLabel('Background', self))

		self.vbox.addLayout(self.picbox)	
		self.vbox.addLayout(self.buttonbox)	

		self.setLayout(self.vbox)
		self.show()




