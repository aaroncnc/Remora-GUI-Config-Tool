import os, traceback, sys
from PyQt5 import QtWidgets, uic
from functools import partial
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QApplication, QMainWindow, QMessageBox, QMenu, QAction, QGridLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QComboBox, QLineEdit, QCheckBox


from datetime import datetime

def build(parent):
	f = open(f'{parent.configName.text()}'".hal", "w")
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
	if parent.boards.currentText() == "SKR v1.3 & v1.4 LPC1768" or parent.boards.currentText() == "MKS SBASE v1.3 LPC1768":
		f.write(f'loadrt remora\n')
	else:
		f.write(f'loadrt remora chip_type=STM SPI_clk_div=16 PRU_base_freq=80000\n')
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
	
#check for encoders to load.
	if parent.qem.isChecked() or parent.enc0.isChecked() or parent.enc1.isChecked() or parent.enc2.isChecked() or parent.enc3.isChecked():
		f.write('\n# Encoder setup\n')
		f.write('loadrt PRUencoder names=')
		if parent.enc0.isChecked(): f.write('encoder.0,')
		if parent.enc1.isChecked(): f.write('encoder.1,')
		if parent.enc2.isChecked(): f.write('encoder.2,')
		if parent.enc3.isChecked(): f.write('encoder.3,')
		if parent.qem.isChecked(): f.write('encoder.spindle,')
		f.write('\naddf PRUencoder.capture-position servo-thread\n')
	f.write('\n\n')

#check for scales to load
	if parent.pwm6.isChecked() or parent.qem.isChecked():
		f.write('#scale setup\n')
		i = 0
		if parent.pwm6.isChecked(): i = i+1
		#if parent.qem.isChecked(): i = i+1
		f.write(f'loadrt scale count ={i}\n')
		#f.write('addf scale.0 servo-thread\n')
	
#spindle setup 'Spindle':['Spindle On', 'Spindle CW', 'Spindle CCW', 'Spindle Brake'
	if parent.pwm6.isChecked():
		f.write('\n# Spindle setup PWM to DAC\n')
		f.write('loadrt abs count 1\n')
		f.write('addf abs.0 servo-thread\n')
		f.write('addf scale.spindle servo-thread\n')
		f.write(f'setp scale.spindle.gain {10 / int(parent.spindleMaxRpm.text())}\n')
		f.write('net spindle-speed-scale spindle.0.speed-out scale.spindle.in\n')
		f.write('net spindle-speed-abs scale.spindle.out abs.0.in\n')
		f.write('net spindle-DAC abs.0.out remora.SP.6\n\n')
	f.write('\n')
	
#High speed encoder setup.
	if parent.qem.isChecked():
		f.write('#Spindle high speed encoder  \n')
		f.write(f'setp encoder.spindle.position-scale {parent.qemtxt.text()}\n')
		f.write(f'net encoder-count remora.PV.{parent.qempv.text()} encoder.spindle.raw_count \n')
		f.write('net spindle-position encoder.spindle.position spindle.0.revs \n')
		f.write('net spindle-velocity encoder.spindle.velocity spindle.0.speed-in \n') 
		if parent.qeminput.text() != "":
			f.write(f'net spindle-index-enable encoder.spindle.index-enable spindle.0.index-enable \n')
			f.write(f'net encoder-phasez remora.input.{parent.qeminput.text()} encoder.spindle.phase-z \n')
			
			
