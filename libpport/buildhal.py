import os, traceback, sys
from PyQt5 import QtWidgets, uic
from functools import partial
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QApplication, QMainWindow, QMessageBox, QMenu, QAction, QGridLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QComboBox, QLineEdit, QCheckBox


from datetime import datetime

def build(parent):
	f = open("hal.txt", "w")

	#halContents = []
	f.write('# This file was created with the Remora Configuration Tool on ')
	f.write(f'# on {datetime.now().strftime("%b %d %Y %H:%M:%S")}\n')
	f.write('# If you make changes to this file DO NOT run the configuration tool again!\n')
	f.write('# This file will be replaced with a new file if you do!\n\n')

	# build the standard header
	f.write('# kinematics\n')
	f.write('loadrt [KINS]KINEMATICS\n\n')
	f.write('# motion controller\n')
	f.write('loadrt [EMCMOT]EMCMOT ')
	f.write('base_period_nsec=[EMCMOT]BASE_PERIOD ')
	f.write('servo_period_nsec=[EMCMOT]SERVO_PERIOD ')
	f.write('num_joints=[KINS]JOINTS\n\n')
	f.write('loadrt remora\n')
	f.write('net user-enable-out 	<= iocontrol.0.user-enable-out		=> remora.SPI-enable\n')
	f.write('net user-enable-out 	<= iocontrol.0.user-enable-out		=> remora.SPI-enable\n')
	f.write('net user-request-enable <= iocontrol.0.user-request-enable	=> remora.SPI-reset\n')
	f.write('net remora-status 	<= remora.SPI-status 			=> iocontrol.0.emc-enable-in\n')
	f.write('\n# add the remora and motion functions to threads\n')
	f.write('addf remora.read servo-thread\n')
	f.write('addf motion-command-handler servo-thread\n')
	f.write('addf motion-controller servo-thread\n')
	f.write('addf remora.update-freq servo-thread\n')
	f.write('addf remora.write servo-thread\n')

	
#build spindle setup 'Spindle':['Spindle On', 'Spindle CW', 'Spindle CCW', 'Spindle Brake'
	if parent.spindle.isChecked():
		f.write('# Spindle setup\n')
		f.write('loadrt scale count 1\n')
		f.write('loadrt abs count 1\n')
		f.write('addf scale.0 servo-thread\n')
		f.write('addf abs.0 servo-thread\n')
		f.write(f'setp scale.0.gain {10 / int(parent.spindleMaxRpm.text())}\n')
		f.write('net spindle-speed-scale spindle.o.speed-out scale.0.in\n')
		f.write('net spindle-speed-abs scale.o.out abs.0.in\n')
		f.write('net spindle-DAC abs.0.out remora.SP.6\n')
	for i in range(8):
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Spindle On":
			print('Spindle On')
			f.write(f'net spindle-on spindle.0.on remora.output.{i}\n')
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Spindle CW":
			print('Spindle CW')
			f.write(f'net spindle-cw spindle.0.forward remora.output.{i}\n')
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Spindle CCW":
			print('Spindle CCW')
			f.write(f'net spindle-ccw spindle.0.reverse remora.output.{i}\n')
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Spindle Brake":
			print('Spindle Brake')
			f.write(f'net spindle-brake spindle.0.brake remora.output.{i}\n')
	f.write('\n')
			
#Build  IO control coolant and lube pump ect 
	f.write('# IO control, Coolant and charge pump setup\n')
	for i in range(8):
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Coolant Flood":
			f.write(f'net coolant-flood iocontrol.0.coolant-flood remora.output.{i}\n')
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Coolant Mist":
			f.write(f'net coolant-mist iocontrol.0.coolant-mist remora.output.{i}\n')
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Lube Pump":
			f.write(f'net coolant-lube iocontrol.0.coolant-lube remora.output.{i}\n')
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Tool Change":
			f.write(f'net tool-change iocontrol.0.tool-change remora.output.{i}\n')
			f.write(f'net tool-prepare iocontrol.0.tool-prepare iocontrol.0.tool-prepared\n')
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Tool Prepare":
			f.write(f'net tool-prepare iocontrol.0.tool-prepare remora.output.{i}\n')
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "E Stop Out":
			f.write(f'net user-enable-out iocontrol.0.user-enable-out  remora.output.{i}\n')
	f.write('\n')
		
