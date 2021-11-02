from PyQt5.QtWidgets import (QMenu, QAction, QGridLayout, QLabel,
	QPushButton, QSpacerItem, QSizePolicy, QComboBox, QLineEdit, QCheckBox)

from libpport import utilities

inputs = [{'Not Used':'Select'},
	{'Homing':['Joint 0 Home', 'Joint 1 Home', 'Joint 2 Home',
		'Joint 3 Home', 'Joint 4 Home', 'Joint 5 Home',
		'Joint 6 Home', 'Joint 7 Home', 'Joint 8 Home', 'Home All']},
	{'Limits':[
		{'Joint 0':['Joint 0 Plus', 'Joint 0 Minus', 'Joint 0 Both']},
		{'Joint 1':['Joint 1 Plus', 'Joint 1 Minus', 'Joint 1 Both']},
		{'Joint 2':['Joint 2 Plus', 'Joint 2 Minus', 'Joint 2 Both']},
		{'Joint 3':['Joint 3 Plus', 'Joint 3 Minus', 'Joint 3 Both']},
		{'Joint 4':['Joint 4 Plus', 'Joint 4 Minus', 'Joint 4 Both']},
		{'Joint 5':['Joint 5 Plus', 'Joint 5 Minus', 'Joint 5 Both']},
		{'Joint 6':['Joint 6 Plus', 'Joint 6 Minus', 'Joint 6 Both']},
		{'Joint 7':['Joint 7 Plus', 'Joint 7 Minus', 'Joint 7 Both']},
		{'Joint 8':['Joint 8 Plus', 'Joint 8 Minus', 'Joint 8 Both']}]},
	{'Jog':[{'X Axis':['Jog X Plus', 'Jog X Minus']},
		{'Y Axis':['Jog Y Plus', 'Jog Y Minus']},
		{'Z Axis':['Jog Z Plus', 'Jog Z Minus']},
		{'A Axis':['Jog A Plus', 'Jog A Minus']},
		{'B Axis':['Jog B Plus', 'Jog B Minus']},
		{'C Axis':['Jog C Plus', 'Jog C Minus']},
		{'U Axis':['Jog U Plus', 'Jog U Minus']},
		{'V Axis':['Jog V Plus', 'Jog V Minus']},
		{'W Axis':['Jog W Plus', 'Jog W Minus']}
	]},
	{'I/O Control':['Flood', 'Mist', 'Lube Level', 'Tool Changed',
		'Tool Prepared', 'External E Stop']},
	{'Motion':['Probe Input', 'Digital 0', 'Digital 1', 'Digital 2', 'Digital 3']}
]

# {'':['', ]},
# '', joint.0.amp-enable-out
outputs = [{'Not Used':'Select'},
	#{'Axes':[
	#	{'X':['X Step', 'X Direction']},
	#	{'Y':['Y Step', 'Y Direction']},
	#	{'Z':['Z Step', 'Z Direction']},
	#	{'A':['A Step', 'A Direction']},
	#	{'B':['B Step', 'B Direction']},
	#	{'C':['C Step', 'C Direction']},
	#	{'U':['U Step', 'U Direction']},
	#	{'V':['V Step', 'V Direction']},
	#]},
	{'Spindle':['Spindle On', 'Spindle CW', 'Spindle CCW', 'Spindle Brake']},
	{'I/O Control':['Drive Enable', 'Coolant Flood', 'Coolant Mist', 'Lube Pump',
		'Tool Change', 'Tool Prepare', 'E Stop Out']},
	{'Digital Out':['Digital Out 0', 'Digital Out 1', 'Digital Out 2', 'Digital Out 3', ]}
]

outJoints = [['Select', False],
						['Joint 0', 0],
						['Joint 1', 1],
						['Joint 2', 2],
						['Joint 3', 3],
						['Joint 4', 4],
						['Joint 5', 5],
						['Joint 6', 6],
						['Joint 7', 7]]

pins = {'in':{'inpins':['0', '1', '2', '3', '4', '5', '6', '7'],
							'outpins':['0', '1', '2', '3', '4', '5', '6', '7']},
				'out':{'inpins':['10', '11', '12', '13', '15'],
							'outpins':['1', '2', '3', '4', '5', '6', '7', '8', '9', '14', '16', '17']}}

#print(pins['out']['inpins'])

def clearLayout(layout):
	for i in reversed(range(layout.count())):
		layoutItem = layout.itemAt(i)
		if layoutItem.widget() is not None:
			widgetToRemove = layoutItem.widget()
			widgetToRemove.setParent(None)
			layout.removeWidget(widgetToRemove)
		elif layoutItem.spacerItem() is not None:
			pass
		else:
			layoutToRemove = layout.itemAt(i)
			clearLayout(layoutToRemove)