#IO control coolant and lube pump ect 

	if parent.out0chk.isChecked() or parent.out1chk.isChecked() or parent.out2chk.isChecked() or parent.out3chk.isChecked() or parent.out4chk.isChecked() or parent.out5chk.isChecked() or parent.out6chk.isChecked() or parent.out7chk.isChecked():
		f.write('# Output setup\n')
		for i in range(8):
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Coolant Flood":
				f.write(f'net coolant-flood iocontrol.0.coolant-flood remora.output.{i}\n')
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Coolant Mist":
				f.write(f'net coolant-mist iocontrol.0.coolant-mist remora.output.{i}\n')
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Lube Pump":
				f.write(f'net coolant-lube iocontrol.0.coolant-lube remora.output.{i}\n')
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Tool Change":
				f.write(f'net tool-change iocontrol.0.tool-change remora.output.{i}\n')
				f.write(f'net tool-prepare iocontrol.0.tool-prepare iocontrol.0.tool-prepared\n')
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Tool Prepare":
				f.write(f'net tool-prepare iocontrol.0.tool-prepare remora.output.{i}\n')
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "E Stop Out":
				f.write(f'net user-enable-out iocontrol.0.user-enable-out  remora.output.{i}\n')
		f.write('\n')
	#f.write('# Spindle output setup\n')
		for i in range(8):
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Spindle On":
				f.write(f'net spindle-on spindle.0.on remora.output.{i}\n')
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Spindle CW":
				f.write(f'net spindle-cw spindle.0.forward remora.output.{i}\n')
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Spindle CCW":
				f.write(f'net spindle-ccw spindle.0.reverse remora.output.{i}\n')
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Spindle Brake":
				f.write(f'net spindle-brake spindle.0.brake remora.output.{i}\n')
	#Build  digital output 0-3
		for i in range(8):
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Digital Out 0":
				f.write(f'net dout-00 motion.digital-out-00 remora.output.{i}\n')
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Digital Out 1":
				f.write(f'net dout-00 motion.digital-out-01 remora.output.{i}\n')
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Digital Out 2":
				f.write(f'net dout-00 motion.digital-out-02 remora.output.{i}\n')
			if getattr(parent, f'{parent.outlist[i]}'"txt").text() == "Digital Out 3":
				f.write(f'net dout-00 motion.digital-out-03 remora.output.{i}\n')
	f.write('\n\n')
	
	
			#if getattr(parent, f'{parent.inlist[x]}'"txt").text() == "All Max" or getattr(parent, f'{parent.inlist[x]}'"txt").text() == "All Min" or getattr(parent, f'{parent.inlist[x]}'"txt").text() == "All Both":
		#		f.write(f'net all-limit remora.input.{x}\n')
		
#limits switches all
	if parent.in0chk.isChecked() or parent.in1chk.isChecked() or parent.in2chk.isChecked() or parent.in3chk.isChecked() or parent.in4chk.isChecked() or parent.in5chk.isChecked() or parent.in6chk.isChecked() or parent.in7chk.isChecked():
		f.write('#Input setup\n')
		f.write('#Home and Limit setup\n')
		for x in range(8):
			for i in range(8):
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "All Max" and getattr(parent, f'{parent.axislist[x]}').isChecked() == 1:
					#if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
					f.write(f'net all-limit-Max remora.input.{i} joint.{x}.pos-lim-sw-in\n')
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "All Min" and getattr(parent, f'{parent.axislist[x]}').isChecked() == 1:
					#if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
					f.write(f'net all-limit-Min remora.input.{i} joint.{x}.neg-lim-sw-in\n')
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "All Both" and getattr(parent, f'{parent.axislist[x]}').isChecked() == 1:
					#if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
					f.write(f'net all-limit remora.input.{i} joint.{x}.neg-lim-sw-in\n')
					f.write(f'net all-limit remora.input.{i} joint.{x}.pos-lim-sw-in\n')
	
