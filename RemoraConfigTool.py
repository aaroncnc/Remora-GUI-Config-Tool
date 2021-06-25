from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('remoreconfig.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'save') # Find the button
        self.button.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!

        self.resettxt = self.findChild(QtWidgets.QLineEdit, 'resettxt')
        self.resetpin = self.findChild(QtWidgets.QLineEdit, 'resetpin')
        self.boards = self.findChild(QtWidgets.QComboBox, 'boards')
        #X axis
        self.xaxis = self.findChild(QtWidgets.QCheckBox, 'xaxis')
        self.xaxistxt = self.findChild(QtWidgets.QLineEdit, 'xaxistxt')
        self.xaxisjoint = self.findChild(QtWidgets.QLineEdit, 'xaxisjoint')
        self.xaxisstep = self.findChild(QtWidgets.QLineEdit, 'xaxisstep')
        self.xaxisdir = self.findChild(QtWidgets.QLineEdit, 'xaxisdir')
        self.xaxisenable = self.findChild(QtWidgets.QLineEdit, 'xaxisenable')
        #y axis
        self.yaxis = self.findChild(QtWidgets.QCheckBox, 'yaxis')
        self.yaxistxt = self.findChild(QtWidgets.QLineEdit, 'yaxistxt')
        self.yaxisjoint = self.findChild(QtWidgets.QLineEdit, 'yaxisjoint')
        self.yaxisstep = self.findChild(QtWidgets.QLineEdit, 'yaxisstep')
        self.yaxisdir = self.findChild(QtWidgets.QLineEdit, 'yaxisdir')
        self.yaxisenable = self.findChild(QtWidgets.QLineEdit, 'yaxisenable')
        #z axis
        self.zaxis = self.findChild(QtWidgets.QCheckBox, 'zaxis')
        self.zaxistxt = self.findChild(QtWidgets.QLineEdit, 'zaxistxt')
        self.zaxisjoint = self.findChild(QtWidgets.QLineEdit, 'zaxisjoint')
        self.zaxisstep = self.findChild(QtWidgets.QLineEdit, 'zaxisstep')
        self.zaxisdir = self.findChild(QtWidgets.QLineEdit, 'zaxisdir')
        self.zaxisenable = self.findChild(QtWidgets.QLineEdit, 'zaxisenable')
        #e0 axis
        self.e0axis = self.findChild(QtWidgets.QCheckBox, 'e0axis')
        self.e0axistxt = self.findChild(QtWidgets.QLineEdit, 'e0axistxt')
        self.e0axisjoint = self.findChild(QtWidgets.QLineEdit, 'e0axisjoint')
        self.e0axisstep = self.findChild(QtWidgets.QLineEdit, 'e0axisstep')
        self.e0axisdir = self.findChild(QtWidgets.QLineEdit, 'e0axisdir')
        self.e0axisenable = self.findChild(QtWidgets.QLineEdit, 'e0axisenable')
        #e1 axis
        self.e1axis = self.findChild(QtWidgets.QCheckBox, 'e1axis')
        self.e1axistxt = self.findChild(QtWidgets.QLineEdit, 'e1axistxt')
        self.e1axisjoint = self.findChild(QtWidgets.QLineEdit, 'e1axisjoint')
        self.e1axisstep = self.findChild(QtWidgets.QLineEdit, 'e1axisstep')
        self.e1axisdir = self.findChild(QtWidgets.QLineEdit, 'e1axisdir')
        self.e1axisenable = self.findChild(QtWidgets.QLineEdit, 'e1axisenable')
        #Output 0
        self.outchk0 = self.findChild(QtWidgets.QCheckBox, 'outchk0')
        self.outtxt0 = self.findChild(QtWidgets.QLineEdit, 'outtxt0')
        self.outpin0 = self.findChild(QtWidgets.QLineEdit, 'outpin0')
        self.outstate0 = self.findChild(QtWidgets.QComboBox, 'outstate0')
        self.outinv0 = self.findChild(QtWidgets.QCheckBox, 'outinv0')
        #Output 1
        self.outchk1 = self.findChild(QtWidgets.QCheckBox, 'outchk1')
        self.outtxt1 = self.findChild(QtWidgets.QLineEdit, 'outtxt1')
        self.outpin1 = self.findChild(QtWidgets.QLineEdit, 'outpin1')
        self.outstate1 = self.findChild(QtWidgets.QComboBox, 'outstate1')
        self.outinv1 = self.findChild(QtWidgets.QCheckBox, 'outinv1')
        #Output 2
        self.outchk2 = self.findChild(QtWidgets.QCheckBox, 'outchk2')
        self.outtxt2 = self.findChild(QtWidgets.QLineEdit, 'outtxt2')
        self.outpin2 = self.findChild(QtWidgets.QLineEdit, 'outpin2')
        self.outstate2 = self.findChild(QtWidgets.QComboBox, 'outstate2')
        self.outinv2 = self.findChild(QtWidgets.QCheckBox, 'outinv2')
        #Output 3
        self.outchk3 = self.findChild(QtWidgets.QCheckBox, 'outchk3')
        self.outtxt3 = self.findChild(QtWidgets.QLineEdit, 'outtxt3')
        self.outpin3 = self.findChild(QtWidgets.QLineEdit, 'outpin3')
        self.outstate3 = self.findChild(QtWidgets.QComboBox, 'outstate3')
        self.outinv3 = self.findChild(QtWidgets.QCheckBox, 'outinv3')
        #Output 4
        self.outchk4 = self.findChild(QtWidgets.QCheckBox, 'outchk4')
        self.outtxt4 = self.findChild(QtWidgets.QLineEdit, 'outtxt4')
        self.outpin4 = self.findChild(QtWidgets.QLineEdit, 'outpin4')
        self.outstate4 = self.findChild(QtWidgets.QComboBox, 'outstate4')
        self.outinv4 = self.findChild(QtWidgets.QCheckBox, 'outinv4')
        #Output 5
        self.outchk5 = self.findChild(QtWidgets.QCheckBox, 'outchk5')
        self.outtxt5 = self.findChild(QtWidgets.QLineEdit, 'outtxt5')
        self.outpin5 = self.findChild(QtWidgets.QLineEdit, 'outpin5')
        self.outstate5 = self.findChild(QtWidgets.QComboBox, 'outstate5')
        self.outinv5 = self.findChild(QtWidgets.QCheckBox, 'outinv5')
        #Output 6
        self.outchk6 = self.findChild(QtWidgets.QCheckBox, 'outchk6')
        self.outtxt6 = self.findChild(QtWidgets.QLineEdit, 'outtxt6')
        self.outpin6 = self.findChild(QtWidgets.QLineEdit, 'outpin6')
        self.outstate6 = self.findChild(QtWidgets.QComboBox, 'outstate6')
        self.outinv6 = self.findChild(QtWidgets.QCheckBox, 'outinv6')
        #Output 7
        self.outchk7 = self.findChild(QtWidgets.QCheckBox, 'outchk7')
        self.outtxt7 = self.findChild(QtWidgets.QLineEdit, 'outtxt7')
        self.outpin7 = self.findChild(QtWidgets.QLineEdit, 'outpin7')
        self.outstate7 = self.findChild(QtWidgets.QComboBox, 'outstate7')
        self.outinv7 = self.findChild(QtWidgets.QCheckBox, 'outinv7')
        #input 0
        self.inchk0 = self.findChild(QtWidgets.QCheckBox, 'inchk0')
        self.intxt0 = self.findChild(QtWidgets.QLineEdit, 'intxt0')
        self.inpin0 = self.findChild(QtWidgets.QLineEdit, 'inpin0')
        self.instate0 = self.findChild(QtWidgets.QComboBox, 'instate0')
        self.ininv0 = self.findChild(QtWidgets.QCheckBox, 'ininv0')
        #input 1
        self.inchk1 = self.findChild(QtWidgets.QCheckBox, 'inchk1')
        self.intxt1 = self.findChild(QtWidgets.QLineEdit, 'intxt1')
        self.inpin1 = self.findChild(QtWidgets.QLineEdit, 'inpin1')
        self.instate1 = self.findChild(QtWidgets.QComboBox, 'instate1')
        self.ininv1 = self.findChild(QtWidgets.QCheckBox, 'ininv1')
        #input 2
        self.inchk2 = self.findChild(QtWidgets.QCheckBox, 'inchk2')
        self.intxt2 = self.findChild(QtWidgets.QLineEdit, 'intxt2')
        self.inpin2 = self.findChild(QtWidgets.QLineEdit, 'inpin2')
        self.instate2 = self.findChild(QtWidgets.QComboBox, 'instate2')
        self.ininv2 = self.findChild(QtWidgets.QCheckBox, 'ininv2')
        #input 3
        self.inchk3 = self.findChild(QtWidgets.QCheckBox, 'inchk3')
        self.intxt3 = self.findChild(QtWidgets.QLineEdit, 'intxt3')
        self.inpin3 = self.findChild(QtWidgets.QLineEdit, 'inpin3')
        self.instate3 = self.findChild(QtWidgets.QComboBox, 'instate3')
        self.ininv3 = self.findChild(QtWidgets.QCheckBox, 'ininv3')
        #input 4
        self.inchk4 = self.findChild(QtWidgets.QCheckBox, 'inchk4')
        self.intxt4 = self.findChild(QtWidgets.QLineEdit, 'intxt4')
        self.inpin4 = self.findChild(QtWidgets.QLineEdit, 'inpin4')
        self.instate4 = self.findChild(QtWidgets.QComboBox, 'instate4')
        self.ininv4 = self.findChild(QtWidgets.QCheckBox, 'ininv4')
        #input 5
        self.inchk5 = self.findChild(QtWidgets.QCheckBox, 'inchk5')
        self.intxt5 = self.findChild(QtWidgets.QLineEdit, 'intxt5')
        self.inpin5 = self.findChild(QtWidgets.QLineEdit, 'inpin5')
        self.instate5 = self.findChild(QtWidgets.QComboBox, 'instate5')
        self.ininv5 = self.findChild(QtWidgets.QCheckBox, 'ininv5')
        #input 6
        self.inchk6 = self.findChild(QtWidgets.QCheckBox, 'inchk6')
        self.intxt6 = self.findChild(QtWidgets.QLineEdit, 'intxt6')
        self.inpin6 = self.findChild(QtWidgets.QLineEdit, 'inpin6')
        self.instate6 = self.findChild(QtWidgets.QComboBox, 'instate6')
        self.ininv6 = self.findChild(QtWidgets.QCheckBox, 'ininv6')
        #input 7
        self.inchk7 = self.findChild(QtWidgets.QCheckBox, 'inchk7')
        self.intxt7 = self.findChild(QtWidgets.QLineEdit, 'intxt7')
        self.inpin7 = self.findChild(QtWidgets.QLineEdit, 'inpin7')
        self.instate7 = self.findChild(QtWidgets.QComboBox, 'instate7')
        self.ininv7 = self.findChild(QtWidgets.QCheckBox, 'ininv7')
        #E-stop
        self.estop = self.findChild(QtWidgets.QCheckBox, 'estop')
        self.estoptxt = self.findChild(QtWidgets.QLineEdit, 'estoptxt')
        self.estoppin = self.findChild(QtWidgets.QLineEdit, 'estoppin')
        #PWM0
        self.pwm0 = self.findChild(QtWidgets.QCheckBox, 'pwm0')
        self.pwmtxt0 = self.findChild(QtWidgets.QLineEdit, 'pwmtxt0')
        self.pwmmax0 = self.findChild(QtWidgets.QLineEdit, 'pwmmax0')
        self.pwmpin0 = self.findChild(QtWidgets.QLineEdit, 'pwmpin0')
        self.pwmhw0 = self.findChild(QtWidgets.QCheckBox, 'pwmhw0')
        self.pwmvf0 = self.findChild(QtWidgets.QCheckBox, 'pwmvf0')
        self.pwmfreq0 = self.findChild(QtWidgets.QLineEdit, 'pwmfreq0')
        self.pwmperiod0 = self.findChild(QtWidgets.QLineEdit, 'pwmperiod0')
        self.pwmspi0 = self.findChild(QtWidgets.QLineEdit, 'pwmspi0')
        #PWM1
        self.pwm1 = self.findChild(QtWidgets.QCheckBox, 'pwm1')
        self.pwmtxt1 = self.findChild(QtWidgets.QLineEdit, 'pwmtxt1')
        self.pwmmax1 = self.findChild(QtWidgets.QLineEdit, 'pwmmax1')
        self.pwmpin1 = self.findChild(QtWidgets.QLineEdit, 'pwmpin1')
        self.pwmhw1 = self.findChild(QtWidgets.QCheckBox, 'pwmhw1')
        self.pwmvf1 = self.findChild(QtWidgets.QCheckBox, 'pwmvf1')
        self.pwmfreq1 = self.findChild(QtWidgets.QLineEdit, 'pwmfreq1')
        self.pwmperiod1 = self.findChild(QtWidgets.QLineEdit, 'pwmperiod1')
        self.pwmspi1 = self.findChild(QtWidgets.QLineEdit, 'pwmspi1')
        #PWM2
        self.pwm2 = self.findChild(QtWidgets.QCheckBox, 'pwm2')
        self.pwmtxt2 = self.findChild(QtWidgets.QLineEdit, 'pwmtxt2')
        self.pwmmax2 = self.findChild(QtWidgets.QLineEdit, 'pwmmax2')
        self.pwmpin2 = self.findChild(QtWidgets.QLineEdit, 'pwmpin2')
        self.pwmhw2 = self.findChild(QtWidgets.QCheckBox, 'pwmhw2')
        self.pwmvf2 = self.findChild(QtWidgets.QCheckBox, 'pwmvf2')
        self.pwmfreq2 = self.findChild(QtWidgets.QLineEdit, 'pwmfreq2')
        self.pwmperiod2 = self.findChild(QtWidgets.QLineEdit, 'pwmperiod2')
        self.pwmspi2 = self.findChild(QtWidgets.QLineEdit, 'pwmspi2')
        #PWM3
        self.pwm3 = self.findChild(QtWidgets.QCheckBox, 'pwm3')
        self.pwmtxt3 = self.findChild(QtWidgets.QLineEdit, 'pwmtxt3')
        self.pwmmax3 = self.findChild(QtWidgets.QLineEdit, 'pwmmax3')
        self.pwmpin3 = self.findChild(QtWidgets.QLineEdit, 'pwmpin3')
        self.pwmhw3 = self.findChild(QtWidgets.QCheckBox, 'pwmhw3')
        self.pwmvf3 = self.findChild(QtWidgets.QCheckBox, 'pwmvf3')
        self.pwmfreq3 = self.findChild(QtWidgets.QLineEdit, 'pwmfreq3')
        self.pwmperiod3 = self.findChild(QtWidgets.QLineEdit, 'pwmperiod3')
        self.pwmspi3 = self.findChild(QtWidgets.QLineEdit, 'pwmspi3')
        #PWM4
        self.pwm4 = self.findChild(QtWidgets.QCheckBox, 'pwm4')
        self.pwmtxt4 = self.findChild(QtWidgets.QLineEdit, 'pwmtxt4')
        self.pwmmax4 = self.findChild(QtWidgets.QLineEdit, 'pwmmax4')
        self.pwmpin4 = self.findChild(QtWidgets.QLineEdit, 'pwmpin4')
        self.pwmhw4 = self.findChild(QtWidgets.QCheckBox, 'pwmhw4')
        self.pwmvf4 = self.findChild(QtWidgets.QCheckBox, 'pwmvf4')
        self.pwmfreq4 = self.findChild(QtWidgets.QLineEdit, 'pwmfreq4')
        self.pwmperiod4 = self.findChild(QtWidgets.QLineEdit, 'pwmperiod4')
        self.pwmspi4 = self.findChild(QtWidgets.QLineEdit, 'pwmspi4')
        #PWM5
        self.pwm5 = self.findChild(QtWidgets.QCheckBox, 'pwm5')
        self.pwmtxt5 = self.findChild(QtWidgets.QLineEdit, 'pwmtxt5')
        self.pwmmax5 = self.findChild(QtWidgets.QLineEdit, 'pwmmax5')
        self.pwmpin5 = self.findChild(QtWidgets.QLineEdit, 'pwmpin5')
        self.pwmhw5 = self.findChild(QtWidgets.QCheckBox, 'pwmhw5')
        self.pwmvf5 = self.findChild(QtWidgets.QCheckBox, 'pwmvf5')
        self.pwmfreq5 = self.findChild(QtWidgets.QLineEdit, 'pwmfreq5')
        self.pwmperiod5 = self.findChild(QtWidgets.QLineEdit, 'pwmperiod5')
        self.pwmspi5 = self.findChild(QtWidgets.QLineEdit, 'pwmspi5')
        #PWM6
        self.pwm6 = self.findChild(QtWidgets.QCheckBox, 'pwm6')
        self.pwmtxt6 = self.findChild(QtWidgets.QLineEdit, 'pwmtxt6')
        self.pwmmax6 = self.findChild(QtWidgets.QLineEdit, 'pwmmax6')
        self.pwmpin6 = self.findChild(QtWidgets.QLineEdit, 'pwmpin6')
        self.pwmhw6 = self.findChild(QtWidgets.QCheckBox, 'pwmhw6')
        self.pwmvf6 = self.findChild(QtWidgets.QCheckBox, 'pwmvf6')
        self.pwmfreq6 = self.findChild(QtWidgets.QLineEdit, 'pwmfreq6')
        self.pwmperiod6 = self.findChild(QtWidgets.QLineEdit, 'pwmperiod6')
        self.pwmspi6 = self.findChild(QtWidgets.QLineEdit, 'pwmspi6')
        #Rc Servo
        self.rcservo = self.findChild(QtWidgets.QCheckBox, 'rcservo')
        self.rcservotxt = self.findChild(QtWidgets.QLineEdit, 'rcservotxt')
        self.rcservopin = self.findChild(QtWidgets.QLineEdit, 'rcservopin')
        self.rcservospi = self.findChild(QtWidgets.QLineEdit, 'rcservospi')
        #QEM
        self.qem = self.findChild(QtWidgets.QCheckBox, 'qem')
        self.qemtxt = self.findChild(QtWidgets.QLineEdit, 'qemtxt')
        self.qempv = self.findChild(QtWidgets.QLineEdit, 'qempv')
        self.qemcha = self.findChild(QtWidgets.QLineEdit, 'qemcha')
        self.qemchb = self.findChild(QtWidgets.QLineEdit, 'qemchb')
        self.qemipin = self.findChild(QtWidgets.QLineEdit, 'qemipin')
        self.qeminput = self.findChild(QtWidgets.QLineEdit, 'qeminput')
        self.qemstate = self.findChild(QtWidgets.QComboBox, 'qemstate')
        #Encoder 0
        self.enc0 = self.findChild(QtWidgets.QCheckBox, 'enc0')
        self.enctxt0 = self.findChild(QtWidgets.QLineEdit, 'enctxt0')
        self.encpv0 = self.findChild(QtWidgets.QLineEdit, 'encpv0')
        self.encapin0 = self.findChild(QtWidgets.QLineEdit, 'encapin0')
        self.encbpin0 = self.findChild(QtWidgets.QLineEdit, 'encbpin0')
        self.encipin0 = self.findChild(QtWidgets.QLineEdit, 'encipin0')
        self.encinput0 = self.findChild(QtWidgets.QLineEdit, 'encinput0')
        self.encstate0 = self.findChild(QtWidgets.QComboBox, 'encstate0')
        #Encoder 1
        self.enc1 = self.findChild(QtWidgets.QCheckBox, 'enc1')
        self.enctxt1 = self.findChild(QtWidgets.QLineEdit, 'enctxt1')
        self.encpv1 = self.findChild(QtWidgets.QLineEdit, 'encpv1')
        self.encapin1 = self.findChild(QtWidgets.QLineEdit, 'encapin1')
        self.encbpin1 = self.findChild(QtWidgets.QLineEdit, 'encbpin1')
        self.encipin1 = self.findChild(QtWidgets.QLineEdit, 'encipin1')
        self.encinput1 = self.findChild(QtWidgets.QLineEdit, 'encinput1')
        self.encstate1 = self.findChild(QtWidgets.QComboBox, 'encstate1')
        #Encoder 2
        self.enc2 = self.findChild(QtWidgets.QCheckBox, 'enc2')
        self.enctxt2 = self.findChild(QtWidgets.QLineEdit, 'enctxt2')
        self.encpv2 = self.findChild(QtWidgets.QLineEdit, 'encpv2')
        self.encapin2 = self.findChild(QtWidgets.QLineEdit, 'encapin2')
        self.encbpin2 = self.findChild(QtWidgets.QLineEdit, 'encbpin2')
        self.encipin2 = self.findChild(QtWidgets.QLineEdit, 'encipin2')
        self.encinput2 = self.findChild(QtWidgets.QLineEdit, 'encinput2')
        self.encstate2 = self.findChild(QtWidgets.QComboBox, 'encstate2')
        #Encoder 3
        self.enc3 = self.findChild(QtWidgets.QCheckBox, 'enc3')
        self.enctxt3 = self.findChild(QtWidgets.QLineEdit, 'enctxt3')
        self.encpv3 = self.findChild(QtWidgets.QLineEdit, 'encpv3')
        self.encapin3 = self.findChild(QtWidgets.QLineEdit, 'encapin3')
        self.encbpin3 = self.findChild(QtWidgets.QLineEdit, 'encbpin3')
        self.encipin3 = self.findChild(QtWidgets.QLineEdit, 'encipin3')
        self.encinput3 = self.findChild(QtWidgets.QLineEdit, 'encinput3')
        self.encstate3 = self.findChild(QtWidgets.QComboBox, 'encstate3')
        #Thermistor 0
        self.temp0 = self.findChild(QtWidgets.QCheckBox, 'temp0')
        self.temptxt0 = self.findChild(QtWidgets.QLineEdit, 'temptxt0')
        self.temppv0 = self.findChild(QtWidgets.QLineEdit, 'temppv0')
        self.temppin0 = self.findChild(QtWidgets.QLineEdit, 'temppin0')
        self.tempr0 = self.findChild(QtWidgets.QLineEdit, 'tempr0')
        self.tempt0 = self.findChild(QtWidgets.QLineEdit, 'tempt0')
        self.tempbeta0 = self.findChild(QtWidgets.QLineEdit, 'tempbeta0')
        #Thermistor 1
        self.temp1 = self.findChild(QtWidgets.QCheckBox, 'temp1')
        self.temptxt1 = self.findChild(QtWidgets.QLineEdit, 'temptxt1')
        self.temppv1 = self.findChild(QtWidgets.QLineEdit, 'temppv1')
        self.temppin1 = self.findChild(QtWidgets.QLineEdit, 'temppin1')
        self.tempr1 = self.findChild(QtWidgets.QLineEdit, 'tempr1')
        self.tempt1 = self.findChild(QtWidgets.QLineEdit, 'tempt1')
        self.tempbeta1 = self.findChild(QtWidgets.QLineEdit, 'tempbeta1')
        #Thermistor 2
        self.temp2 = self.findChild(QtWidgets.QCheckBox, 'temp2')
        self.temptxt2 = self.findChild(QtWidgets.QLineEdit, 'temptxt2')
        self.temppv2 = self.findChild(QtWidgets.QLineEdit, 'temppv2')
        self.temppin2 = self.findChild(QtWidgets.QLineEdit, 'temppin2')
        self.tempr2 = self.findChild(QtWidgets.QLineEdit, 'tempr2')
        self.tempt2 = self.findChild(QtWidgets.QLineEdit, 'tempt2')
        self.tempbeta2 = self.findChild(QtWidgets.QLineEdit, 'tempbeta2')
        #Thermistor 3
        self.temp3 = self.findChild(QtWidgets.QCheckBox, 'temp3')
        self.temptxt3 = self.findChild(QtWidgets.QLineEdit, 'temptxt3')
        self.temppv3 = self.findChild(QtWidgets.QLineEdit, 'temppv3')
        self.temppin3 = self.findChild(QtWidgets.QLineEdit, 'temppin3')
        self.tempr3 = self.findChild(QtWidgets.QLineEdit, 'tempr3')
        self.tempt3 = self.findChild(QtWidgets.QLineEdit, 'tempt3')
        self.tempbeta3 = self.findChild(QtWidgets.QLineEdit, 'tempbeta3')
        #Switch 0
        self.sw0 = self.findChild(QtWidgets.QCheckBox, 'sw0')
        self.swtxt0 = self.findChild(QtWidgets.QLineEdit, 'swtxt0')
        self.swpv0 = self.findChild(QtWidgets.QLineEdit, 'swpv0')
        self.swpin0 = self.findChild(QtWidgets.QLineEdit, 'swpin0')
        self.swsp0 = self.findChild(QtWidgets.QLineEdit, 'swsp0')
        self.swmode0 = self.findChild(QtWidgets.QComboBox, 'swmode0')
        #Switch 1
        self.sw1 = self.findChild(QtWidgets.QCheckBox, 'sw1')
        self.swtxt1 = self.findChild(QtWidgets.QLineEdit, 'swtxt1')
        self.swpv1 = self.findChild(QtWidgets.QLineEdit, 'swpv1')
        self.swpin1 = self.findChild(QtWidgets.QLineEdit, 'swpin1')
        self.swsp1 = self.findChild(QtWidgets.QLineEdit, 'swsp1')
        self.swmode1 = self.findChild(QtWidgets.QComboBox, 'swmode1')
        #Switch 2
        self.sw2 = self.findChild(QtWidgets.QCheckBox, 'sw2')
        self.swtxt2 = self.findChild(QtWidgets.QLineEdit, 'swtxt2')
        self.swpv2 = self.findChild(QtWidgets.QLineEdit, 'swpv2')
        self.swpin2 = self.findChild(QtWidgets.QLineEdit, 'swpin2')
        self.swsp2 = self.findChild(QtWidgets.QLineEdit, 'swsp2')
        self.swmode2 = self.findChild(QtWidgets.QComboBox, 'swmode2')

        self.show()

    def printButtonPressed(self):
        # This is executed when the button is pressed
        with open('config.txt', 'w') as f:
            f.write('{'+'\n')
            #Boards
            f.write('\t'+'"Board": "'+ self.boards.currentText() + '",' +'\n' )
            f.write('\t'+'"Modules":['+'\n')
            #E-stop
            if self.estop.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "eStop",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.estoptxt.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.estoppin.text()+'"'+'\n'+'\t'+'},'+'\n')
            #X axis
            if self.xaxis.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.xaxistxt.text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+'\t'+ self.xaxisjoint.text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + self.xaxisstep.text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t'+'\t' +'"' + self.xaxisdir.text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t'+'\t' +'"' + self.xaxisenable.text()+'"' +'\n'+'\t'+'},'+'\n')
            #y axis
            if self.yaxis.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.yaxistxt.text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+'\t'+ self.yaxisjoint.text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + self.yaxisstep.text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t'+'\t' +'"' + self.yaxisdir.text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t'+'\t' +'"' + self.yaxisenable.text()+'"' +'\n'+'\t'+'},'+'\n')
            #z axis
            if self.zaxis.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.zaxistxt.text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+'\t'+ self.zaxisjoint.text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + self.zaxisstep.text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t'+'\t' +'"' + self.zaxisdir.text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t'+'\t' +'"' + self.zaxisenable.text()+'"' +'\n'+'\t'+'},'+'\n')
            #e0 axis
            if self.e0axis.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.e0axistxt.text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+'\t'+ self.e0axisjoint.text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + self.e0axisstep.text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t'+'\t' +'"' + self.e0axisdir.text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t'+'\t' +'"' + self.e0axisenable.text()+'"' +'\n'+'\t'+'},'+'\n')
            #e1 axis
            if self.e1axis.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.e1axistxt.text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+'\t'+ self.e1axisjoint.text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + self.e1axisstep.text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t'+'\t' +'"' + self.e1axisdir.text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t'+'\t' +'"' + self.e1axisenable.text()+'"' +'\n'+'\t'+'},'+'\n')
            #output 0
            if self.outchk0.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.outtxt0.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.outpin0.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Output",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.outstate0.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.outinv0.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'0'+'\n'+'\t'+'},'+'\n')
            #output 1
            if self.outchk1.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.outtxt1.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.outpin1.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Output",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.outstate1.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.outinv1.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'1'+'\n'+'\t'+'},'+'\n')
            #output 2
            if self.outchk2.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.outtxt2.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.outpin2.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Output",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.outstate2.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.outinv2.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'2'+'\n'+'\t'+'},'+'\n')
            #output 3
            if self.outchk3.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.outtxt3.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.outpin3.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Output",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.outstate3.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.outinv3.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'3'+'\n'+'\t'+'},'+'\n')
            #output 4
            if self.outchk4.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.outtxt4.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.outpin4.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Output",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.outstate4.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.outinv4.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'4'+'\n'+'\t'+'},'+'\n')
            #output 5
            if self.outchk5.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.outtxt5.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.outpin5.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Output",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.outstate5.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.outinv5.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'5'+'\n'+'\t'+'},'+'\n')
            #output 6
            if self.outchk6.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.outtxt6.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.outpin6.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Output",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.outstate6.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.outinv6.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'6'+'\n'+'\t'+'},'+'\n')
            #output 7
            if self.outchk7.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.outtxt7.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.outpin7.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Output",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.outstate7.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.outinv7.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'7'+'\n'+'\t'+'},'+'\n')
            #input 0
            if self.inchk0.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.intxt0.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.inpin0.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Input",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.instate0.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.ininv0.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'0'+'\n'+'\t'+'},'+'\n')
            #input 1
            if self.inchk1.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.intxt1.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.inpin1.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Input",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.instate1.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.ininv1.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'1'+'\n'+'\t'+'},'+'\n')
            #input 2
            if self.inchk2.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.intxt2.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.inpin2.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Input",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.instate2.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.ininv2.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'2'+'\n'+'\t'+'},'+'\n')
            #input 3
            if self.inchk3.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.intxt3.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.inpin3.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Input",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.instate3.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.ininv3.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'3'+'\n'+'\t'+'},'+'\n')
            #input 4
            if self.inchk4.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.intxt4.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.inpin4.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Input",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.instate4.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.ininv4.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'4'+'\n'+'\t'+'},'+'\n')
            #input 5
            if self.inchk5.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.intxt5.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.inpin5.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Input",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.instate5.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.ininv5.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'5'+'\n'+'\t'+'},'+'\n')
            #input 6
            if self.inchk6.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.intxt6.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.inpin6.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Input",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.instate6.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.ininv6.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'6'+'\n'+'\t'+'},'+'\n')
            #input 7
            if self.inchk7.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Digital Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.intxt7.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.inpin7.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t' +'"Input",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.instate7.currentText()+ '"'+','+'\n'+'\t'+'\t'+'"Invert":'+'\t'+'\t'+'\t' + '"'+ str(self.ininv7.isChecked())+'",' +'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' +'7'+'\n'+'\t'+'},'+'\n')
            #PWM0
            if self.pwm0.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "PWM",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.pwmtxt0.text() + '",' +'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t'+ self.pwmspi0.text()+','+'\n'+'\t'+'\t'+'"PWM Pin":'+'\t'+'\t'+'\t' +'"' + self.pwmpin0.text()+'",'+'\n'+'\t'+'\t'+'"PWM Max":'+'\t'+'\t'+'\t' + self.pwmmax0.text()+',' +'\n'+'\t'+'\t'+'"Hardware PWM":'+'\t'+'\t'+'\t' +'"' +  str(self.pwmhw0.isChecked())+'",'+'\n'+'\t'+'\t'+'"Variable Freq":'+'\t'+'\t' +'"' +  str(self.pwmvf0.isChecked())+'",'+'\n'+'\t'+'\t'+'"Perioid SP[i]":'+'\t'+'\t' + self.pwmperiod0.text()+',' +'\n'+'\t'+'\t'+'"Perioid US":'+'\t'+'\t'+'\t' + self.pwmfreq0.text() +'\n'+'\t'+'},'+'\n')
            #PWM1
            if self.pwm1.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "PWM",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.pwmtxt1.text() + '",' +'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t'+ self.pwmspi1.text()+','+'\n'+'\t'+'\t'+'"PWM Pin":'+'\t'+'\t'+'\t' +'"' + self.pwmpin1.text()+'",'+'\n'+'\t'+'\t'+'"PWM Max":'+'\t'+'\t'+'\t' + self.pwmmax1.text()+',' +'\n'+'\t'+'\t'+'"Hardware PWM":'+'\t'+'\t'+'\t' +'"' +  str(self.pwmhw1.isChecked())+'",'+'\n'+'\t'+'\t'+'"Variable Freq":'+'\t'+'\t' +'"' +  str(self.pwmvf1.isChecked())+'",'+'\n'+'\t'+'\t'+'"Perioid SP[i]":'+'\t'+'\t' + self.pwmperiod1.text()+',' +'\n'+'\t'+'\t'+'"Perioid US":'+'\t'+'\t'+'\t' + self.pwmfreq1.text() +'\n'+'\t'+'},'+'\n')
            #PWM2
            if self.pwm2.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "PWM",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.pwmtxt2.text() + '",' +'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t'+ self.pwmspi2.text()+','+'\n'+'\t'+'\t'+'"PWM Pin":'+'\t'+'\t'+'\t' +'"' + self.pwmpin2.text()+'",'+'\n'+'\t'+'\t'+'"PWM Max":'+'\t'+'\t'+'\t' + self.pwmmax2.text()+',' +'\n'+'\t'+'\t'+'"Hardware PWM":'+'\t'+'\t'+'\t' +'"' +  str(self.pwmhw2.isChecked())+'",'+'\n'+'\t'+'\t'+'"Variable Freq":'+'\t'+'\t' +'"' +  str(self.pwmvf2.isChecked())+'",'+'\n'+'\t'+'\t'+'"Perioid SP[i]":'+'\t'+'\t' + self.pwmperiod2.text()+',' +'\n'+'\t'+'\t'+'"Perioid US":'+'\t'+'\t'+'\t' + self.pwmfreq2.text() +'\n'+'\t'+'},'+'\n')
            #PWM3
            if self.pwm3.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "PWM",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.pwmtxt3.text() + '",' +'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t'+ self.pwmspi3.text()+','+'\n'+'\t'+'\t'+'"PWM Pin":'+'\t'+'\t'+'\t' +'"' + self.pwmpin3.text()+'",'+'\n'+'\t'+'\t'+'"PWM Max":'+'\t'+'\t'+'\t' + self.pwmmax3.text()+',' +'\n'+'\t'+'\t'+'"Hardware PWM":'+'\t'+'\t'+'\t' +'"' +  str(self.pwmhw3.isChecked())+'",'+'\n'+'\t'+'\t'+'"Variable Freq":'+'\t'+'\t' +'"' +  str(self.pwmvf3.isChecked())+'",'+'\n'+'\t'+'\t'+'"Perioid SP[i]":'+'\t'+'\t' + self.pwmperiod3.text()+',' +'\n'+'\t'+'\t'+'"Perioid US":'+'\t'+'\t'+'\t' + self.pwmfreq3.text() +'\n'+'\t'+'},'+'\n')
            #PWM4
            if self.pwm4.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "PWM",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.pwmtxt4.text() + '",' +'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t'+ self.pwmspi4.text()+','+'\n'+'\t'+'\t'+'"PWM Pin":'+'\t'+'\t'+'\t' +'"' + self.pwmpin4.text()+'",'+'\n'+'\t'+'\t'+'"PWM Max":'+'\t'+'\t'+'\t' + self.pwmmax4.text()+',' +'\n'+'\t'+'\t'+'"Hardware PWM":'+'\t'+'\t'+'\t' +'"' +  str(self.pwmhw4.isChecked())+'",'+'\n'+'\t'+'\t'+'"Variable Freq":'+'\t'+'\t' +'"' +  str(self.pwmvf4.isChecked())+'",'+'\n'+'\t'+'\t'+'"Perioid SP[i]":'+'\t'+'\t' + self.pwmperiod4.text()+',' +'\n'+'\t'+'\t'+'"Perioid US":'+'\t'+'\t'+'\t' + self.pwmfreq4.text() +'\n'+'\t'+'},'+'\n')
            #PWM5
            if self.pwm5.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "PWM",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.pwmtxt5.text() + '",' +'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t'+ self.pwmspi5.text()+','+'\n'+'\t'+'\t'+'"PWM Pin":'+'\t'+'\t'+'\t' +'"' + self.pwmpin5.text()+'",'+'\n'+'\t'+'\t'+'"PWM Max":'+'\t'+'\t'+'\t' + self.pwmmax5.text()+',' +'\n'+'\t'+'\t'+'"Hardware PWM":'+'\t'+'\t'+'\t' +'"' +  str(self.pwmhw5.isChecked())+'",'+'\n'+'\t'+'\t'+'"Variable Freq":'+'\t'+'\t' +'"' +  str(self.pwmvf5.isChecked())+'",'+'\n'+'\t'+'\t'+'"Perioid SP[i]":'+'\t'+'\t' + self.pwmperiod5.text()+',' +'\n'+'\t'+'\t'+'"Perioid US":'+'\t'+'\t'+'\t' + self.pwmfreq5.text() +'\n'+'\t'+'},'+'\n')
            #PWM6
            if self.pwm6.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "PWM",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.pwmtxt6.text() + '",' +'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t'+ self.pwmspi6.text()+','+'\n'+'\t'+'\t'+'"PWM Pin":'+'\t'+'\t'+'\t' +'"' + self.pwmpin6.text()+'",'+'\n'+'\t'+'\t'+'"PWM Max":'+'\t'+'\t'+'\t' + self.pwmmax6.text()+',' +'\n'+'\t'+'\t'+'"Hardware PWM":'+'\t'+'\t'+'\t' +'"' +  str(self.pwmhw6.isChecked())+'",'+'\n'+'\t'+'\t'+'"Variable Freq":'+'\t'+'\t' +'"' +  str(self.pwmvf6.isChecked())+'",'+'\n'+'\t'+'\t'+'"Perioid SP[i]":'+'\t'+'\t' + self.pwmperiod6.text()+',' +'\n'+'\t'+'\t'+'"Perioid US":'+'\t'+'\t'+'\t' + self.pwmfreq6.text() +'\n'+'\t'+'},'+'\n')
            #Rc Servo
            if self.rcservo.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "RCServo",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.rcservotxt.text() + '",' +'\n'+'\t'+'\t'+'"Servo Pin":'+'\t'+'\t'+'\t'+ '"' + self.rcservopin.text()+'",'+'\n'+'\t'+'\t'+'"SP[i]":'+'\t'+'\t'+'\t' + self.rcservospi.text()+'\n'+'\t'+'},'+'\n')
            #QEM
            if self.qem.isChecked() == 1: 
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "QEI",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ self.qemtxt.text() + '",' +'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.qemstate.currentText()+ '",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ self.qempv.text())
                if self.qeminput.text() == "":
                    f.write('\n'+'\t'+'},'+'\n')
                else:
                    f.write(','+'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' + self.qeminput.text()+','+'\n'+'\t'+'\t'+'"Enable Index":'+'\t'+'\t'+'\t' +'"True"' +'\n'+'\t'+'},'+'\n')
             #Encoder 0
            if self.enc0.isChecked() == 1: 
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "Encoder",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ self.enctxt0.text() + '",' +'\n'+'\t'+'\t'+'"ChA Pin":' +'\t'+'\t'+'\t'+'"'+ self.encapin0.text() + '",' +'\n'+'\t'+'\t'+'"ChB Pin":' +'\t'+'\t'+'\t'+'"'+ self.encbpin0.text() + '",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.encstate0.currentText()+ '",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ self.encpv0.text())
                if self.encinput0.text() == "":
                    f.write('\n'+'\t'+'},'+'\n')
                else:
                    f.write(','+'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' + self.encinput0.text()+','+'\n'+'\t'+'\t'+'"Index Pin":'+'\t'+'\t'+'\t'+'"' + self.encipin0.text()+'"' +'\n'+'\t'+'},'+'\n')
            #Encoder 1
            if self.enc1.isChecked() == 1: 
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "Encoder",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ self.enctxt1.text() + '",' +'\n'+'\t'+'\t'+'"ChA Pin":' +'\t'+'\t'+'\t'+'"'+ self.encapin1.text() + '",' +'\n'+'\t'+'\t'+'"ChB Pin":' +'\t'+'\t'+'\t'+'"'+ self.encbpin1.text() + '",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.encstate1.currentText()+ '",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ self.encpv1.text())
                if self.encinput1.text() == "":
                    f.write('\n'+'\t'+'},'+'\n')
                else:
                    f.write(','+'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' + self.encinput1.text()+','+'\n'+'\t'+'\t'+'"Index Pin":'+'\t'+'\t'+'\t'+'"' + self.encipin1.text()+'"' +'\n'+'\t'+'},'+'\n')   
            #Encoder 2
            if self.enc2.isChecked() == 1: 
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "Encoder",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ self.enctxt2.text() + '",' +'\n'+'\t'+'\t'+'"ChA Pin":' +'\t'+'\t'+'\t'+'"'+ self.encapin2.text() + '",' +'\n'+'\t'+'\t'+'"ChB Pin":' +'\t'+'\t'+'\t'+'"'+ self.encbpin2.text() + '",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.encstate2.currentText()+ '",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ self.encpv2.text())
                if self.encinput2.text() == "":
                    f.write('\n'+'\t'+'},'+'\n')
                else:
                    f.write(','+'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' + self.encinput2.text()+','+'\n'+'\t'+'\t'+'"Index Pin":'+'\t'+'\t'+'\t'+'"' + self.encipin2.text()+'"' +'\n'+'\t'+'},'+'\n')   
            #Encoder 3
            if self.enc3.isChecked() == 1: 
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "Encoder",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ self.enctxt3.text() + '",' +'\n'+'\t'+'\t'+'"ChA Pin":' +'\t'+'\t'+'\t'+'"'+ self.encapin3.text() + '",' +'\n'+'\t'+'\t'+'"ChB Pin":' +'\t'+'\t'+'\t'+'"'+ self.encbpin3.text() + '",'+'\n'+'\t'+'\t'+'"Modifier":'+'\t'+'\t'+'\t'+ '"'+ self.encstate3.currentText()+ '",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ self.encpv3.text())
                if self.encinput3.text() == "":
                    f.write('\n'+'\t'+'},'+'\n')
                else:
                    f.write(','+'\n'+'\t'+'\t'+'"Data Bit":'+'\t'+'\t'+'\t' + self.encinput3.text()+','+'\n'+'\t'+'\t'+'"Index Pin":'+'\t'+'\t'+'\t'+'"' + self.encipin3.text()+'"' +'\n'+'\t'+'},'+'\n')
             #Temp 0
            if self.temp0.isChecked() == 1: 
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Temperature",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ self.temptxt0.text() + '",' +'\n'+'\t'+'\t'+'"PV[i]":' +'\t'+'\t'+'\t'+'"'+ self.temppv0.text() + '",' +'\n'+'\t'+'\t'+'"Sensor":' +'\t'+'\t'+'\t'+'"Thermistor",'+'\n'+'\t'+'\t'+'\t'+'"Thermistor":'+'\n'+'\t'+'\t'+'\t'+'{'+'\n'+'\t'+'\t'+'\t'+'\t'+'"Pin":'+ '\t'+'\t'+'"'+ self.temppin0.text()+'",' +'\n'+'\t'+'\t'+'\t'+'\t'+'"beta":'+ '\t'+'\t'+ self.tempbeta0.text()+',' +'\n'+ '\t'+'\t'+'\t'+'\t'+'"r0":'+ '\t'+'\t'+ self.tempr0.text()+',' +'\n'+'\t'+'\t'+'\t'+'\t'+'"t0":'+ '\t'+'\t'+ self.tempt0.text() +'\n'+ '\t'+'\t'+'\t'+'}'+'\n'+'\t'+'},'+'\n')
            #Temp 1
            if self.temp1.isChecked() == 1: 
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Temperature",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ self.temptxt1.text() + '",' +'\n'+'\t'+'\t'+'"PV[i]":' +'\t'+'\t'+'\t'+'"'+ self.temppv1.text() + '",' +'\n'+'\t'+'\t'+'"Sensor":' +'\t'+'\t'+'\t'+'"Thermistor",'+'\n'+'\t'+'\t'+'\t'+'"Thermistor":'+'\n'+'\t'+'\t'+'\t'+'{'+'\n'+'\t'+'\t'+'\t'+'\t'+'"Pin":'+ '\t'+'\t'+'"'+ self.temppin1.text()+'",' +'\n'+'\t'+'\t'+'\t'+'\t'+'"beta":'+ '\t'+'\t'+ self.tempbeta1.text()+',' +'\n'+ '\t'+'\t'+'\t'+'\t'+'"r1":'+ '\t'+'\t'+ self.tempr1.text()+',' +'\n'+'\t'+'\t'+'\t'+'\t'+'"t1":'+ '\t'+'\t'+ self.tempt1.text() +'\n'+ '\t'+'\t'+'\t'+'}'+'\n'+'\t'+'},'+'\n')
            #Temp 2
            if self.temp2.isChecked() == 1: 
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Temperature",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ self.temptxt2.text() + '",' +'\n'+'\t'+'\t'+'"PV[i]":' +'\t'+'\t'+'\t'+'"'+ self.temppv2.text() + '",' +'\n'+'\t'+'\t'+'"Sensor":' +'\t'+'\t'+'\t'+'"Thermistor",'+'\n'+'\t'+'\t'+'\t'+'"Thermistor":'+'\n'+'\t'+'\t'+'\t'+'{'+'\n'+'\t'+'\t'+'\t'+'\t'+'"Pin":'+ '\t'+'\t'+'"'+ self.temppin2.text()+'",' +'\n'+'\t'+'\t'+'\t'+'\t'+'"beta":'+ '\t'+'\t'+ self.tempbeta2.text()+',' +'\n'+ '\t'+'\t'+'\t'+'\t'+'"r2":'+ '\t'+'\t'+ self.tempr2.text()+',' +'\n'+'\t'+'\t'+'\t'+'\t'+'"t2":'+ '\t'+'\t'+ self.tempt2.text() +'\n'+ '\t'+'\t'+'\t'+'}'+'\n'+'\t'+'},'+'\n')
            #Temp 3
            if self.temp3.isChecked() == 1: 
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Temperature",'+'\n'+'\t'+'\t'+'"Comment":' +'\t'+'\t'+'\t'+'"'+ self.temptxt3.text() + '",' +'\n'+'\t'+'\t'+'"PV[i]":' +'\t'+'\t'+'\t'+'"'+ self.temppv3.text() + '",' +'\n'+'\t'+'\t'+'"Sensor":' +'\t'+'\t'+'\t'+'"Thermistor",'+'\n'+'\t'+'\t'+'\t'+'"Thermistor":'+'\n'+'\t'+'\t'+'\t'+'{'+'\n'+'\t'+'\t'+'\t'+'\t'+'"Pin":'+ '\t'+'\t'+'"'+ self.temppin3.text()+'",' +'\n'+'\t'+'\t'+'\t'+'\t'+'"beta":'+ '\t'+'\t'+ self.tempbeta3.text()+',' +'\n'+ '\t'+'\t'+'\t'+'\t'+'"r3":'+ '\t'+'\t'+ self.tempr3.text()+',' +'\n'+'\t'+'\t'+'\t'+'\t'+'"t3":'+ '\t'+'\t'+ self.tempt3.text() +'\n'+ '\t'+'\t'+'\t'+'}'+'\n'+'\t'+'},'+'\n')
            #swtich 0
            if self.sw0.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Switch",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.swtxt0.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.swpin0.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t'+'"' + self.swmode0.currentText()+'",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ self.swpv0.text()+','+'\n'+'\t'+'\t'+'"SP":'+'\t'+'\t'+'\t'+'\t'+ self.swsp0.text() +'\n'+'\t'+'},'+'\n')
            #swtich 1
            if self.sw1.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Switch",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.swtxt1.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.swpin1.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t'+'"' + self.swmode1.currentText()+'",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ self.swpv1.text()+','+'\n'+'\t'+'\t'+'"SP":'+'\t'+'\t'+'\t'+'\t'+ self.swsp1.text() +'\n'+'\t'+'},'+'\n')
            #swtich 2
            if self.sw2.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Switch",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.swtxt2.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.swpin2.text()+'"'+','+'\n'+'\t'+'\t'+'"Mode":'+'\t'+'\t'+'\t'+'\t'+'"' + self.swmode2.currentText()+'",'+'\n'+'\t'+'\t'+'"PV[i]":'+'\t'+'\t'+'\t'+ self.swpv2.text()+','+'\n'+'\t'+'\t'+'"SP":'+'\t'+'\t'+'\t'+'\t'+ self.swsp2.text() +'\n'+'\t'+'},'+'\n')
            
            
            
            
            
            
            #reset pin this must be last
            f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "Reset Pin",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.resettxt.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+'"'+ self.resetpin.text() +'"' +'\n'+'\t'+'}'+'\n')
            # ending format
            f.write('\t'+']'+'\n'+'}')


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()