from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QInputDialog, QFileDialog
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('remoreconfig.ui', self)

    #Setup actions
        self.save.clicked.connect(self.saveButtonPressed)
        self.load.clicked.connect(self.loadButtonPressed)
        self.boards.activated.connect(self.loadboards)
        self.xaxistmc.activated.connect(self.xtmc) 
        self.yaxistmc.activated.connect(self.ytmc) 
        self.zaxistmc.activated.connect(self.ztmc) 
        self.e0axistmc.activated.connect(self.e0tmc)
        self.e1axistmc.activated.connect(self.e1tmc)

    #Lists
        self.axislist = ['xaxis', 'yaxis', 'zaxis', 'e0axis', 'e1axis']
        self.outlist = ['out0', 'out1', 'out2', 'out3', 'out4', 'out5', 'out6', 'out7']
        self.inlist = ['in0', 'in1', 'in2', 'in3', 'in4', 'in5', 'in6', 'in7']
        self.pwmlist = ['pwm0', 'pwm1', 'pwm2', 'pwm3', 'pwm4', 'pwm5', 'pwm6']
        self.enclist = ['enc0', 'enc1', 'enc2', 'enc3']
        self.templist = ['temp0', 'temp1', 'temp2', 'temp3']
        self.swlist = ['sw0', 'sw1', 'sw2']

        self.show()
        
    #hide elements not needed on startup
        for z in range(5):
            getattr(self, f'{self.axislist[z]}'"cur").setEnabled(0)
            getattr(self, f'{self.axislist[z]}'"cur").setVisible(0)
            getattr(self, f'{self.axislist[z]}'"cursense").setEnabled(0)
            getattr(self, f'{self.axislist[z]}'"cursense").setVisible(0)
            getattr(self, f'{self.axislist[z]}'"microstep").setEnabled(0)
            getattr(self, f'{self.axislist[z]}'"microstep").setVisible(0)
            getattr(self, f'{self.axislist[z]}'"stealthcop").setEnabled(0)
            getattr(self, f'{self.axislist[z]}'"stealthcop").setVisible(0)