#Build  digital output 0-3
	f.write('# Build  digital output 0-3\n')
	for i in range(8):
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Digital Out 0":
			f.write(f'net dout-00 motion.digital-out-00 remora.output.{i}\n')
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Digital Out 1":
			f.write(f'net dout-00 motion.digital-out-01 remora.output.{i}\n')
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Digital Out 2":
			f.write(f'net dout-00 motion.digital-out-02 remora.output.{i}\n')
		if getattr(parent, f'{parent.outbtnlist[i]}').text() == "Digital Out 3":
			f.write(f'net dout-00 motion.digital-out-03 remora.output.{i}\n')
	f.write('\n')
	
#limits switches
	f.write('#Build  digital inputs limits min max both\n')
	for x in range(8):
		for i in range(8):
			if getattr(parent, f'{parent.inbtnlist[i]}').text() == "All Max" or getattr(parent, f'{parent.inbtnlist[i]}').text() == "All Min" or getattr(parent, f'{parent.inbtnlist[i]}').text() == "All Both":
				f.write(f'net all-limit remora.input.{i}\n')
				
			if getattr(parent, f'{parent.inbtnlist[i]}').text() == f'Joint {x} max':
				f.write(f'net max-J{x} remora.input.{i} joint.{x}.pos-lim-sw-in\n')
				
			if getattr(parent, f'{parent.inbtnlist[i]}').text() == f'Joint {x} min':
				f.write(f'net min-J{x} remora.input.{i} joint.{x}.neg-lim-sw-in\n')
				
			if getattr(parent, f'{parent.inbtnlist[i]}').text() == f'Joint {x} Both':
				f.write(f'net both-J{x} remora.input.{i} joint.{x}.pos-lim-sw-in joint.{x}.neg-lim-sw-in\n')
	f.write('\n')

#Home switches
	f.write('#Build  digital inputs home switches\n')
	for x in range(8):
		if getattr(parent, f'{parent.inbtnlist[x]}').text() == f'Home All':
				f.write(f'net home-all remora.input.{x} joint.0.home-sw-in joint.1.home-sw-in joint.2.home-sw-in\n')
		for i in range(8):	
			if getattr(parent, f'{parent.inbtnlist[i]}').text() == f'Joint {x} Home':
				f.write(f'net home-joint.{x}.minus remora.input.{i} joint.{x}.home-sw-in\n')
				
	f.write('\n')

#Jog buttons
	f.write('#Build  digital inputs Jog buttons\n')
	for x in range(8):
		for i in range(8):	
			if getattr(parent, f'{parent.inbtnlist[i]}').text() == f'Joint {x} Plus':
				f.write(f'net jog-joint.{x}.plus remora.input.{i} halui.joint.{x}.plus\n')
				
			if getattr(parent, f'{parent.inbtnlist[i]}').text() == f'Joint {x} Minus':
				f.write(f'net jog-joint.{x}.minus remora.input.{i} halui.joint.{x}.minus\n')
				
	f.write('\n')
	
