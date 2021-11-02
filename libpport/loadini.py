import os, configparser

from PyQt5.QtWidgets import (QFileDialog, QLabel, QLineEdit, QSpinBox,
	QDoubleSpinBox, QCheckBox, QGroupBox, QComboBox, QPushButton)

from libpport import utilities

config = configparser.ConfigParser(strict=False)
config.optionxform = str

def openini(parent, fileName = ''):
	parent.tabWidget.setCurrentIndex(0)
	parent.machinePTE.clear()
	if not fileName:
		if os.path.isdir(os.path.expanduser('~/linuxcnc/configs')):
			configsDir = os.path.expanduser('~/linuxcnc/configs')
		else:
			configsDir = os.path.expanduser('~/')
		fileName = QFileDialog.getOpenFileName(parent,
		caption="Select Configuration INI File", directory=configsDir,
		filter='*.ini', options=QFileDialog.DontUseNativeDialog,)
		if fileName:
			parent.machinePTE.appendPlainText(f'Loading {fileName[0]}')
			iniFile = (fileName[0])
		else:
			parent.machinePTE.appendPlainText('Open File Cancled')
			iniFile = ''
	else: # we passed a file name and path for testing
		#print(fileName)
		iniFile = (fileName)

	if config.read(iniFile):
		if config.has_option('PARAPORT', 'VERSION'):
			iniVersion = config['PARAPORT']['VERSION']
			if iniVersion == parent.version:
				loadini(parent)
			else:
				msg = (f'The ini file version is {iniVersion}\n'
					f'The Configuration Tool version is {parent.version}\n'
					'Try and open the ini?')
				if parent.errorMsg(msg, 'Version Difference'):
					loadini(parent)
		else:
			msg = ('This ini file may have been built with an older version\n'
				'Try and open?')
			if parent.errorMsg(msg, 'No Version'):
				loadini(parent)

