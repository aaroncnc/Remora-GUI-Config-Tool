from PyQt5 import QtWidgets, uic
from functools import partial
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QApplication, QMainWindow, QMessageBox, QMenu, QAction, QGridLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QComboBox, QLineEdit, QCheckBox, QButtonGroup


import sys, os
from libpport import buildini
from libpport import buildhal
from libpport import buildconfig
from libpport import buildsave
from libpport import buildcombos
from libpport import utilities
from libpport import checkconfig

outputs = [{'Not Used':'Select'},
	{'Spindle':['Spindle On', 'Spindle CW', 'Spindle CCW', 'Spindle Brake']},
	{'I/O Control':['Coolant Flood', 'Coolant Mist', 'Lube Pump',
		'Tool Change', 'Tool Prepare', 'E Stop Out']},
	{'Digital Out':['Digital Out 0', 'Digital Out 1', 'Digital Out 2', 'Digital Out 3', ]}
]

inputs = [{'Not Used':'Select'},
	{'Home':[
		'Home All', 'Joint 0 Home', 'Joint 1 Home', 'Joint 2 Home',
		'Joint 3 Home', 'Joint 4 Home', 'Joint 5 Home',
		'Joint 6 Home', 'Joint 7 Home']},
	{'Limits':[
		{'Joint all':['All Max', 'All Min', 'All Both']},
		{'Joint 0':['Joint 0 max', 'Joint 0 min', 'Joint 0 Both']},
		{'Joint 1':['Joint 1 max', 'Joint 1 min', 'Joint 1 Both']},
		{'Joint 2':['Joint 2 max', 'Joint 2 min', 'Joint 2 Both']},
		{'Joint 3':['Joint 3 max', 'Joint 3 min', 'Joint 3 Both']},
		{'Joint 4':['Joint 4 max', 'Joint 4 min', 'Joint 4 Both']},
		{'Joint 5':['Joint 5 max', 'Joint 5 min', 'Joint 5 Both']},
		{'Joint 6':['Joint 6 max', 'Joint 6 min', 'Joint 6 Both']},
		{'Joint 7':['Joint 7 max', 'Joint 7 min', 'Joint 7 Both']}]},
	{'Home + Limits':[
		{'Home all + Joint all':['Home + Limit All Max', 'Home + Limit All Min', 'Home + Limit All Both']},
		{'Home + Limit Joint 0':['Home + Limit Joint 0 max', 'Home + Limit Joint 0 min', 'Home + Limit Joint 0 Both']},
		{'Home + Limit Joint 1':['Home + Limit Joint 1 max', 'Home + Limit Joint 1 min', 'Home + Limit Joint 1 Both']},
		{'Home + Limit Joint 2':['Home + Limit Joint 2 max', 'Home + Limit Joint 2 min', 'Home + Limit Joint 2 Both']},
		{'Home + Limit Joint 3':['Home + Limit Joint 3 max', 'Home + Limit Joint 3 min', 'Home + Limit Joint 3 Both']},
		{'Home + Limit Joint 4':['Home + Limit Joint 4 max', 'Home + Limit Joint 4 min', 'Home + Limit Joint 4 Both']},
		{'Home + Limit Joint 5':['Home + Limit Joint 5 max', 'Home + Limit Joint 5 min', 'Home + Limit Joint 5 Both']},
		{'Home + Limit Joint 6':['Home + Limit Joint 6 max', 'Home + Limit Joint 6 min', 'Home + Limit Joint 6 Both']},
		{'Home + Limit Joint 7':['Home + Limit Joint 7 max', 'Home + Limit Joint 7 min', 'Home + Limit Joint 7 Both']}]},
		
	{'Jog':[
		{'Joint 0':['Joint 0 Plus', 'Joint 0 Minus']},
		{'Joint 1':['Joint 1 Plus', 'Joint 1 Minus']},
		{'Joint 2':['Joint 2 Plus', 'Joint 2 Minus']},
		{'Joint 3':['Joint 3 Plus', 'Joint 3 Minus']},
		{'Joint 4':['Joint 4 Plus', 'Joint 4 Minus']},
		{'Joint 5':['Joint 5 Plus', 'Joint 5 Minus']},
		{'Joint 6':['Joint 6 Plus', 'Joint 6 Minus']},
		{'Joint 7':['Joint 7 Plus', 'Joint 7 Minus']}
	]},
	{'I/O Control':['Flood', 'Mist', 'Tool Changed',
		'Tool Prepared', 'External E Stop']},
	{'Motion':['Probe Input', 'Digital 0', 'Digital 1', 'Digital 2', 'Digital 3']}
]
def add_menu(data, menu_obj):
	if isinstance(data, dict):
		for k, v in data.items():
			sub_menu = QMenu(k, menu_obj)
			menu_obj.addMenu(sub_menu)
			add_menu(v, sub_menu)
	elif isinstance(data, list):
		for element in data:
			add_menu(element, menu_obj)
	else:
		action = menu_obj.addAction(data)
		action.setIconVisibleInMenu(False)