#I/O Control
	f.write('# Build  digital I/O Control\n')
	for i in range(8):
		if getattr(parent, f'{parent.inbtnlist[i]}').text() == "Flood":
			f.write("#flood coolant \n")
			f.write("loadrt toggle2nist count=1 \nloadrt edge count=1 \naddf toggle2nist.0 servo-thread \naddf edge.0 servo-thread \nnet coolant-flood  <=  iocontrol.0.coolant-flood")
			f.write(f'net flood-button <= remora.input.{i} => edge.0.in \n')
			f.write(f'net button-edge <= edge.0.out => toggle2nist.0.in  \n')
			f.write(f'net flood-on <= toggle2nist.0.on => halui.flood.on  \n')
			f.write(f'net flood-off <= toggle2nist.0.off => halui.flood.off \n')
			f.write(f'net flood-control <= halui.flood.is-on => toggle2nist.0.is-on \n')
		if getattr(parent, f'{parent.inbtnlist[i]}').text() == "Mist":
			f.write("#mist coolant \n")
			f.write("loadrt toggle2nist count=1 \nloadrt edge count=1 \naddf toggle2nist.0 servo-thread \naddf edge.0 servo-thread \nnet coolant-mist  <=  iocontrol.0.coolant-mist")
			f.write(f'net mist-button <= remora.input.{i} => edge.0.in \n')
			f.write(f'net button-edge <= edge.0.out => toggle2nist.0.in  \n')
			f.write(f'net mist-on <= toggle2nist.0.on => halui.mist.on  \n')
			f.write(f'net mist-off <= toggle2nist.0.off => halui.mist.off \n')
			f.write(f'net mist-control <= halui.mist.is-on => toggle2nist.0.is-on \n')
		if getattr(parent, f'{parent.inbtnlist[i]}').text() == "Tool Changed":
			f.write("#Tool Changed \n")
			f.write(f'net tool-changed.0 remora.input.{i} iocontrol.0.tool-changed\n')
		if getattr(parent, f'{parent.inbtnlist[i]}').text() == "Tool Prepared":
			f.write("#Tool Prepared \n")
			f.write(f'net tool-prepared.0 remora.input.{i} iocontrol.0.tool-prepared\n')
		if getattr(parent, f'{parent.inbtnlist[i]}').text() == "External E Stop":
			f.write("#E-Stop \n")
			f.write(f'net estop-ext remora.input.{i} \n')
			f.write(f'net estop-out iocontrol.0.user-enable-out \n')
			f.write(f'net estop-ext iocontrol.0.emc-enable-in \n')
	f.write('\n')
	
