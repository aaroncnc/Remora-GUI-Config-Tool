import os, traceback, sys
from PyQt5 import QtWidgets, uic
from functools import partial
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QApplication, QMainWindow, QMessageBox, QMenu, QAction, QGridLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QComboBox, QLineEdit, QCheckBox

#Import save data or pre configs into hmi
def load(parent):
	options = QFileDialog.Options()
	options |= QFileDialog.DontUseNativeDialog
	fileName, _ = QFileDialog.getOpenFileName(parent,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
	with open(fileName,"r") as infile:
	#boards line 1
		a, b = map(str,infile.readline().split("|"))
		parent.boards.setCurrentText(str(a))
	#axis line 2-6
		for z in range(8):
			a, b, c, d, e, f, g, h, i, j, k, l, m = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.axislist[z]}'"txt").setText(b),getattr(parent, f'{parent.axislist[z]}'"joint").setText(c),getattr(parent, f'{parent.axislist[z]}'"step").setText(d),getattr(parent, f'{parent.axislist[z]}'"dir").setText(e),getattr(parent, f'{parent.axislist[z]}'"enable").setText(f),getattr(parent, f'{parent.axislist[z]}'"cur").setText(g) ,getattr(parent, f'{parent.axislist[z]}'"tmc").setCurrentText(h) ,getattr(parent, f'{parent.axislist[z]}'"cursense").setText(i) , getattr(parent, f'{parent.axislist[z]}'"microstep").setText(j) ,getattr(parent, f'{parent.axislist[z]}'"stealthcop").setCurrentText(k),getattr(parent, f'{parent.axislist[z]}'"rxpin").setText(l)
			if a == "True": getattr(parent, f'{parent.axislist[z]}').setChecked(1)
			else: getattr(parent, f'{parent.axislist[z]}').setChecked(0) 
	#output line 7-14
		for z in range(8):
			a, b, c, d, e, f = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.outlist[z]}'"txt").setText(b),getattr(parent, f'{parent.outlist[z]}'"pin").setText(c),getattr(parent, f'{parent.outlist[z]}'"state").setCurrentText(d)
			if a == "True": getattr(parent, f'{parent.outlist[z]}'"chk").setChecked(1)
			else: getattr(parent, f'{parent.outlist[z]}'"chk").setChecked(0)
			if e == "True": getattr(parent, f'{parent.outlist[z]}'"inv").setChecked(1)
			else: getattr(parent, f'{parent.outlist[z]}'"inv").setChecked(0)	
	#input line 14-21
		for z in range(8):
			a, b, c, d, e, f = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.inlist[z]}'"txt").setText(b),getattr(parent, f'{parent.inlist[z]}'"pin").setText(c),getattr(parent, f'{parent.inlist[z]}'"state").setCurrentText(d)
			if a == "True": getattr(parent, f'{parent.inlist[z]}'"chk").setChecked(1)
			else: getattr(parent, f'{parent.inlist[z]}'"chk").setChecked(0)
			if e == "True": getattr(parent, f'{parent.inlist[z]}'"inv").setChecked(1)
			else: getattr(parent, f'{parent.inlist[z]}'"inv").setChecked(0)	 
	#E stop line 22
		a, b, c, d = map(str,infile.readline().split("|"))
		parent.estoptxt.setText(b),parent.estoppin.setText(c)
		if a == "True": parent.estop.setChecked(1)
		else: parent.estop.setChecked(0)
	#reset line 23
		a, b, c, d = map(str,infile.readline().split("|"))
		parent.resettxt.setText(b),parent.resetpin.setText(c)
		if a == "True": parent.reset.setChecked(1)
		else: parent.reset.setChecked(0) 
	#PWM line 24-31
		for z in range(7):
			a, b, c, d, e, f, g, h, i, j = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.pwmlist[z]}'"txt").setText(b),getattr(parent, f'{parent.pwmlist[z]}'"max").setText(c),getattr(parent, f'{parent.pwmlist[z]}'"pin").setText(d),getattr(parent, f'{parent.pwmlist[z]}'"freq").setText(g),getattr(parent, f'{parent.pwmlist[z]}'"period").setText(h)
			if a == "True": getattr(parent, f'{parent.pwmlist[z]}').setChecked(1)
			else: getattr(parent, f'{parent.pwmlist[z]}').setChecked(0)
			if e == "True": getattr(parent, f'{parent.pwmlist[z]}'"hw").setChecked(1)
			else: getattr(parent, f'{parent.pwmlist[z]}'"hw").setChecked(0)
			if f == "True": getattr(parent, f'{parent.pwmlist[z]}'"vf").setChecked(1)
			else: getattr(parent, f'{parent.pwmlist[z]}'"vf").setChecked(0)
	#rc servo line 32
		a, b, c, d, e = map(str,infile.readline().split("|"))
		parent.rcservotxt.setText(b),parent.rcservopin.setText(c)
		if a == "True": parent.rcservo.setChecked(1)
		else: parent.rcservo.setChecked(0)  
	#QEM line 33
		a, b, c, d, e, f, g, h, i = map(str,infile.readline().split("|"))
		parent.qemtxt.setText(b),parent.qempv.setText(c),parent.qeminput.setText(g),parent.qemstate.setCurrentText(h)
		if a == "True": parent.qem.setChecked(1),
		else: parent.qem.setChecked(0)
	#encoder line 34-37
		for z in range(4):
			a, b, c, d, e, f, g, h, i = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.enclist[z]}'"txt").setText(b),getattr(parent, f'{parent.enclist[z]}'"pv").setText(c), getattr(parent, f'{parent.enclist[z]}'"apin").setText(d), getattr(parent, f'{parent.enclist[z]}'"bpin").setText(e), getattr(parent, f'{parent.enclist[z]}'"ipin").setText(f),getattr(parent, f'{parent.enclist[z]}'"input").setText(g),getattr(parent, f'{parent.enclist[z]}'"state").setCurrentText(h)
			if a == "True": getattr(parent, f'{parent.enclist[z]}').setChecked(1),
			else: getattr(parent, f'{parent.enclist[z]}').setChecked(0)
	#temp line 38-41
		for z in range(4):
			a, b, c, d, e, f, g, h = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.templist[z]}'"txt").setText(b),getattr(parent, f'{parent.templist[z]}'"pv").setText(c),getattr(parent, f'{parent.templist[z]}'"pin").setText(d),getattr(parent, f'{parent.templist[z]}'"r").setText(e),getattr(parent, f'{parent.templist[z]}'"t").setText(f),getattr(parent, f'{parent.templist[z]}'"beta").setText(g)
			if a == "True": getattr(parent, f'{parent.templist[z]}').setChecked(1),
			else: getattr(parent, f'{parent.templist[z]}').setChecked(0)
	
	#switch line 42-44
		for z in range(3):
			a, b, c, d, e, f, g = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.swlist[z]}'"txt").setText(b),getattr(parent, f'{parent.swlist[z]}'"pv").setText(c),getattr(parent, f'{parent.swlist[z]}'"pin").setText(d),getattr(parent, f'{parent.swlist[z]}'"sp").setText(e),getattr(parent, f'{parent.swlist[z]}'"mode").setCurrentText(f)
			if a == "True": getattr(parent, f'{parent.swlist[z]}').setChecked(1),
			else: getattr(parent, f'{parent.swlist[z]}').setChecked(0)