#Import save data or pre configs into hmi        
    def loadButtonPressed(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        with open(fileName,"r") as infile:
        #boards line 1
            a, b = map(str,infile.readline().split("|"))
            self.boards.setCurrentText(str(a))
        #axis line 2-6
            for z in range(5):
                a, b, c, d, e, f, g, h, i, j, k, l = map(str,infile.readline().split("|"))
                getattr(self, f'{self.axislist[z]}'"txt").setText(b),getattr(self, f'{self.axislist[z]}'"joint").setText(c),getattr(self, f'{self.axislist[z]}'"step").setText(d),getattr(self, f'{self.axislist[z]}'"dir").setText(e),getattr(self, f'{self.axislist[z]}'"enable").setText(f),getattr(self, f'{self.axislist[z]}'"cur").setText(g) ,getattr(self, f'{self.axislist[z]}'"tmc").setCurrentText(h) ,getattr(self, f'{self.axislist[z]}'"cursense").setText(i) , getattr(self, f'{self.axislist[z]}'"microstep").setText(j) ,getattr(self, f'{self.axislist[z]}'"stealthcop").setCurrentText(k)
                if a == "True": getattr(self, f'{self.axislist[z]}').setChecked(1)
                else: getattr(self, f'{self.axislist[z]}').setChecked(0) 
        #output line 7-14
            for z in range(8):
                a, b, c, d, e, f = map(str,infile.readline().split("|"))
                getattr(self, f'{self.outlist[z]}'"txt").setText(b),getattr(self, f'{self.outlist[z]}'"pin").setText(c),getattr(self, f'{self.outlist[z]}'"state").setCurrentText(d)
                if a == "True": getattr(self, f'{self.outlist[z]}'"chk").setChecked(1)
                else: getattr(self, f'{self.outlist[z]}'"chk").setChecked(0)
                if e == "True": getattr(self, f'{self.outlist[z]}'"inv").setChecked(1)
                else: getattr(self, f'{self.outlist[z]}'"inv").setChecked(0)    
        #input line 14-21
            for z in range(8):
                a, b, c, d, e, f = map(str,infile.readline().split("|"))
                getattr(self, f'{self.inlist[z]}'"txt").setText(b),getattr(self, f'{self.inlist[z]}'"pin").setText(c),getattr(self, f'{self.inlist[z]}'"state").setCurrentText(d)
                if a == "True": getattr(self, f'{self.inlist[z]}'"chk").setChecked(1)
                else: getattr(self, f'{self.inlist[z]}'"chk").setChecked(0)
                if e == "True": getattr(self, f'{self.inlist[z]}'"inv").setChecked(1)
                else: getattr(self, f'{self.inlist[z]}'"inv").setChecked(0)  
        #E stop line 22
            a, b, c, d = map(str,infile.readline().split("|"))
            self.estoptxt.setText(b),self.estoppin.setText(c)
            if a == "True": self.estop.setChecked(1)
            else: self.estop.setChecked(0)
        #reset line 23
            a, b, c, d = map(str,infile.readline().split("|"))
            self.resettxt.setText(b),self.resetpin.setText(c)
            if a == "True": self.reset.setChecked(1)
            else: self.reset.setChecked(0) 
        #PWM line 24-31
            for z in range(7):
                a, b, c, d, e, f, g, h, i, j = map(str,infile.readline().split("|"))
                getattr(self, f'{self.pwmlist[z]}'"txt").setText(b),getattr(self, f'{self.pwmlist[z]}'"max").setText(c),getattr(self, f'{self.pwmlist[z]}'"pin").setText(d),getattr(self, f'{self.pwmlist[z]}'"freq").setText(g),getattr(self, f'{self.pwmlist[z]}'"period").setText(h)
                if a == "True": getattr(self, f'{self.pwmlist[z]}').setChecked(1)
                else: getattr(self, f'{self.pwmlist[z]}').setChecked(0)
                if e == "True": getattr(self, f'{self.pwmlist[z]}'"hw").setChecked(1)
                else: getattr(self, f'{self.pwmlist[z]}'"hw").setChecked(0)
                if f == "True": getattr(self, f'{self.pwmlist[z]}'"vf").setChecked(1)
                else: getattr(self, f'{self.pwmlist[z]}'"vf").setChecked(0)
        #rc servo line 32
            a, b, c, d, e = map(str,infile.readline().split("|"))
            self.rcservotxt.setText(b),self.rcservopin.setText(c)
            if a == "True": self.rcservo.setChecked(1)
            else: self.rcservo.setChecked(0)  
        #QEM line 33
            a, b, c, d, e, f, g, h, i = map(str,infile.readline().split("|"))
            self.qemtxt.setText(b),self.qempv.setText(c),self.qeminput.setText(g),self.qemstate.setCurrentText(h)
            if a == "True": self.qem.setChecked(1),
            else: self.qem.setChecked(0)
        #encoder line 34-37
            for z in range(4):
                a, b, c, d, e, f, g, h, i = map(str,infile.readline().split("|"))
                getattr(self, f'{self.enclist[z]}'"txt").setText(b),getattr(self, f'{self.enclist[z]}'"pv").setText(c), getattr(self, f'{self.enclist[z]}'"apin").setText(d), getattr(self, f'{self.enclist[z]}'"bpin").setText(e), getattr(self, f'{self.enclist[z]}'"ipin").setText(f),getattr(self, f'{self.enclist[z]}'"input").setText(g),getattr(self, f'{self.enclist[z]}'"state").setCurrentText(h)
                if a == "True": getattr(self, f'{self.enclist[z]}').setChecked(1),
                else: getattr(self, f'{self.enclist[z]}').setChecked(0)
        #temp line 38-41
            for z in range(4):
                a, b, c, d, e, f, g, h = map(str,infile.readline().split("|"))
                getattr(self, f'{self.templist[z]}'"txt").setText(b),getattr(self, f'{self.templist[z]}'"pv").setText(c),getattr(self, f'{self.templist[z]}'"pin").setText(d),getattr(self, f'{self.templist[z]}'"r").setText(e),getattr(self, f'{self.templist[z]}'"t").setText(f),getattr(self, f'{self.templist[z]}'"beta").setText(g)
                if a == "True": getattr(self, f'{self.templist[z]}').setChecked(1),
                else: getattr(self, f'{self.templist[z]}').setChecked(0)
        
        #switch line 42-44
            for z in range(3):
                a, b, c, d, e, f, g = map(str,infile.readline().split("|"))
                getattr(self, f'{self.swlist[z]}'"txt").setText(b),getattr(self, f'{self.swlist[z]}'"pv").setText(c),getattr(self, f'{self.swlist[z]}'"pin").setText(d),getattr(self, f'{self.swlist[z]}'"sp").setText(e),getattr(self, f'{self.swlist[z]}'"mode").setCurrentText(f)
                if a == "True": getattr(self, f'{self.swlist[z]}').setChecked(1),
                else: getattr(self, f'{self.swlist[z]}').setChecked(0)

# Write data out to the config file for the board        
    def saveButtonPressed(self):
        with open('config.txt', 'w') as f:
            f.write('{'+'\n')
        #Boards
            if self.boards.currentText() == "MKS SBASE v1.3":
                f.write('\t'+'"Board": "'+ self.boards.currentText() + '",' +'\n'+'\t'+'"Modules":['+'\n'+'\t'+'{'+'\n'+'\t'+'"Thread": "On load",'+'\n'+'\t'+'"Type": "MCP4451",'+'\n'+'\t'+'"Comment": "Digipot for joints/Axis 0 - 3",'+'\n'+'\t'+'\t'+'"I2C SDA pin":'+'\t'+'\t'+'"0.0",'+'\n'+'\t'+'\t'+'"I2C SCL pin":'+'\t'+'\t'+'"0.1",'+'\n'+'\t'+'\t'+'"I2C address":'+'\t'+'\t'+'0,'+'\n'+'\t'+'\t'+'"Max current":'+'\t'+'\t'+'2.0,'+'\n'+'\t'+'\t'+'"Factor":'+'\t'+'\t'+'\t'+'113.33,'+'\n'+'\t'+'\t'+'"Current 0":'+'\t'+'\t'+self.xaxiscur.text()+','+'\n'+'\t'+'\t'+'"Current 1":'+'\t'+'\t'+self.yaxiscur.text()+','+'\n'+'\t'+'\t'+'"Current 2":'+'\t'+'\t'+self.zaxiscur.text()+','+'\n'+'\t'+'\t'+'"Current 3":'+'\t'+'\t'+self.e0axiscur.text()+'\n'+'\t'+'},'+'\n'+'\t'+'{'+'\n'+'\t'+'"Thread": "On load",'+'\n'+'\t'+'"Type": "MCP4451",'+'\n'+'\t'+'"Comment": "Digipot for joints/Axis 4 - 7",'+'\n'+'\t'+'\t'+'"I2C SDA pin":'+'\t'+'\t'+'"0.0",'+'\n'+'\t'+'\t'+'"I2C SCL pin":'+'\t'+'\t'+'"0.1",'+'\n'+'\t'+'\t'+'"I2C address":'+'\t'+'\t'+'2,'+'\n'+'\t'+'\t'+'"Max current":'+'\t'+'\t'+'2.0,'+'\n'+'\t'+'\t'+'"Factor":'+'\t'+'\t'+'\t'+'113.33,'+'\n'+'\t'+'\t'+'"Current 0":'+'\t'+'\t'+self.e1axiscur.text()+','+'\n'+'\t'+'\t'+'"Current 1":'+'\t'+'\t'+'0.0'+','+'\n'+'\t'+'\t'+'"Current 2":'+'\t'+'\t'+'0.0'+','+'\n'+'\t'+'\t'+'"Current 3":'+'\t'+'\t'+'0.0'+'\n'+'\t'+'},'+'\n')
            else:
                f.write('\t'+'"Board": "'+ self.boards.currentText() + '",' +'\n'+'\t'+'"Modules":['+'\n')
        #E-stop
            if self.estop.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "eStop",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.estoptxt.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.estoppin.text()+'"'+'\n'+'\t'+'},'+'\n')
        #axis
            for i in range(5):
                if getattr(self, f'{self.axislist[i]}').isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(self, f'{self.axislist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+ getattr(self, f'{self.axislist[i]}'"joint").text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + getattr(self, f'{self.axislist[i]}'"step").text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t' +'"' + getattr(self, f'{self.axislist[i]}'"dir").text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t' +'"' + getattr(self, f'{self.axislist[i]}'"enable").text()+'"' +'\n'+'\t'+'},'+'\n')
        #TMC
            for i in range(5):
                if getattr(self, f'{self.axislist[i]}').isChecked() == 1:
                    if str(getattr(self, f'{self.axislist[i]}'"tmc").currentText()) != "None": f.write('\t'+'{'+'\n'+'\t'+'"Thread": "On Load",'+'\n'+'\t'+'"Type": "' + getattr(self, f'{self.axislist[i]}'"tmc").currentText() + '",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(self, f'{self.axislist[i]}'"txt").text() + ' TMC Driver",' +'\n'+'\t'+'\t'+'"RX pin":'+'\t'+'\t'+'\t'+ "1.10" +','+'\n'+'\t'+'\t'+'"RSense":'+'\t'+'\t'+'\t' +'"' + getattr(self, f'{self.axislist[i]}'"cursense").text()+'",'+'\n'+'\t'+'\t'+'"Current":'+'\t'+'\t'+'\t' +'"' + getattr(self, f'{self.axislist[i]}'"cur").text()+'",' +'\n'+'\t'+'\t'+'"Microsteps":'+'\t'+'\t' +'"' + getattr(self, f'{self.axislist[i]}'"microstep").text()+'",' +'\n'+'\t'+'\t'+'"Stealth chop":'+'\t'+'\t' +'"' + getattr(self, f'{self.axislist[i]}'"stealthcop").currentText()+'"' +'\n'+'\t'+'},'+'\n')
        #output 
            for i in range(8):
                    if getattr(self, f'{self.outlist[i]}'"chk").isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(self, f'{self.outlist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + getattr(self, f'{self.outlist[i]}'"pin").text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Output",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ getattr(self, f'{self.outlist[i]}'"state").currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(getattr(self, f'{self.outlist[i]}'"inv").isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +f'{i}'+'\n'+'\t'+'},'+'\n')
        #input
            for i in range(8):
                    if getattr(self, f'{self.inlist[i]}'"chk").isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(self, f'{self.inlist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + getattr(self, f'{self.inlist[i]}'"pin").text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Input",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ getattr(self, f'{self.inlist[i]}'"state").currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(getattr(self, f'{self.inlist[i]}'"inv").isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +f'{i}'+'\n'+'\t'+'},'+'\n')
        #PWM
            for i in range(7):
                    if getattr(self, f'{self.pwmlist[i]}').isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "PWM",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(self, f'{self.pwmlist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t'+ getattr(self, f'{self.pwmlist[i]}'"spi").text()+','+'\n'+'\t'+'\t'+'"PWM Pin":'+'\t'+'\t'+'\t' +'"' + getattr(self, f'{self.pwmlist[i]}'"pin").text()+'",'+'\n'+'\t'+'\t'+'"PWM Max":'+'\t'+'\t'+'\t' + getattr(self, f'{self.pwmlist[i]}'"max").text()+',' +'\n'+'\t'+'\t'+'"Hardware PWM":'+'\t'+'\t' +'"' +  str(getattr(self, f'{self.pwmlist[i]}'"hw").isChecked())+'",'+'\n'+'\t'+'\t'+'"Variable Freq":'+'\t' +'"' +  str(getattr(self, f'{self.pwmlist[i]}'"vf").isChecked())+'",'+'\n'+'\t'+'\t'+'"Perioid SP[i]":'+'\t' + getattr(self, f'{self.pwmlist[i]}'"period").text()+',' +'\n'+'\t'+'\t'+'"Perioid US":'+'\t'+'\t' + getattr(self, f'{self.pwmlist[i]}'"freq").text() +'\n'+'\t'+'},'+'\n')
        #Rc Servo
            if self.rcservo.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "RCServo",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.rcservotxt.text() + '",' +'\n'+'\t'+'\t'+'"Servo Pin":'+'\t'+'\t'+ '"' + self.rcservopin.text()+'",'+'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t' + self.rcservospi.text()+'\n'+'\t'+'},'+'\n')
        #QEM
            if self.qem.isChecked() == 1: 
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "QEI",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ self.qemtxt.text() + '",' +'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.qemstate.currentText()+ '",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ self.qempv.text())
                if self.qeminput.text() == "":
                    f.write('\n'+'\t'+'},'+'\n')
                else:
                    f.write(','+'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' + self.qeminput.text()+','+'\n'+'\t'+'\t'+'"Enable Index":'+'\t'+'\t' +'"True"' +'\n'+'\t'+'},'+'\n')
        #Encoder 
            for i in range(4):
                    if getattr(self, f'{self.enclist[i]}').isChecked() == 1:
                        f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "Encoder",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ getattr(self, f'{self.enclist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"ChA Pin":' +'\t'+'\t'+'\t'+'"'+ getattr(self, f'{self.enclist[i]}'"apin").text() + '",' +'\n'+'\t'+'\t'+'"ChB Pin":' +'\t'+'\t'+'\t'+'"'+ getattr(self, f'{self.enclist[i]}'"bpin").text() + '",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+  str(getattr(self, f'{self.enclist[i]}'"state").currentText())+ '",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ getattr(self, f'{self.enclist[i]}'"pv").text())
                        if getattr(self, f'{self.enclist[i]}'"input").text() == "":  f.write('\n'+'\t'+'},'+'\n')
                        else: f.write(','+'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' + getattr(self, f'{self.enclist[i]}'"input").text()+','+'\n'+'\t'+'\t'+'"Index Pin":'+'\t'+'\t'+'"' + getattr(self, f'{self.enclist[i]}'"ipin").text()+'"' +'\n'+'\t'+'},'+'\n')
        #Temp 
            for i in range(4):
                    if getattr(self, f'{self.templist[i]}').isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Temperature",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ getattr(self, f'{self.templist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"PV[i]":' +'\t'+'\t'+'\t'+'"'+ getattr(self, f'{self.templist[i]}'"pv").text() + '",' +'\n'+'\t'+'\t'+'"Sensor":' +'\t'+'\t'+'\t'+'"Thermistor",'+'\n'+'\t'+'\t'+'\t'+'"Thermistor":'+'\n'+'\t'+'\t'+'\t'+'{'+'\n'+'\t'+'\t'+'\t'+'\t'+'"Pin":'+ '\t'+'\t'+'"'+ getattr(self, f'{self.templist[i]}'"pin").text()+'",' +'\n'+'\t'+'\t'+'\t'+'\t'+'"beta":'+ '\t'+'\t'+ getattr(self, f'{self.templist[i]}'"beta").text()+',' +'\n'+ '\t'+'\t'+'\t'+'\t'+'"r0":'+ '\t'+'\t'+ getattr(self, f'{self.templist[i]}'"r").text()+',' +'\n'+'\t'+'\t'+'\t'+'\t'+'"t0":'+ '\t'+'\t'+ getattr(self, f'{self.templist[i]}'"t").text() +'\n'+ '\t'+'\t'+'\t'+'}'+'\n'+'\t'+'},'+'\n')
        #swtich 
            for i in range(3):
                    if getattr(self, f'{self.swlist[i]}').isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Switch",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ getattr(self, f'{self.swlist[i]}'"txt").text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + getattr(self, f'{self.swlist[i]}'"pin").text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t'+'"' + str(getattr(self, f'{self.swlist[i]}'"mode").currentText())+'",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ getattr(self, f'{self.swlist[i]}'"pv").text()+','+'\n'+'\t'+'\t'+'"SP":'+'\t'+'\t'+'\t'+'\t'+ getattr(self, f'{self.swlist[i]}'"sp").text() +'\n'+'\t'+'},'+'\n')
        #reset pin this must be last
            f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Reset Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.resettxt.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+'"'+ self.resetpin.text() +'"' +'\n'+'\t'+'}'+'\n')
         # ending format
            f.write('\t'+']'+'\n'+'}')
            