#Home + limits switches all
		for x in range(8):
			for i in range(8):
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Home + Limit All Max" and getattr(parent, f'{parent.axislist[x]}').isChecked() == 1:
					#if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
					f.write(f'net all-home-limit-Max remora.input.{i} joint.{x}.home-sw-in\n')
					f.write(f'net all-home-limit-Max remora.input.{i} joint.{x}.pos-lim-sw-in\n')
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Home + Limit All Min" and getattr(parent, f'{parent.axislist[x]}').isChecked() == 1:
					#if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
					f.write(f'net all-home-limit-Min remora.input.{i} joint.{x}.home-sw-in\n')
					f.write(f'net all-home-limit-Min remora.input.{i} joint.{x}.neg-lim-sw-in\n')
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Home + Limit All Both" and getattr(parent, f'{parent.axislist[x]}').isChecked() == 1:
					#if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
					f.write(f'net all-home-limit remora.input.{i} joint.{x}.home-sw-in\n')
					f.write(f'net all-home-limit remora.input.{i} joint.{x}.neg-lim-sw-in\n')
					f.write(f'net all-home-limit remora.input.{i} joint.{x}.pos-lim-sw-in\n')
	
#Home + limits switches individual
		for x in range(8):
			for i in range(8):
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == f'Home + Limit Joint {x} max' and getattr(parent, f'{parent.axislist[x]}').isChecked() == 1:
					#if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
					f.write(f'net J{x}-home-limit-Max remora.input.{i} joint.{x}.home-sw-in\n')
					f.write(f'net J{x}-home-limit-Max remora.input.{i} joint.{x}.pos-lim-sw-in\n')
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == f'Home + Limit Joint {x} min' and getattr(parent, f'{parent.axislist[x]}').isChecked() == 1:
					#if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
					f.write(f'net J{x}-home-limit-Min remora.input.{i} joint.{x}.home-sw-in\n')
					f.write(f'net J{x}-home-limit-Min remora.input.{i} joint.{x}.neg-lim-sw-in\n')
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == f'Home + Limit Joint {x} Both' and getattr(parent, f'{parent.axislist[x]}').isChecked() == 1:
					#if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
					f.write(f'net J{x}-home-limit remora.input.{i} joint.{x}.home-sw-in\n')
					f.write(f'net J{x}-home-limit remora.input.{i} joint.{x}.neg-lim-sw-in\n')
					f.write(f'net J{x}-home-limit remora.input.{i} joint.{x}.pos-lim-sw-in\n')
	
#limits switches individual
		for x in range(8):
			for i in range(8):
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == f'Joint {x} max':
					f.write(f'net max-J{x} remora.input.{i} joint.{x}.pos-lim-sw-in\n')
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == f'Joint {x} min':
					f.write(f'net min-J{x} remora.input.{i} joint.{x}.neg-lim-sw-in\n')	
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == f'Joint {x} Both':
					f.write(f'net both-J{x} remora.input.{i} joint.{x}.pos-lim-sw-in joint.{x}.neg-lim-sw-in\n')

#Home switches
		for x in range(8):
			for i in range(8):	
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == f'Joint {x} Home':
					f.write(f'net home-joint.{x}.minus remora.input.{i} joint.{x}.home-sw-in\n')		
					
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Home All" and getattr(parent, f'{parent.axislist[x]}').isChecked() == 1:
					f.write(f'net home-all remora.input.{i} joint.{x}.home-sw-in\n')

#Jog buttons
		f.write('\n#Jog buttons inputs\n')
		for x in range(8):
			for i in range(8):	
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == f'Joint {x} Plus':
					f.write(f'net jog-joint.{x}.plus remora.input.{i} halui.joint.{x}.plus\n')
					
				if getattr(parent, f'{parent.inlist[i]}'"txt").text() == f'Joint {x} Minus':
					f.write(f'net jog-joint.{x}.minus remora.input.{i} halui.joint.{x}.minus\n')	
		f.write('\n')
	