def buildPort1(parent):
	outGrid = parent.pp1outGB.findChild(QGridLayout)
	inGrid = parent.pp1inGB.findChild(QGridLayout)
	verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding) 
	clearLayout(outGrid)
	clearLayout(inGrid)
	parent.p1inBtns = {}
	parent.p1inCkBxs = {}
	parent.p1outBtns = {}
	parent.p1outJoints = {}
	parent.p1outCkBxs = {}
	
	inPins = pins['in']['inpins']
	outPins = pins['in']['outpins']

	inGrid.addWidget(QLabel('Input'), 0, 0)
	inGrid.addWidget(QLabel('Function'), 0, 1)
	outGrid.addWidget(QLabel('Pin'), 0, 2)
	outGrid.addWidget(QLabel('state'), 0, 3)
	outGrid.addWidget(QLabel('Invert'), 0, 4)
	for i in range(len(inPins)):
		inGrid.addWidget(QLabel(f'Input {inPins[i]}'), i+1 , 0)
		parent.p1inBtns[f'p1InPB_{i}'] = QPushButton('Select')
		inGrid.addWidget(parent.p1inBtns[f'p1InPB_{i}'],i+1 , 1)
		parent.p1inCkBxs[f'p1InCB_{i}'] = QCheckBox()
		inGrid.addWidget(parent.p1inCkBxs[f'p1InCB_{i}'],i+1 , 2)
	inGrid.addItem(verticalSpacer)

	outGrid.addWidget(QLabel('Output'), 0, 0)
	outGrid.addWidget(QLabel('Function'), 0, 1)
	outGrid.addWidget(QLabel('Pin'), 0, 2)
	outGrid.addWidget(QLabel('state'), 0, 3)
	outGrid.addWidget(QLabel('Invert'), 0, 4)
	for i in range(len(outPins)):
		outGrid.addWidget(QLabel(f'Output {outPins[i]}'), i+1, 0)
		parent.p1outBtns[f'p1OutPB_{i}'] = QPushButton('Select')
		outGrid.addWidget(parent.p1outBtns[f'p1OutPB_{i}'],i+1 , 1)
		parent.p1outJoints[f'p1OutCB_{i}'] = QLineEdit()
		#for item in outJoints:
			#parent.p1outJoints[f'p1OutCB_{i}'].addItem(item[0], item[1])
		outGrid.addWidget(parent.p1outJoints[f'p1OutCB_{i}'],i+1 , 2)
		#parent.p1outJoints[f'p1OutCB_{i}'].setEnabled(False)
		parent.p1outCkBxs[f'p1OutCB_{i}'] = QCheckBox()
		outGrid.addWidget(parent.p1outCkBxs[f'p1OutCB_{i}'],i+1 , 3)
	outGrid.addItem(verticalSpacer)
	for i in range(len(outPins)):
		button = parent.p1outBtns.get(f'p1OutPB_{i}')
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		menu.triggered.connect(lambda: utilities.setAxisTabs(parent))
		#menu.triggered.connect(lambda action: utilities.test(parent, action))
		add_menu(outputs, menu)
		button.setMenu(menu)
	
	for i in range(len(inPins)):
		button = parent.p1inBtns.get(f'p1InPB_{i}')
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(inputs, menu)
		button.setMenu(menu)
	
	
def buildPort2(parent):
	outGrid = parent.pp2outGB.findChild(QGridLayout)
	inGrid = parent.pp2inGB.findChild(QGridLayout)
	verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding) 
	clearLayout(outGrid)
	clearLayout(inGrid)

	parent.p2inBtns = {}
	parent.p2inCkBxs = {}
	parent.p2outBtns = {}
	parent.p2outJoints = {}
	parent.p2outCkBxs = {}

	if parent.pp2typeCB.currentData(): # port type is in or out
		inPins = pins[parent.pp2typeCB.currentData()]['inpins']
		outPins = pins[parent.pp2typeCB.currentData()]['outpins']

		inGrid.addWidget(QLabel('Port'), 0, 0)
		inGrid.addWidget(QLabel('Function'), 0, 1)
		inGrid.addWidget(QLabel('Invert'), 0, 2)
		for i in range(len(inPins)):
			inGrid.addWidget(QLabel(f'Pin {inPins[i]}'), i+1 , 0)
			parent.p2inBtns[f'p2InPB_{i}'] = QPushButton('Select')
			inGrid.addWidget(parent.p2inBtns[f'p2InPB_{i}'],i+1 , 1)
			parent.p2inCkBxs[f'p2InCB_{i}'] = QCheckBox()
			inGrid.addWidget(parent.p2inCkBxs[f'p2InCB_{i}'],i+1 , 2)
		inGrid.addItem(verticalSpacer)

		outGrid.addWidget(QLabel('Port'), 0, 0)
		outGrid.addWidget(QLabel('Function'), 0, 1)
		outGrid.addWidget(QLabel('Joint'), 0, 2)
		outGrid.addWidget(QLabel('Invert'), 0, 3)
		for i in range(len(outPins)):
			outGrid.addWidget(QLabel(f'Pin {outPins[i]}'), i+1 , 0)
			parent.p2outBtns[f'p2OutPB_{i}'] = QPushButton('Select')
			outGrid.addWidget(parent.p2outBtns[f'p2OutPB_{i}'],i+1 , 1)
			parent.p2outJoints[f'p2OutCB_{i}'] = QComboBox()
			for item in outJoints:
				parent.p2outJoints[f'p2OutCB_{i}'].addItem(item[0], item[1])
			outGrid.addWidget(parent.p2outJoints[f'p2OutCB_{i}'],i+1 , 2)
			parent.p2outJoints[f'p2OutCB_{i}'].setEnabled(False)
			parent.p2outCkBxs[f'p2OutCB_{i}'] = QCheckBox()
			outGrid.addWidget(parent.p2outCkBxs[f'p2OutCB_{i}'],i+1 , 3)
		outGrid.addItem(verticalSpacer)

	# add the menu to buttons
	if parent.pp2typeCB.currentData():
		for i in range(len(outPins)):
			button = parent.p2outBtns.get(f'p2OutPB_{i}')
			menu = QMenu()
			menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
			menu.triggered.connect(lambda: utilities.setAxisTabs(parent))
			add_menu(outputs, menu)
			button.setMenu(menu)

		for i in range(len(inPins)):
			button = parent.p2inBtns.get(f'p2InPB_{i}')
			menu = QMenu()
			menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
			add_menu(inputs, menu)
			button.setMenu(menu)

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
