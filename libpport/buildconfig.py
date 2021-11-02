import os, traceback, sys
from PyQt5 import QtWidgets, uic
from functools import partial
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QApplication, QMainWindow, QMessageBox, QMenu, QAction, QGridLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QComboBox, QLineEdit, QCheckBox

# Write data out to the config file for the board		 
def build(parent):
	with open('config.txt', 'w') as f:
		f.write('{'+'\n')
	#Boards
		if parent.boards.currentText() == "MKS SBASE v1.3 LPC1768":
			f.write('\t'+'"Board": "'+ parent.boards.currentText() + '",' +'\n'+'\t'+'"Modules":['+'\n'+'\t'+'{'+'\n'+'\t'+'"Thread": "On load",'+'\n'+'\t'+'"Type": "MCP4451",'+'\n'+'\t'+'"Comment": "Digipot for joints/Axis 0 - 3",'+'\n'+'\t'+'\t'+'"I2C SDA pin":'+'\t'+'\t'+'"0.0",'+'\n'+'\t'+'\t'+'"I2C SCL pin":'+'\t'+'\t'+'"0.1",'+'\n'+'\t'+'\t'+'"I2C address":'+'\t'+'\t'+'0,'+'\n'+'\t'+'\t'+'"Max current":'+'\t'+'\t'+'2.0,'+'\n'+'\t'+'\t'+'"Factor":'+'\t'+'\t'+'\t'+'113.33,'+'\n'+'\t'+'\t'+'"Current 0":'+'\t'+'\t'+parent.xaxiscur.text()+','+'\n'+'\t'+'\t'+'"Current 1":'+'\t'+'\t'+parent.yaxiscur.text()+','+'\n'+'\t'+'\t'+'"Current 2":'+'\t'+'\t'+parent.zaxiscur.text()+','+'\n'+'\t'+'\t'+'"Current 3":'+'\t'+'\t'+parent.e0axiscur.text()+'\n'+'\t'+'},'+'\n'+'\t'+'{'+'\n'+'\t'+'"Thread": "On load",'+'\n'+'\t'+'"Type": "MCP4451",'+'\n'+'\t'+'"Comment": "Digipot for joints/Axis 4 - 7",'+'\n'+'\t'+'\t'+'"I2C SDA pin":'+'\t'+'\t'+'"0.0",'+'\n'+'\t'+'\t'+'"I2C SCL pin":'+'\t'+'\t'+'"0.1",'+'\n'+'\t'+'\t'+'"I2C address":'+'\t'+'\t'+'2,'+'\n'+'\t'+'\t'+'"Max current":'+'\t'+'\t'+'2.0,'+'\n'+'\t'+'\t'+'"Factor":'+'\t'+'\t'+'\t'+'113.33,'+'\n'+'\t'+'\t'+'"Current 0":'+'\t'+'\t'+parent.e1axiscur.text()+','+'\n'+'\t'+'\t'+'"Current 1":'+'\t'+'\t'+'0.0'+','+'\n'+'\t'+'\t'+'"Current 2":'+'\t'+'\t'+'0.0'+','+'\n'+'\t'+'\t'+'"Current 3":'+'\t'+'\t'+'0.0'+'\n'+'\t'+'},'+'\n')
		if parent.boards.currentText() == "SRK2 STM32F407":
			f.write('\t'+'"Board": "'+ parent.boards.currentText() + '",' +'\n'+'\t'+'"Modules":['+'\n'+'\t'+'{'+'\n'+'\t'+'"Thread": "On load",'+'\n'+'\t'+'"Type": "Motor Power",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"Enable motor power SKR2",'+'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+'"PC_13"'+'\n'+'\t'+'},'+'\n')
		if parent.boards.currentText() == "SKR v1.3 & v1.4 LPC1768":
			f.write('\t'+'"Board": "'+ parent.boards.currentText() + '",' +'\n'+'\t'+'"Modules":['+'\n')
	#E-stop
		if parent.estop.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "eStop",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ parent.estoptxt.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + parent.estoppin.text()+'"'+'\n'+'\t'+'},'+'\n')
	#axis
		for i in range(8):
			if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(parent, f'{parent.axislist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+ getattr(parent, f'{parent.axislist[i]}'"joint").text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + getattr(parent, f'{parent.axislist[i]}'"step").text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t' +'"' + getattr(parent, f'{parent.axislist[i]}'"dir").text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t' +'"' + getattr(parent, f'{parent.axislist[i]}'"enable").text()+'"' +'\n'+'\t'+'},'+'\n')
	#TMC
		for i in range(8):
			if getattr(parent, f'{parent.axislist[i]}').isChecked() == 1:
				if str(getattr(parent, f'{parent.axislist[i]}'"tmc").currentText()) != "None": f.write('\t'+'{'+'\n'+'\t'+'"Thread": "On Load",'+'\n'+'\t'+'"Type": "' + getattr(parent, f'{parent.axislist[i]}'"tmc").currentText() + '",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(parent, f'{parent.axislist[i]}'"txt").text() + ' TMC Driver",' +'\n'+'\t'+'\t'+'"RX pin":'+'\t'+'\t'+'\t'+ getattr(parent, f'{parent.axislist[i]}'"rxpin").text() +','+'\n'+'\t'+'\t'+'"RSense":'+'\t'+'\t'+'\t' +'"' + getattr(parent, f'{parent.axislist[i]}'"cursense").text()+'",'+'\n'+'\t'+'\t'+'"Current":'+'\t'+'\t'+'\t' +'"' + getattr(parent, f'{parent.axislist[i]}'"cur").text()+'",' +'\n'+'\t'+'\t'+'"Microsteps":'+'\t'+'\t' +'"' + getattr(parent, f'{parent.axislist[i]}'"microstep").text()+'",' +'\n'+'\t'+'\t'+'"Stealth chop":'+'\t'+'\t' +'"' + getattr(parent, f'{parent.axislist[i]}'"stealthcop").currentText()+'"' +'\n'+'\t'+'},'+'\n')
	#output 
		for i in range(8):
				if getattr(parent, f'{parent.outlist[i]}'"chk").isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(parent, f'{parent.outlist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + getattr(parent, f'{parent.outlist[i]}'"pin").text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Output",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ getattr(parent, f'{parent.outlist[i]}'"state").currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(getattr(parent, f'{parent.outlist[i]}'"inv").isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +f'{i}'+'\n'+'\t'+'},'+'\n')
	#input
		for i in range(8):
				if getattr(parent, f'{parent.inlist[i]}'"chk").isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(parent, f'{parent.inlist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + getattr(parent, f'{parent.inlist[i]}'"pin").text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Input",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ getattr(parent, f'{parent.inlist[i]}'"state").currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(getattr(parent, f'{parent.inlist[i]}'"inv").isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +f'{i}'+'\n'+'\t'+'},'+'\n')
	#PWM
		for i in range(7):
				if getattr(parent, f'{parent.pwmlist[i]}').isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "PWM",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(parent, f'{parent.pwmlist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t'+ getattr(parent, f'{parent.pwmlist[i]}'"spi").text()+','+'\n'+'\t'+'\t'+'"PWM Pin":'+'\t'+'\t'+'\t' +'"' + getattr(parent, f'{parent.pwmlist[i]}'"pin").text()+'",'+'\n'+'\t'+'\t'+'"PWM Max":'+'\t'+'\t'+'\t' + getattr(parent, f'{parent.pwmlist[i]}'"max").text()+',' +'\n'+'\t'+'\t'+'"Hardware PWM":'+'\t'+'\t' +'"' +  str(getattr(parent, f'{parent.pwmlist[i]}'"hw").isChecked())+'",'+'\n'+'\t'+'\t'+'"Variable Freq":'+'\t' +'"' +  str(getattr(parent, f'{parent.pwmlist[i]}'"vf").isChecked())+'",'+'\n'+'\t'+'\t'+'"Perioid SP[i]":'+'\t' + getattr(parent, f'{parent.pwmlist[i]}'"period").text()+',' +'\n'+'\t'+'\t'+'"Perioid US":'+'\t'+'\t' + getattr(parent, f'{parent.pwmlist[i]}'"freq").text() +'\n'+'\t'+'},'+'\n')
	#Rc Servo
		if parent.rcservo.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "RCServo",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ parent.rcservotxt.text() + '",' +'\n'+'\t'+'\t'+'"Servo Pin":'+'\t'+'\t'+ '"' + parent.rcservopin.text()+'",'+'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t' + parent.rcservospi.text()+'\n'+'\t'+'},'+'\n')
	#QEM
		if parent.qem.isChecked() == 1: 
			f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "QEI",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ parent.qemtxt.text() + '",' +'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ parent.qemstate.currentText()+ '",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ parent.qempv.text())
			if parent.qeminput.text() == "":
				f.write('\n'+'\t'+'},'+'\n')
			else:
				f.write(','+'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' + parent.qeminput.text()+','+'\n'+'\t'+'\t'+'"Enable Index":'+'\t'+'\t' +'"True"' +'\n'+'\t'+'},'+'\n')
	#Encoder 
		for i in range(4):
				if getattr(parent, f'{parent.enclist[i]}').isChecked() == 1:
					f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "Encoder",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ getattr(parent, f'{parent.enclist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"ChA Pin":' +'\t'+'\t'+'\t'+'"'+ getattr(parent, f'{parent.enclist[i]}'"apin").text() + '",' +'\n'+'\t'+'\t'+'"ChB Pin":' +'\t'+'\t'+'\t'+'"'+ getattr(parent, f'{parent.enclist[i]}'"bpin").text() + '",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+	 str(getattr(parent, f'{parent.enclist[i]}'"state").currentText())+ '",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ getattr(parent, f'{parent.enclist[i]}'"pv").text())
					if getattr(parent, f'{parent.enclist[i]}'"input").text() == "":	 f.write('\n'+'\t'+'},'+'\n')
					else: f.write(','+'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' + getattr(parent, f'{parent.enclist[i]}'"input").text()+','+'\n'+'\t'+'\t'+'"Index Pin":'+'\t'+'\t'+'"' + getattr(parent, f'{parent.enclist[i]}'"ipin").text()+'"' +'\n'+'\t'+'},'+'\n')
	#Temp 
		for i in range(4):
				if getattr(parent, f'{parent.templist[i]}').isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Temperature",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ getattr(parent, f'{parent.templist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"PV[i]":' +'\t'+'\t'+'\t'+'"'+ getattr(parent, f'{parent.templist[i]}'"pv").text() + '",' +'\n'+'\t'+'\t'+'"Sensor":' +'\t'+'\t'+'\t'+'"Thermistor",'+'\n'+'\t'+'\t'+'\t'+'"Thermistor":'+'\n'+'\t'+'\t'+'\t'+'{'+'\n'+'\t'+'\t'+'\t'+'\t'+'"Pin":'+ '\t'+'\t'+'"'+ getattr(parent, f'{parent.templist[i]}'"pin").text()+'",' +'\n'+'\t'+'\t'+'\t'+'\t'+'"beta":'+ '\t'+'\t'+ getattr(parent, f'{parent.templist[i]}'"beta").text()+',' +'\n'+ '\t'+'\t'+'\t'+'\t'+'"r0":'+ '\t'+'\t'+ getattr(parent, f'{parent.templist[i]}'"r").text()+',' +'\n'+'\t'+'\t'+'\t'+'\t'+'"t0":'+ '\t'+'\t'+ getattr(parent, f'{parent.templist[i]}'"t").text() +'\n'+ '\t'+'\t'+'\t'+'}'+'\n'+'\t'+'},'+'\n')
	#swtich 
		for i in range(3):
				if getattr(parent, f'{parent.swlist[i]}').isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Switch",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(parent, f'{parent.swlist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + getattr(parent, f'{parent.swlist[i]}'"pin").text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t'+'"' + str(getattr(parent, f'{parent.swlist[i]}'"mode").currentText())+'",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ getattr(parent, f'{parent.swlist[i]}'"pv").text()+','+'\n'+'\t'+'\t'+'"SP":'+'\t'+'\t'+'\t'+'\t'+ getattr(parent, f'{parent.swlist[i]}'"sp").text() +'\n'+'\t'+'},'+'\n')
	#reset pin this must be last
		f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Reset Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ parent.resettxt.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+'"'+ parent.resetpin.text() +'"' +'\n'+'\t'+'}'+'\n')
	 # ending format
		f.write('\t'+']'+'\n'+'}')