class Ui(QtWidgets.QMainWindow):
	def __init__(self):
		super(Ui, self).__init__()
		uic.loadUi('remoreconfig.ui', self)
		self.lib_path = os.path.split(os.path.realpath(sys.argv[0]))[0]
#Lists
		
		self.axislist = ['xaxis', 'yaxis', 'zaxis', 'e0axis', 'e1axis', 'e2axis', 'e3axis', 'e4axis']
		self.outbtnlist = ['outbtn0', 'outbtn1', 'outbtn2', 'outbtn3', 'outbtn4', 'outbtn5', 'outbtn6', 'outbtn7']
		self.inbtnlist = ['inbtn0', 'inbtn1', 'inbtn2', 'inbtn3', 'inbtn4', 'inbtn5', 'inbtn6', 'inbtn7']
		self.outlist = ['out0', 'out1', 'out2', 'out3', 'out4', 'out5', 'out6', 'out7']
		self.inlist = ['in0', 'in1', 'in2', 'in3', 'in4', 'in5', 'in6', 'in7']
		self.pwmlist = ['pwm0', 'pwm1', 'pwm2', 'pwm3', 'pwm4', 'pwm5', 'pwm6']
		self.enclist = ['enc0', 'enc1', 'enc2', 'enc3']
		self.templist = ['temp0', 'temp1', 'temp2', 'temp3']
		self.swlist = ['sw0', 'sw1', 'sw2']

		self.show()


	#Setup actions
		
		self.buildini.clicked.connect(partial(buildini.build, self))
		self.buildhal.clicked.connect(partial(buildhal.build, self))
		self.buildconfig.clicked.connect(partial(buildconfig.build, self))
		self.save.clicked.connect(partial(buildsave.build, self))
		self.load.clicked.connect(partial(buildsave.load, self))
		self.boards.currentIndexChanged.connect(self.loadboards)
		self.xaxistmc.currentIndexChanged.connect(self.xtmc) 
		self.yaxistmc.currentIndexChanged.connect(self.ytmc) 
		self.zaxistmc.currentIndexChanged.connect(self.ztmc) 
		self.e0axistmc.currentIndexChanged.connect(self.e0tmc)
		self.e1axistmc.currentIndexChanged.connect(self.e1tmc)
		self.e2axistmc.currentIndexChanged.connect(self.e2tmc)
		self.e3axistmc.currentIndexChanged.connect(self.e3tmc)
		self.e4axistmc.currentIndexChanged.connect(self.e4tmc)
		

		self.buttonGroup.buttonClicked.connect(self.axisUpdate)
		
		
		#self.actionOpenConfig.triggered.connect(partial(loadini.openini, self))
		
		#self.actionCheckConfiguration.triggered.connect(partial(checkconfig.checkit, self))
		self.actionCheckConfiguration.clicked.connect(partial(checkconfig.checkit, self))
		
		#self.actionBuildConfiguration.triggered.connect(partial(buildfiles.build, self))
		#self.actionTabHelp.triggered.connect(self.help)
		#self.actionBuildHelp.triggered.connect(partial(self.help, 20))
		#self.actionPCHelp.triggered.connect(partial(self.help, 30))
		self.configName.textChanged[str].connect(partial(utilities.configNameChanged, self))
		#self.driveCB.currentIndexChanged.connect(partial(utilities.driveChanged, self))
		#self.pp1typeCB.currentIndexChanged.connect(partial(buildmenus.buildPort1, self))
		#self.pp2typeCB.currentIndexChanged.connect(partial(buildmenus.buildPort2, self))
		#self.resetTimingPB.clicked.connect(partial(utilities.setTiming, self))
		#self.startUpFilePB.clicked.connect(partial(utilities.fileDialog, self, 'startUpFileLE'))
		#self.portInfoPB.clicked.connect(partial(utilities.getPortInfo, self))
		
	#run actions	
		buildcombos.build(self)

		
	#add menu options to outputs and inputs	
		for i in range(8):
			button =  getattr(self, f'{self.outlist[i]}'"txt")
			menu = QMenu()
			menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
			add_menu(outputs, menu)
			button.setMenu(menu)
		for i in range(8):
			button =  getattr(self, f'{self.inlist[i]}'"txt")
			menu = QMenu()
			menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
			add_menu(inputs, menu)
			button.setMenu(menu)
		
	#hide elements not needed on startup
		for z in range(8):
			getattr(self, f'{self.axislist[z]}'"cur").setEnabled(0)
			getattr(self, f'{self.axislist[z]}'"cur").setVisible(0)
			getattr(self, f'{self.axislist[z]}'"cursense").setEnabled(0)
			getattr(self, f'{self.axislist[z]}'"cursense").setVisible(0)
			getattr(self, f'{self.axislist[z]}'"microstep").setEnabled(0)
			getattr(self, f'{self.axislist[z]}'"microstep").setVisible(0)
			getattr(self, f'{self.axislist[z]}'"stealthcop").setEnabled(0)
			getattr(self, f'{self.axislist[z]}'"stealthcop").setVisible(0)
			getattr(self, f'{self.axislist[z]}'"rxpin").setEnabled(0)
			getattr(self, f'{self.axislist[z]}'"rxpin").setVisible(0)
			
	def axisUpdate(self):
		axislist2 = ['X', 'Y', 'Z', 'A', 'B', 'C', 'U', 'V']
		temp = ""
		for i in range(8):
				if getattr(self, f'{self.axislist[i]}').isChecked() == 1:
					temp = temp + f'{axislist2[i]}'
					self.coordinatesLB.setText(temp)
		