def loadini(parent):
	# Section, Item, Object Name
	iniError = False
	iniList = []
	iniList.append(['EMC', 'MACHINE', 'configName'])
	iniList.append(['EMC', 'DEBUG', 'debugCB'])

	iniList.append(['DISPLAY', 'DISPLAY', 'guiCB'])
	iniList.append(['DISPLAY', 'EDITOR', 'editorCB'])
	iniList.append(['DISPLAY', 'POSITION_OFFSET', 'positionOffsetCB'])
	iniList.append(['DISPLAY', 'POSITION_FEEDBACK', 'positionFeedbackCB'])
	iniList.append(['DISPLAY', 'MAX_FEED_OVERRIDE', 'maxFeedOverrideSB'])
	iniList.append(['DISPLAY', 'INTRO_GRAPHIC', 'introGraphicLE'])
	iniList.append(['DISPLAY', 'INTRO_GRAPHIC_TIME', 'introGraphicSB'])
	iniList.append(['DISPLAY', 'DEFAULT_LINEAR_VELOCITY', 'defaultJogSpeedDSB'])

	iniList.append(['EMCMOT', 'SERVO_PERIOD', 'servoPeriodSB'])
	iniList.append(['EMCMOT', 'BASE_PERIOD', 'basePeriodSB'])

	iniList.append(['TRAJ', 'LINEAR_UNITS', 'linearUnitsCB'])
	iniList.append(['TRAJ', 'COORDINATES', 'coordinatesLB'])
	iniList.append(['TRAJ', 'MAX_LINEAR_VELOCITY', 'maxLinearVel'])

	axes = {1:'X', 2:'Y', 3:'Z', 4:'A', 5:'B', 6:'C', 7:'U', 8:'V', 9:'W'}
	for i in range(1, 9):
		if config.has_section(f'AXIS_{axes[i]}'):
			iniList.append([f'AXIS_{axes[i]}', 'MIN_LIMIT', f'minLimit_{i}'])
			iniList.append([f'AXIS_{axes[i]}', 'MAX_LIMIT', f'maxLimit_{i}'])
			iniList.append([f'AXIS_{axes[i]}', 'MAX_VELOCITY', f'maxVelocity_{i}'])
			iniList.append([f'AXIS_{axes[i]}', 'MAX_ACCELERATION', f'maxAccel_{i}'])
			iniList.append([f'JOINT_{i-1}', 'SCALE', f'scale_{i}'])
			iniList.append([f'JOINT_{i-1}', 'HOME', f'home_{i}'])
			iniList.append([f'JOINT_{i-1}', 'HOME_OFFSET', f'homeOffset_{i}'])
			iniList.append([f'JOINT_{i-1}', 'HOME_SEARCH_VEL', f'homeSearchVel_{i}'])
			iniList.append([f'JOINT_{i-1}', 'HOME_LATCH_VEL', f'homeLatchVel_{i}'])
			iniList.append([f'JOINT_{i-1}', 'HOME_USE_INDEX', f'homeUseIndex_{i}'])
			iniList.append([f'JOINT_{i-1}', 'HOME_IGNORE_LIMITS', f'homeIgnoreLimits_{i}'])
			iniList.append([f'JOINT_{i-1}', 'HOME_SEQUENCE', f'homeSequence_{i}'])


			'''
			iniList.append([f'AXIS_{axes[i]}', 'MIN_LIMIT = ' + config[f'AXIS_{axes[i]}']['MIN_LIMIT'], f'minLimit_{i}'])
			iniList.append('MAX_LIMIT = ' + config[f'AXIS_{axes[i]}']['MAX_LIMIT'])
			iniList.append('MAX_VELOCITY = ' + config[f'AXIS_{axes[i]}']['MAX_VELOCITY'])
			iniList.append('MAX_ACCELERATION = ' + config[f'AXIS_{axes[i]}']['MAX_ACCELERATION'])
			'''

	'''

	for i in range(parent.card['joints']):
		iniList.append([f'JOINT_{i}', 'AXIS', f'axisCB_{i}'])
		iniList.append([f'JOINT_{i}', 'STEPLEN', f'stepTime_{i}'])
		iniList.append([f'JOINT_{i}', 'STEPSPACE', f'stepSpace_{i}'])
		iniList.append([f'JOINT_{i}', 'DIRSETUP', f'dirSetup_{i}'])
		iniList.append([f'JOINT_{i}', 'DIRHOLD', f'dirHold_{i}'])

		iniList.append([f'JOINT_{i}', 'P', f'p_{i}'])
		iniList.append([f'JOINT_{i}', 'I', f'i_{i}'])
		iniList.append([f'JOINT_{i}', 'D', f'd_{i}'])
		iniList.append([f'JOINT_{i}', 'FF0', f'ff0_{i}'])
		iniList.append([f'JOINT_{i}', 'FF1', f'ff1_{i}'])
		iniList.append([f'JOINT_{i}', 'FF2', f'ff2_{i}'])
		iniList.append([f'JOINT_{i}', 'DEADBAND', f'deadband_{i}'])
		iniList.append([f'JOINT_{i}', 'BIAS', f'bias_{i}'])
		iniList.append([f'JOINT_{i}', 'MAX_OUTPUT', f'maxOutput_{i}'])
		iniList.append([f'JOINT_{i}', 'MAX_ERROR', f'maxError_{i}'])

	iniList.append(['SPINDLE', 'SPINDLE_TYPE', 'spindleTypeCB'])
	iniList.append(['SPINDLE', 'SCALE', 'spindleScale'])
	iniList.append(['SPINDLE', 'PWM_FREQUENCY', 'pwmFrequencySB'])
	iniList.append(['SPINDLE', 'MAX_RPM', 'spindleMaxRpm'])
	iniList.append(['SPINDLE', 'MIN_RPM', 'spindleMinRpm'])
	iniList.append(['SPINDLE', 'DEADBAND', 'deadband_s'])
	iniList.append(['SPINDLE', 'P', 'p_s'])
	iniList.append(['SPINDLE', 'I', 'i_s'])
	iniList.append(['SPINDLE', 'D', 'd_s'])
	iniList.append(['SPINDLE', 'FF0', 'ff0_s'])
	iniList.append(['SPINDLE', 'FF1', 'ff1_s'])
	iniList.append(['SPINDLE', 'FF2', 'ff2_s'])
	iniList.append(['SPINDLE', 'BIAS', 'bias_s'])
	iniList.append(['SPINDLE', 'MAX_ERROR', 'maxError_s'])

	for i in range(parent.card['inputs']):
		iniList.append(['INPUT_PB', f'INPUT_PB_{i}', f'inputPB_{i}'])
		iniList.append(['INPUT_PB', f'INPUT_INVERT_{i}', f'inputInvertCB_{i}'])

	for i in range(parent.card['outputs']):
		iniList.append(['OUTPUT_PB', f'OUTPUT_PB_{i}', f'outputPB_{i}'])
	'''

	iniList.append(['DRIVER', 'DRIVER', 'driveCB'])


	if config.has_option('PARAPORT_1','PARAPORT_1_TYPE'):
		iniList.append(['PARAPORT_1', 'PARAPORT_1_TYPE', 'pp1typeCB'])
	if config.has_option('PARAPORT_2','PARAPORT_2_TYPE'):
		iniList.append(['PARAPORT_2', 'PARAPORT_2_TYPE', 'pp2typeCB'])

	#iniList.append(['OPTIONS', 'PARAPORT_2_TYPE', 'pp2typeCB'])
	iniList.append(['OPTIONS', 'MANUAL_TOOL_CHANGE', 'manualToolChangeCB'])
	iniList.append(['OPTIONS', 'CUSTOM_HAL', 'customhalCB'])
	iniList.append(['OPTIONS', 'POST_GUI_HAL', 'postguiCB'])
	iniList.append(['OPTIONS', 'SHUTDOWN_HAL', 'shutdownCB'])
	iniList.append(['OPTIONS', 'HALUI', 'haluiCB'])
	iniList.append(['OPTIONS', 'PYVCP', 'pyvcpCB'])
	iniList.append(['OPTIONS', 'LADDER', 'ladderGB'])
	iniList.append(['OPTIONS', 'LADDER_RUNGS', 'ladderRungsSB'])
	iniList.append(['OPTIONS', 'BACKUP', 'backupCB'])

