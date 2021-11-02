import subprocess
import shutil
#command = 'ls'
#print(shutil.which(command) is not None)
#cmd_exists = lambda x: shutil.which(x) is not None

#editors = ['gedit', 'geany', 'pyroom', 'pluma', 'scite', 'kwrite',
#	'kate', 'mousepad', 'jedit']



'''
rc = subprocess.check_output(['which', 'wget'], encoding='UTF-8')
print(rc)
if rc:
    print('wget installed!')
else:
    print('wget missing in path!')
'''

def build(parent):
	linearUnits = [
		['Select', False],
		['Imperial', 'inch'],
		['Metric', 'metric']
		]

	for item in linearUnits:
		parent.linearUnitsCB.addItem(item[0], item[1])

	gui = [
		['Select', False],
		['Axis', 'axis'],
		['Touchy', 'touchy']
		]

	for item in gui:
		parent.guiCB.addItem(item[0], item[1])

	positionOffset = [
		['Select', False],
		['Relative', 'RELATIVE'],
		['Machine', 'MACHINE']
		]

	for item in positionOffset:
		parent.positionOffsetCB.addItem(item[0], item[1])

	positionFeedback = [
		['Select', False],
		['Commanded', 'COMMANDED'],
		['Actual', 'ACTUAL']
		]

	for item in positionFeedback:
		parent.positionFeedbackCB.addItem(item[0], item[1])


	editors = {'Gedit':'gedit', 'Geany':'geany', 'Pyroom':'pyroom',
		'Pluma':'pluma', 'Scite':'scite', 'Kwrite':'kwrite',
		'Kate':'kate', 'Mousepad':'mousepad', 'Jedit':'jedit',
		'XED':'xed'}
	installed = False
	for key, value in editors.items():
		if shutil.which(value) is not None:
			if not installed:
				parent.editorCB.addItem('Select', False)
				installed = True
			parent.editorCB.addItem(key, value)
	if not installed:
		parent.editorCB.addItem('None', False)
		parent.machinePTE.appendPlainText('No Editors were found!')

	debug = [
		['Debug Off', '0x00000000'],
		['Debug Configuration', '0x00000002'],
		['Debug Task Issues', '0x00000008'],
		['Debug NML', '0x00000010'],
		['Debug Motion Time', '0x00000040'],
		['Debug Interpreter', '0x00000080'],
		['Debug RCS', '0x00000100'],
		['Debug Interperter List', '0x00000800'],
		['Debug IO Control', '0x00001000'],
		['Debug O Word', '0x00002000'],
		['Debug Remap', '0x00004000'],
		['Debug Python', '0x00008000'],
		['Debug Named Parameters', '0x00010000'],
		['Debug Gdbon Signal', '0x00020000'],
		['Debug Python Task', '0x00040000'],
		['Debug User 1', '0x10000000'],
		['Debug User 2', '0x20000000'],
		['Debug Unconditional', '0x40000000'],
		['Debug All', '0x7FFFFFFF']
		]

	for item in debug:
		parent.debugCB.addItem(item[0], item[1])