#load boards from combo box		   
	def loadboards(self):
		if self.boards.currentText() == "MKS SBASE v1.3 LPC1768": self.xaxiscur.setEnabled(1),self.xaxiscur.setVisible(1),self.yaxiscur.setEnabled(1),self.yaxiscur.setVisible(1),self.zaxiscur.setEnabled(1),self.zaxiscur.setVisible(1),self.e0axiscur.setEnabled(1),self.e0axiscur.setVisible(1),self.e1axiscur.setEnabled(1),self.e1axiscur.setVisible(1),self.e2axiscur.setEnabled(1),self.e2axiscur.setVisible(1),self.e3axiscur.setEnabled(1),self.e3axiscur.setVisible(1),self.e4axiscur.setEnabled(1),self.e4axiscur.setVisible(1)
		else:self.xaxiscur.setEnabled(0),self.xaxiscur.setVisible(0),self.yaxiscur.setEnabled(0),self.yaxiscur.setVisible(0),self.zaxiscur.setEnabled(0),self.zaxiscur.setVisible(0),self.e0axiscur.setEnabled(0),self.e0axiscur.setVisible(0),self.e1axiscur.setEnabled(0),self.e1axiscur.setVisible(0)
 
#hide and show X axis tmc options 
	def xtmc(self):	 
		if self.xaxistmc.currentText() == "None": self.xaxiscur.setEnabled(0), self.xaxiscur.setVisible(0), self.xaxiscursense.setEnabled(0), self.xaxiscursense.setVisible(0), self.xaxismicrostep.setEnabled(0), self.xaxismicrostep.setVisible(0), self.xaxisstealthcop.setEnabled(0), self.xaxisstealthcop.setVisible(0), self.xaxisrxpin.setEnabled(0), self.xaxisrxpin.setVisible(0)
		else: self.xaxiscur.setEnabled(1), self.xaxiscur.setVisible(1), self.xaxiscursense.setEnabled(1), self.xaxiscursense.setVisible(1), self.xaxismicrostep.setEnabled(1), self.xaxismicrostep.setVisible(1), self.xaxisstealthcop.setEnabled(1), self.xaxisstealthcop.setVisible(1), self.xaxisrxpin.setEnabled(1), self.xaxisrxpin.setVisible(1)
			