#write out data to save file for hmi
def build(parent):	
	with open('save.txt', 'w') as s:
	#boards line 1
		s.write(str(parent.boards.currentText())+'|'+'\n')
	#axis line 2-7
		for i in range(8):
			s.write(str(getattr(parent, f'{parent.axislist[i]}').isChecked())+'|'+ getattr(parent, f'{parent.axislist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.axislist[i]}'"joint").text()+'|'+ getattr(parent, f'{parent.axislist[i]}'"step").text()+'|'+ getattr(parent, f'{parent.axislist[i]}'"dir").text()+'|'+ getattr(parent, f'{parent.axislist[i]}'"enable").text()+'|'+ getattr(parent, f'{parent.axislist[i]}'"cur").text()+'|'+ getattr(parent, f'{parent.axislist[i]}'"tmc").currentText()+'|'+ getattr(parent, f'{parent.axislist[i]}'"cursense").text()+'|'+ getattr(parent, f'{parent.axislist[i]}'"microstep").text()+'|'+ getattr(parent, f'{parent.axislist[i]}'"stealthcop").currentText()+'|'+ getattr(parent, f'{parent.axislist[i]}'"rxpin").text()+'|'+'\n')
	#output line 7-14
		for i in range(8):
			s.write(str(getattr(parent, f'{parent.outlist[i]}'"chk").isChecked())+'|'+ getattr(parent, f'{parent.outlist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.outlist[i]}'"pin").text()+'|'+ getattr(parent, f'{parent.outlist[i]}'"state").currentText()+'|'+ str(getattr(parent, f'{parent.outlist[i]}'"inv").isChecked())+'|'+'\n')
	#input0 line 15-22
		for i in range(8):
			s.write(str(getattr(parent, f'{parent.inlist[i]}'"chk").isChecked())+'|'+ getattr(parent, f'{parent.inlist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.inlist[i]}'"pin").text()+'|'+ getattr(parent, f'{parent.inlist[i]}'"state").currentText()+'|'+ str(getattr(parent, f'{parent.inlist[i]}'"inv").isChecked())+'|'+'\n')
	#reset pin line 23
		s.write(str(parent.estop.isChecked())+'|'+ parent.estoptxt.text()+'|'+parent.estoppin.text()+'|'+'\n')
	#reset pin line 24
		s.write(str(parent.reset.isChecked())+'|'+ parent.resettxt.text()+'|'+parent.resetpin.text()+'|'+'\n')
	#PWM line 25-31
		for i in range(7):
			s.write(str(getattr(parent, f'{parent.pwmlist[i]}').isChecked())+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"max").text()+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"pin").text()+'|'+ str(getattr(parent, f'{parent.pwmlist[i]}'"hw").isChecked())+'|'+ str(getattr(parent, f'{parent.pwmlist[i]}'"vf").isChecked())+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"freq").text()+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"period").text()+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"spi").text()+'|'+'\n')
	#rc Servo line 32
		s.write(str(parent.rcservo.isChecked())+'|'+ parent.rcservotxt.text()+'|'+parent.rcservopin.text()+'|'+parent.rcservospi.text()+'|'+'\n')
	#QEM line 33
		s.write(str(parent.qem.isChecked())+'|'+ parent.qemtxt.text()+'|'+parent.qempv.text()+'|'+parent.qemapin.text()+'|'+parent.qembpin.text()+'|'+parent.qemipin.text()+'|'+parent.qeminput.text()+'|'+str(parent.qemstate.currentText())+'|'+'\n')
	#Encoder line 34-37
		for i in range(4):
			s.write(str(getattr(parent, f'{parent.enclist[i]}').isChecked())+'|'+ getattr(parent, f'{parent.enclist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.enclist[i]}'"pv").text()+'|'+ getattr(parent, f'{parent.enclist[i]}'"apin").text()+'|'+ getattr(parent, f'{parent.enclist[i]}'"bpin").text()+'|'+ getattr(parent, f'{parent.enclist[i]}'"ipin").text()+'|'+ getattr(parent, f'{parent.enclist[i]}'"input").text()+'|'+ str(getattr(parent, f'{parent.enclist[i]}'"state").currentText())+'|'+'\n')
	#temp line 38-41
		for i in range(4):
			s.write(str(getattr(parent, f'{parent.templist[i]}').isChecked())+'|'+ getattr(parent, f'{parent.templist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.templist[i]}'"pv").text()+'|'+ getattr(parent, f'{parent.templist[i]}'"pin").text()+'|'+ getattr(parent, f'{parent.templist[i]}'"r").text()+'|'+ getattr(parent, f'{parent.templist[i]}'"t").text()+'|'+ getattr(parent, f'{parent.templist[i]}'"beta").text()+'|'+'\n')
	#swtich	 line 42-44
		for i in range(3):
			s.write(str(getattr(parent, f'{parent.swlist[i]}').isChecked())+'|'+ getattr(parent, f'{parent.swlist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.swlist[i]}'"pv").text()+'|'+ getattr(parent, f'{parent.swlist[i]}'"pin").text()+'|'+ getattr(parent, f'{parent.swlist[i]}'"sp").text()+'|'+ str(getattr(parent, f'{parent.swlist[i]}'"mode").currentText())+'|'+'\n')
	