#motion inputs
	f.write('# Build Probe inputs and digital inputs\n')
	for i in range(8):
		if getattr(parent, f'{parent.inbtnlist[i]}').text() == "Probe Input":
			f.write("#Probe Input \n")
			f.write(f'net probe-in motion.probe-input\n')
			f.write(f'net probe-in remora.input.{i}\n')
		if getattr(parent, f'{parent.inbtnlist[i]}').text() == "Digital 0":
			f.write("#Digital 0 \n")
			f.write(f'net din-00 motion.digital-in-00\n')
			f.write(f'net din-00 remora.input.{i}\n')
		if getattr(parent, f'{parent.inbtnlist[i]}').text() == "Digital 1":
			f.write("#Digital 1 \n")
			f.write(f'net din-01 motion.digital-in-01\n')
			f.write(f'net din-01 remora.input.{i}\n')
		if getattr(parent, f'{parent.inbtnlist[i]}').text() == "Digital 2":
			f.write("#Digital 2 \n")
			f.write(f'net din-02 motion.digital-in-02\n')
			f.write(f'net din-02 remora.input.{i}\n')
		if getattr(parent, f'{parent.inbtnlist[i]}').text() == "Digital 3":
			f.write("#Digital 3 \n")
			f.write(f'net din-03 motion.digital-in-03\n')
			f.write(f'net din-03 remora.input.{i}\n')

	f.write('\n')






	#for i in range(8):
	#	if getattr(parent, f'{parent.inbtnlist[i]}').text() == "Joint all":
	#		f.write(f'net all-limit remora.input.{i}\n')
		
		
		
	for i in range(8):
		#if parent.axisTabs.isTabEnabled(i):
		if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
			pass
	# check port 1 for axes
	axes = ['X', 'Y', 'Z', 'A', 'B', 'C', 'U', 'V']
	#if parent.pp1typeCB.currentData() == 'out':
	halpins = {'p1OutPB_0':'parport.0.pin-01-out',
					'p1OutPB_1':'parport.0.pin-02-out',
					'p1OutPB_2':'parport.0.pin-03-out',
					'p1OutPB_3':'parport.0.pin-04-out',
					'p1OutPB_4':'parport.0.pin-05-out',
					'p1OutPB_5':'parport.0.pin-06-out',
					'p1OutPB_6':'parport.0.pin-07-out',
					'p1OutPB_7':'parport.0.pin-08-out',
					'p1OutPB_8':'parport.0.pin-09-out',
					'p1OutPB_9':'parport.0.pin-14-out',
					'p1OutPB_10':'parport.0.pin-16-out',
					'p1OutPB_11':'parport.0.pin-17-out',
					'p1InPB_0':'parport.0.pin-10-in',
					'p1InPB_1':'parport.0.pin-11-in',
					'p1InPB_2':'parport.0.pin-12-in',
					'p1InPB_3':'parport.0.pin-13-in',
					'p1InPB_4':'parport.0.pin-15-in',}
	

	portpins = {'in':{'out':{0:'01', 1:'14', 2:'16', 3:'17'},
										'in':{0:'2', 1:'3', 2:'4', 3:'5', 4:'6',
										5:'7', 6:'8', 7:'9', 8:'10', 9:'11',
										10:'12', 11:'13', 12:'15'}},
							'out':{}}

	axes = ['X Step', 'X Direction',
					'Y Step', 'Y Direction',
					'Z Step', 'Z Direction',
					'A Step', 'A Direction',
					'B Step', 'B Direction',
					'C Step', 'C Direction',
					'U Step', 'U Direction',
					'V Step', 'V Direction',
					'W Step', 'W Direction']

	signal = {'X Step': 'x-step',
						'X Direction': 'x-direction',
						'Y Step': 'y-step',
						'Y Direction': 'y-direction',
						'Z Step': 'z-step',
						'Z Direction': 'z-direction',
						'A Step': 'a-step',
						'A Direction': 'a-direction',
						'B Step': 'b-step',
						'B Direction': 'b-direction',
						'C Step': 'c-step',
						'C Direction': 'c-direction',
						'U Step': 'u-step',
						'U Direction': 'u-direction',
						'V Step': 'v-step',
						'V Direction': 'v-direction',
						'W Step': 'w-step',
						'W Direction': 'w-direction'}

	pins = {'in':{'inpins':['02', '03', '04', '05', '06',
							'07', '08', '09', '10', '11', '12', '13', '15'],
							'outpins':['01', '14', '16', '17']},
				'out':{'inpins':['10', '11', '12', '13', '15'],
							'outpins':['01', '02', '03', '04', '05',
							'06', '07', '08', '09', '14', '16', '17']}}
	f.close()
	inPins = pins[parent.pp1typeCB.currentData()]['inpins']
	outPins = pins[parent.pp1typeCB.currentData()]['outpins']


	if len(set(parent.coordinatesLB.text())) != len(parent.coordinatesLB.text()):
		print('gantry')

	for axis in parent.coordinatesLB.text():
		pass

	f.write('\n# Axes\n')
	f.write('net enable <= motion.motion-enabled\n')
	for i, (k, v) in enumerate(parent.p1outBtns.items()):
		if v.text() in axes:
			signal = v.text().replace(' ', '-').lower()
			f.write(f'net {signal} => parport.0.pin-{outPins[i]}-out\n')
			#if p1inCkBxs p1outCkBxs
			if parent.p1outCkBxs[f'p1OutCB_{i}'].isChecked():
				f.write(f'setp parport.0.pin-{outPins[i]}-out-reset 1\n')

	for k, v in parent.p2outBtns.items():
		if v.text() in axes:
			signal = v.text().replace(' ', '-').lower()
			f.write(f'net {signal} => parport.1.pin-{outPins[i]}-out\n')
			if parent.p2outCkBxs[f'p2OutCB_{i}'].isChecked():
				f.write(f'setp parport.1.pin-{outPins[i]}-out-reset 1\n')

	f.write('\n# Step Generators\n')
	for i, k in enumerate(parent.coordinatesLB.text()):
		f.write(f'setp stepgen.{i}.position-scale [JOINT_{i}]SCALE\n')
		f.write(f'setp stepgen.{i}.steplen 1\n')
		f.write(f'setp stepgen.{i}.stepspace 0\n')
		f.write(f'setp stepgen.{i}.dirhold {parent.dirHoldLE.text()}\n')
		f.write(f'setp stepgen.{i}.dirsetup {parent.dirSetupLE.text()}\n')
		f.write(f'setp stepgen.{i}.maxaccel [JOINT_{i}]STEPGEN_MAX_ACC\n')
		f.write(f'net {k.lower()}-position-command joint.{i}.motor-pos-cmd => stepgen.{i}.position-cmd\n')
		f.write(f'net {k.lower()}-position-feedback stepgen.{i}.position-fb => joint.{i}.motor-pos-fb\n')
		f.write(f'net {k.lower()}-step <= stepgen.{i}.step\n')
		f.write(f'net {k.lower()}-direction <= stepgen.{i}.dir\n')
		f.write(f'net enable => stepgen.{i}.enable\n\n')

	'''
	net xpos-cmd joint.0.motor-pos-cmd => stepgen.0.position-cmd
	net xpos-fb stepgen.0.position-fb => joint.0.motor-pos-fb
	net xstep <= stepgen.0.step
	net xdir <= stepgen.0.dir
	'''

	f.write('\n# E-Stop Loopback\n')
	f.write('net estop-loopback <= iocontrol.0.user-enable-out\n')
	f.write('net estop-loopback => iocontrol.0.emc-enable-in\n')


		# f.write(f'{i}\n')
		# f.write('\n')

	'''
	f.write('\n# Port 1 Inputs\n')
	for k, v in parent.p1inBtns.items():
		if v.text() != 'Select':
			signal = v.text().replace(' ', '-').lower()
			f.write(f'net {signal} <= {pins[k]}\n')
	'''

			#print(pins[k])
			#print(signal[v.text()])

	'''
	# don't forget to add not!!!
	coords = parent.coordinatesLB.text()
	port1 = list(parent.p1outBtns.items())
	#print(type(port1[0]))
	for l in coords:
		f.write(f'# {l} Axis\n')
		for i, (k, v) in enumerate(port1):
			if v.text().startswith(l):
				f.write(f'net {stepDir[v.text()]}_{i} => {pins[k]}\n')
				del port1[i]
			#print(f'{i} {k} {v.text()}')
	'''

	'''
	#print(type(port1))
	for i, c in enumerate(coords):
		f.write(f'\n# {c} Axis Joint {i}\n')
		for k, v in port1.items():
			if v.text().startswith(c):
				f.write(f'net {stepDir[v.text()]}_{i} => {pins[k]}\n')
				del port1[k]
	'''
	'''
	if parent.pp1typeCB:

		#for k, v in parent.p1inBtns.items():
		#		print(v.text())
		#		print(pins[k])




	f.write('\n# standard components\n')


	f.write(f'loadrt pid num_chan={parent.axes} \n\n')
	f.write('# hostmot2 driver\n')
	f.write('loadrt hostmot2\n\n')
	f.write('loadrt [HOSTMOT2](DRIVER) ')
	f.write('board_ip=[HOSTMOT2](IPADDRESS) ')
	if parent.stepgensCB.currentData():
		f.write('num_stepgens=[HOSTMOT2](STEPGENS) ')
	if parent.encodersCB.currentData():
		f.write('config="num_encoders=[HOSTMOT2](ENCODERS) ')
	if parent.pwmgensCB.currentData():
		f.write('num_pwmgens=[HOSTMOT2](PWMS) ')
	f.write(f'\nsetp hm2_[HOSTMOT2](BOARD).0.watchdog.timeout_ns {parent.servoPeriodSB.value() * 5}\n')
	f.write('\n# THREADS\n')
	f.write('addf hm2_[HOSTMOT2](BOARD).0.read servo-thread\n')
	f.write('addf motion-command-handler servo-thread\n')
	f.write('addf motion-controller servo-thread\n')
	f.write('setp hm2_[HOSTMOT2](BOARD).0.dpll.01.timer-us -100\n')
	f.write('setp hm2_[HOSTMOT2](BOARD).0.stepgen.timer-number 1 \n')
	for i in range(len(parent.coordinatesLB.text())):
		f.write(f'addf pid.{i}.do-pid-calcs servo-thread\n')
	f.write('addf hm2_[HOSTMOT2](BOARD).0.write servo-thread\n')
	for i in range(parent.axes):
		f.write(f'\n# Joint {i}\n')
		f.write('# axis enable chain\n')
		f.write(f'newsig emcmot.{i}.enable bit\n')
		f.write(f'sets emcmot.{i}.enable FALSE\n')
		f.write(f'net emcmot.{i}.enable <= joint.{i}.amp-enable-out\n')
		f.write(f'net emcmot.{i}.enable => hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.enable pid.{i}.enable\n\n')
		f.write('# position command and feedback\n')
		f.write(f'net emcmot.{i}.pos-cmd joint.{i}.motor-pos-cmd => pid.{i}.command\n')
		f.write(f'net motor.{i}.pos-fb <= hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.position-fb joint.{i}.motor-pos-fb pid.{i}.feedback\n')
		f.write(f'net motor.{i}.command pid.{i}.output hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.velocity-cmd\n')
		f.write(f'setp pid.{i}.error-previous-target true\n\n')
		f.write(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.dirsetup [JOINT_{i}]DIRSETUP\n')
		f.write(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.dirhold [JOINT_{i}]DIRHOLD\n')
		f.write(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.steplen [JOINT_{i}]STEPLEN\n')
		f.write(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.stepspace [JOINT_{i}]STEPSPACE\n')
		f.write(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.position-scale [JOINT_{i}]SCALE\n')
		f.write(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.maxvel [JOINT_{i}]STEPGEN_MAX_VEL\n')
		f.write(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.maxaccel [JOINT_{i}]STEPGEN_MAX_ACC\n')
		f.write(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.step_type 0\n')
		f.write(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.control-type 1\n\n')

		f.write(f'setp pid.{i}.Pgain [JOINT_{i}]P\n')
		f.write(f'setp pid.{i}.Igain [JOINT_{i}]I\n')
		f.write(f'setp pid.{i}.Dgain [JOINT_{i}]D\n')
		f.write(f'setp pid.{i}.bias [JOINT_{i}]BIAS\n')
		f.write(f'setp pid.{i}.FF0 [JOINT_{i}]FF0\n')
		f.write(f'setp pid.{i}.FF1 [JOINT_{i}]FF1\n')
		f.write(f'setp pid.{i}.FF2 [JOINT_{i}]FF2\n')
		f.write(f'setp pid.{i}.deadband [JOINT_{i}]DEADBAND\n')
		f.write(f'setp pid.{i}.maxoutput [JOINT_{i}]MAX_OUTPUT\n')
		f.write(f'setp pid.{i}.maxerror [JOINT_{i}]MAX_ERROR\n')

	if parent.spindleTypeCB.itemData(parent.spindleTypeCB.currentIndex()):
		f.write('\n# Spindle\n')
		f.write('setp hm2_[HOSTMOT2](BOARD).0.pwmgen.00.output-type [SPINDLE]OUTPUT_TYPE\n')
		f.write('setp hm2_[HOSTMOT2](BOARD).0.pwmgen.00.scale [SPINDLE]MAX_RPM\n')
		f.write('setp hm2_[HOSTMOT2](BOARD).0.pwmgen.pwm_frequency [SPINDLE]PWM_FREQUENCY\n')
		f.write('net spindle-on spindle.0.on => hm2_[HOSTMOT2](BOARD).0.pwmgen.00.enable\n')
		f.write('net spindle-speed spindle.0.speed-out => hm2_[HOSTMOT2](BOARD).0.pwmgen.00.value\n')

	externalEstop = False
	for i in range(6):
		key = getattr(parent, 'outputPB_' + str(i)).text()
		if key == 'E Stop Out':
			externalEstop = True
	if not externalEstop:
		f.write('\n# Standard I/O Block - EStop, Etc\n')
		f.write('# create a signal for the estop loopback\n')
		f.write('net estop-loopback iocontrol.0.emc-enable-in <= iocontrol.0.user-enable-out\n')

	if parent.manualToolChangeCB.isChecked():
		f.write('\n# create signals for tool loading loopback\n')
		f.write('net tool-prep-loop iocontrol.0.tool-prepare => iocontrol.0.tool-prepared\n')
		f.write('net tool-change-loop iocontrol.0.tool-change => iocontrol.0.tool-changed\n')

	if parent.ladderGB.isChecked():
		f.write('\n# # Load Classicladder without GUI\n')
		# this line needs to be built from the options if any are above 0
		ladderOptions = []
		for option in parent.ladderOptionsList:
			if getattr(parent, option).value() > 0:
				ladderOptions.append(getattr(parent, option).property('option') + '=' + str(getattr(parent, option).value()))
		if ladderOptions:
				f.write(f'loadrt classicladder_rt {" ".join(ladderOptions)}\n')
		else:
			f.write('loadrt classicladder_rt\n')
		f.write('addf classicladder.0.refresh servo-thread 1\n')
	'''

	try:
		with open(halFilePath, 'w') as halFile:
			halFile.writelines(halContents)
			return True
	except OSError:
		parent.machinePTE.appendPlainText(f'OS error\n {traceback.print_exc()}')
		return False