#hide and show Y axis tmc options			 
	def ytmc(self):
		if self.yaxistmc.currentText() == "None": self.yaxiscur.setEnabled(0), self.yaxiscur.setVisible(0), self.yaxiscursense.setEnabled(0), self.yaxiscursense.setVisible(0), self.yaxismicrostep.setEnabled(0), self.yaxismicrostep.setVisible(0), self.yaxisstealthcop.setEnabled(0), self.yaxisstealthcop.setVisible(0), self.yaxisrxpin.setEnabled(0), self.yaxisrxpin.setVisible(0)
		else: self.yaxiscur.setEnabled(1), self.yaxiscur.setVisible(1), self.yaxiscursense.setEnabled(1), self.yaxiscursense.setVisible(1), self.yaxismicrostep.setEnabled(1), self.yaxismicrostep.setVisible(1), self.yaxisstealthcop.setEnabled(1), self.yaxisstealthcop.setVisible(1), self.yaxisrxpin.setEnabled(1), self.yaxisrxpin.setVisible(1) 

#hide and show Z axis tmc options			 
	def ztmc(self):
		if self.zaxistmc.currentText() == "None": self.zaxiscur.setEnabled(0), self.zaxiscur.setVisible(0), self.zaxiscursense.setEnabled(0), self.zaxiscursense.setVisible(0), self.zaxismicrostep.setEnabled(0), self.zaxismicrostep.setVisible(0), self.zaxisstealthcop.setEnabled(0), self.zaxisstealthcop.setVisible(0), self.zaxisrxpin.setEnabled(0), self.zaxisrxpin.setVisible(0)
		else: self.zaxiscur.setEnabled(1), self.zaxiscur.setVisible(1), self.zaxiscursense.setEnabled(1), self.zaxiscursense.setVisible(1), self.zaxismicrostep.setEnabled(1), self.zaxismicrostep.setVisible(1), self.zaxisstealthcop.setEnabled(1), self.zaxisstealthcop.setVisible(1), self.zaxisrxpin.setEnabled(1), self.zaxisrxpin.setVisible(1) 

#hide and show E0 axis tmc options			  
	def e0tmc(self):
		if self.e0axistmc.currentText() == "None": self.e0axiscur.setEnabled(0), self.e0axiscur.setVisible(0), self.e0axiscursense.setEnabled(0), self.e0axiscursense.setVisible(0), self.e0axismicrostep.setEnabled(0), self.e0axismicrostep.setVisible(0), self.e0axisstealthcop.setEnabled(0), self.e0axisstealthcop.setVisible(0), self.e0axisrxpin.setEnabled(0), self.e0axisrxpin.setVisible(0)
		else: self.e0axiscur.setEnabled(1), self.e0axiscur.setVisible(1), self.e0axiscursense.setEnabled(1), self.e0axiscursense.setVisible(1), self.e0axismicrostep.setEnabled(1), self.e0axismicrostep.setVisible(1), self.e0axisstealthcop.setEnabled(1), self.e0axisstealthcop.setVisible(1), self.e0axisrxpin.setEnabled(1), self.e0axisrxpin.setVisible(1) 