#write out data to save file for hmi    
            with open('save.txt', 'w') as s:
            #boards line 1
                s.write(str(self.boards.currentText())+'|'+'\n')
            #axis line 2-7
                for i in range(5):
                    s.write(str(getattr(self, f'{self.axislist[i]}').isChecked())+'|'+ getattr(self, f'{self.axislist[i]}'"txt").text()+'|'+ getattr(self, f'{self.axislist[i]}'"joint").text()+'|'+ getattr(self, f'{self.axislist[i]}'"step").text()+'|'+ getattr(self, f'{self.axislist[i]}'"dir").text()+'|'+ getattr(self, f'{self.axislist[i]}'"enable").text()+'|'+ getattr(self, f'{self.axislist[i]}'"cur").text()+'|'+ getattr(self, f'{self.axislist[i]}'"tmc").currentText()+'|'+ getattr(self, f'{self.axislist[i]}'"cursense").text()+'|'+ getattr(self, f'{self.axislist[i]}'"microstep").text()+'|'+ getattr(self, f'{self.axislist[i]}'"stealthcop").currentText()+'|'+'\n')
            #output line 7-14
                for i in range(8):
                    s.write(str(getattr(self, f'{self.outlist[i]}'"chk").isChecked())+'|'+ getattr(self, f'{self.outlist[i]}'"txt").text()+'|'+ getattr(self, f'{self.outlist[i]}'"pin").text()+'|'+ getattr(self, f'{self.outlist[i]}'"state").currentText()+'|'+ str(getattr(self, f'{self.outlist[i]}'"inv").isChecked())+'|'+'\n')
            #input0 line 15-22
                for i in range(8):
                    s.write(str(getattr(self, f'{self.inlist[i]}'"chk").isChecked())+'|'+ getattr(self, f'{self.inlist[i]}'"txt").text()+'|'+ getattr(self, f'{self.inlist[i]}'"pin").text()+'|'+ getattr(self, f'{self.inlist[i]}'"state").currentText()+'|'+ str(getattr(self, f'{self.inlist[i]}'"inv").isChecked())+'|'+'\n')
            #reset pin line 23
                s.write(str(self.estop.isChecked())+'|'+ self.estoptxt.text()+'|'+self.estoppin.text()+'|'+'\n')
            #reset pin line 24
                s.write(str(self.reset.isChecked())+'|'+ self.resettxt.text()+'|'+self.resetpin.text()+'|'+'\n')
            #PWM line 25-31
                for i in range(7):
                    s.write(str(getattr(self, f'{self.pwmlist[i]}').isChecked())+'|'+ getattr(self, f'{self.pwmlist[i]}'"txt").text()+'|'+ getattr(self, f'{self.pwmlist[i]}'"max").text()+'|'+ getattr(self, f'{self.pwmlist[i]}'"pin").text()+'|'+ str(getattr(self, f'{self.pwmlist[i]}'"hw").isChecked())+'|'+ str(getattr(self, f'{self.pwmlist[i]}'"vf").isChecked())+'|'+ getattr(self, f'{self.pwmlist[i]}'"freq").text()+'|'+ getattr(self, f'{self.pwmlist[i]}'"period").text()+'|'+ getattr(self, f'{self.pwmlist[i]}'"spi").text()+'|'+'\n')
            #rc Servo line 32
                s.write(str(self.rcservo.isChecked())+'|'+ self.rcservotxt.text()+'|'+self.rcservopin.text()+'|'+self.rcservospi.text()+'|'+'\n')
            #QEM line 33
                s.write(str(self.qem.isChecked())+'|'+ self.qemtxt.text()+'|'+self.qempv.text()+'|'+self.qemapin.text()+'|'+self.qembpin.text()+'|'+self.qemipin.text()+'|'+self.qeminput.text()+'|'+str(self.qemstate.currentText())+'|'+'\n')
            #Encoder line 34-37
                for i in range(4):
                    s.write(str(getattr(self, f'{self.enclist[i]}').isChecked())+'|'+ getattr(self, f'{self.enclist[i]}'"txt").text()+'|'+ getattr(self, f'{self.enclist[i]}'"pv").text()+'|'+ getattr(self, f'{self.enclist[i]}'"apin").text()+'|'+ getattr(self, f'{self.enclist[i]}'"bpin").text()+'|'+ getattr(self, f'{self.enclist[i]}'"ipin").text()+'|'+ getattr(self, f'{self.enclist[i]}'"input").text()+'|'+ str(getattr(self, f'{self.enclist[i]}'"state").currentText())+'|'+'\n')
            #temp line 38-41
                for i in range(4):
                    s.write(str(getattr(self, f'{self.templist[i]}').isChecked())+'|'+ getattr(self, f'{self.templist[i]}'"txt").text()+'|'+ getattr(self, f'{self.templist[i]}'"pv").text()+'|'+ getattr(self, f'{self.templist[i]}'"pin").text()+'|'+ getattr(self, f'{self.templist[i]}'"r").text()+'|'+ getattr(self, f'{self.templist[i]}'"t").text()+'|'+ getattr(self, f'{self.templist[i]}'"beta").text()+'|'+'\n')
            #swtich  line 42-44
                for i in range(3):
                    s.write(str(getattr(self, f'{self.swlist[i]}').isChecked())+'|'+ getattr(self, f'{self.swlist[i]}'"txt").text()+'|'+ getattr(self, f'{self.swlist[i]}'"pv").text()+'|'+ getattr(self, f'{self.swlist[i]}'"pin").text()+'|'+ getattr(self, f'{self.swlist[i]}'"sp").text()+'|'+ str(getattr(self, f'{self.swlist[i]}'"mode").currentText())+'|'+'\n')

