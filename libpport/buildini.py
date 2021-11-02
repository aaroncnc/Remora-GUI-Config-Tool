import os, traceback, sys
from PyQt5 import QtWidgets, uic
from functools import partial
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QApplication, QMainWindow, QMessageBox, QMenu, QAction, QGridLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QComboBox, QLineEdit, QCheckBox


from datetime import datetime

def build(parent):
	#self.configPath = os.path.expanduser('~/linuxcnc/configs') # + '/' + parent.configName
	#configPath = os.path.split(os.path.realpath(sys.argv[0]))[0]
	#iniFilePath = os.path.join(parent.configPath, parent.configName + '.ini')
	#parent.machinePTE.appendPlainText(f'Building {iniFilePath}')
	#
	#if os.path.isfile(iniFilePath):
	#	pass
	#
	#if not os.path.exists(parent.configPath):
	#	try:
	#		os.mkdir(parent.configPath)
	#	except OSError:
	#		parent.machinePTE.appendPlainText(f'OS error\n {traceback.print_exc()}')
	
	f = open("ini.txt", "w")

	f.write('# This file was created by the Remora Configuration Tool\n')
	f.write(f'# on {datetime.now().strftime("%b %d %Y %H:%M:%S")}\n')
	f.write('# Changes to most values are ok and will be read by the Configuration Tool\n')

	# build the [EMC] section
	f.write('\n[EMC]\n')
	#f.close()
	#f.write(f'VERSION = {parent.emcVersion}\n')
	f.write(f'VERSION = 1.1\n')
	f.write(f'MACHINE = {parent.configName}\n')
	f.write(f'DEBUG = {parent.debugCB.currentText()}\n')

	# build the [DISPLAY] section maxFeedOverrideLE
	f.write('\n[DISPLAY]\n')
	f.write(f'DISPLAY = {parent.guiCB.currentText()}\n')
	if parent.editorCB.currentText():
		f.write(f'EDITOR = {parent.editorCB.currentText()}\n')
	f.write(f'PROGRAM_PREFIX = {os.path.expanduser("~/linuxcnc/nc_files")}\n')
	f.write(f'POSITION_OFFSET = {parent.positionOffsetCB.currentText()}\n')
	f.write(f'POSITION_FEEDBACK = {parent.positionFeedbackCB.currentText()}\n')
	f.write(f'MAX_FEED_OVERRIDE = {parent.maxFeedOverrideSB.value()}\n')
	f.write(f'DEFAULT_LINEAR_VELOCITY = {parent.defaultJogSpeedDSB.value()}\n')
	f.write('CYCLE_TIME = 0.1\n')
	f.write(f'INTRO_GRAPHIC = {parent.introGraphicLE.text()}\n')
	f.write(f'INTRO_TIME = {parent.introGraphicSB.value()}\n')
	if parent.startUpFileLE.text():
		f.write(f'OPEN_FILE = {parent.startUpFileLE.text()}\n')
	else:
		f.write('OPEN_FILE = ""\n')
	if parent.pyvcpCB.isChecked():
		f.write(f'PYVCP = {parent.configName}.xml\n')
	if parent.frontToolLatheRB.isChecked():
		f.write('LATHE = 1\n')
	if parent.frontToolLatheRB.isChecked():
		f.write('BACK_TOOL_LATHE = 1\n')

	# build the [KINS] section
	f.write('\n[KINS]\n')
	#logic to jount joints
	jointcnt = 0
	for i in range(8):
				if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1: 
					jointcnt = jointcnt +1
	
	f.write(f'JOINTS = {jointcnt}\n')
	
	f.write(f'KINEMATICS = trivkins coordinates= {parent.coordinatesLB.text()}')
	axislist2 = ['X', 'Y', 'Z', 'A', 'B', 'C', 'U', 'V', 'W']
	for i in range(8):
				if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
					f.write(f'{axislist2[i]}')			
	#if len(set(parent.coordinatesLB.text())) == len(parent.coordinatesLB.text()):
	#	f.write(f'KINEMATICS = trivkins coordinates={parent.coordinatesLB.text()}')
	#	for i in range(8):
	#			if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1: 
	#				jointcnt = jointcnt +1
	#else: # more than one joint per axis
	#	f.write(f'KINEMATICS = trivkins coordinates={parent.coordinatesLB.text()} kinstype=BOTH\n')

	# build the [EMCIO] section
	f.write('\n')
	f.write('\n[EMCIO]\n')
	f.write('EMCIO = iov2\n')
	f.write('CYCLE_TIME = 0.100\n')
	f.write('TOOL_TABLE = tool.tbl\n')

	# build the [RS274NGC] section
	f.write('\n[RS274NGC]\n')
	f.write(f'PARAMETER_FILE = linuxcnc.var\n')
	#f.write(f'SUBROUTINE_PATH = {os.path.expanduser("~/linuxcnc/subroutines")}\n')

	# build the [EMCMOT] section
	f.write('\n[EMCMOT]\n')
	f.write('EMCMOT = motmod\n')
	f.write(f'BASE_PERIOD = {parent.basePeriodSB.value()}\n')
	f.write(f'SERVO_PERIOD = {parent.servoPeriodSB.value()}\n')

	# build the [TASK] section
	f.write('\n[TASK]\n')
	f.write('TASK = milltask\n')
	f.write('CYCLE_TIME = 0.010\n')

	# build the [TRAJ] section
	f.write('\n[TRAJ]\n')
	f.write(f'COORDINATES = ')
	for i in range(8):
				if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
					f.write(f'{axislist2[i]}'" ")
	f.write('\n')
	f.write(f'LINEAR_UNITS = {parent.linearUnitsCB.currentText()}\n')
	f.write('ANGULAR_UNITS = degree\n')
	f.write(f'MAX_LINEAR_VELOCITY = {parent.maxLinearVel.text()}\n')

	# build the [HAL] section
	f.write('\n[HAL]\n')
	f.write(f'HALFILE = {parent.configName}.hal\n')
	f.write('HALFILE = io.hal\n')
	if parent.customhalCB.isChecked():
		f.write('HALFILE = custom.hal\n')
	if parent.postguiCB.isChecked():
		f.write('POSTGUI_HALFILE = postgui.hal\n')
	if parent.shutdownCB.isChecked():
		f.write('SHUTDOWN = shutdown.hal\n')
	f.write('HALUI = halui\n')

	# build the [HALUI] section
	f.write('\n[HALUI]\n')
	#f.close()

	# build the AXES and JOINT sections
	axes = {1:'X', 2:'Y', 3:'Z', 4:'A', 5:'B', 6:'C', 7:'U', 8:'V'}
	axisType = {1:'LINEAR', 2:'LINEAR', 3:'LINEAR',
		4:'ANGULAR', 5:'ANGULAR', 6:'ANGULAR',
		7:'LINEAR', 8:'LINEAR', 9:'LINEAR'}
	for i in range(1, 8):
		if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
		#if parent.axisTabs.isTabEnabled(i):
			f.write(f'\n[AXIS_{axes[i]}]\n')
			f.write(f'MIN_LIMIT = {getattr(parent, "minLimit_" + str(i)).text()}\n')
			f.write(f'MAX_LIMIT = {getattr(parent, "maxLimit_" + str(i)).text()}\n')
			f.write(f'MAX_VELOCITY = {getattr(parent, "maxVelocity_" + str(i)).text()}\n')
			f.write(f'MAX_ACCELERATION = {getattr(parent, "maxAccel_" + str(i)).text()}\n')

			f.write(f'\n[JOINT_{i-1}]\n')
			f.write(f'TYPE = {getattr(parent, "axisType_" + str(i)).text()}\n')
			f.write(f'MIN_LIMIT = {getattr(parent, "minLimit_" + str(i)).text()}\n')
			f.write(f'MAX_LIMIT = {getattr(parent, "maxLimit_" + str(i)).text()}\n')
			f.write(f'MAX_VELOCITY = {getattr(parent, "maxVelocity_" + str(i)).text()}\n')
			f.write(f'MAX_ACCELERATION = {getattr(parent, "maxAccel_" + str(i)).text()}\n')
			if getattr(parent, "reverse_" + str(i)).isChecked():
				f.write(f'SCALE = -{getattr(parent, "scale_" + str(i)).text()}\n')
			else:
				f.write(f'SCALE = {getattr(parent, "scale_" + str(i)).text()}\n')
			#f.write(f'STEPGEN_MAX_VEL = {str(float(getattr(parent, "maxVelocity_" + str(i)).text()) * 1.2)}\n')
			#f.write(f'STEPGEN_MAX_ACC = {str(float(getattr(parent, "maxAccel_" + str(i)).text()) * 1.2)}\n')
			if parent.linearUnitsCB.currentText()  == 'inch':
				f.write('FERROR = 0.0002\n')
				f.write('MIN_FERROR = 0.0001\n')
			else:
				f.write('FERROR = 0.0050\n')
				f.write('MIN_FERROR = 0.0025\n')
			if getattr(parent, "home_" + str(i)).text():
				f.write(f'HOME = {getattr(parent, "home_" + str(i)).text()}\n')
			if getattr(parent, "homeOffset_" + str(i)).text():
				f.write(f'HOME_OFFSET = {getattr(parent, "homeOffset_" + str(i)).text()}\n')
			if getattr(parent, "homeSearchVel_" + str(i)).text():
				f.write(f'HOME_SEARCH_VEL = {getattr(parent, "homeSearchVel_" + str(i)).text()}\n')
			if getattr(parent, "homeLatchVel_" + str(i)).text():
				f.write(f'HOME_LATCH_VEL = {getattr(parent, "homeLatchVel_" + str(i)).text()}\n')
			if getattr(parent, "homeUseIndex_" + str(i)).isChecked():
				f.write(f'HOME_USE_INDEX = {getattr(parent, "homeUseIndex_" + str(i)).isChecked()}\n')
			if getattr(parent, "homeIgnoreLimits_" + str(i)).isChecked():
				f.write(f'HOME_IGNORE_LIMITS = {getattr(parent, "homeIgnoreLimits_" + str(i)).isChecked()}\n')
			if getattr(parent, "homeSequence_" + str(i)).text():
				f.write(f'HOME_SEQUENCE = {getattr(parent, "homeSequence_" + str(i)).text()}\n')

	f.write('\n# DO NOT change anything below this line\n')

	# build the [OPTIONS] section
	f.write('\n[OPTIONS]\n')
	f.write(f'MANUAL_TOOL_CHANGE = {parent.manualToolChangeCB.isChecked()}\n'.format())
	f.write(f'CUSTOM_HAL = {parent.customhalCB.isChecked()}\n')
	f.write(f'POST_GUI_HAL = {parent.postguiCB.isChecked()}\n')
	f.write(f'SHUTDOWN_HAL = {parent.shutdownCB.isChecked()}\n')
	f.write(f'PYVCP = {parent.pyvcpCB.isChecked()}\n')
	#f.write(f'GLADEVCP = {parent.gladevcpCB.isChecked()}\n')
	

	'''

			f.write(f'DIRSETUP = {getattr(parent, "dirSetup_" + str(i)).text()}\n')
			f.write(f'DIRHOLD = {getattr(parent, "dirHold_" + str(i)).text()}\n')
			f.write(f'STEPLEN = {getattr(parent, "stepTime_" + str(i)).text()}\n')
			f.write(f'STEPSPACE = {getattr(parent, "stepSpace_" + str(i)).text()}\n')
			f.write(f'DEADBAND = {getattr(parent, "deadband_" + str(i)).text()}\n')
			f.write(f'P = {getattr(parent, "p_" + str(i)).text()}\n')
			f.write(f'I = {getattr(parent, "i_" + str(i)).text()}\n')
			f.write(f'D = {getattr(parent, "d_" + str(i)).text()}\n')
			f.write(f'FF0 = {getattr(parent, "ff0_" + str(i)).text()}\n')
			f.write(f'FF1 = {getattr(parent, "ff1_" + str(i)).text()}\n')
			f.write(f'FF2 = {getattr(parent, "ff2_" + str(i)).text()}\n')
			f.write(f'BIAS = {getattr(parent, "bias_" + str(i)).text()}\n')
			f.write(f'MAX_OUTPUT = {getattr(parent, "maxOutput_" + str(i)).text()}\n')
			f.write(f'MAX_ERROR = {getattr(parent, "maxError_" + str(i)).text()}\n')

	# build the [SPINDLE] section if enabled
	#print(parent.spindleTypeCB.currentText())
	if parent.spindleTypeCB.itemText(parent.spindleTypeCB.currentIndex()):
		f.write('\n[SPINDLE]\n')
		f.write('OUTPUT_TYPE = {}\n'.format(parent.spindleTypeCB.itemText(parent.spindleTypeCB.currentIndex())))
		f.write('SCALE = {}\n'.format(parent.spindleScale.text()))
		f.write('PWM_FREQUENCY = {}\n'.format(parent.pwmFrequencySB.value()))
		f.write('MAX_RPM = {}\n'.format(parent.spindleMaxRpm.text()))
		f.write('MIN_RPM = {}\n'.format(parent.spindleMinRpm.text()))
		f.write('DEADBAND = {}\n'.format(parent.deadband_s.text()))
		f.write('P = {}\n'.format(parent.p_s.text()))
		f.write('I = {}\n'.format(parent.i_s.text()))
		f.write('D = {}\n'.format(parent.d_s.text()))
		f.write('FF0 = {}\n'.format(parent.ff0_s.text()))
		f.write('FF1 = {}\n'.format(parent.ff1_s.text()))
		f.write('FF2 = {}\n'.format(parent.ff2_s.text()))
		f.write('BIAS = {}\n'.format(parent.bias_s.text()))
		f.write('MAX_ERROR = {}\n'.format(parent.maxError_s.text()))

	f.write('\n# Everything below this line is only used to\n')
	f.write('# setup the Configuration Tool when loading the ini.\n')

	# build the [INPUTS] section from pushbuttons
	f.write('\n[INPUT_PB]\n')
	f.write('# DO NOT change the inputs text\n')
	for i in range(11):
		f.write(f'INPUT_PB_{i} = {getattr(parent, "inputPB_" + str(i)).text()}\n')
		f.write(f'INPUT_INVERT_{i} = {getattr(parent, "inputInvertCB_" + str(i)).isChecked()}\n')

	# build the [OUTPUTS] section from pushbuttons
	f.write('\n[OUTPUT_PB]\n')
	f.write('# DO NOT change the outputs text\n')
	for i in range(6):
		f.write(f'OUTPUT_PB_{i} = {getattr(parent, "outputPB_" + str(i)).text()}\n')

	'''
	
