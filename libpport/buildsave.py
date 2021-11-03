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
	#axis line 2-9
		for z in range(8):
			a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26 = map(str,infile.readline().split("|"))
			if a1 == "True": getattr(parent, f'{parent.axislist[z]}').setChecked(1)
			getattr(parent, f'{parent.axislist[z]}'"txt").setText(a2)
			getattr(parent, f'{parent.axislist[z]}'"joint").setText(a3)
			getattr(parent, f'{parent.axislist[z]}'"step").setText(a4)
			getattr(parent, f'{parent.axislist[z]}'"dir").setText(a5)
			getattr(parent, f'{parent.axislist[z]}'"enable").setText(a6)
			getattr(parent, f'{parent.axislist[z]}'"cur").setText(a7) 
			getattr(parent, f'{parent.axislist[z]}'"tmc").setCurrentText(a8) 
			getattr(parent, f'{parent.axislist[z]}'"cursense").setText(a9) 
			getattr(parent, f'{parent.axislist[z]}'"microstep").setText(a10)
			getattr(parent, f'{parent.axislist[z]}'"stealthcop").setCurrentText(a11)
			getattr(parent, f'{parent.axislist[z]}'"rxpin").setText(a12)
			f'{getattr(parent, "scale_" + str(z+1)).setText(a13)}'
			f'{getattr(parent, "minLimit_" + str(z+1)).setText(a14)}'
			f'{getattr(parent, "maxLimit_" + str(z+1)).setText(a15)}'
			f'{getattr(parent, "maxVelocity_" + str(z+1)).setText(a16)}'
			f'{getattr(parent, "maxAccel_" + str(z+1)).setText(a17)}'
			f'{getattr(parent, "home_" + str(z+1)).setText(a18)}'
			f'{getattr(parent, "homeOffset_" + str(z+1)).setText(a19)}'
			f'{getattr(parent, "homeSearchVel_" + str(z+1)).setText(a20)}'
			f'{getattr(parent, "homeLatchVel_" + str(z+1)).setText(a21)}'
			f'{getattr(parent, "homeSequence_" + str(z+1)).setText(a22)}'
			if a23 == "True": f'{getattr(parent, "reverse_" + str(z+1)).setChecked(1)}'
			if a24 == "True": f'{getattr(parent, "homeUseIndex_" + str(z+1)).setChecked(1)}'
			if a25 == "True": f'{getattr(parent, "homeIgnoreLimits_" + str(z+1)).setChecked(1)}'

	#output line 10-17
		for z in range(8):
			a, b, c, d, e, f = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.outlist[z]}'"txt").setText(b),getattr(parent, f'{parent.outlist[z]}'"pin").setText(c),getattr(parent, f'{parent.outlist[z]}'"state").setCurrentText(d)
			if a == "True": getattr(parent, f'{parent.outlist[z]}'"chk").setChecked(1)
			else: getattr(parent, f'{parent.outlist[z]}'"chk").setChecked(0)
			if e == "True": getattr(parent, f'{parent.outlist[z]}'"inv").setChecked(1)
			else: getattr(parent, f'{parent.outlist[z]}'"inv").setChecked(0)	
	#input line 18-25
		for z in range(8):
			a, b, c, d, e, f = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.inlist[z]}'"txt").setText(b),getattr(parent, f'{parent.inlist[z]}'"pin").setText(c),getattr(parent, f'{parent.inlist[z]}'"state").setCurrentText(d)
			if a == "True": getattr(parent, f'{parent.inlist[z]}'"chk").setChecked(1)
			else: getattr(parent, f'{parent.inlist[z]}'"chk").setChecked(0)
			if e == "True": getattr(parent, f'{parent.inlist[z]}'"inv").setChecked(1)
			else: getattr(parent, f'{parent.inlist[z]}'"inv").setChecked(0)	 
	#E stop line 26
		a, b, c, d = map(str,infile.readline().split("|"))
		parent.estoptxt.setText(b),parent.estoppin.setText(c)
		if a == "True": parent.estop.setChecked(1)
		else: parent.estop.setChecked(0)
	#reset line 27
		a, b, c, d = map(str,infile.readline().split("|"))
		parent.resettxt.setText(b),parent.resetpin.setText(c)
		if a == "True": parent.reset.setChecked(1)
		else: parent.reset.setChecked(0) 
	#PWM line 28-34
		for z in range(7):
			a, b, c, d, e, f, g, h, i, j = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.pwmlist[z]}'"txt").setText(b),getattr(parent, f'{parent.pwmlist[z]}'"max").setText(c),getattr(parent, f'{parent.pwmlist[z]}'"pin").setText(d),getattr(parent, f'{parent.pwmlist[z]}'"freq").setText(g),getattr(parent, f'{parent.pwmlist[z]}'"period").setText(h)
			if a == "True": getattr(parent, f'{parent.pwmlist[z]}').setChecked(1)
			else: getattr(parent, f'{parent.pwmlist[z]}').setChecked(0)
			if e == "True": getattr(parent, f'{parent.pwmlist[z]}'"hw").setChecked(1)
			else: getattr(parent, f'{parent.pwmlist[z]}'"hw").setChecked(0)
			if f == "True": getattr(parent, f'{parent.pwmlist[z]}'"vf").setChecked(1)
			else: getattr(parent, f'{parent.pwmlist[z]}'"vf").setChecked(0)
	#rc servo line 35
		a, b, c, d, e = map(str,infile.readline().split("|"))
		parent.rcservotxt.setText(b),parent.rcservopin.setText(c)
		if a == "True": parent.rcservo.setChecked(1)
		else: parent.rcservo.setChecked(0)  
	#QEM line 36
		a, b, c, d, e, f, g, h, i = map(str,infile.readline().split("|"))
		parent.qemtxt.setText(b),parent.qempv.setText(c),parent.qeminput.setText(g),parent.qemstate.setCurrentText(h)
		if a == "True": parent.qem.setChecked(1),
		else: parent.qem.setChecked(0)
	#encoder line 37-40
		for z in range(4):
			a, b, c, d, e, f, g, h, i = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.enclist[z]}'"txt").setText(b),getattr(parent, f'{parent.enclist[z]}'"pv").setText(c), getattr(parent, f'{parent.enclist[z]}'"apin").setText(d), getattr(parent, f'{parent.enclist[z]}'"bpin").setText(e), getattr(parent, f'{parent.enclist[z]}'"ipin").setText(f),getattr(parent, f'{parent.enclist[z]}'"input").setText(g),getattr(parent, f'{parent.enclist[z]}'"state").setCurrentText(h)
			if a == "True": getattr(parent, f'{parent.enclist[z]}').setChecked(1),
			else: getattr(parent, f'{parent.enclist[z]}').setChecked(0)
	#temp line 41-44
		for z in range(4):
			a, b, c, d, e, f, g, h = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.templist[z]}'"txt").setText(b),getattr(parent, f'{parent.templist[z]}'"pv").setText(c),getattr(parent, f'{parent.templist[z]}'"pin").setText(d),getattr(parent, f'{parent.templist[z]}'"r").setText(e),getattr(parent, f'{parent.templist[z]}'"t").setText(f),getattr(parent, f'{parent.templist[z]}'"beta").setText(g)
			if a == "True": getattr(parent, f'{parent.templist[z]}').setChecked(1),
			else: getattr(parent, f'{parent.templist[z]}').setChecked(0)
	
	#switch line 45-47
		for z in range(3):
			a, b, c, d, e, f, g = map(str,infile.readline().split("|"))
			getattr(parent, f'{parent.swlist[z]}'"txt").setText(b),getattr(parent, f'{parent.swlist[z]}'"pv").setText(c),getattr(parent, f'{parent.swlist[z]}'"pin").setText(d),getattr(parent, f'{parent.swlist[z]}'"sp").setText(e),getattr(parent, f'{parent.swlist[z]}'"mode").setCurrentText(f)
			if a == "True": getattr(parent, f'{parent.swlist[z]}').setChecked(1),
			else: getattr(parent, f'{parent.swlist[z]}').setChecked(0)

	#machine UI and options 48
		a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25 = map(str,infile.readline().split("|"))
		f'{getattr(parent, "configName").setText(a1)}'
		f'{getattr(parent, "linearUnitsCB" ).setCurrentText(a2)}'
		f'{getattr(parent, "maxLinearVel" ).setText(a3)}'
		f'{getattr(parent, "guiCB" ).setCurrentText(a4)}'
		f'{getattr(parent, "positionOffsetCB" ).setCurrentText(a5)}'
		f'{getattr(parent, "positionFeedbackCB" ).setCurrentText(a6)}'
		b7 = float(a7)
		getattr(parent, "maxFeedOverrideSB" ).setValue(b7)
		f'{getattr(parent, "editorCB" ).setCurrentText(a8)}'
		f'{getattr(parent, "debugCB" ).setCurrentText(a9)}'
		if a10 == "True": getattr(parent, "backupCB" ).setChecked(1)
		if a11 == "True": getattr(parent, "pyvcpCB" ).setChecked(1)
		if a12 == "True": getattr(parent, "manualToolChangeCB" ).setChecked(1)
		if a13 == "True": getattr(parent, "millRB" ).setChecked(1)
		if a14 == "True": getattr(parent, "frontToolLatheRB" ).setChecked(1)
		if a15 == "True": getattr(parent, "backToolLatheRB" ).setChecked(1)
		f'{getattr(parent, "startUpFileLE" ).setText(a16)}'
		if a17 == "True": getattr(parent, "customhalCB" ).setChecked(1)
		if a18 == "True": getattr(parent, "postguiCB" ).setChecked(1)
		if a19 == "True": getattr(parent, "shutdownCB" ).setChecked(1)
		b20 = float(a20)
		getattr(parent, "servoPeriodSB" ).setValue(b20)
		b21 = float(a21)
		getattr(parent, "basePeriodSB" ).setValue(b21)
		b22 = float(a22)
		getattr(parent, "defaultJogSpeedDSB" ).setValue(b22)
		f'{getattr(parent, "introGraphicLE" ).setText(a23)}'
		b24 = float(a24)
		getattr(parent, "introGraphicSB" ).setValue(b24)
	#spindle 49
		a1, a2, a3 = map(str,infile.readline().split("|"))
		f'{getattr(parent, "spindleMinRpm").setText(a1)}'
		f'{getattr(parent, "spindleMaxRpm").setText(a2)}'