#I/O Control
		f.write('#Flood mist tool changed buttons\n')
		for i in range(8):
			if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Flood":
				f.write("#flood coolant \n")
				f.write("loadrt toggle2nist count=1 \nloadrt edge count=1 \naddf toggle2nist.0 servo-thread \naddf edge.0 servo-thread \nnet coolant-flood  <=  iocontrol.0.coolant-flood")
				f.write(f'net flood-button <= remora.input.{i} => edge.0.in \n')
				f.write(f'net button-edge <= edge.0.out => toggle2nist.0.in  \n')
				f.write(f'net flood-on <= toggle2nist.0.on => halui.flood.on  \n')
				f.write(f'net flood-off <= toggle2nist.0.off => halui.flood.off \n')
				f.write(f'net flood-control <= halui.flood.is-on => toggle2nist.0.is-on \n')
			if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Mist":
				f.write("#mist coolant \n")
				f.write("loadrt toggle2nist count=1 \nloadrt edge count=1 \naddf toggle2nist.0 servo-thread \naddf edge.0 servo-thread \nnet coolant-mist  <=  iocontrol.0.coolant-mist")
				f.write(f'net mist-button <= remora.input.{i} => edge.0.in \n')
				f.write(f'net button-edge <= edge.0.out => toggle2nist.0.in  \n')
				f.write(f'net mist-on <= toggle2nist.0.on => halui.mist.on  \n')
				f.write(f'net mist-off <= toggle2nist.0.off => halui.mist.off \n')
				f.write(f'net mist-control <= halui.mist.is-on => toggle2nist.0.is-on \n')
			if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Tool Changed":
				f.write("#Tool Changed \n")
				f.write(f'net tool-changed.0 remora.input.{i} iocontrol.0.tool-changed\n')
			if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Tool Prepared":
				f.write("#Tool Prepared \n")
				f.write(f'net tool-prepared.0 remora.input.{i} iocontrol.0.tool-prepared\n')
			if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "External E Stop":
				f.write("#E-Stop \n")
				f.write(f'net estop-ext remora.input.{i} \n')
				f.write(f'net estop-out iocontrol.0.user-enable-out \n')
				f.write(f'net estop-ext iocontrol.0.emc-enable-in \n')
		f.write('\n')
	
#motion inputs
		f.write('#Probe inputs and digital inputs\n')
		for i in range(8):
			if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Probe Input":
				f.write("#Probe Input \n")
				f.write(f'net probe-in motion.probe-input\n')
				f.write(f'net probe-in remora.input.{i}\n')
			if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Digital 0":
				f.write("#Digital 0 \n")
				f.write(f'net din-00 motion.digital-in-00\n')
				f.write(f'net din-00 remora.input.{i}\n')
			if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Digital 1":
				f.write("#Digital 1 \n")
				f.write(f'net din-01 motion.digital-in-01\n')
				f.write(f'net din-01 remora.input.{i}\n')
			if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Digital 2":
				f.write("#Digital 2 \n")
				f.write(f'net din-02 motion.digital-in-02\n')
				f.write(f'net din-02 remora.input.{i}\n')
			if getattr(parent, f'{parent.inlist[i]}'"txt").text() == "Digital 3":
				f.write("#Digital 3 \n")
				f.write(f'net din-03 motion.digital-in-03\n')
				f.write(f'net din-03 remora.input.{i}\n')
		f.write('\n')

#Joint setup
	f.write('#Joint setups\n')
	for i in range(8):
		if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
			f.write(f'#Joint {i} setups\n')
			f.write(f'setp remora.joint.{i}.scale 		[JOINT_{i}]SCALE\n')
			f.write(f'setp remora.joint.{i}.maxaccel 	[JOINT_{i}]STEPGEN_MAXACCEL\n')
			f.write(f'net j{i}pos-cmd 		<= joint.{i}.motor-pos-cmd 	=> remora.joint.{i}.pos-cmd  \n')
			f.write(f'net j{i}pos-fb 		<= remora.joint.{i}.pos-fb 	=> joint.{i}.motor-pos-fb  \n')
			f.write(f'net j{i}enable 		<= joint.{i}.amp-enable-out 	=> remora.joint.{i}.enable  \n\n')
			
			
			

