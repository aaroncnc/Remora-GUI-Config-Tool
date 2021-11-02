import os, subprocess
from PyQt5.QtWidgets import (QMessageBox, QApplication, QGridLayout,
	QLabel, QPushButton, QFileDialog)

def isNumber(s):
	try:
		s[-1].isdigit()
		float(s)
		return True
	except ValueError:
		return False


def configNameChanged(parent, text):
	if text:
		parent.configNameUnderscored = text.replace(' ','_').lower()
		parent.configPath = os.path.expanduser('~/linuxcnc/configs') + '/' + parent.configNameUnderscored
		parent.pathLabel.setText(parent.configPath)
	else:
		parent.pathLabel.setText('')


def fileNew(parent):
	parent.errorMsgOk('Close the Tool,\n Then open', 'Info!')

def fileSaveAs(parent):
	parent.errorMsgOk('Change the Name,\n Then Save', 'Info!')

def copyOutput(parent):
	qclip = QApplication.clipboard()
	qclip.setText(parent.machinePTE.toPlainText())
	parent.statusbar.showMessage('Output copied to clipboard')


def fileDialog(parent, output=None, fileName = ''):
	if os.path.isdir(os.path.expanduser('~/linuxcnc/configs')):
		gcodeDir = os.path.expanduser('~/linuxcnc/nc_files')
	else:
		gcodeDir = os.path.expanduser('~/')
	fileName = QFileDialog.getOpenFileName(parent,
	caption="Select G Code File", directory=gcodeDir,
	filter='*.ngc', options=QFileDialog.DontUseNativeDialog,)
	if fileName:
		getattr(parent, f'{output}').setText(fileName[0])