#write out data to save file for hmi
def build(parent):	
	with open('save.txt', 'w') as s:
	#boards line 1
		s.write(str(parent.boards.currentText())+'|'+'\n')
	#axis line 2-9
		for i in range(8):
			s.write(str(getattr(parent, f'{parent.axislist[i]}').isChecked())+'|')
			s.write(getattr(parent, f'{parent.axislist[i]}'"txt").text()+'|')
			s.write(getattr(parent, f'{parent.axislist[i]}'"joint").text()+'|')
			s.write(getattr(parent, f'{parent.axislist[i]}'"step").text()+'|')
			s.write(getattr(parent, f'{parent.axislist[i]}'"dir").text()+'|')
			s.write(getattr(parent, f'{parent.axislist[i]}'"enable").text()+'|')
			s.write(getattr(parent, f'{parent.axislist[i]}'"cur").text()+'|')
			s.write(getattr(parent, f'{parent.axislist[i]}'"tmc").currentText()+'|')
			s.write(getattr(parent, f'{parent.axislist[i]}'"cursense").text()+'|')
			s.write(getattr(parent, f'{parent.axislist[i]}'"microstep").text()+'|')
			s.write(getattr(parent, f'{parent.axislist[i]}'"stealthcop").currentText()+'|')
			s.write(getattr(parent, f'{parent.axislist[i]}'"rxpin").text()+'|')
			s.write(f'{getattr(parent, "scale_" + str(i+1)).text()}' +'|')
			s.write(f'{getattr(parent, "minLimit_" + str(i+1)).text()}' +'|')
			s.write(f'{getattr(parent, "maxLimit_" + str(i+1)).text()}' +'|')
			s.write(f'{getattr(parent, "maxVelocity_" + str(i+1)).text()}' +'|')
			s.write(f'{getattr(parent, "maxAccel_" + str(i+1)).text()}' +'|')
			s.write(f'{getattr(parent, "home_" + str(i+1)).text()}' +'|')
			s.write(f'{getattr(parent, "homeOffset_" + str(i+1)).text()}' +'|')
			s.write(f'{getattr(parent, "homeSearchVel_" + str(i+1)).text()}' +'|')
			s.write(f'{getattr(parent, "homeLatchVel_" + str(i+1)).text()}' +'|')
			s.write(f'{getattr(parent, "homeSequence_" + str(i+1)).text()}' +'|')
			s.write(f'{getattr(parent, "reverse_" + str(i+1)).isChecked()}' +'|')
			s.write(f'{getattr(parent, "homeUseIndex_" + str(i+1)).isChecked()}' +'|')
			s.write(f'{getattr(parent, "homeIgnoreLimits_" + str(i+1)).isChecked()}' +'|')
			s.write('\n')
	#output line 10-17
		for i in range(8):
			s.write(str(getattr(parent, f'{parent.outlist[i]}'"chk").isChecked())+'|'+ getattr(parent, f'{parent.outlist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.outlist[i]}'"pin").text()+'|'+ getattr(parent, f'{parent.outlist[i]}'"state").currentText()+'|'+ str(getattr(parent, f'{parent.outlist[i]}'"inv").isChecked())+'|'+'\n')
	#input0 line 18-25
		for i in range(8):
			s.write(str(getattr(parent, f'{parent.inlist[i]}'"chk").isChecked())+'|'+ getattr(parent, f'{parent.inlist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.inlist[i]}'"pin").text()+'|'+ getattr(parent, f'{parent.inlist[i]}'"state").currentText()+'|'+ str(getattr(parent, f'{parent.inlist[i]}'"inv").isChecked())+'|'+'\n')
	#E stop line 26
		s.write(str(parent.estop.isChecked())+'|'+ parent.estoptxt.text()+'|'+parent.estoppin.text()+'|'+'\n')
	#reset pin line 27
		s.write(str(parent.reset.isChecked())+'|'+ parent.resettxt.text()+'|'+parent.resetpin.text()+'|'+'\n')
	#PWM line 28-34
		for i in range(7):
			s.write(str(getattr(parent, f'{parent.pwmlist[i]}').isChecked())+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"max").text()+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"pin").text()+'|'+ str(getattr(parent, f'{parent.pwmlist[i]}'"hw").isChecked())+'|'+ str(getattr(parent, f'{parent.pwmlist[i]}'"vf").isChecked())+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"freq").text()+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"period").text()+'|'+ getattr(parent, f'{parent.pwmlist[i]}'"spi").text()+'|'+'\n')
	#rc Servo line 35
		s.write(str(parent.rcservo.isChecked())+'|'+ parent.rcservotxt.text()+'|'+parent.rcservopin.text()+'|'+parent.rcservospi.text()+'|'+'\n')
	#QEM line 36
		s.write(str(parent.qem.isChecked())+'|'+ parent.qemtxt.text()+'|'+parent.qempv.text()+'|'+parent.qemapin.text()+'|'+parent.qembpin.text()+'|'+parent.qemipin.text()+'|'+parent.qeminput.text()+'|'+str(parent.qemstate.currentText())+'|'+'\n')
	#Encoder line 37-40
		for i in range(4):
			s.write(str(getattr(parent, f'{parent.enclist[i]}').isChecked())+'|'+ getattr(parent, f'{parent.enclist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.enclist[i]}'"pv").text()+'|'+ getattr(parent, f'{parent.enclist[i]}'"apin").text()+'|'+ getattr(parent, f'{parent.enclist[i]}'"bpin").text()+'|'+ getattr(parent, f'{parent.enclist[i]}'"ipin").text()+'|'+ getattr(parent, f'{parent.enclist[i]}'"input").text()+'|'+ str(getattr(parent, f'{parent.enclist[i]}'"state").currentText())+'|'+'\n')
	#temp line 41-44
		for i in range(4):
			s.write(str(getattr(parent, f'{parent.templist[i]}').isChecked())+'|'+ getattr(parent, f'{parent.templist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.templist[i]}'"pv").text()+'|'+ getattr(parent, f'{parent.templist[i]}'"pin").text()+'|'+ getattr(parent, f'{parent.templist[i]}'"r").text()+'|'+ getattr(parent, f'{parent.templist[i]}'"t").text()+'|'+ getattr(parent, f'{parent.templist[i]}'"beta").text()+'|'+'\n')
	#swtich	 line 45-47
		for i in range(3):
			s.write(str(getattr(parent, f'{parent.swlist[i]}').isChecked())+'|'+ getattr(parent, f'{parent.swlist[i]}'"txt").text()+'|'+ getattr(parent, f'{parent.swlist[i]}'"pv").text()+'|'+ getattr(parent, f'{parent.swlist[i]}'"pin").text()+'|'+ getattr(parent, f'{parent.swlist[i]}'"sp").text()+'|'+ str(getattr(parent, f'{parent.swlist[i]}'"mode").currentText())+'|'+'\n')
	#machine UI and options 48
		s.write(f'{getattr(parent, "configName").text()}' +'|')
		s.write(f'{getattr(parent, "linearUnitsCB" ).currentText()}' +'|')
		s.write(f'{getattr(parent, "maxLinearVel" ).text()}' +'|')
		s.write(f'{getattr(parent, "guiCB" ).currentText()}' +'|')
		s.write(f'{getattr(parent, "positionOffsetCB" ).currentText()}' +'|')
		s.write(f'{getattr(parent, "positionFeedbackCB" ).currentText()}' +'|')
		s.write(f'{getattr(parent, "maxFeedOverrideSB" ).text()}' +'|')
		s.write(f'{getattr(parent, "editorCB" ).currentText()}' +'|')
		s.write(f'{getattr(parent, "debugCB" ).currentText()}' +'|')
		s.write(f'{getattr(parent, "backupCB" ).isChecked()}' +'|')
		s.write(f'{getattr(parent, "pyvcpCB" ).isChecked()}' +'|')
		s.write(f'{getattr(parent, "manualToolChangeCB" ).isChecked()}' +'|')
		s.write(f'{getattr(parent, "millRB" ).isChecked()}' +'|')
		s.write(f'{getattr(parent, "frontToolLatheRB" ).isChecked()}' +'|')
		s.write(f'{getattr(parent, "backToolLatheRB" ).isChecked()}' +'|')
		s.write(f'{getattr(parent, "startUpFileLE" ).text()}' +'|')
		s.write(f'{getattr(parent, "customhalCB" ).isChecked()}' +'|')
		s.write(f'{getattr(parent, "postguiCB" ).isChecked()}' +'|')
		s.write(f'{getattr(parent, "shutdownCB" ).isChecked()}' +'|')
		s.write(f'{getattr(parent, "servoPeriodSB" ).value()}' +'|')
		s.write(f'{getattr(parent, "basePeriodSB" ).value()}' +'|')
		s.write(f'{getattr(parent, "defaultJogSpeedDSB" ).value()}' +'|')
		s.write(f'{getattr(parent, "introGraphicLE" ).text()}' +'|')
		s.write(f'{getattr(parent, "introGraphicSB" ).value()}' +'|')
		s.write('\n')
	#spindle 49
		s.write(f'{getattr(parent, "spindleMinRpm").text()}' +'|')
		s.write(f'{getattr(parent, "spindleMaxRpm").text()}' +'|')
		s.write('\n')
	