from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('remoreconfig.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'save')
        self.button.clicked.connect(self.printButtonPressed) # action
        
        self.button2 = self.findChild(QtWidgets.QPushButton, 'load')
        self.button2.clicked.connect(self.printButtonPressed2) # action
        
        self.setup = self.findChild(QtWidgets.QComboBox, 'setup') 
        self.setup.activated.connect(self.comboboxselected) # action
        
        self.current = self.findChild(QtWidgets.QComboBox, 'boards') 
        self.current.activated.connect(self.comboboxselected2) # action
        
        self.current = self.findChild(QtWidgets.QComboBox, 'xaxistmc') 
        self.current.activated.connect(self.comboboxselected3) # action
        
        self.current = self.findChild(QtWidgets.QComboBox, 'yaxistmc') 
        self.current.activated.connect(self.comboboxselected4) # action
        
        self.current = self.findChild(QtWidgets.QComboBox, 'zaxistmc') 
        self.current.activated.connect(self.comboboxselected5) # action
        
        self.current = self.findChild(QtWidgets.QComboBox, 'e0axistmc') 
        self.current.activated.connect(self.comboboxselected6) # action
        
        self.current = self.findChild(QtWidgets.QComboBox, 'e1axistmc') 
        self.current.activated.connect(self.comboboxselected7) # action

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
        self.xaxiscur = self.findChild(QtWidgets.QLineEdit, 'xaxiscur')
        self.xaxistmc = self.findChild(QtWidgets.QComboBox, 'xaxistmc')
        self.xaxiscursense = self.findChild(QtWidgets.QLineEdit, 'xaxiscursense')
        self.xaxismicrostep = self.findChild(QtWidgets.QLineEdit, 'xaxismicrostep')
        self.xaxisstealthcop = self.findChild(QtWidgets.QComboBox, 'xaxisstealthcop')      
        #y axis
        self.yaxis = self.findChild(QtWidgets.QCheckBox, 'yaxis')
        self.yaxistxt = self.findChild(QtWidgets.QLineEdit, 'yaxistxt')
        self.yaxisjoint = self.findChild(QtWidgets.QLineEdit, 'yaxisjoint')
        self.yaxisstep = self.findChild(QtWidgets.QLineEdit, 'yaxisstep')
        self.yaxisdir = self.findChild(QtWidgets.QLineEdit, 'yaxisdir')
        self.yaxisenable = self.findChild(QtWidgets.QLineEdit, 'yaxisenable')
        self.yaxiscur = self.findChild(QtWidgets.QLineEdit, 'yaxiscur')
        self.yaxistmc = self.findChild(QtWidgets.QComboBox, 'yaxistmc')
        self.yaxiscursense = self.findChild(QtWidgets.QLineEdit, 'yaxiscursense')
        self.yaxismicrostep = self.findChild(QtWidgets.QLineEdit, 'yaxismicrostep')
        self.yaxisstealthcop = self.findChild(QtWidgets.QComboBox, 'yaxisstealthcop')   
        #z axis
        self.zaxis = self.findChild(QtWidgets.QCheckBox, 'zaxis')
        self.zaxistxt = self.findChild(QtWidgets.QLineEdit, 'zaxistxt')
        self.zaxisjoint = self.findChild(QtWidgets.QLineEdit, 'zaxisjoint')
        self.zaxisstep = self.findChild(QtWidgets.QLineEdit, 'zaxisstep')
        self.zaxisdir = self.findChild(QtWidgets.QLineEdit, 'zaxisdir')
        self.zaxisenable = self.findChild(QtWidgets.QLineEdit, 'zaxisenable')
        self.zaxiscur = self.findChild(QtWidgets.QLineEdit, 'zaxiscur')
        self.zaxistmc = self.findChild(QtWidgets.QComboBox, 'zaxistmc')
        self.zaxiscursense = self.findChild(QtWidgets.QLineEdit, 'zaxiscursense')
        self.zaxismicrostep = self.findChild(QtWidgets.QLineEdit, 'zaxismicrostep')
        self.zaxisstealthcop = self.findChild(QtWidgets.QComboBox, 'zaxisstealthcop')   
        #e0 axis
        self.e0axis = self.findChild(QtWidgets.QCheckBox, 'e0axis')
        self.e0axistxt = self.findChild(QtWidgets.QLineEdit, 'e0axistxt')
        self.e0axisjoint = self.findChild(QtWidgets.QLineEdit, 'e0axisjoint')
        self.e0axisstep = self.findChild(QtWidgets.QLineEdit, 'e0axisstep')
        self.e0axisdir = self.findChild(QtWidgets.QLineEdit, 'e0axisdir')
        self.e0axisenable = self.findChild(QtWidgets.QLineEdit, 'e0axisenable')
        self.e0axiscur = self.findChild(QtWidgets.QLineEdit, 'e0axiscur')
        self.e0axistmc = self.findChild(QtWidgets.QComboBox, 'e0axistmc')
        self.e0axiscursense = self.findChild(QtWidgets.QLineEdit, 'e0axiscursense')
        self.e0axismicrostep = self.findChild(QtWidgets.QLineEdit, 'e0axismicrostep')
        self.e0axisstealthcop = self.findChild(QtWidgets.QComboBox, 'e0axisstealthcop')   
        #e1 axis
        self.e1axis = self.findChild(QtWidgets.QCheckBox, 'e1axis')
        self.e1axistxt = self.findChild(QtWidgets.QLineEdit, 'e1axistxt')
        self.e1axisjoint = self.findChild(QtWidgets.QLineEdit, 'e1axisjoint')
        self.e1axisstep = self.findChild(QtWidgets.QLineEdit, 'e1axisstep')
        self.e1axisdir = self.findChild(QtWidgets.QLineEdit, 'e1axisdir')
        self.e1axisenable = self.findChild(QtWidgets.QLineEdit, 'e1axisenable')
        self.e1axiscur = self.findChild(QtWidgets.QLineEdit, 'e1axiscur')
        self.e1axistmc = self.findChild(QtWidgets.QComboBox, 'e1axistmc')
        self.e1axiscursense = self.findChild(QtWidgets.QLineEdit, 'e1axiscursense')
        self.e1axismicrostep = self.findChild(QtWidgets.QLineEdit, 'e1axismicrostep')
        self.e1axisstealthcop = self.findChild(QtWidgets.QComboBox, 'e1axisstealthcop')   
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
        self.qemcha = self.findChild(QtWidgets.QLineEdit, 'qemapin')
        self.qemchb = self.findChild(QtWidgets.QLineEdit, 'qembpin')
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
        #hide elements not needed on startup
        #X axis
        self.xaxiscur.setEnabled(0)
        self.xaxiscur.setVisible(0)
        self.xaxiscursense.setEnabled(0)
        self.xaxiscursense.setVisible(0)
        self.xaxismicrostep.setEnabled(0)
        self.xaxismicrostep.setVisible(0)
        self.xaxisstealthcop.setEnabled(0)
        self.xaxisstealthcop.setVisible(0)
        #y axis
        self.yaxiscur.setEnabled(0)
        self.yaxiscur.setVisible(0)
        self.yaxiscursense.setEnabled(0)
        self.yaxiscursense.setVisible(0)
        self.yaxismicrostep.setEnabled(0)
        self.yaxismicrostep.setVisible(0)
        self.yaxisstealthcop.setEnabled(0)
        self.yaxisstealthcop.setVisible(0)
        #Z axis
        self.zaxiscur.setEnabled(0)
        self.zaxiscur.setVisible(0)
        self.zaxiscursense.setEnabled(0)
        self.zaxiscursense.setVisible(0)
        self.zaxismicrostep.setEnabled(0)
        self.zaxismicrostep.setVisible(0)
        self.zaxisstealthcop.setEnabled(0)
        self.zaxisstealthcop.setVisible(0)
        #e0 axis
        self.e0axiscur.setEnabled(0)
        self.e0axiscur.setVisible(0)
        self.e0axiscursense.setEnabled(0)
        self.e0axiscursense.setVisible(0)
        self.e0axismicrostep.setEnabled(0)
        self.e0axismicrostep.setVisible(0)
        self.e0axisstealthcop.setEnabled(0)
        self.e0axisstealthcop.setVisible(0)
        #e1 axis
        self.e1axiscur.setEnabled(0)
        self.e1axiscur.setVisible(0)
        self.e1axiscursense.setEnabled(0)
        self.e1axiscursense.setVisible(0)
        self.e1axismicrostep.setEnabled(0)
        self.e1axismicrostep.setVisible(0)
        self.e1axisstealthcop.setEnabled(0)
        self.e1axisstealthcop.setVisible(0)
        
    def comboboxselected2(self):
        if self.boards.currentText() == "MKS SBASE v1.3":
            self.xaxiscur.setEnabled(1)
            self.xaxiscur.setVisible(1)
            self.yaxiscur.setEnabled(1)
            self.yaxiscur.setVisible(1)
            self.zaxiscur.setEnabled(1)
            self.zaxiscur.setVisible(1)
            self.e0axiscur.setEnabled(1)
            self.e0axiscur.setVisible(1)
            self.e1axiscur.setEnabled(1)
            self.e1axiscur.setVisible(1)
        else:
            self.xaxiscur.setEnabled(0)
            self.xaxiscur.setVisible(0)
            self.yaxiscur.setEnabled(0)
            self.yaxiscur.setVisible(0)
            self.zaxiscur.setEnabled(0)
            self.zaxiscur.setVisible(0)
            self.e0axiscur.setEnabled(0)
            self.e0axiscur.setVisible(0)
            self.e1axiscur.setEnabled(0)
            self.e1axiscur.setVisible(0)
            
    def comboboxselected3(self): # x axis hide 
        if self.xaxistmc.currentText() == "None":
            self.xaxiscur.setEnabled(0)
            self.xaxiscur.setVisible(0)
            self.xaxiscursense.setEnabled(0)
            self.xaxiscursense.setVisible(0)
            self.xaxismicrostep.setEnabled(0)
            self.xaxismicrostep.setVisible(0)
            self.xaxisstealthcop.setEnabled(0)
            self.xaxisstealthcop.setVisible(0)
 
        else:
            self.xaxiscur.setEnabled(1)
            self.xaxiscur.setVisible(1)
            self.xaxiscursense.setEnabled(1)
            self.xaxiscursense.setVisible(1)
            self.xaxismicrostep.setEnabled(1)
            self.xaxismicrostep.setVisible(1)
            self.xaxisstealthcop.setEnabled(1)
            self.xaxisstealthcop.setVisible(1)
            
    def comboboxselected4(self): # y axis hide
        if self.yaxistmc.currentText() == "None":
            self.yaxiscur.setEnabled(0)
            self.yaxiscur.setVisible(0)
            self.yaxiscursense.setEnabled(0)
            self.yaxiscursense.setVisible(0)
            self.yaxismicrostep.setEnabled(0)
            self.yaxismicrostep.setVisible(0)
            self.yaxisstealthcop.setEnabled(0)
            self.yaxisstealthcop.setVisible(0)
 
        else:
            self.yaxiscur.setEnabled(1)
            self.yaxiscur.setVisible(1)
            self.yaxiscursense.setEnabled(1)
            self.yaxiscursense.setVisible(1)
            self.yaxismicrostep.setEnabled(1)
            self.yaxismicrostep.setVisible(1)
            self.yaxisstealthcop.setEnabled(1)
            self.yaxisstealthcop.setVisible(1)
            
    def comboboxselected5(self): # z axis hide
        if self.zaxistmc.currentText() == "None":
            self.zaxiscur.setEnabled(0)
            self.zaxiscur.setVisible(0)
            self.zaxiscursense.setEnabled(0)
            self.zaxiscursense.setVisible(0)
            self.zaxismicrostep.setEnabled(0)
            self.zaxismicrostep.setVisible(0)
            self.zaxisstealthcop.setEnabled(0)
            self.zaxisstealthcop.setVisible(0)
 
        else:
            self.zaxiscur.setEnabled(1)
            self.zaxiscur.setVisible(1)
            self.zaxiscursense.setEnabled(1)
            self.zaxiscursense.setVisible(1)
            self.zaxismicrostep.setEnabled(1)
            self.zaxismicrostep.setVisible(1)
            self.zaxisstealthcop.setEnabled(1)
            self.zaxisstealthcop.setVisible(1)
            
    def comboboxselected6(self): # e0 axis hide
        if self.e0axistmc.currentText() == "None":
            self.e0axiscur.setEnabled(0)
            self.e0axiscur.setVisible(0)
            self.e0axiscursense.setEnabled(0)
            self.e0axiscursense.setVisible(0)
            self.e0axismicrostep.setEnabled(0)
            self.e0axismicrostep.setVisible(0)
            self.e0axisstealthcop.setEnabled(0)
            self.e0axisstealthcop.setVisible(0)
 
        else:
            self.e0axiscur.setEnabled(1)
            self.e0axiscur.setVisible(1)
            self.e0axiscursense.setEnabled(1)
            self.e0axiscursense.setVisible(1)
            self.e0axismicrostep.setEnabled(1)
            self.e0axismicrostep.setVisible(1)
            self.e0axisstealthcop.setEnabled(1)
            self.e0axisstealthcop.setVisible(1)
            
    def comboboxselected7(self): # e1 axis hide
        if self.e1axistmc.currentText() == "None":
            self.e1axiscur.setEnabled(0)
            self.e1axiscur.setVisible(0)
            self.e1axiscursense.setEnabled(0)
            self.e1axiscursense.setVisible(0)
            self.e1axismicrostep.setEnabled(0)
            self.e1axismicrostep.setVisible(0)
            self.e1axisstealthcop.setEnabled(0)
            self.e1axisstealthcop.setVisible(0)
 
        else:
            self.e1axiscur.setEnabled(1)
            self.e1axiscur.setVisible(1)
            self.e1axiscursense.setEnabled(1)
            self.e1axiscursense.setVisible(1)
            self.e1axismicrostep.setEnabled(1)
            self.e1axismicrostep.setVisible(1)
            self.e1axisstealthcop.setEnabled(1)
            self.e1axisstealthcop.setVisible(1)            
        
    def comboboxselected(self):
        if self.setup.currentText() == "None":
        #axis setup
            self.xaxis.setChecked(0),self.xaxistxt.setText(""),self.xaxisjoint.setText(""),self.xaxisstep.setText(""),self.xaxisdir.setText(""),self.xaxisenable.setText("") ,self.xaxistmc.setCurrentText("None")
            self.yaxis.setChecked(0),self.yaxistxt.setText(""),self.yaxisjoint.setText(""),self.yaxisstep.setText(""),self.yaxisdir.setText(""),self.yaxisenable.setText("") ,self.yaxistmc.setCurrentText("None")
            self.zaxis.setChecked(0),self.zaxistxt.setText(""),self.zaxisjoint.setText(""),self.zaxisstep.setText(""),self.zaxisdir.setText(""),self.zaxisenable.setText(""),self.zaxistmc.setCurrentText("None")
            self.e0axis.setChecked(0),self.e0axistxt.setText(""),self.e0axisjoint.setText(""),self.e0axisstep.setText(""),self.e0axisdir.setText(""),self.e0axisenable.setText("") ,self.e0axistmc.setCurrentText("None")
            self.e1axis.setChecked(0),self.e1axistxt.setText(""),self.e1axisjoint.setText(""),self.e1axisstep.setText(""),self.e1axisdir.setText(""),self.e1axisenable.setText("") ,self.e1axistmc.setCurrentText("None")
            #output setup
            self.outchk0.setChecked(0),self.outtxt0.setText(""),self.outpin0.setText(""),self.outstate0.setCurrentText("Pull None")
            self.outchk1.setChecked(0),self.outtxt1.setText(""),self.outpin1.setText(""),self.outstate1.setCurrentText("Pull None")
            self.outchk2.setChecked(0),self.outtxt2.setText(""),self.outpin2.setText(""),self.outstate2.setCurrentText("Pull None")
            self.outchk3.setChecked(0),self.outtxt3.setText(""),self.outpin3.setText(""),self.outstate3.setCurrentText("Pull None")
            self.outchk4.setChecked(0),self.outtxt4.setText(""),self.outpin4.setText(""),self.outstate4.setCurrentText("Pull None")
            self.outchk5.setChecked(0),self.outtxt5.setText(""),self.outpin5.setText(""),self.outstate5.setCurrentText("Pull None")
            self.outchk6.setChecked(0),self.outtxt6.setText(""),self.outpin6.setText(""),self.outstate6.setCurrentText("Pull None")
            self.outchk7.setChecked(0),self.outtxt7.setText(""),self.outpin7.setText(""),self.outstate7.setCurrentText("Pull None")
            #Input setup
            self.inchk0.setChecked(0),self.intxt0.setText(""),self.inpin0.setText(""),self.instate0.setCurrentText("Pull None")
            self.inchk1.setChecked(0),self.intxt1.setText(""),self.inpin1.setText(""),self.instate1.setCurrentText("Pull None")
            self.inchk2.setChecked(0),self.intxt2.setText(""),self.inpin2.setText(""),self.instate2.setCurrentText("Pull None")
            self.inchk3.setChecked(0),self.intxt3.setText(""),self.inpin3.setText(""),self.instate3.setCurrentText("Pull None")
            self.inchk4.setChecked(0),self.intxt4.setText(""),self.inpin4.setText(""),self.instate4.setCurrentText("Pull None")
            self.inchk5.setChecked(0),self.intxt5.setText(""),self.inpin5.setText(""),self.instate5.setCurrentText("Pull None")
            self.inchk6.setChecked(0),self.intxt6.setText(""),self.inpin6.setText(""),self.instate6.setCurrentText("Pull None")
            self.inchk7.setChecked(0),self.intxt7.setText(""),self.inpin7.setText(""),self.instate7.setCurrentText("Pull None")
            self.estop.setChecked(0),self.estoptxt.setText(""),self.estoppin.setText("")
            #Pwm Setup
            self.pwm0.setChecked(0),self.pwmtxt0.setText(""),self.pwmmax0.setText(""),self.pwmpin0.setText(""),self.pwmhw0.setChecked(0),self.pwmvf0.setChecked(0),self.pwmperiod0.setText(""),self.pwmfreq0.setText("")
            self.pwm1.setChecked(0),self.pwmtxt1.setText(""),self.pwmmax1.setText(""),self.pwmpin1.setText(""),self.pwmhw1.setChecked(0),self.pwmvf1.setChecked(0),self.pwmperiod1.setText(""),self.pwmfreq1.setText("")
            self.pwm2.setChecked(0),self.pwmtxt2.setText(""),self.pwmmax2.setText(""),self.pwmpin2.setText(""),self.pwmhw2.setChecked(0),self.pwmvf2.setChecked(0),self.pwmperiod2.setText(""),self.pwmfreq2.setText("")
            self.pwm3.setChecked(0),self.pwmtxt3.setText(""),self.pwmmax3.setText(""),self.pwmpin3.setText(""),self.pwmhw3.setChecked(0),self.pwmvf3.setChecked(0),self.pwmperiod3.setText(""),self.pwmfreq3.setText("")
            self.pwm4.setChecked(0),self.pwmtxt4.setText(""),self.pwmmax4.setText(""),self.pwmpin4.setText(""),self.pwmhw4.setChecked(0),self.pwmvf4.setChecked(0),self.pwmperiod4.setText(""),self.pwmfreq4.setText("")
            self.pwm5.setChecked(0),self.pwmtxt5.setText(""),self.pwmmax5.setText(""),self.pwmpin5.setText(""),self.pwmhw5.setChecked(0),self.pwmvf5.setChecked(0),self.pwmperiod5.setText(""),self.pwmfreq5.setText("")
            self.pwm6.setChecked(0),self.pwmtxt6.setText(""),self.pwmmax6.setText(""),self.pwmpin6.setText(""),self.pwmhw6.setChecked(0),self.pwmvf6.setChecked(0),self.pwmperiod6.setText(""),self.pwmfreq6.setText("")
            self.rcservo.setChecked(0),self.rcservotxt.setText(""),self.rcservopin.setText("")
            #Encoder Setup
            self.qem.setChecked(0),self.qemtxt.setText(""),self.qeminput.setText(""),self.qemstate.setCurrentText("Pull None"),self.qempv.setText("")
            self.enc0.setChecked(0),self.enctxt0.setText(""),self.encapin0.setText(""),self.encbpin0.setText(""),self.encpv0.setText(""),self.encstate0.setCurrentText("Pull None"),self.encipin0.setText(""),self.encinput0.setText("")
            self.enc1.setChecked(0),self.enctxt1.setText(""),self.encapin1.setText(""),self.encbpin1.setText(""),self.encpv1.setText(""),self.encstate1.setCurrentText("Pull None"),self.encipin1.setText(""),self.encinput1.setText("")
            self.enc2.setChecked(0),self.enctxt2.setText(""),self.encapin2.setText(""),self.encbpin2.setText(""),self.encpv2.setText(""),self.encstate2.setCurrentText("Pull None"),self.encipin2.setText(""),self.encinput2.setText("")
            self.enc3.setChecked(0),self.enctxt3.setText(""),self.encapin3.setText(""),self.encbpin3.setText(""),self.encpv3.setText(""),self.encstate3.setCurrentText("Pull None"),self.encipin3.setText(""),self.encinput3.setText("")
            #Temp switch setup
            self.temp0.setChecked(0),self.temptxt0.setText(""),self.temppin0.setText(""),self.temppv0.setText(""),self.tempbeta0.setText(""),self.tempr0.setText(""),self.tempt0.setText("")
            self.temp1.setChecked(0),self.temptxt1.setText(""),self.temppin1.setText(""),self.temppv1.setText(""),self.tempbeta1.setText(""),self.tempr1.setText(""),self.tempt1.setText("")
            self.temp2.setChecked(0),self.temptxt2.setText(""),self.temppin2.setText(""),self.temppv2.setText(""),self.tempbeta2.setText(""),self.tempr2.setText(""),self.tempt2.setText("")
            self.temp3.setChecked(0),self.temptxt3.setText(""),self.temppin3.setText(""),self.temppv3.setText(""),self.tempbeta3.setText(""),self.tempr3.setText(""),self.tempt3.setText("")
            self.sw0.setChecked(0),self.swpin0.setText(""),self.swpv0.setText(""),self.swtxt0.setText(""),self.swsp0.setText(""),self.swmode0.setCurrentText("On")
            self.sw1.setChecked(0),self.swpin1.setText(""),self.swpv1.setText(""),self.swtxt1.setText(""),self.swsp1.setText(""),self.swmode1.setCurrentText("On")
            self.sw2.setChecked(0),self.swpin2.setText(""),self.swpv2.setText(""),self.swtxt2.setText(""),self.swsp2.setText(""),self.swmode2.setCurrentText("On")
            
        if self.setup.currentText() == "Mill XYZ":
        #axis setup
            self.xaxis.setChecked(1),self.xaxistxt.setText("x axis"),self.xaxisjoint.setText("0"),self.xaxisstep.setText("2.2"),self.xaxisdir.setText("2.6"),self.xaxisenable.setText("2.1") ,self.xaxistmc.setCurrentText("None")
            self.yaxis.setChecked(1),self.yaxistxt.setText("y axis"),self.yaxisjoint.setText("1"),self.yaxisstep.setText("0.19"),self.yaxisdir.setText("0.20"),self.yaxisenable.setText("2.8"),self.yaxistmc.setCurrentText("None")
            self.zaxis.setChecked(1),self.zaxistxt.setText("z axis"),self.zaxisjoint.setText("2"),self.zaxisstep.setText("0.22"),self.zaxisdir.setText("2.11"),self.zaxisenable.setText("0.21") ,self.zaxistmc.setCurrentText("None")
            self.e0axis.setChecked(0),self.e0axistxt.setText(""),self.e0axisjoint.setText(""),self.e0axisstep.setText(""),self.e0axisdir.setText(""),self.e0axisenable.setText("") ,self.e0axistmc.setCurrentText("None")
            self.e1axis.setChecked(0),self.e1axistxt.setText(""),self.e1axisjoint.setText(""),self.e1axisstep.setText(""),self.e1axisdir.setText(""),self.e1axisenable.setText("") ,self.e1axistmc.setCurrentText("None")

            #Output setup
            self.outchk0.setChecked(1),self.outtxt0.setText("spindle relay"),self.outpin0.setText("2.5"),self.outstate0.setCurrentText("Pull None"),self.outinv0.setChecked(0)
            self.outchk1.setChecked(0),self.outtxt1.setText(""),self.outpin1.setText(""),self.outstate1.setCurrentText("Pull None")
            self.outchk2.setChecked(0),self.outtxt2.setText(""),self.outpin2.setText(""),self.outstate2.setCurrentText("Pull None")
            self.outchk3.setChecked(0),self.outtxt3.setText(""),self.outpin3.setText(""),self.outstate3.setCurrentText("Pull None")
            self.outchk4.setChecked(0),self.outtxt4.setText(""),self.outpin4.setText(""),self.outstate4.setCurrentText("Pull None")
            self.outchk5.setChecked(0),self.outtxt5.setText(""),self.outpin5.setText(""),self.outstate5.setCurrentText("Pull None")
            self.outchk6.setChecked(0),self.outtxt6.setText(""),self.outpin6.setText(""),self.outstate6.setCurrentText("Pull None")
            self.outchk7.setChecked(0),self.outtxt7.setText(""),self.outpin7.setText(""),self.outstate7.setCurrentText("Pull None")
            #Input Setup
            self.inchk0.setChecked(1),self.intxt0.setText("X - limit / home"),self.inpin0.setText("1.29"),self.instate0.setCurrentText("Pull Up"),self.ininv0.setChecked(0)
            self.inchk1.setChecked(1),self.intxt1.setText("Y - limit / home"),self.inpin1.setText("1.28"),self.instate1.setCurrentText("Pull Up"),self.ininv1.setChecked(0)
            self.inchk2.setChecked(1),self.intxt2.setText("Z - limit / home"),self.inpin2.setText("1.27"),self.instate2.setCurrentText("Pull Up"),self.ininv2.setChecked(0)
            self.estop.setChecked(1),self.estoptxt.setText("E-stop"),self.estoppin.setText("1.0")
            self.inchk3.setChecked(0),self.intxt3.setText(""),self.inpin3.setText(""),self.instate3.setCurrentText("Pull None")
            self.inchk4.setChecked(0),self.intxt4.setText(""),self.inpin4.setText(""),self.instate4.setCurrentText("Pull None")
            self.inchk5.setChecked(0),self.intxt5.setText(""),self.inpin5.setText(""),self.instate5.setCurrentText("Pull None")
            self.inchk6.setChecked(0),self.intxt6.setText(""),self.inpin6.setText(""),self.instate6.setCurrentText("Pull None")
            self.inchk7.setChecked(0),self.intxt7.setText(""),self.inpin7.setText(""),self.instate7.setCurrentText("Pull None")
            #PWM setup
            self.pwm0.setChecked(0),self.pwmtxt0.setText(""),self.pwmmax0.setText(""),self.pwmpin0.setText(""),self.pwmhw0.setChecked(0),self.pwmvf0.setChecked(0),self.pwmperiod0.setText(""),self.pwmfreq0.setText("")
            self.pwm1.setChecked(0),self.pwmtxt1.setText(""),self.pwmmax1.setText(""),self.pwmpin1.setText(""),self.pwmhw1.setChecked(0),self.pwmvf1.setChecked(0),self.pwmperiod1.setText(""),self.pwmfreq1.setText("")
            self.pwm2.setChecked(0),self.pwmtxt2.setText(""),self.pwmmax2.setText(""),self.pwmpin2.setText(""),self.pwmhw2.setChecked(0),self.pwmvf2.setChecked(0),self.pwmperiod2.setText(""),self.pwmfreq2.setText("")
            self.pwm3.setChecked(0),self.pwmtxt3.setText(""),self.pwmmax3.setText(""),self.pwmpin3.setText(""),self.pwmhw3.setChecked(0),self.pwmvf3.setChecked(0),self.pwmperiod3.setText(""),self.pwmfreq3.setText("")
            self.pwm4.setChecked(0),self.pwmtxt4.setText(""),self.pwmmax4.setText(""),self.pwmpin4.setText(""),self.pwmhw4.setChecked(0),self.pwmvf4.setChecked(0),self.pwmperiod4.setText(""),self.pwmfreq4.setText("")
            self.pwm5.setChecked(0),self.pwmtxt5.setText(""),self.pwmmax5.setText(""),self.pwmpin5.setText(""),self.pwmhw5.setChecked(0),self.pwmvf5.setChecked(0),self.pwmperiod5.setText(""),self.pwmfreq5.setText("")
            self.pwm6.setChecked(0),self.pwmtxt6.setText(""),self.pwmmax6.setText(""),self.pwmpin6.setText(""),self.pwmhw6.setChecked(0),self.pwmvf6.setChecked(0),self.pwmperiod6.setText(""),self.pwmfreq6.setText("")
            self.rcservo.setChecked(0),self.rcservotxt.setText(""),self.rcservopin.setText("")
            #Encoder setup
            self.qem.setChecked(0),self.qemtxt.setText(""),self.qeminput.setText(""),self.qemstate.setCurrentText("Pull None"),self.qempv.setText("")
            self.enc0.setChecked(0),self.enctxt0.setText(""),self.encapin0.setText(""),self.encbpin0.setText(""),self.encpv0.setText(""),self.encstate0.setCurrentText("Pull None"),self.encipin0.setText(""),self.encinput0.setText("")
            self.enc1.setChecked(0),self.enctxt1.setText(""),self.encapin1.setText(""),self.encbpin1.setText(""),self.encpv1.setText(""),self.encstate1.setCurrentText("Pull None"),self.encipin1.setText(""),self.encinput1.setText("")
            self.enc2.setChecked(0),self.enctxt2.setText(""),self.encapin2.setText(""),self.encbpin2.setText(""),self.encpv2.setText(""),self.encstate2.setCurrentText("Pull None"),self.encipin2.setText(""),self.encinput2.setText("")
            self.enc3.setChecked(0),self.enctxt3.setText(""),self.encapin3.setText(""),self.encbpin3.setText(""),self.encpv3.setText(""),self.encstate3.setCurrentText("Pull None"),self.encipin3.setText(""),self.encinput3.setText("")
            #temp swtich setup
            self.temp0.setChecked(0),self.temptxt0.setText(""),self.temppin0.setText(""),self.temppv0.setText(""),self.tempbeta0.setText(""),self.tempr0.setText(""),self.tempt0.setText("")
            self.temp1.setChecked(0),self.temptxt1.setText(""),self.temppin1.setText(""),self.temppv1.setText(""),self.tempbeta1.setText(""),self.tempr1.setText(""),self.tempt1.setText("")
            self.temp2.setChecked(0),self.temptxt2.setText(""),self.temppin2.setText(""),self.temppv2.setText(""),self.tempbeta2.setText(""),self.tempr2.setText(""),self.tempt2.setText("")
            self.temp3.setChecked(0),self.temptxt3.setText(""),self.temppin3.setText(""),self.temppv3.setText(""),self.tempbeta3.setText(""),self.tempr3.setText(""),self.tempt3.setText("")
            self.sw0.setChecked(0),self.swpin0.setText(""),self.swpv0.setText(""),self.swtxt0.setText(""),self.swsp0.setText(""),self.swmode0.setCurrentText("On")
            self.sw1.setChecked(0),self.swpin1.setText(""),self.swpv1.setText(""),self.swtxt1.setText(""),self.swsp1.setText(""),self.swmode1.setCurrentText("On")
            self.sw2.setChecked(0),self.swpin2.setText(""),self.swpv2.setText(""),self.swtxt2.setText(""),self.swsp2.setText(""),self.swmode2.setCurrentText("On")
            
        if self.setup.currentText() == "Mill XYZ +spindle encoder +VFD":
        #axis setup
            self.xaxis.setChecked(1),self.xaxistxt.setText("x axis"),self.xaxisjoint.setText("0"),self.xaxisstep.setText("2.2"),self.xaxisdir.setText("2.6"),self.xaxisenable.setText("2.1") ,self.xaxistmc.setCurrentText("None")
            self.yaxis.setChecked(1),self.yaxistxt.setText("y axis"),self.yaxisjoint.setText("1"),self.yaxisstep.setText("0.19"),self.yaxisdir.setText("0.20"),self.yaxisenable.setText("2.8") ,self.yaxistmc.setCurrentText("None")
            self.zaxis.setChecked(1),self.zaxistxt.setText("z axis"),self.zaxisjoint.setText("2"),self.zaxisstep.setText("0.22"),self.zaxisdir.setText("2.11"),self.zaxisenable.setText("0.21") ,self.zaxistmc.setCurrentText("None")
            self.e0axis.setChecked(0),self.e0axistxt.setText(""),self.e0axisjoint.setText(""),self.e0axisstep.setText(""),self.e0axisdir.setText(""),self.e0axisenable.setText("") ,self.e0axistmc.setCurrentText("None")
            self.e1axis.setChecked(0),self.e1axistxt.setText(""),self.e1axisjoint.setText(""),self.e1axisstep.setText(""),self.e1axisdir.setText(""),self.e1axisenable.setText("") ,self.e1axistmc.setCurrentText("None")
            #Output setup
            self.outchk0.setChecked(1),self.outtxt0.setText("spindle enable"),self.outpin0.setText("2.5"),self.outstate0.setCurrentText("Pull None"),self.outinv0.setChecked(0)
            self.outchk1.setChecked(0),self.outtxt1.setText(""),self.outpin1.setText(""),self.outstate1.setCurrentText("Pull None")
            self.outchk2.setChecked(0),self.outtxt2.setText(""),self.outpin2.setText(""),self.outstate2.setCurrentText("Pull None")
            self.outchk3.setChecked(0),self.outtxt3.setText(""),self.outpin3.setText(""),self.outstate3.setCurrentText("Pull None")
            self.outchk4.setChecked(0),self.outtxt4.setText(""),self.outpin4.setText(""),self.outstate4.setCurrentText("Pull None")
            self.outchk5.setChecked(0),self.outtxt5.setText(""),self.outpin5.setText(""),self.outstate5.setCurrentText("Pull None")
            self.outchk6.setChecked(0),self.outtxt6.setText(""),self.outpin6.setText(""),self.outstate6.setCurrentText("Pull None")
            self.outchk7.setChecked(0),self.outtxt7.setText(""),self.outpin7.setText(""),self.outstate7.setCurrentText("Pull None")
            #Input Setup
            self.inchk0.setChecked(1),self.intxt0.setText("X - limit / home"),self.inpin0.setText("1.29"),self.instate0.setCurrentText("Pull Up"),self.ininv0.setChecked(0)
            self.inchk1.setChecked(1),self.intxt1.setText("Y - limit / home"),self.inpin1.setText("1.28"),self.instate1.setCurrentText("Pull Up"),self.ininv1.setChecked(0)
            self.inchk2.setChecked(1),self.intxt2.setText("Z - limit / home"),self.inpin2.setText("1.27"),self.instate2.setCurrentText("Pull Up"),self.ininv2.setChecked(0)
            self.estop.setChecked(1),self.estoptxt.setText("E-stop"),self.estoppin.setText("1.0")
            self.inchk3.setChecked(0),self.intxt3.setText(""),self.inpin3.setText(""),self.instate3.setCurrentText("Pull None")
            self.inchk4.setChecked(0),self.intxt4.setText(""),self.inpin4.setText(""),self.instate4.setCurrentText("Pull None")
            self.inchk5.setChecked(0),self.intxt5.setText(""),self.inpin5.setText(""),self.instate5.setCurrentText("Pull None")
            self.inchk6.setChecked(0),self.intxt6.setText(""),self.inpin6.setText(""),self.instate6.setCurrentText("Pull None")
            self.inchk7.setChecked(0),self.intxt7.setText(""),self.inpin7.setText(""),self.instate7.setCurrentText("Pull None")
            self.estop.setChecked(1),self.estoptxt.setText("E-stop"),self.estoppin.setText("1.0")
            #PWM setup
            self.pwm0.setChecked(1),self.pwmtxt0.setText("0-10v signal"),self.pwmmax0.setText("256"),self.pwmpin0.setText("1.24"),self.pwmhw0.setChecked(1),self.pwmvf0.setChecked(1),self.pwmperiod0.setText("1"),self.pwmfreq0.setText("200")
            self.pwm1.setChecked(0),self.pwmtxt1.setText(""),self.pwmmax1.setText(""),self.pwmpin1.setText(""),self.pwmhw1.setChecked(0),self.pwmvf1.setChecked(0),self.pwmperiod1.setText(""),self.pwmfreq1.setText("")
            self.pwm2.setChecked(0),self.pwmtxt2.setText(""),self.pwmmax2.setText(""),self.pwmpin2.setText(""),self.pwmhw2.setChecked(0),self.pwmvf2.setChecked(0),self.pwmperiod2.setText(""),self.pwmfreq2.setText("")
            self.pwm3.setChecked(0),self.pwmtxt3.setText(""),self.pwmmax3.setText(""),self.pwmpin3.setText(""),self.pwmhw3.setChecked(0),self.pwmvf3.setChecked(0),self.pwmperiod3.setText(""),self.pwmfreq3.setText("")
            self.pwm4.setChecked(0),self.pwmtxt4.setText(""),self.pwmmax4.setText(""),self.pwmpin4.setText(""),self.pwmhw4.setChecked(0),self.pwmvf4.setChecked(0),self.pwmperiod4.setText(""),self.pwmfreq4.setText("")
            self.pwm5.setChecked(0),self.pwmtxt5.setText(""),self.pwmmax5.setText(""),self.pwmpin5.setText(""),self.pwmhw5.setChecked(0),self.pwmvf5.setChecked(0),self.pwmperiod5.setText(""),self.pwmfreq5.setText("")
            self.pwm6.setChecked(0),self.pwmtxt6.setText(""),self.pwmmax6.setText(""),self.pwmpin6.setText(""),self.pwmhw6.setChecked(0),self.pwmvf6.setChecked(0),self.pwmperiod6.setText(""),self.pwmfreq6.setText("")
            self.rcservo.setChecked(0),self.rcservotxt.setText(""),self.rcservopin.setText("")
            #Encoder setup
            self.qem.setChecked(1),self.qemtxt.setText("Spindle encoder"),self.qeminput.setText("7"),self.qemstate.setCurrentText("Pull Up"),self.qempv.setText("0")
            self.enc0.setChecked(0),self.enctxt0.setText(""),self.encapin0.setText(""),self.encbpin0.setText(""),self.encpv0.setText(""),self.encstate0.setCurrentText("Pull None"),self.encipin0.setText(""),self.encinput0.setText("")
            self.enc1.setChecked(0),self.enctxt1.setText(""),self.encapin1.setText(""),self.encbpin1.setText(""),self.encpv1.setText(""),self.encstate1.setCurrentText("Pull None"),self.encipin1.setText(""),self.encinput1.setText("")
            self.enc2.setChecked(0),self.enctxt2.setText(""),self.encapin2.setText(""),self.encbpin2.setText(""),self.encpv2.setText(""),self.encstate2.setCurrentText("Pull None"),self.encipin2.setText(""),self.encinput2.setText("")
            self.enc3.setChecked(0),self.enctxt3.setText(""),self.encapin3.setText(""),self.encbpin3.setText(""),self.encpv3.setText(""),self.encstate3.setCurrentText("Pull None"),self.encipin3.setText(""),self.encinput3.setText("")
            #temp swtich setup
            self.temp0.setChecked(0),self.temptxt0.setText(""),self.temppin0.setText(""),self.temppv0.setText(""),self.tempbeta0.setText(""),self.tempr0.setText(""),self.tempt0.setText("")
            self.temp1.setChecked(0),self.temptxt1.setText(""),self.temppin1.setText(""),self.temppv1.setText(""),self.tempbeta1.setText(""),self.tempr1.setText(""),self.tempt1.setText("")
            self.temp2.setChecked(0),self.temptxt2.setText(""),self.temppin2.setText(""),self.temppv2.setText(""),self.tempbeta2.setText(""),self.tempr2.setText(""),self.tempt2.setText("")
            self.temp3.setChecked(0),self.temptxt3.setText(""),self.temppin3.setText(""),self.temppv3.setText(""),self.tempbeta3.setText(""),self.tempr3.setText(""),self.tempt3.setText("")
            self.sw0.setChecked(0),self.swpin0.setText(""),self.swpv0.setText(""),self.swtxt0.setText(""),self.swsp0.setText(""),self.swmode0.setCurrentText("On")
            self.sw1.setChecked(0),self.swpin1.setText(""),self.swpv1.setText(""),self.swtxt1.setText(""),self.swsp1.setText(""),self.swmode1.setCurrentText("On")
            self.sw2.setChecked(0),self.swpin2.setText(""),self.swpv2.setText(""),self.swtxt2.setText(""),self.swsp2.setText(""),self.swmode2.setCurrentText("On")
        
        if self.setup.currentText() == "K40 Laser cutter":
        #axis setup
            self.xaxis.setChecked(1),self.xaxistxt.setText("x axis"),self.xaxisjoint.setText("0"),self.xaxisstep.setText("2.2"),self.xaxisdir.setText("2.6"),self.xaxisenable.setText("2.1") ,self.xaxistmc.setCurrentText("None")
            self.yaxis.setChecked(1),self.yaxistxt.setText("y axis"),self.yaxisjoint.setText("1"),self.yaxisstep.setText("0.19"),self.yaxisdir.setText("0.20"),self.yaxisenable.setText("2.8") ,self.yaxistmc.setCurrentText("None")
            self.zaxis.setChecked(0),self.zaxistxt.setText(""),self.zaxisjoint.setText(""),self.zaxisstep.setText(""),self.zaxisdir.setText(""),self.zaxisenable.setText("") ,self.zaxistmc.setCurrentText("None")
            self.e0axis.setChecked(0),self.e0axistxt.setText(""),self.e0axisjoint.setText(""),self.e0axisstep.setText(""),self.e0axisdir.setText(""),self.e0axisenable.setText("") ,self.e0axistmc.setCurrentText("None")
            self.e1axis.setChecked(0),self.e1axistxt.setText(""),self.e1axisjoint.setText(""),self.e1axisstep.setText(""),self.e1axisdir.setText(""),self.e1axisenable.setText("") ,self.e1axistmc.setCurrentText("None")
            #Output setup
            self.outchk0.setChecked(1),self.outtxt0.setText("driver enable"),self.outpin0.setText("2.5"),self.outstate0.setCurrentText("Pull Down"),self.outinv0.setChecked(0)
            self.outchk1.setChecked(1),self.outtxt1.setText("Air Pump"),self.outpin1.setText("2.7"),self.outstate1.setCurrentText("Pull None"),self.outinv1.setChecked(0)
            self.outchk2.setChecked(0),self.outtxt2.setText(""),self.outpin2.setText(""),self.outstate2.setCurrentText("Pull None")
            self.outchk3.setChecked(0),self.outtxt3.setText(""),self.outpin3.setText(""),self.outstate3.setCurrentText("Pull None")
            self.outchk4.setChecked(0),self.outtxt4.setText(""),self.outpin4.setText(""),self.outstate4.setCurrentText("Pull None")
            self.outchk5.setChecked(0),self.outtxt5.setText(""),self.outpin5.setText(""),self.outstate5.setCurrentText("Pull None")
            self.outchk6.setChecked(0),self.outtxt6.setText(""),self.outpin6.setText(""),self.outstate6.setCurrentText("Pull None")
            self.outchk7.setChecked(0),self.outtxt7.setText(""),self.outpin7.setText(""),self.outstate7.setCurrentText("Pull None")
            #Input Setup
            self.inchk0.setChecked(1),self.intxt0.setText("X - limit / home"),self.inpin0.setText("1.29"),self.instate0.setCurrentText("Pull Up"),self.ininv0.setChecked(0)
            self.inchk1.setChecked(1),self.intxt1.setText("Y - limit / home"),self.inpin1.setText("1.28"),self.instate1.setCurrentText("Pull Up"),self.ininv1.setChecked(0)
            self.inchk2.setChecked(1),self.intxt2.setText("Door Shut"),self.inpin2.setText("1.27"),self.instate2.setCurrentText("Pull Up"),self.ininv2.setChecked(0)
            self.estop.setChecked(1),self.estoptxt.setText("E-stop"),self.estoppin.setText("1.0")
            self.inchk3.setChecked(0),self.intxt3.setText(""),self.inpin3.setText(""),self.instate3.setCurrentText("Pull None")
            self.inchk4.setChecked(0),self.intxt4.setText(""),self.inpin4.setText(""),self.instate4.setCurrentText("Pull None")
            self.inchk5.setChecked(0),self.intxt5.setText(""),self.inpin5.setText(""),self.instate5.setCurrentText("Pull None")
            self.inchk6.setChecked(0),self.intxt6.setText(""),self.inpin6.setText(""),self.instate6.setCurrentText("Pull None")
            self.inchk7.setChecked(0),self.intxt7.setText(""),self.inpin7.setText(""),self.instate7.setCurrentText("Pull None")
            #PWM setup
            self.pwm0.setChecked(1),self.pwmtxt0.setText("Laser PWM"),self.pwmmax0.setText("256"),self.pwmpin0.setText("1.24"),self.pwmhw0.setChecked(1),self.pwmvf0.setChecked(1),self.pwmperiod0.setText("1"),self.pwmfreq0.setText("200")
            self.pwm1.setChecked(0),self.pwmtxt1.setText(""),self.pwmmax1.setText(""),self.pwmpin1.setText(""),self.pwmhw1.setChecked(0),self.pwmvf1.setChecked(0),self.pwmperiod1.setText(""),self.pwmfreq1.setText("")
            self.pwm2.setChecked(0),self.pwmtxt2.setText(""),self.pwmmax2.setText(""),self.pwmpin2.setText(""),self.pwmhw2.setChecked(0),self.pwmvf2.setChecked(0),self.pwmperiod2.setText(""),self.pwmfreq2.setText("")
            self.pwm3.setChecked(0),self.pwmtxt3.setText(""),self.pwmmax3.setText(""),self.pwmpin3.setText(""),self.pwmhw3.setChecked(0),self.pwmvf3.setChecked(0),self.pwmperiod3.setText(""),self.pwmfreq3.setText("")
            self.pwm4.setChecked(0),self.pwmtxt4.setText(""),self.pwmmax4.setText(""),self.pwmpin4.setText(""),self.pwmhw4.setChecked(0),self.pwmvf4.setChecked(0),self.pwmperiod4.setText(""),self.pwmfreq4.setText("")
            self.pwm5.setChecked(0),self.pwmtxt5.setText(""),self.pwmmax5.setText(""),self.pwmpin5.setText(""),self.pwmhw5.setChecked(0),self.pwmvf5.setChecked(0),self.pwmperiod5.setText(""),self.pwmfreq5.setText("")
            self.pwm6.setChecked(0),self.pwmtxt6.setText(""),self.pwmmax6.setText(""),self.pwmpin6.setText(""),self.pwmhw6.setChecked(0),self.pwmvf6.setChecked(0),self.pwmperiod6.setText(""),self.pwmfreq6.setText("")
            self.rcservo.setChecked(0),self.rcservotxt.setText(""),self.rcservopin.setText("")
            #Encoder setup
            self.qem.setChecked(0),self.qemtxt.setText(""),self.qeminput.setText(""),self.qemstate.setCurrentText("Pull None"),self.qempv.setText("")
            self.enc0.setChecked(0),self.enctxt0.setText(""),self.encapin0.setText(""),self.encbpin0.setText(""),self.encpv0.setText(""),self.encstate0.setCurrentText("Pull None"),self.encipin0.setText(""),self.encinput0.setText("")
            self.enc1.setChecked(0),self.enctxt1.setText(""),self.encapin1.setText(""),self.encbpin1.setText(""),self.encpv1.setText(""),self.encstate1.setCurrentText("Pull None"),self.encipin1.setText(""),self.encinput1.setText("")
            self.enc2.setChecked(0),self.enctxt2.setText(""),self.encapin2.setText(""),self.encbpin2.setText(""),self.encpv2.setText(""),self.encstate2.setCurrentText("Pull None"),self.encipin2.setText(""),self.encinput2.setText("")
            self.enc3.setChecked(0),self.enctxt3.setText(""),self.encapin3.setText(""),self.encbpin3.setText(""),self.encpv3.setText(""),self.encstate3.setCurrentText("Pull None"),self.encipin3.setText(""),self.encinput3.setText("")
            #temp swtich setup
            self.temp0.setChecked(0),self.temptxt0.setText(""),self.temppin0.setText(""),self.temppv0.setText(""),self.tempbeta0.setText(""),self.tempr0.setText(""),self.tempt0.setText("")
            self.temp1.setChecked(0),self.temptxt1.setText(""),self.temppin1.setText(""),self.temppv1.setText(""),self.tempbeta1.setText(""),self.tempr1.setText(""),self.tempt1.setText("")
            self.temp2.setChecked(0),self.temptxt2.setText(""),self.temppin2.setText(""),self.temppv2.setText(""),self.tempbeta2.setText(""),self.tempr2.setText(""),self.tempt2.setText("")
            self.temp3.setChecked(0),self.temptxt3.setText(""),self.temppin3.setText(""),self.temppv3.setText(""),self.tempbeta3.setText(""),self.tempr3.setText(""),self.tempt3.setText("")
            self.sw0.setChecked(0),self.swpin0.setText(""),self.swpv0.setText(""),self.swtxt0.setText(""),self.swsp0.setText(""),self.swmode0.setCurrentText("On")
            self.sw1.setChecked(0),self.swpin1.setText(""),self.swpv1.setText(""),self.swtxt1.setText(""),self.swsp1.setText(""),self.swmode1.setCurrentText("On")
            self.sw2.setChecked(0),self.swpin2.setText(""),self.swpv2.setText(""),self.swtxt2.setText(""),self.swsp2.setText(""),self.swmode2.setCurrentText("On")
            
        if self.setup.currentText() == "3D printer":
        #axis setup
            self.xaxis.setChecked(1),self.xaxistxt.setText("x axis"),self.xaxisjoint.setText("0"),self.xaxisstep.setText("2.2"),self.xaxisdir.setText("2.6"),self.xaxisenable.setText("2.1") ,self.xaxistmc.setCurrentText("None")
            self.yaxis.setChecked(1),self.yaxistxt.setText("y axis"),self.yaxisjoint.setText("1"),self.yaxisstep.setText("0.19"),self.yaxisdir.setText("0.20"),self.yaxisenable.setText("2.8") ,self.yaxistmc.setCurrentText("None")
            self.zaxis.setChecked(1),self.zaxistxt.setText("z axis"),self.zaxisjoint.setText("2"),self.zaxisstep.setText("0.22"),self.zaxisdir.setText("2.11"),self.zaxisenable.setText("0.21") ,self.zaxistmc.setCurrentText("None")
            self.e0axis.setChecked(1),self.e0axistxt.setText("E0 axis"),self.e0axisjoint.setText("3"),self.e0axisstep.setText("2.13"),self.e0axisdir.setText("0.11"),self.e0axisenable.setText("2.12") ,self.e0axistmc.setCurrentText("None")
            self.e1axis.setChecked(0),self.e1axistxt.setText(""),self.e1axisjoint.setText(""),self.e1axisstep.setText(""),self.e1axisdir.setText(""),self.e1axisenable.setText("") ,self.e1axistmc.setCurrentText("None")
            #Output setup
            self.outchk0.setChecked(1),self.outtxt0.setText("Part Cooling Fan"),self.outpin0.setText("2.4"),self.outstate0.setCurrentText("Pull None"),self.outinv0.setChecked(0)
            self.outchk1.setChecked(0),self.outtxt1.setText(""),self.outpin1.setText(""),self.outstate1.setCurrentText("Pull None")
            self.outchk2.setChecked(0),self.outtxt2.setText(""),self.outpin2.setText(""),self.outstate2.setCurrentText("Pull None")
            self.outchk3.setChecked(0),self.outtxt3.setText(""),self.outpin3.setText(""),self.outstate3.setCurrentText("Pull None")
            self.outchk4.setChecked(0),self.outtxt4.setText(""),self.outpin4.setText(""),self.outstate4.setCurrentText("Pull None")
            self.outchk5.setChecked(0),self.outtxt5.setText(""),self.outpin5.setText(""),self.outstate5.setCurrentText("Pull None")
            self.outchk6.setChecked(0),self.outtxt6.setText(""),self.outpin6.setText(""),self.outstate6.setCurrentText("Pull None")
            self.outchk7.setChecked(0),self.outtxt7.setText(""),self.outpin7.setText(""),self.outstate7.setCurrentText("Pull None")
            #Input Setup
            self.inchk0.setChecked(1),self.intxt0.setText("X  home"),self.inpin0.setText("1.29"),self.instate0.setCurrentText("Pull Up"),self.ininv0.setChecked(0)
            self.inchk1.setChecked(1),self.intxt1.setText("Y home"),self.inpin1.setText("1.28"),self.instate1.setCurrentText("Pull Up"),self.ininv1.setChecked(0)
            self.inchk2.setChecked(1),self.intxt2.setText("Z home"),self.inpin2.setText("1.27"),self.instate2.setCurrentText("Pull Up"),self.ininv2.setChecked(0)
            self.estop.setChecked(0),self.estoptxt.setText(""),self.estoppin.setText("")
            self.inchk3.setChecked(0),self.intxt3.setText(""),self.inpin3.setText(""),self.instate3.setCurrentText("Pull None")
            self.inchk4.setChecked(0),self.intxt4.setText(""),self.inpin4.setText(""),self.instate4.setCurrentText("Pull None")
            self.inchk5.setChecked(0),self.intxt5.setText(""),self.inpin5.setText(""),self.instate5.setCurrentText("Pull None")
            self.inchk6.setChecked(0),self.intxt6.setText(""),self.inpin6.setText(""),self.instate6.setCurrentText("Pull None")
            self.inchk7.setChecked(0),self.intxt7.setText(""),self.inpin7.setText(""),self.instate7.setCurrentText("Pull None")
            #PWM setup
            self.pwm0.setChecked(1),self.pwmtxt0.setText("Hotend"),self.pwmmax0.setText("256"),self.pwmpin0.setText("2.7"),self.pwmhw0.setChecked(0),self.pwmvf0.setChecked(0),self.pwmperiod0.setText("1"),self.pwmfreq0.setText("200")
            self.pwm1.setChecked(1),self.pwmtxt1.setText("Heated Bed"),self.pwmmax1.setText("256"),self.pwmpin1.setText("2.5"),self.pwmhw1.setChecked(1),self.pwmvf1.setChecked(1),self.pwmperiod1.setText("1"),self.pwmfreq1.setText("200")
            self.pwm2.setChecked(0),self.pwmtxt2.setText(""),self.pwmmax2.setText(""),self.pwmpin2.setText(""),self.pwmhw2.setChecked(0),self.pwmvf2.setChecked(0),self.pwmperiod2.setText(""),self.pwmfreq2.setText("")
            self.pwm3.setChecked(0),self.pwmtxt3.setText(""),self.pwmmax3.setText(""),self.pwmpin3.setText(""),self.pwmhw3.setChecked(0),self.pwmvf3.setChecked(0),self.pwmperiod3.setText(""),self.pwmfreq3.setText("")
            self.pwm4.setChecked(0),self.pwmtxt4.setText(""),self.pwmmax4.setText(""),self.pwmpin4.setText(""),self.pwmhw4.setChecked(0),self.pwmvf4.setChecked(0),self.pwmperiod4.setText(""),self.pwmfreq4.setText("")
            self.pwm5.setChecked(0),self.pwmtxt5.setText(""),self.pwmmax5.setText(""),self.pwmpin5.setText(""),self.pwmhw5.setChecked(0),self.pwmvf5.setChecked(0),self.pwmperiod5.setText(""),self.pwmfreq5.setText("")
            self.pwm6.setChecked(0),self.pwmtxt6.setText(""),self.pwmmax6.setText(""),self.pwmpin6.setText(""),self.pwmhw6.setChecked(0),self.pwmvf6.setChecked(0),self.pwmperiod6.setText(""),self.pwmfreq6.setText("")
            self.rcservo.setChecked(0),self.rcservotxt.setText(""),self.rcservopin.setText("")
            #Encoder setup
            self.qem.setChecked(0),self.qemtxt.setText(""),self.qeminput.setText(""),self.qemstate.setCurrentText(""),self.qempv.setText("")
            self.enc0.setChecked(0),self.enctxt0.setText(""),self.encapin0.setText(""),self.encbpin0.setText(""),self.encpv0.setText(""),self.encstate0.setCurrentText("Pull None"),self.encipin0.setText(""),self.encinput0.setText("")
            self.enc1.setChecked(0),self.enctxt1.setText(""),self.encapin1.setText(""),self.encbpin1.setText(""),self.encpv1.setText(""),self.encstate1.setCurrentText("Pull None"),self.encipin1.setText(""),self.encinput1.setText("")
            self.enc2.setChecked(0),self.enctxt2.setText(""),self.encapin2.setText(""),self.encbpin2.setText(""),self.encpv2.setText(""),self.encstate2.setCurrentText("Pull None"),self.encipin2.setText(""),self.encinput2.setText("")
            self.enc3.setChecked(0),self.enctxt3.setText(""),self.encapin3.setText(""),self.encbpin3.setText(""),self.encpv3.setText(""),self.encstate3.setCurrentText("Pull None"),self.encipin3.setText(""),self.encinput3.setText("")
            #temp swtich setup
            self.temp0.setChecked(1),self.temptxt0.setText("Hotend Thermistor"),self.temppin0.setText("0.23"),self.temppv0.setText("0"),self.tempbeta0.setText("3990"),self.tempr0.setText("100000"),self.tempt0.setText("25")
            self.temp1.setChecked(1),self.temptxt1.setText("Bed Thermistor"),self.temppin1.setText("0.25"),self.temppv1.setText("1"),self.tempbeta1.setText("3990"),self.tempr1.setText("100000"),self.tempt1.setText("25")
            self.temp2.setChecked(0),self.temptxt2.setText(""),self.temppin2.setText(""),self.temppv2.setText(""),self.tempbeta2.setText(""),self.tempr2.setText(""),self.tempt2.setText("")
            self.temp3.setChecked(0),self.temptxt3.setText(""),self.temppin3.setText(""),self.temppv3.setText(""),self.tempbeta3.setText(""),self.tempr3.setText(""),self.tempt3.setText("")
            self.sw0.setChecked(1),self.swpin0.setText("2.3"),self.swpv0.setText("0"),self.swtxt0.setText("Hotend Fan"),self.swsp0.setText("25.5"),self.swmode0.setCurrentText("On"),
            self.sw1.setChecked(0),self.swpin1.setText(""),self.swpv1.setText(""),self.swtxt1.setText(""),self.swsp1.setText(""),self.swmode1.setCurrentText("On")
            self.sw2.setChecked(0),self.swpin2.setText(""),self.swpv2.setText(""),self.swtxt2.setText(""),self.swsp2.setText(""),self.swmode2.setCurrentText("On")
        
        if self.setup.currentText() == "3D printer + BL Touch":
        #axis setup
            self.xaxis.setChecked(1),self.xaxistxt.setText("x axis"),self.xaxisjoint.setText("0"),self.xaxisstep.setText("2.2"),self.xaxisdir.setText("2.6"),self.xaxisenable.setText("2.1") ,self.xaxistmc.setCurrentText("None")
            self.yaxis.setChecked(1),self.yaxistxt.setText("y axis"),self.yaxisjoint.setText("1"),self.yaxisstep.setText("0.19"),self.yaxisdir.setText("0.20"),self.yaxisenable.setText("2.8") ,self.yaxistmc.setCurrentText("None")
            self.zaxis.setChecked(1),self.zaxistxt.setText("z axis"),self.zaxisjoint.setText("2"),self.zaxisstep.setText("0.22"),self.zaxisdir.setText("2.11"),self.zaxisenable.setText("0.21") ,self.zaxistmc.setCurrentText("None")
            self.e0axis.setChecked(1),self.e0axistxt.setText("E0 axis"),self.e0axisjoint.setText("3"),self.e0axisstep.setText("2.13"),self.e0axisdir.setText("0.11"),self.e0axisenable.setText("2.12") ,self.e0axistmc.setCurrentText("None")
            self.e1axis.setChecked(0),self.e1axistxt.setText(""),self.e1axisjoint.setText(""),self.e1axisstep.setText(""),self.e1axisdir.setText(""),self.e1axisenable.setText("") ,self.e1axistmc.setCurrentText("None")
            #Output setup
            self.outchk0.setChecked(1),self.outtxt0.setText("Part Cooling Fan"),self.outpin0.setText("2.4"),self.outstate0.setCurrentText("Pull None"),self.outinv0.setChecked(0)
            self.outchk1.setChecked(0),self.outtxt1.setText(""),self.outpin1.setText(""),self.outstate1.setCurrentText("Pull None")
            self.outchk2.setChecked(0),self.outtxt2.setText(""),self.outpin2.setText(""),self.outstate2.setCurrentText("Pull None")
            self.outchk3.setChecked(0),self.outtxt3.setText(""),self.outpin3.setText(""),self.outstate3.setCurrentText("Pull None")
            self.outchk4.setChecked(0),self.outtxt4.setText(""),self.outpin4.setText(""),self.outstate4.setCurrentText("Pull None")
            self.outchk5.setChecked(0),self.outtxt5.setText(""),self.outpin5.setText(""),self.outstate5.setCurrentText("Pull None")
            self.outchk6.setChecked(0),self.outtxt6.setText(""),self.outpin6.setText(""),self.outstate6.setCurrentText("Pull None")
            self.outchk7.setChecked(0),self.outtxt7.setText(""),self.outpin7.setText(""),self.outstate7.setCurrentText("Pull None")
            #Input Setup
            self.inchk0.setChecked(1),self.intxt0.setText("X  home"),self.inpin0.setText("1.29"),self.instate0.setCurrentText("Pull Up"),self.ininv0.setChecked(0)
            self.inchk1.setChecked(1),self.intxt1.setText("Y home"),self.inpin1.setText("1.28"),self.instate1.setCurrentText("Pull Up"),self.ininv1.setChecked(0)
            self.inchk2.setChecked(1),self.intxt2.setText("BL Touch Z"),self.inpin2.setText("1.27"),self.instate2.setCurrentText("Pull Up"),self.ininv2.setChecked(0)
            self.estop.setChecked(0),self.estoptxt.setText(""),self.estoppin.setText("")
            self.inchk3.setChecked(0),self.intxt3.setText(""),self.inpin3.setText(""),self.instate3.setCurrentText("Pull None")
            self.inchk4.setChecked(0),self.intxt4.setText(""),self.inpin4.setText(""),self.instate4.setCurrentText("Pull None")
            self.inchk5.setChecked(0),self.intxt5.setText(""),self.inpin5.setText(""),self.instate5.setCurrentText("Pull None")
            self.inchk6.setChecked(0),self.intxt6.setText(""),self.inpin6.setText(""),self.instate6.setCurrentText("Pull None")
            self.inchk7.setChecked(0),self.intxt7.setText(""),self.inpin7.setText(""),self.instate7.setCurrentText("Pull None")
            #PWM setup
            self.pwm0.setChecked(1),self.pwmtxt0.setText("Hotend"),self.pwmmax0.setText("256"),self.pwmpin0.setText("2.7"),self.pwmhw0.setChecked(0),self.pwmvf0.setChecked(0),self.pwmperiod0.setText("1"),self.pwmfreq0.setText("200")
            self.pwm1.setChecked(1),self.pwmtxt1.setText("Heated Bed"),self.pwmmax1.setText("256"),self.pwmpin1.setText("2.5"),self.pwmhw1.setChecked(1),self.pwmvf1.setChecked(1),self.pwmperiod1.setText("1"),self.pwmfreq1.setText("200")
            self.pwm2.setChecked(0),self.pwmtxt2.setText(""),self.pwmmax2.setText(""),self.pwmpin2.setText(""),self.pwmhw2.setChecked(0),self.pwmvf2.setChecked(0),self.pwmperiod2.setText(""),self.pwmfreq2.setText("")
            self.pwm3.setChecked(0),self.pwmtxt3.setText(""),self.pwmmax3.setText(""),self.pwmpin3.setText(""),self.pwmhw3.setChecked(0),self.pwmvf3.setChecked(0),self.pwmperiod3.setText(""),self.pwmfreq3.setText("")
            self.pwm4.setChecked(0),self.pwmtxt4.setText(""),self.pwmmax4.setText(""),self.pwmpin4.setText(""),self.pwmhw4.setChecked(0),self.pwmvf4.setChecked(0),self.pwmperiod4.setText(""),self.pwmfreq4.setText("")
            self.pwm5.setChecked(0),self.pwmtxt5.setText(""),self.pwmmax5.setText(""),self.pwmpin5.setText(""),self.pwmhw5.setChecked(0),self.pwmvf5.setChecked(0),self.pwmperiod5.setText(""),self.pwmfreq5.setText("")
            self.pwm6.setChecked(0),self.pwmtxt6.setText(""),self.pwmmax6.setText(""),self.pwmpin6.setText(""),self.pwmhw6.setChecked(0),self.pwmvf6.setChecked(0),self.pwmperiod6.setText(""),self.pwmfreq6.setText("")
            self.rcservo.setChecked(1),self.rcservotxt.setText("BL Touch"),self.rcservopin.setText("2.0"),self.rcservospi.setText("7"),
            #Encoder setup
            self.qem.setChecked(0),self.qemtxt.setText(""),self.qeminput.setText(""),self.qemstate.setCurrentText(""),self.qempv.setText("")
            self.enc0.setChecked(0),self.enctxt0.setText(""),self.encapin0.setText(""),self.encbpin0.setText(""),self.encpv0.setText(""),self.encstate0.setCurrentText("Pull None"),self.encipin0.setText(""),self.encinput0.setText("")
            self.enc1.setChecked(0),self.enctxt1.setText(""),self.encapin1.setText(""),self.encbpin1.setText(""),self.encpv1.setText(""),self.encstate1.setCurrentText("Pull None"),self.encipin1.setText(""),self.encinput1.setText("")
            self.enc2.setChecked(0),self.enctxt2.setText(""),self.encapin2.setText(""),self.encbpin2.setText(""),self.encpv2.setText(""),self.encstate2.setCurrentText("Pull None"),self.encipin2.setText(""),self.encinput2.setText("")
            self.enc3.setChecked(0),self.enctxt3.setText(""),self.encapin3.setText(""),self.encbpin3.setText(""),self.encpv3.setText(""),self.encstate3.setCurrentText("Pull None"),self.encipin3.setText(""),self.encinput3.setText("")
            #temp swtich setup
            self.temp0.setChecked(1),self.temptxt0.setText("Hotend Thermistor"),self.temppin0.setText("0.23"),self.temppv0.setText("0"),self.tempbeta0.setText("3990"),self.tempr0.setText("100000"),self.tempt0.setText("25")
            self.temp1.setChecked(1),self.temptxt1.setText("Bed Thermistor"),self.temppin1.setText("0.25"),self.temppv1.setText("1"),self.tempbeta1.setText("3990"),self.tempr1.setText("100000"),self.tempt1.setText("25")
            self.temp2.setChecked(0),self.temptxt2.setText(""),self.temppin2.setText(""),self.temppv2.setText(""),self.tempbeta2.setText(""),self.tempr2.setText(""),self.tempt2.setText("")
            self.temp3.setChecked(0),self.temptxt3.setText(""),self.temppin3.setText(""),self.temppv3.setText(""),self.tempbeta3.setText(""),self.tempr3.setText(""),self.tempt3.setText("")
            self.sw0.setChecked(1),self.swpin0.setText("2.3"),self.swpv0.setText("0"),self.swtxt0.setText("Hotend Fan"),self.swsp0.setText("25.5"),self.swmode0.setCurrentText("On"),
            self.sw1.setChecked(0),self.swpin1.setText(""),self.swpv1.setText(""),self.swtxt1.setText(""),self.swsp1.setText(""),self.swmode1.setCurrentText("On")
            self.sw2.setChecked(0),self.swpin2.setText(""),self.swpv2.setText(""),self.swtxt2.setText(""),self.swsp2.setText(""),self.swmode2.setCurrentText("On")
        
    def printButtonPressed2(self):
        # Import save data into hmi
        with open("save.txt","r") as infile:
            #boards
            a, b = map(str,infile.readline().split("|"))
            self.boards.setCurrentText(str(a))
            #X axis
            a, b, c, d, e, f, g, h, i, j, k, l = map(str,infile.readline().split("|"))
            self.xaxistxt.setText(b),self.xaxisjoint.setText(c),self.xaxisstep.setText(d),self.xaxisdir.setText(e),self.xaxisenable.setText(f),self.xaxiscur.setText(g) ,self.xaxistmc.setCurrentText(h) ,self.xaxiscursense.setText(i) ,self.xaxismicrostep.setText(j) ,self.xaxisstealthcop.setCurrentText(k)
            if a == "True": self.xaxis.setChecked(1)
            else: self.xaxis.setChecked(0)
            #Y axis
            a, b, c, d, e, f, g, h, i, j, k, l = map(str,infile.readline().split("|"))
            self.yaxistxt.setText(b),self.yaxisjoint.setText(c),self.yaxisstep.setText(d),self.yaxisdir.setText(e),self.yaxisenable.setText(f),self.yaxiscur.setText(g)  ,self.yaxistmc.setCurrentText(h) ,self.yaxiscursense.setText(i) ,self.yaxismicrostep.setText(j) ,self.yaxisstealthcop.setCurrentText(k)
            if a == "True": self.yaxis.setChecked(1)
            else: self.yaxis.setChecked(0)
            #Z axis
            a, b, c, d, e, f, g, h, i, j, k, l = map(str,infile.readline().split("|"))
            self.zaxistxt.setText(b),self.zaxisjoint.setText(c),self.zaxisstep.setText(d),self.zaxisdir.setText(e),self.zaxisenable.setText(f),self.zaxiscur.setText(g) ,self.zaxistmc.setCurrentText(h) ,self.zaxiscursense.setText(i) ,self.zaxismicrostep.setText(j) ,self.zaxisstealthcop.setCurrentText(k)
            if a == "True": self.zaxis.setChecked(1)
            else: self.zaxis.setChecked(0)
            #E0 axis
            a, b, c, d, e, f, g, h, i, j, k, l = map(str,infile.readline().split("|"))
            self.e0axistxt.setText(b),self.e0axisjoint.setText(c),self.e0axisstep.setText(d),self.e0axisdir.setText(e),self.e0axisenable.setText(f),self.e0axiscur.setText(g) ,self.e0axistmc.setCurrentText(h) ,self.e0axiscursense.setText(i) ,self.e0axismicrostep.setText(j) ,self.e0axisstealthcop.setCurrentText(k)
            if a == "True": self.e0axis.setChecked(1)
            else: self.e0axis.setChecked(0)
            #E1 axis
            a, b, c, d, e, f, g, h, i, j, k, l = map(str,infile.readline().split("|"))
            self.e1axistxt.setText(b),self.e1axisjoint.setText(c),self.e1axisstep.setText(d),self.e1axisdir.setText(e),self.e1axisenable.setText(f),self.e1axiscur.setText(g) ,self.e1axistmc.setCurrentText(h) ,self.e1axiscursense.setText(i) ,self.e1axismicrostep.setText(j) ,self.e1axisstealthcop.setCurrentText(k)
            if a == "True": self.e1axis.setChecked(1)
            else: self.e1axis.setChecked(0)
            
            #output 0
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.outtxt0.setText(b),self.outpin0.setText(c),self.outstate0.setCurrentText(d)
            if a == "True": 
                self.outchk0.setChecked(1)
            else: self.outchk0.setChecked(0)
            if e == "True": self.outinv0.setChecked(1)
            else: self.outinv0.setChecked(0)
            #output 1
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.outtxt1.setText(b),self.outpin1.setText(c),self.outstate1.setCurrentText(d)
            if a == "True": 
                self.outchk1.setChecked(1)
            else: self.outchk1.setChecked(0)
            if e == "True": self.outinv1.setChecked(1)
            else: self.outinv1.setChecked(0)
            #output 2
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.outtxt2.setText(b),self.outpin2.setText(c),self.outstate2.setCurrentText(d)
            if a == "True": 
                self.outchk2.setChecked(1)
            else: self.outchk2.setChecked(0)
            if e == "True": self.outinv2.setChecked(1)
            else: self.outinv2.setChecked(0)
            #output 3
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.outtxt3.setText(b),self.outpin3.setText(c),self.outstate3.setCurrentText(d)
            if a == "True": 
                self.outchk3.setChecked(1)
            else: self.outchk3.setChecked(0)
            if e == "True": self.outinv3.setChecked(1)
            else: self.outinv3.setChecked(0)
            #output 4
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.outtxt4.setText(b),self.outpin4.setText(c),self.outstate4.setCurrentText(d)
            if a == "True": 
                self.outchk4.setChecked(1)
            else: self.outchk4.setChecked(0)
            if e == "True": self.outinv4.setChecked(1)
            else: self.outinv4.setChecked(0)
            #output 5
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.outtxt5.setText(b),self.outpin5.setText(c),self.outstate5.setCurrentText(d)
            if a == "True": 
                self.outchk5.setChecked(1)
            else: self.outchk5.setChecked(0)
            if e == "True": self.outinv5.setChecked(1)
            else: self.outinv5.setChecked(0)
            #output 6
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.outtxt6.setText(b),self.outpin6.setText(c),self.outstate6.setCurrentText(d)
            if a == "True": 
                self.outchk6.setChecked(1)
            else: self.outchk6.setChecked(0)
            if e == "True": self.outinv6.setChecked(1)
            else: self.outinv6.setChecked(0)
            #output 7
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.outtxt7.setText(b),self.outpin7.setText(c),self.outstate7.setCurrentText(d)
            if a == "True": 
                self.outchk7.setChecked(1)
            else: self.outchk7.setChecked(0)
            if e == "True": self.outinv7.setChecked(1)
            else: self.outinv7.setChecked(0)

            
            #input 0
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.intxt0.setText(b),self.inpin0.setText(c),self.instate0.setCurrentText(d)
            if a == "True": self.inchk0.setChecked(1)
            else: self.inchk0.setChecked(0)
            if e == "True": self.ininv0.setChecked(1)
            else: self.ininv0.setChecked(0)
            #input 1
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.intxt1.setText(b),self.inpin1.setText(c),self.instate1.setCurrentText(d)
            if a == "True": self.inchk1.setChecked(1)
            else: self.inchk1.setChecked(0)
            if e == "True": self.ininv1.setChecked(1)
            else: self.ininv1.setChecked(0)
            #input 2
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.intxt2.setText(b),self.inpin2.setText(c),self.instate2.setCurrentText(d)
            if a == "True": self.inchk2.setChecked(1)
            else: self.inchk2.setChecked(0)
            if e == "True": self.ininv2.setChecked(1)
            else: self.ininv2.setChecked(0)
            #input 3
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.intxt3.setText(b),self.inpin3.setText(c),self.instate3.setCurrentText(d)
            if a == "True": self.inchk3.setChecked(1)
            else: self.inchk3.setChecked(0)
            if e == "True": self.ininv3.setChecked(1)
            else: self.ininv3.setChecked(0)
            #input 4
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.intxt4.setText(b),self.inpin4.setText(c),self.instate4.setCurrentText(d)
            if a == "True": self.inchk4.setChecked(1)
            else: self.inchk4.setChecked(0)
            if e == "True": self.ininv4.setChecked(1)
            else: self.ininv4.setChecked(0)
            #input 5
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.intxt5.setText(b),self.inpin5.setText(c),self.instate5.setCurrentText(d)
            if a == "True": self.inchk5.setChecked(1)
            else: self.inchk5.setChecked(0)
            if e == "True": self.ininv5.setChecked(1)
            else: self.ininv5.setChecked(0)
            #input 6
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.intxt6.setText(b),self.inpin6.setText(c),self.instate6.setCurrentText(d)
            if a == "True": self.inchk6.setChecked(1)
            else: self.inchk6.setChecked(0)
            if e == "True": self.ininv6.setChecked(1)
            else: self.ininv6.setChecked(0)
            #input 7
            a, b, c, d, e, f = map(str,infile.readline().split("|"))
            self.intxt7.setText(b),self.inpin7.setText(c),self.instate7.setCurrentText(d)
            if a == "True": self.inchk7.setChecked(1)
            else: self.inchk7.setChecked(0)
            if e == "True": self.ininv7.setChecked(1)
            else: self.ininv7.setChecked(0)
            
            #E stop
            a, b, c, d = map(str,infile.readline().split("|"))
            self.estoptxt.setText(b),self.estoppin.setText(c)
            if a == "True": self.estop.setChecked(1)
            else: self.estop.setChecked(0)
            #reset
            a, b, c, d = map(str,infile.readline().split("|"))
            self.resettxt.setText(b),self.resetpin.setText(c)
            if a == "True": self.reset.setChecked(1)
            else: self.reset.setChecked(0)
            
            #PWM 0
            a, b, c, d, e, f, g, h, i, j = map(str,infile.readline().split("|"))
            self.pwmtxt0.setText(b),self.pwmmax0.setText(c),self.pwmpin0.setText(d),self.pwmfreq0.setText(g),self.pwmperiod0.setText(h)
            if a == "True": self.pwm0.setChecked(1)
            else: self.pwm0.setChecked(0)
            if e == "True": self.pwmhw0.setChecked(1)
            else: self.pwmhw0.setChecked(0)
            if f == "True": self.pwmvf0.setChecked(1)
            else: self.pwmvf0.setChecked(0)
            #PWM 1
            a, b, c, d, e, f, g, h, i, j = map(str,infile.readline().split("|"))
            self.pwmtxt1.setText(b),self.pwmmax1.setText(c),self.pwmpin1.setText(d),self.pwmfreq1.setText(g),self.pwmperiod1.setText(h)
            if a == "True": self.pwm1.setChecked(1)
            else: self.pwm1.setChecked(0)
            if e == "True": self.pwmhw1.setChecked(1)
            else: self.pwmhw1.setChecked(0)
            if f == "True": self.pwmvf1.setChecked(1)
            else: self.pwmvf1.setChecked(0)
            #PWM 2
            a, b, c, d, e, f, g, h, i, j = map(str,infile.readline().split("|"))
            self.pwmtxt2.setText(b),self.pwmmax2.setText(c),self.pwmpin2.setText(d),self.pwmfreq2.setText(g),self.pwmperiod2.setText(h)
            if a == "True": self.pwm2.setChecked(1)
            else: self.pwm2.setChecked(0)
            if e == "True": self.pwmhw2.setChecked(1)
            else: self.pwmhw2.setChecked(0)
            if f == "True": self.pwmvf2.setChecked(1)
            else: self.pwmvf2.setChecked(0)
            #PWM 3
            a, b, c, d, e, f, g, h, i, j = map(str,infile.readline().split("|"))
            self.pwmtxt3.setText(b),self.pwmmax3.setText(c),self.pwmpin3.setText(d),self.pwmfreq3.setText(g),self.pwmperiod3.setText(h)
            if a == "True": self.pwm3.setChecked(1)
            else: self.pwm3.setChecked(0)
            if e == "True": self.pwmhw3.setChecked(1)
            else: self.pwmhw3.setChecked(0)
            if f == "True": self.pwmvf3.setChecked(1)
            else: self.pwmvf3.setChecked(0)
            #PWM 4
            a, b, c, d, e, f, g, h, i, j = map(str,infile.readline().split("|"))
            self.pwmtxt4.setText(b),self.pwmmax4.setText(c),self.pwmpin4.setText(d),self.pwmfreq4.setText(g),self.pwmperiod4.setText(h)
            if a == "True": self.pwm4.setChecked(1)
            else: self.pwm4.setChecked(0)
            if e == "True": self.pwmhw4.setChecked(1)
            else: self.pwmhw4.setChecked(0)
            if f == "True": self.pwmvf4.setChecked(1)
            else: self.pwmvf4.setChecked(0)
            #PWM 5
            a, b, c, d, e, f, g, h, i, j = map(str,infile.readline().split("|"))
            self.pwmtxt5.setText(b),self.pwmmax5.setText(c),self.pwmpin5.setText(d),self.pwmfreq5.setText(g),self.pwmperiod5.setText(h)
            if a == "True": self.pwm5.setChecked(1)
            else: self.pwm5.setChecked(0)
            if e == "True": self.pwmhw5.setChecked(1)
            else: self.pwmhw5.setChecked(0)
            if f == "True": self.pwmvf5.setChecked(1)
            else: self.pwmvf5.setChecked(0)
            #PWM 6
            a, b, c, d, e, f, g, h, i, j = map(str,infile.readline().split("|"))
            self.pwmtxt6.setText(b),self.pwmmax6.setText(c),self.pwmpin6.setText(d),self.pwmfreq6.setText(g),self.pwmperiod6.setText(h)
            if a == "True": self.pwm6.setChecked(1)
            else: self.pwm6.setChecked(0)
            if e == "True": self.pwmhw6.setChecked(1)
            else: self.pwmhw6.setChecked(0)
            if f == "True": self.pwmvf6.setChecked(1)
            else: self.pwmvf6.setChecked(0)
           
            #rc servo
            a, b, c, d, e = map(str,infile.readline().split("|"))
            self.rcservotxt.setText(b),self.rcservopin.setText(c)
            if a == "True": self.rcservo.setChecked(1)
            else: self.rcservo.setChecked(0)
            
            #QEM
            a, b, c, d, e, f, g, h, i = map(str,infile.readline().split("|"))
            self.qemtxt.setText(b),self.qempv.setText(c),self.qeminput.setText(g),self.qemstate.setCurrentText(h)
            if a == "True": 
                self.qem.setChecked(1),
            else: self.qem.setChecked(0)
            #encoder 0
            a, b, c, d, e, f, g, h, i = map(str,infile.readline().split("|"))
            self.enctxt0.setText(b),self.encpv0.setText(c),self.encapin0.setText(d),self.encbpin0.setText(e),self.encipin0.setText(f),self.encinput0.setText(g),self.encstate0.setCurrentText(h)
            if a == "True": 
                self.enc0.setChecked(1),
            else: self.enc0.setChecked(0)
            #encoder 1
            a, b, c, d, e, f, g, h, i = map(str,infile.readline().split("|"))
            self.enctxt1.setText(b),self.encpv1.setText(c),self.encapin1.setText(d),self.encbpin1.setText(e),self.encipin1.setText(f),self.encinput1.setText(g),self.encstate1.setCurrentText(h)
            if a == "True": 
                self.enc1.setChecked(1),
            else: self.enc1.setChecked(0)
            #encoder 2
            a, b, c, d, e, f, g, h, i = map(str,infile.readline().split("|"))
            self.enctxt2.setText(b),self.encpv2.setText(c),self.encapin2.setText(d),self.encbpin2.setText(e),self.encipin2.setText(f),self.encinput2.setText(g),self.encstate2.setCurrentText(h)
            if a == "True": 
                self.enc2.setChecked(1),
            else: self.enc2.setChecked(0)
            #encoder 3
            a, b, c, d, e, f, g, h, i = map(str,infile.readline().split("|"))
            self.enctxt3.setText(b),self.encpv3.setText(c),self.encapin3.setText(d),self.encbpin3.setText(e),self.encipin3.setText(f),self.encinput3.setText(g),self.encstate3.setCurrentText(h)
            if a == "True": 
                self.enc3.setChecked(1),
            else: self.enc3.setChecked(0)
            
            #temp 0
            a, b, c, d, e, f, g, h = map(str,infile.readline().split("|"))
            self.temptxt0.setText(b),self.temppv0.setText(c),self.temppin0.setText(d),self.tempr0.setText(e),self.tempt0.setText(f),self.tempbeta0.setText(g)
            if a == "True": 
                self.temp0.setChecked(1),
            else: self.temp0.setChecked(0)
            #temp 1
            a, b, c, d, e, f, g, h = map(str,infile.readline().split("|"))
            self.temptxt1.setText(b),self.temppv1.setText(c),self.temppin1.setText(d),self.tempr1.setText(e),self.tempt1.setText(f),self.tempbeta1.setText(g)
            if a == "True": 
                self.temp1.setChecked(1),
            else: self.temp1.setChecked(0)
            #temp 2
            a, b, c, d, e, f, g, h = map(str,infile.readline().split("|"))
            self.temptxt2.setText(b),self.temppv2.setText(c),self.temppin2.setText(d),self.tempr2.setText(e),self.tempt2.setText(f),self.tempbeta2.setText(g)
            if a == "True": 
                self.temp2.setChecked(1),
            else: self.temp2.setChecked(0)
            #temp 3
            a, b, c, d, e, f, g, h = map(str,infile.readline().split("|"))
            self.temptxt3.setText(b),self.temppv3.setText(c),self.temppin3.setText(d),self.tempr3.setText(e),self.tempt3.setText(f),self.tempbeta3.setText(g)
            if a == "True": 
                self.temp3.setChecked(1),
            else: self.temp3.setChecked(0)
            #switch 0
            a, b, c, d, e, f, g = map(str,infile.readline().split("|"))
            self.swtxt0.setText(b),self.swpv0.setText(c),self.swpin0.setText(d),self.swsp0.setText(e),self.swmode0.setCurrentText(f)
            if a == "True": 
                self.sw0.setChecked(1),
            else: self.sw0.setChecked(0)
            #switch 1
            a, b, c, d, e, f, g = map(str,infile.readline().split("|"))
            self.swtxt1.setText(b),self.swpv1.setText(c),self.swpin1.setText(d),self.swsp1.setText(e),self.swmode1.setCurrentText(f)
            if a == "True": 
                self.sw1.setChecked(1),
            else: self.sw1.setChecked(0)
            #switch 2
            a, b, c, d, e, f, g = map(str,infile.readline().split("|"))
            self.swtxt2.setText(b),self.swpv2.setText(c),self.swpin2.setText(d),self.swsp2.setText(e),self.swmode2.setCurrentText(f)
            if a == "True": 
                self.sw2.setChecked(1),
            else: self.sw2.setChecked(0)
        
    def printButtonPressed(self):
        # Write data out to the config file for the board
        with open('config.txt', 'w') as f:
            f.write('{'+'\n')
            #Boards
            if self.boards.currentText() == "MKS SBASE v1.3":
                f.write('\t'+'"Board": "'+ self.boards.currentText() + '",' +'\n' )
                f.write('\t'+'"Modules":['+'\n')
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "On load",'+'\n'+'\t'+'"Type": "MCP4451",'+'\n'+'\t'+'"Comment": "Digipot for joints/Axis 0 - 3",'+'\n'+'\t'+'\t'+'"I2C SDA pin": "0.0",'+'\n'+'\t'+'\t'+'"I2C SCL pin": "0.1",'+'\n'+'\t'+'\t'+'"I2C address": 0,'+'\n'+'\t'+'\t'+'"Max current": 2.0,'+'\n'+'\t'+'\t'+'"Factor": 113.33,'+'\n'+'\t'+'\t'+'"Current 0":'+'\t'+self.xaxiscur.text()+','+'\n'+'\t'+'\t'+'"Current 1":'+'\t'+self.yaxiscur.text()+','+'\n'+'\t'+'\t'+'"Current 2":'+'\t'+self.zaxiscur.text()+','+'\n'+'\t'+'\t'+'"Current 3":'+'\t'+self.e0axiscur.text()+'\n'+'\t'+'},'+'\n')
                f.write('\t'+'{'+'\n'+'\t'+'"Thread": "On load",'+'\n'+'\t'+'"Type": "MCP4451",'+'\n'+'\t'+'"Comment": "Digipot for joints/Axis 4 - 7",'+'\n'+'\t'+'\t'+'"I2C SDA pin": "0.0",'+'\n'+'\t'+'\t'+'"I2C SCL pin": "0.1",'+'\n'+'\t'+'\t'+'"I2C address": 2,'+'\n'+'\t'+'\t'+'"Max current": 2.0,'+'\n'+'\t'+'\t'+'"Factor": 113.33,'+'\n'+'\t'+'\t'+'"Current 0":'+'\t'+self.e1axiscur.text()+','+'\n'+'\t'+'\t'+'"Current 1":'+'\t'+'0.0'+','+'\n'+'\t'+'\t'+'"Current 2":'+'\t'+'0.0'+','+'\n'+'\t'+'\t'+'"Current 3":'+'\t'+'0.0'+'\n'+'\t'+'},'+'\n')
            else:
                f.write('\t'+'"Board": "'+ self.boards.currentText() + '",' +'\n' )
                f.write('\t'+'"Modules":['+'\n')
            #E-stop
            if self.estop.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Servo",'+'\n'+'\t'+'"Type": "eStop",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.estoptxt.text() + '",' +'\n'+'\t'+'\t'+'"Pin":'+'\t'+'\t'+'\t'+'\t'+ '"' + self.estoppin.text()+'"'+'\n'+'\t'+'},'+'\n')
            #X axis
            if self.xaxis.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.xaxistxt.text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+'\t'+ self.xaxisjoint.text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + self.xaxisstep.text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t'+'\t' +'"' + self.xaxisdir.text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t'+'\t' +'"' + self.xaxisenable.text()+'"' +'\n'+'\t'+'},'+'\n')
            #X axis TMC
            if self.xaxistmc.currentText() != "None": f.write('\t'+'{'+'\n'+'\t'+'"Thread": "On Load",'+'\n'+'\t'+'"Type": "' + self.xaxistmc.currentText() + '",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.xaxistxt.text() + ' TMC Driver",' +'\n'+'\t'+'\t'+'"RX pin":'+'\t'+'\t'+'\t'+ "1.10" +','+'\n'+'\t'+'\t'+'"RSense":'+'\t'+'\t'+'\t' +'"' + self.xaxiscursense.text()+'",'+'\n'+'\t'+'\t'+'"Current":'+'\t'+'\t' +'"' + self.xaxiscur.text()+'",' +'\n'+'\t'+'\t'+'"Microsteps":'+'\t'+'\t'+'\t' +'"' + self.xaxismicrostep.text()+'",' +'\n'+'\t'+'\t'+'"Stealth chop":'+'\t'+'\t'+'\t' +'"' + self.xaxisstealthcop.currentText()+'"' +'\n'+'\t'+'},'+'\n')
            #y axis
            if self.yaxis.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.yaxistxt.text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+'\t'+ self.yaxisjoint.text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + self.yaxisstep.text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t'+'\t' +'"' + self.yaxisdir.text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t'+'\t' +'"' + self.yaxisenable.text()+'"' +'\n'+'\t'+'},'+'\n')
            #y axis TMC
            if self.yaxistmc.currentText() != "None": f.write('\t'+'{'+'\n'+'\t'+'"Thread": "On Load",'+'\n'+'\t'+'"Type": "' + self.yaxistmc.currentText() + '",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.yaxistxt.text() + ' TMC Driver",' +'\n'+'\t'+'\t'+'"RX pin":'+'\t'+'\t'+'\t'+ "1.9" +','+'\n'+'\t'+'\t'+'"RSense":'+'\t'+'\t'+'\t' +'"' + self.yaxiscursense.text()+'",'+'\n'+'\t'+'\t'+'"Current":'+'\t'+'\t' +'"' + self.yaxiscur.text()+'",' +'\n'+'\t'+'\t'+'"Microsteps":'+'\t'+'\t'+'\t' +'"' + self.yaxismicrostep.text()+'",' +'\n'+'\t'+'\t'+'"Stealth chop":'+'\t'+'\t'+'\t' +'"' + self.yaxisstealthcop.currentText()+'"' +'\n'+'\t'+'},'+'\n')
            #z axis
            if self.zaxis.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.zaxistxt.text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+'\t'+ self.zaxisjoint.text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + self.zaxisstep.text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t'+'\t' +'"' + self.zaxisdir.text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t'+'\t' +'"' + self.zaxisenable.text()+'"' +'\n'+'\t'+'},'+'\n')
            #Z axis TMC
            if self.zaxistmc.currentText() != "None": f.write('\t'+'{'+'\n'+'\t'+'"Thread": "On Load",'+'\n'+'\t'+'"Type": "' + self.zaxistmc.currentText() + '",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.zaxistxt.text() + ' TMC Driver",' +'\n'+'\t'+'\t'+'"RX pin":'+'\t'+'\t'+'\t'+ "1.8" +','+'\n'+'\t'+'\t'+'"RSense":'+'\t'+'\t'+'\t' +'"' + self.zaxiscursense.text()+'",'+'\n'+'\t'+'\t'+'"Current":'+'\t'+'\t' +'"' + self.zaxiscur.text()+'",' +'\n'+'\t'+'\t'+'"Microsteps":'+'\t'+'\t'+'\t' +'"' + self.zaxismicrostep.text()+'",' +'\n'+'\t'+'\t'+'"Stealth chop":'+'\t'+'\t'+'\t' +'"' + self.zaxisstealthcop.currentText()+'"' +'\n'+'\t'+'},'+'\n')
            #e0 axis
            if self.e0axis.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.e0axistxt.text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+'\t'+ self.e0axisjoint.text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + self.e0axisstep.text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t'+'\t' +'"' + self.e0axisdir.text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t'+'\t' +'"' + self.e0axisenable.text()+'"' +'\n'+'\t'+'},'+'\n')
            #E0 axis TMC
            if self.e0axistmc.currentText() != "None": f.write('\t'+'{'+'\n'+'\t'+'"Thread": "On Load",'+'\n'+'\t'+'"Type": "' + self.e0axistmc.currentText() + '",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.e0axistxt.text() + ' TMC Driver",' +'\n'+'\t'+'\t'+'"RX pin":'+'\t'+'\t'+'\t'+ "1.4" +','+'\n'+'\t'+'\t'+'"RSense":'+'\t'+'\t'+'\t' +'"' + self.e0axiscursense.text()+'",'+'\n'+'\t'+'\t'+'"Current":'+'\t'+'\t' +'"' + self.e0axiscur.text()+'",' +'\n'+'\t'+'\t'+'"Microsteps":'+'\t'+'\t'+'\t' +'"' + self.e0axismicrostep.text()+'",' +'\n'+'\t'+'\t'+'"Stealth chop":'+'\t'+'\t'+'\t' +'"' + self.e0axisstealthcop.currentText()+'"' +'\n'+'\t'+'},'+'\n')
            #e1 axis
            if self.e1axis.isChecked() == 1: f.write('\t'+'{'+'\n'+'\t'+'"Thread": "Base",'+'\n'+'\t'+'"Type": "stepgen",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.e1axistxt.text() + '",' +'\n'+'\t'+'\t'+'"Joint Number":'+'\t'+'\t'+'\t'+ self.e1axisjoint.text()+','+'\n'+'\t'+'\t'+'"Step Pin":'+'\t'+'\t'+'\t' +'"' + self.e1axisstep.text()+'",'+'\n'+'\t'+'\t'+'"Direction Pin":'+'\t'+'\t' +'"' + self.e1axisdir.text()+'",' +'\n'+'\t'+'\t'+'"Enable Pin":'+'\t'+'\t'+'\t' +'"' + self.e1axisenable.text()+'"' +'\n'+'\t'+'},'+'\n')
            #e1 axis TMC
            if self.e1axistmc.currentText() != "None": f.write('\t'+'{'+'\n'+'\t'+'"Thread": "On Load",'+'\n'+'\t'+'"Type": "' + self.e1axistmc.currentText() + '",'+'\n'+'\t'+'\t'+'"Comment":'+'\t'+'\t'+'\t'+'"'+ self.e1axistxt.text() + ' TMC Driver",' +'\n'+'\t'+'\t'+'"RX pin":'+'\t'+'\t'+'\t'+ "1.1" +','+'\n'+'\t'+'\t'+'"RSense":'+'\t'+'\t'+'\t' +'"' + self.e1axiscursense.text()+'",'+'\n'+'\t'+'\t'+'"Current":'+'\t'+'\t' +'"' + self.e1axiscur.text()+'",' +'\n'+'\t'+'\t'+'"Microsteps":'+'\t'+'\t'+'\t' +'"' + self.e1axismicrostep.text()+'",' +'\n'+'\t'+'\t'+'"Stealth chop":'+'\t'+'\t'+'\t' +'"' + self.e1axisstealthcop.currentText()+'"' +'\n'+'\t'+'},'+'\n')
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
            
            #write out data to save file for hmi
            with open('save.txt', 'w') as s:
                #boards line 1
                s.write(str(self.boards.currentText())+'|'+'\n')
                #Xaxis line 2
                s.write(str(self.xaxis.isChecked())+'|'+ self.xaxistxt.text()+'|'+self.xaxisjoint.text()+'|'+self.xaxisstep.text()+'|'+self.xaxisdir.text()+'|'+self.xaxisenable.text()+'|'+self.xaxiscur.text()+'|'+self.xaxistmc.currentText()+'|'+self.xaxiscursense.text()+'|'+self.xaxismicrostep.text()+'|'+self.xaxisstealthcop.currentText()+'|'+'\n')
                #Yaxis line 3
                s.write(str(self.yaxis.isChecked())+'|'+ self.yaxistxt.text()+'|'+self.yaxisjoint.text()+'|'+self.yaxisstep.text()+'|'+self.yaxisdir.text()+'|'+self.yaxisenable.text()+'|'+self.yaxiscur.text()+'|'+self.yaxistmc.currentText()+'|'+self.yaxiscursense.text()+'|'+self.yaxismicrostep.text()+'|'+self.yaxisstealthcop.currentText()+'|'+'\n')
                #Zaxis line 4
                s.write(str(self.zaxis.isChecked())+'|'+ self.zaxistxt.text()+'|'+self.zaxisjoint.text()+'|'+self.zaxisstep.text()+'|'+self.zaxisdir.text()+'|'+self.zaxisenable.text()+'|'+self.zaxiscur.text()+'|'+self.zaxistmc.currentText()+'|'+self.zaxiscursense.text()+'|'+self.zaxismicrostep.text()+'|'+self.zaxisstealthcop.currentText()+'|'+'\n')
                #E0axis line 5
                s.write(str(self.e0axis.isChecked())+'|'+ self.e0axistxt.text()+'|'+self.e0axisjoint.text()+'|'+self.e0axisstep.text()+'|'+self.e0axisdir.text()+'|'+self.e0axisenable.text()+'|'+self.e0axiscur.text()+'|'+self.e0axistmc.currentText()+'|'+self.e0axiscursense.text()+'|'+self.e0axismicrostep.text()+'|'+self.e0axisstealthcop.currentText()+'|'+'\n')
                #E1axis line 6
                s.write(str(self.e1axis.isChecked())+'|'+ self.e1axistxt.text()+'|'+self.e1axisjoint.text()+'|'+self.e1axisstep.text()+'|'+self.e1axisdir.text()+'|'+self.e1axisenable.text()+'|'+self.e1axiscur.text()+'|'+self.e1axistmc.currentText()+'|'+self.e1axiscursense.text()+'|'+self.e1axismicrostep.text()+'|'+self.e1axisstealthcop.currentText()+'|'+'\n')
                #output0 line 7
                s.write(str(self.outchk0.isChecked())+'|'+ self.outtxt0.text()+'|'+self.outpin0.text()+'|'+self.outstate0.currentText()+'|'+str(self.outinv0.isChecked())+'|'+'\n')
                #output1 line 8
                s.write(str(self.outchk1.isChecked())+'|'+ self.outtxt1.text()+'|'+self.outpin1.text()+'|'+self.outstate1.currentText()+'|'+str(self.outinv1.isChecked())+'|'+'\n')
                #output2 line 9
                s.write(str(self.outchk2.isChecked())+'|'+ self.outtxt2.text()+'|'+self.outpin2.text()+'|'+self.outstate2.currentText()+'|'+str(self.outinv2.isChecked())+'|'+'\n')
                #output3 line 10
                s.write(str(self.outchk3.isChecked())+'|'+ self.outtxt3.text()+'|'+self.outpin3.text()+'|'+self.outstate3.currentText()+'|'+str(self.outinv3.isChecked())+'|'+'\n')
                #output4 line 11
                s.write(str(self.outchk4.isChecked())+'|'+ self.outtxt4.text()+'|'+self.outpin4.text()+'|'+self.outstate4.currentText()+'|'+str(self.outinv4.isChecked())+'|'+'\n')
                #output5 line 12
                s.write(str(self.outchk5.isChecked())+'|'+ self.outtxt5.text()+'|'+self.outpin5.text()+'|'+self.outstate5.currentText()+'|'+str(self.outinv5.isChecked())+'|'+'\n')
                #output6 line 13
                s.write(str(self.outchk6.isChecked())+'|'+ self.outtxt6.text()+'|'+self.outpin6.text()+'|'+self.outstate6.currentText()+'|'+str(self.outinv6.isChecked())+'|'+'\n')
                #output7 line 14
                s.write(str(self.outchk7.isChecked())+'|'+ self.outtxt7.text()+'|'+self.outpin7.text()+'|'+self.outstate7.currentText()+'|'+str(self.outinv7.isChecked())+'|'+'\n')
                #input0 line 15
                s.write(str(self.inchk0.isChecked())+'|'+ self.intxt0.text()+'|'+self.inpin0.text()+'|'+self.instate0.currentText()+'|'+str(self.ininv0.isChecked())+'|'+'\n')
                #input1 line 16
                s.write(str(self.inchk1.isChecked())+'|'+ self.intxt1.text()+'|'+self.inpin1.text()+'|'+self.instate1.currentText()+'|'+str(self.ininv1.isChecked())+'|'+'\n')
                #input2 line 17
                s.write(str(self.inchk2.isChecked())+'|'+ self.intxt2.text()+'|'+self.inpin2.text()+'|'+self.instate2.currentText()+'|'+str(self.ininv2.isChecked())+'|'+'\n')
                #input3 line 18
                s.write(str(self.inchk3.isChecked())+'|'+ self.intxt3.text()+'|'+self.inpin3.text()+'|'+self.instate3.currentText()+'|'+str(self.ininv3.isChecked())+'|'+'\n')
                #input4 line 19
                s.write(str(self.inchk4.isChecked())+'|'+ self.intxt4.text()+'|'+self.inpin4.text()+'|'+self.instate4.currentText()+'|'+str(self.ininv4.isChecked())+'|'+'\n')
                #input5 line 20
                s.write(str(self.inchk5.isChecked())+'|'+ self.intxt5.text()+'|'+self.inpin5.text()+'|'+self.instate5.currentText()+'|'+str(self.ininv5.isChecked())+'|'+'\n')
                #input6 line 21
                s.write(str(self.inchk6.isChecked())+'|'+ self.intxt6.text()+'|'+self.inpin6.text()+'|'+self.instate6.currentText()+'|'+str(self.ininv6.isChecked())+'|'+'\n')
                #input7 line 22
                s.write(str(self.inchk7.isChecked())+'|'+ self.intxt7.text()+'|'+self.inpin7.text()+'|'+self.instate7.currentText()+'|'+str(self.ininv7.isChecked())+'|'+'\n')
                #reset pin line 23
                s.write(str(self.estop.isChecked())+'|'+ self.estoptxt.text()+'|'+self.estoppin.text()+'|'+'\n')
                #reset pin line 24
                s.write(str(self.reset.isChecked())+'|'+ self.resettxt.text()+'|'+self.resetpin.text()+'|'+'\n')
                #PWM0 line 25
                s.write(str(self.pwm0.isChecked())+'|'+ self.pwmtxt0.text()+'|'+self.pwmmax0.text()+'|'+self.pwmpin0.text()+'|'+str(self.pwmhw0.isChecked())+'|'+str(self.pwmvf0.isChecked())+'|'+self.pwmfreq0.text()+'|'+self.pwmperiod0.text()+'|'+self.pwmspi0.text()+'|'+'\n')
                #PWM1 line 26
                s.write(str(self.pwm1.isChecked())+'|'+ self.pwmtxt1.text()+'|'+self.pwmmax1.text()+'|'+self.pwmpin1.text()+'|'+str(self.pwmhw1.isChecked())+'|'+str(self.pwmvf1.isChecked())+'|'+self.pwmfreq1.text()+'|'+self.pwmperiod1.text()+'|'+self.pwmspi1.text()+'|'+'\n')
                #PWM2 line 27
                s.write(str(self.pwm2.isChecked())+'|'+ self.pwmtxt2.text()+'|'+self.pwmmax2.text()+'|'+self.pwmpin2.text()+'|'+str(self.pwmhw2.isChecked())+'|'+str(self.pwmvf2.isChecked())+'|'+self.pwmfreq2.text()+'|'+self.pwmperiod2.text()+'|'+self.pwmspi2.text()+'|'+'\n')
                #PWM3 line 28
                s.write(str(self.pwm3.isChecked())+'|'+ self.pwmtxt3.text()+'|'+self.pwmmax3.text()+'|'+self.pwmpin3.text()+'|'+str(self.pwmhw3.isChecked())+'|'+str(self.pwmvf3.isChecked())+'|'+self.pwmfreq3.text()+'|'+self.pwmperiod3.text()+'|'+self.pwmspi3.text()+'|'+'\n')
                #PWM4 line 29
                s.write(str(self.pwm4.isChecked())+'|'+ self.pwmtxt4.text()+'|'+self.pwmmax4.text()+'|'+self.pwmpin4.text()+'|'+str(self.pwmhw4.isChecked())+'|'+str(self.pwmvf4.isChecked())+'|'+self.pwmfreq4.text()+'|'+self.pwmperiod4.text()+'|'+self.pwmspi4.text()+'|'+'\n')
                #PWM5 line 30
                s.write(str(self.pwm5.isChecked())+'|'+ self.pwmtxt5.text()+'|'+self.pwmmax5.text()+'|'+self.pwmpin5.text()+'|'+str(self.pwmhw5.isChecked())+'|'+str(self.pwmvf5.isChecked())+'|'+self.pwmfreq5.text()+'|'+self.pwmperiod5.text()+'|'+self.pwmspi5.text()+'|'+'\n')
                #PWM6 line 31
                s.write(str(self.pwm6.isChecked())+'|'+ self.pwmtxt6.text()+'|'+self.pwmmax6.text()+'|'+self.pwmpin6.text()+'|'+str(self.pwmhw6.isChecked())+'|'+str(self.pwmvf6.isChecked())+'|'+self.pwmfreq6.text()+'|'+self.pwmperiod6.text()+'|'+self.pwmspi6.text()+'|'+'\n')
                #rc Servo line 32
                s.write(str(self.rcservo.isChecked())+'|'+ self.rcservotxt.text()+'|'+self.rcservopin.text()+'|'+self.rcservospi.text()+'|'+'\n')
                #QEM line 33
                s.write(str(self.qem.isChecked())+'|'+ self.qemtxt.text()+'|'+self.qempv.text()+'|'+self.qemcha.text()+'|'+self.qemchb.text()+'|'+self.qemipin.text()+'|'+self.qeminput.text()+'|'+str(self.qemstate.currentText())+'|'+'\n')
                #Encoder 0 line 34
                s.write(str(self.enc0.isChecked())+'|'+ self.enctxt0.text()+'|'+self.encpv0.text()+'|'+self.encapin0.text()+'|'+self.encbpin0.text()+'|'+self.encipin0.text()+'|'+self.encinput0.text()+'|'+str(self.encstate0.currentText())+'|'+'\n')
                #Encoder 1 line 35
                s.write(str(self.enc1.isChecked())+'|'+ self.enctxt1.text()+'|'+self.encpv1.text()+'|'+self.encapin1.text()+'|'+self.encbpin1.text()+'|'+self.encipin1.text()+'|'+self.encinput1.text()+'|'+str(self.encstate1.currentText())+'|'+'\n')
                #Encoder 2 line 36
                s.write(str(self.enc2.isChecked())+'|'+ self.enctxt2.text()+'|'+self.encpv2.text()+'|'+self.encapin2.text()+'|'+self.encbpin2.text()+'|'+self.encipin2.text()+'|'+self.encinput2.text()+'|'+str(self.encstate2.currentText())+'|'+'\n')
                #Encoder 3 line 37
                s.write(str(self.enc3.isChecked())+'|'+ self.enctxt3.text()+'|'+self.encpv3.text()+'|'+self.encapin3.text()+'|'+self.encbpin3.text()+'|'+self.encipin3.text()+'|'+self.encinput3.text()+'|'+str(self.encstate3.currentText())+'|'+'\n')
                #temp 0 line 38
                s.write(str(self.temp0.isChecked())+'|'+ self.temptxt0.text()+'|'+self.temppv0.text()+'|'+self.temppin0.text()+'|'+self.tempr0.text()+'|'+self.tempt0.text()+'|'+self.tempbeta0.text()+'|'+'\n')
                #temp 1 line 39
                s.write(str(self.temp1.isChecked())+'|'+ self.temptxt1.text()+'|'+self.temppv1.text()+'|'+self.temppin1.text()+'|'+self.tempr1.text()+'|'+self.tempt1.text()+'|'+self.tempbeta1.text()+'|'+'\n')
                #temp 2 line 40
                s.write(str(self.temp2.isChecked())+'|'+ self.temptxt2.text()+'|'+self.temppv2.text()+'|'+self.temppin2.text()+'|'+self.tempr2.text()+'|'+self.tempt2.text()+'|'+self.tempbeta2.text()+'|'+'\n')
                #temp 3 line 41
                s.write(str(self.temp3.isChecked())+'|'+ self.temptxt3.text()+'|'+self.temppv3.text()+'|'+self.temppin3.text()+'|'+self.tempr3.text()+'|'+self.tempt3.text()+'|'+self.tempbeta3.text()+'|'+'\n')
                #swtich 0 line 42
                s.write(str(self.sw0.isChecked())+'|'+ self.swtxt0.text()+'|'+self.swpv0.text()+'|'+self.swpin0.text()+'|'+self.swsp0.text()+'|'+self.swmode0.currentText()+'|'+'\n')
                #swtich 1 line 43
                s.write(str(self.sw1.isChecked())+'|'+ self.swtxt1.text()+'|'+self.swpv1.text()+'|'+self.swpin1.text()+'|'+self.swsp1.text()+'|'+self.swmode1.currentText()+'|'+'\n')
                #swtich 2 line 44
                s.write(str(self.sw2.isChecked())+'|'+ self.swtxt2.text()+'|'+self.swpv2.text()+'|'+self.swpin2.text()+'|'+self.swsp2.text()+'|'+self.swmode2.currentText()+'|'+'\n')


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()