#hide and show E1 axis tmc options			  
	def e1tmc(self):
		if self.e1axistmc.currentText() == "None": self.e1axiscur.setEnabled(0), self.e1axiscur.setVisible(0), self.e1axiscursense.setEnabled(0), self.e1axiscursense.setVisible(0), self.e1axismicrostep.setEnabled(0), self.e1axismicrostep.setVisible(0), self.e1axisstealthcop.setEnabled(0), self.e1axisstealthcop.setVisible(0), self.e1axisrxpin.setEnabled(0), self.e1axisrxpin.setVisible(0)
		else: self.e1axiscur.setEnabled(1), self.e1axiscur.setVisible(1), self.e1axiscursense.setEnabled(1), self.e1axiscursense.setVisible(1), self.e1axismicrostep.setEnabled(1), self.e1axismicrostep.setVisible(1), self.e1axisstealthcop.setEnabled(1), self.e1axisstealthcop.setVisible(1), self.e1axisrxpin.setEnabled(1), self.e1axisrxpin.setVisible(1)			
#hide and show e2 axis tmc options			  
	def e2tmc(self):
		if self.e2axistmc.currentText() == "None": self.e2axiscur.setEnabled(0), self.e2axiscur.setVisible(0), self.e2axiscursense.setEnabled(0), self.e2axiscursense.setVisible(0), self.e2axismicrostep.setEnabled(0), self.e2axismicrostep.setVisible(0), self.e2axisstealthcop.setEnabled(0), self.e2axisstealthcop.setVisible(0), self.e2axisrxpin.setEnabled(0), self.e2axisrxpin.setVisible(0)
		else: self.e2axiscur.setEnabled(1), self.e2axiscur.setVisible(1), self.e2axiscursense.setEnabled(1), self.e2axiscursense.setVisible(1), self.e2axismicrostep.setEnabled(1), self.e2axismicrostep.setVisible(1), self.e2axisstealthcop.setEnabled(1), self.e2axisstealthcop.setVisible(1), self.e2axisrxpin.setEnabled(1), self.e2axisrxpin.setVisible(1)			
#hide and show e3 axis tmc options			  
	def e3tmc(self):
		if self.e3axistmc.currentText() == "None": self.e3axiscur.setEnabled(0), self.e3axiscur.setVisible(0), self.e3axiscursense.setEnabled(0), self.e3axiscursense.setVisible(0), self.e3axismicrostep.setEnabled(0), self.e3axismicrostep.setVisible(0), self.e3axisstealthcop.setEnabled(0), self.e3axisstealthcop.setVisible(0), self.e3axisrxpin.setEnabled(0), self.e3axisrxpin.setVisible(0)
		else: self.e3axiscur.setEnabled(1), self.e3axiscur.setVisible(1), self.e3axiscursense.setEnabled(1), self.e3axiscursense.setVisible(1), self.e3axismicrostep.setEnabled(1), self.e3axismicrostep.setVisible(1), self.e3axisstealthcop.setEnabled(1), self.e3axisstealthcop.setVisible(1), self.e3axisrxpin.setEnabled(1), self.e3axisrxpin.setVisible(1)			
#hide and show e4 axis tmc options			  
	def e4tmc(self):
		if self.e4axistmc.currentText() == "None": self.e4axiscur.setEnabled(0), self.e4axiscur.setVisible(0), self.e4axiscursense.setEnabled(0), self.e4axiscursense.setVisible(0), self.e4axismicrostep.setEnabled(0), self.e4axismicrostep.setVisible(0), self.e4axisstealthcop.setEnabled(0), self.e4axisstealthcop.setVisible(0), self.e4axisrxpin.setEnabled(0), self.e4axisrxpin.setVisible(0)
		else: self.e4axiscur.setEnabled(1), self.e4axiscur.setVisible(1), self.e4axiscursense.setEnabled(1), self.e4axiscursense.setVisible(1), self.e4axismicrostep.setEnabled(1), self.e4axismicrostep.setVisible(1), self.e4axisstealthcop.setEnabled(1), self.e4axisstealthcop.setVisible(1), self.e4axisrxpin.setEnabled(1), self.e4axisrxpin.setVisible(1)			
	
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()