#load boards from combo box        
    def loadboards(self):
        if self.boards.currentText() == "MKS SBASE v1.3": self.xaxiscur.setEnabled(1),self.xaxiscur.setVisible(1),self.yaxiscur.setEnabled(1),self.yaxiscur.setVisible(1),self.zaxiscur.setEnabled(1),self.zaxiscur.setVisible(1),self.e0axiscur.setEnabled(1),self.e0axiscur.setVisible(1),self.e1axiscur.setEnabled(1),self.e1axiscur.setVisible(1)
        else:self.xaxiscur.setEnabled(0),self.xaxiscur.setVisible(0),self.yaxiscur.setEnabled(0),self.yaxiscur.setVisible(0),self.zaxiscur.setEnabled(0),self.zaxiscur.setVisible(0),self.e0axiscur.setEnabled(0),self.e0axiscur.setVisible(0),self.e1axiscur.setEnabled(0),self.e1axiscur.setVisible(0)
 
#hide and show X axis tmc options 
    def xtmc(self):  
        if self.xaxistmc.currentText() == "None": self.xaxiscur.setEnabled(0), self.xaxiscur.setVisible(0), self.xaxiscursense.setEnabled(0), self.xaxiscursense.setVisible(0), self.xaxismicrostep.setEnabled(0), self.xaxismicrostep.setVisible(0), self.xaxisstealthcop.setEnabled(0), self.xaxisstealthcop.setVisible(0)
        else: self.xaxiscur.setEnabled(1), self.xaxiscur.setVisible(1), self.xaxiscursense.setEnabled(1), self.xaxiscursense.setVisible(1), self.xaxismicrostep.setEnabled(1), self.xaxismicrostep.setVisible(1), self.xaxisstealthcop.setEnabled(1), self.xaxisstealthcop.setVisible(1) 
            