#iniList.append(['', '', ''])
	# iniList section, item, value
	for item in iniList:
		if config.has_option(item[0], item[1]):
			if isinstance(getattr(parent, item[2]), QLabel):
				getattr(parent, item[2]).setText(config[item[0]][item[1]])
			elif isinstance(getattr(parent, item[2]), QLineEdit):
				getattr(parent, item[2]).setText(config[item[0]][item[1]])
			elif isinstance(getattr(parent, item[2]), QSpinBox):
				getattr(parent, item[2]).setValue(abs(int(config[item[0]][item[1]])))
			elif isinstance(getattr(parent, item[2]), QDoubleSpinBox):
				getattr(parent, item[2]).setValue(float(config[item[0]][item[1]]))
			elif isinstance(getattr(parent, item[2]), QCheckBox):
				getattr(parent, item[2]).setChecked(eval(config[item[0]][item[1]]))
			elif isinstance(getattr(parent, item[2]), QGroupBox):
				getattr(parent, item[2]).setChecked(eval(config[item[0]][item[1]]))
			elif isinstance(getattr(parent, item[2]), QComboBox):
				index = getattr(parent, item[2]).findData(config[item[0]][item[1]])
				if index >= 0:
					getattr(parent, item[2]).setCurrentIndex(index)
				else: # if it can't find a data match check for a text match
					index = getattr(parent, item[2]).findText(config[item[0]][item[1]])
					if index >= 0:
						getattr(parent, item[2]).setCurrentIndex(index)
			elif isinstance(getattr(parent, item[2]), QPushButton):
				getattr(parent, item[2]).setText(config[item[0]][item[1]])
			else:
				print(item[2])

	# handle special cases iniList.append(['DISPLAY', 'OPEN_FILE', 'startUpFileLE'])

	if config.has_option('DISPLAY', 'OPEN_FILE'):
		if config['DISPLAY']['OPEN_FILE'] != '""':
			parent.startUpFileLE.setText(config['DISPLAY']['OPEN_FILE'])

	if config.has_option('PARAPORT_1', 'PARAPORT_1_TYPE'):
		if config.has_option('PARAPORT_1', 'PORT_1_IN_0'):
			for i in range(len(parent.p1inBtns)):
				button = parent.p1inBtns.get(f'p1InPB_{i}')
				button.setText(config['PARAPORT_1'][f'PORT_1_IN_{i}'])
		else:
			iniError = True
		if config.has_option('PARAPORT_1', 'PORT_1_IN_CB_0'):
			for i in range(len(parent.p1inCkBxs)):
				cb = parent.p1inCkBxs.get(f'p1InCB_{i}')
				cb.setChecked(config['PARAPORT_1'].getboolean(f'PORT_1_IN_CB_{i}'))
		else:
			iniError = True
		if config.has_option('PARAPORT_1', 'PORT_1_OUT_0'):
			for i in range(len(parent.p1outBtns)):
				button = parent.p1outBtns.get(f'p1OutPB_{i}')
				button.setText(config['PARAPORT_1'][f'PORT_1_OUT_{i}'])
		else:
			iniError = True
		if config.has_option('PARAPORT_1', 'PORT_1_OUT_CB_0'):
				for i in range(len(parent.p1outCkBxs)):
					cb = parent.p1outCkBxs.get(f'p1OutCB_{i}')
					cb.setChecked(config['PARAPORT_1'].getboolean(f'PORT_1_OUT_CB_{i}'))
		else:
			iniError = True

	if config.has_option('PARAPORT_2', 'PARAPORT_2_TYPE'):
		for i in range(len(parent.p2inBtns)):
			button = parent.p2inBtns.get(f'p2InPB_{i}')
			button.setText(config['PARAPORT_2'][f'PORT_2_IN_{i}'])
		for i in range(len(parent.p2inCkBxs)):
			cb = parent.p2inCkBxs.get(f'p2InCB_{i}')
			cb.setChecked(config['PARAPORT_2'].getboolean(f'PORT_2_IN_CB_{i}'))

		for i in range(len(parent.p2outBtns)):
			button = parent.p2outBtns.get(f'p2OutPB_{i}')
			button.setText(config['PARAPORT_2'][f'PORT_2_OUT_{i}'])
		for i in range(len(parent.p2outCkBxs)):
			cb = parent.p2outCkBxs.get(f'p2OutCB_{i}')
			cb.setChecked(config['PARAPORT_2'].getboolean(f'PORT_2_OUT_CB_{i}'))

	# PORT_1_IN_0 = Select
	#print(config['PARAPORT_1', f'PORT_1_IN_{i}'])
	#button.setText()
	#print(button.text())
		#for i in range(12):
		#	button = parent.p1outBtns.get(f'p1OutPB_{i}')
		#	print(button)

		#if config['PARAPORT_1']['PARAPORT_1_TYPE'] == 'OUT':
		#	for i in range(12):
		#		iniList.append(['PARAPORT_1', f'PORT_1_IN_{i}', f'p1InPB_{i}'])
		#	for i in range(5):
		#		iniList.append(['PARAPORT_1', f'PORT_1_OUT_{i}', f'p1OutPB_{i}'])

	if not iniError:
		parent.machinePTE.appendPlainText('INI file Loaded')
	else:
		parent.machinePTE.appendPlainText('Some items were missing in the ini file.')
	utilities.setAxisTabs(parent)