#hide and show Y axis tmc options            
    def ytmc(self):
        if self.yaxistmc.currentText() == "None": self.yaxiscur.setEnabled(0), self.yaxiscur.setVisible(0), self.yaxiscursense.setEnabled(0), self.yaxiscursense.setVisible(0), self.yaxismicrostep.setEnabled(0), self.yaxismicrostep.setVisible(0), self.yaxisstealthcop.setEnabled(0), self.yaxisstealthcop.setVisible(0)
        else: self.yaxiscur.setEnabled(1), self.yaxiscur.setVisible(1), self.yaxiscursense.setEnabled(1), self.yaxiscursense.setVisible(1), self.yaxismicrostep.setEnabled(1), self.yaxismicrostep.setVisible(1), self.yaxisstealthcop.setEnabled(1), self.yaxisstealthcop.setVisible(1) 

#hide and show Z axis tmc options            
    def ztmc(self):
        if self.zaxistmc.currentText() == "None": self.zaxiscur.setEnabled(0), self.zaxiscur.setVisible(0), self.zaxiscursense.setEnabled(0), self.zaxiscursense.setVisible(0), self.zaxismicrostep.setEnabled(0), self.zaxismicrostep.setVisible(0), self.zaxisstealthcop.setEnabled(0), self.zaxisstealthcop.setVisible(0)
        else: self.zaxiscur.setEnabled(1), self.zaxiscur.setVisible(1), self.zaxiscursense.setEnabled(1), self.zaxiscursense.setVisible(1), self.zaxismicrostep.setEnabled(1), self.zaxismicrostep.setVisible(1), self.zaxisstealthcop.setEnabled(1), self.zaxisstealthcop.setVisible(1) 

#hide and show E0 axis tmc options            
    def e0tmc(self):
        if self.e0axistmc.currentText() == "None": self.e0axiscur.setEnabled(0), self.e0axiscur.setVisible(0), self.e0axiscursense.setEnabled(0), self.e0axiscursense.setVisible(0), self.e0axismicrostep.setEnabled(0), self.e0axismicrostep.setVisible(0), self.e0axisstealthcop.setEnabled(0), self.e0axisstealthcop.setVisible(0)
        else: self.e0axiscur.setEnabled(1), self.e0axiscur.setVisible(1), self.e0axiscursense.setEnabled(1), self.e0axiscursense.setVisible(1), self.e0axismicrostep.setEnabled(1), self.e0axismicrostep.setVisible(1), self.e0axisstealthcop.setEnabled(1), self.e0axisstealthcop.setVisible(1) 

#hide and show E1 axis tmc options            
    def e1tmc(self):
        if self.e1axistmc.currentText() == "None": self.e1axiscur.setEnabled(0), self.e1axiscur.setVisible(0), self.e1axiscursense.setEnabled(0), self.e1axiscursense.setVisible(0), self.e1axismicrostep.setEnabled(0), self.e1axismicrostep.setVisible(0), self.e1axisstealthcop.setEnabled(0), self.e1axisstealthcop.setVisible(0)
        else: self.e1axiscur.setEnabled(1), self.e1axiscur.setVisible(1), self.e1axiscursense.setEnabled(1), self.e1axiscursense.setVisible(1), self.e1axismicrostep.setEnabled(1), self.e1axismicrostep.setVisible(1), self.e1axisstealthcop.setEnabled(1), self.e1axisstealthcop.setVisible(1)            


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()