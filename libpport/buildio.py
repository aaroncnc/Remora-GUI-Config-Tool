import os
from datetime import datetime

def build(parent):
	filePath = os.path.join(parent.configPath, 'io.hal')
	parent.machinePTE.appendPlainText(f'Building {filePath}')
	contents = []
	contents = ['# This file was created with the Parallel Port Configuration Tool on ']
	contents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	contents.append('# If you make changes to this file DO NOT use the Configuration Tool\n\n')

	pins = {'in':{'inpins':['02', '03', '04', '05', '06',
							'07', '08', '09', '10', '11', '12', '13', '15'],
							'outpins':['01', '14', '16', '17']},
				'out':{'inpins':['10', '11', '12', '13', '15'],
							'outpins':['01', '02', '03', '04', '05',
							'06', '07', '08', '09', '14', '16', '17']}}

	inPins = pins[parent.pp1typeCB.currentData()]['inpins']
	outPins = pins[parent.pp1typeCB.currentData()]['outpins']


	input_dict = {
		'Joint 0 Home':'net joint-0-home joint.0.home-sw-in <= ',
		'Joint 1 Home':'net joint-1-home joint.1.home-sw-in <= ',
		'Joint 2 Home':'net joint-2-home joint.2.home-sw-in <= ',
		'Joint 3 Home':'net joint-3-home joint.3.home-sw-in <= ',
		'Joint 4 Home':'net joint-4-home joint.4.home-sw-in <= ',
		'Joint 5 Home':'net joint-5-home joint.5.home-sw-in <= ',
		'Joint 6 Home':'net joint-6-home joint.6.home-sw-in <= ',
		'Joint 7 Home':'net joint-7-home joint.7.home-sw-in <= ',
		'Joint 8 Home':'net joint-8-home joint.8.home-sw-in <= ',
		'Home All':'fix me',

		'Joint 0 Plus':'net pos-limit-joint-0 joint.0.pos-lim-sw-in <= ',
		'Joint 0 Minus':'net neg-limit-joint-0 joint.0.neg-lim-sw-in <= ',
		'Joint 0 Both':'net both-limit-joint-0 joint.0.pos-lim-sw-in\n'
			'net both-limit-joint-0 joint.0.neg-lim-sw-in <= ',
		'Joint 1 Plus':'net pos-limit-joint-1 joint.1.pos-lim-sw-in <= ',
		'Joint 1 Minus':'net neg-limit-joint-1 joint.1.neg-lim-sw-in <= ',
		'Joint 1 Both':'net both-limit-joint-1 joint.1.pos-lim-sw-in\n'
			'net both-limit-joint-1 joint.1.neg-lim-sw-in <= ',
		'Joint 2 Plus':'net pos-limit-joint-2 joint.2.pos-lim-sw-in <= ',
		'Joint 2 Minus':'net neg-limit-joint-2 joint.2.neg-lim-sw-in <= ',
		'Joint 2 Both':'net both-limit-joint-2 joint.2.pos-lim-sw-in\n'
			'net both-limit-joint-2 joint.2.neg-lim-sw-in <= ',
		'Joint 3 Plus':'net pos-limit-joint-3 joint.3.pos-lim-sw-in <= ',
		'Joint 3 Minus':'net neg-limit-joint-3 joint.3.neg-lim-sw-in <= ',
		'Joint 3 Both':'net both-limit-joint-3 joint.3.pos-lim-sw-in\n'
			'net both-limit-joint-3 joint..neg-lim-sw-in <= ',
		'Joint 4 Plus':'net pos-limit-joint-4 joint.4.pos-lim-sw-in <= ',
		'Joint 4 Minus':'net neg-limit-joint-4 joint.4.neg-lim-sw-in <= ',
		'Joint 4 Both':'net both-limit-joint-4 joint.4.pos-lim-sw-in\n'
			'net both-limit-joint-4 joint.4.neg-lim-sw-in <= ',
		'Joint 5 Plus':'net pos-limit-joint-5 joint.5.pos-lim-sw-in <= ',
		'Joint 5 Minus':'net neg-limit-joint-5 joint.5.neg-lim-sw-in <= ',
		'Joint 5 Both':'net both-limit-joint-5 joint.5.pos-lim-sw-in\n'
			'net both-limit-joint-5 joint.5.neg-lim-sw-in <= ',
		'Joint 6 Plus':'net pos-limit-joint-6 joint.6.pos-lim-sw-in <= ',
		'Joint 6 Minus':'net neg-limit-joint-6 joint.6.neg-lim-sw-in <= ',
		'Joint 6 Both':'net both-limit-joint-6 joint.6.pos-lim-sw-in\n'
			'net both-limit-joint-6 joint.6.neg-lim-sw-in <= ',
		'Joint 7 Plus':'net pos-limit-joint-7 joint.7.pos-lim-sw-in <= ',
		'Joint 7 Minus':'net neg-limit-joint-7 joint.7.neg-lim-sw-in <= ',
		'Joint 7 Both':'net both-limit-joint-7 joint.7.pos-lim-sw-in\n'
			'net both-limit-joint-7 joint.7.neg-lim-sw-in <= ',
		'Joint 8 Plus':'net pos-limit-joint-8 joint.8.pos-lim-sw-in <= ',
		'Joint 8 Minus':'net neg-limit-joint-8 joint.8.neg-lim-sw-in <= ',
		'Joint 8 Both':'net both-limit-joint-8 joint.8.pos-lim-sw-in\n'
			'net both-limit-joint-8 joint.8.neg-lim-sw-in <= ',

		'Jog X Plus':'net jog-x-plus halui.axis.x.plus <= ',
		'Jog X Minus':'net jog-x-minus halui.axis.x.minus <= ',
		'Jog Y Plus':'net jog-y-plus halui.axis.y.plus <= ',
		'Jog Y Minus':'net jog-y-minus halui.axis.y.minus <= ',
		'Jog Z Plus':'net jog-z-plus halui.axis.z.plus <= ',
		'Jog Z Minus':'net jog-z-minus halui.axis.z.minus <= ',
		'Jog A Plus':'net jog-a-plus halui.axis.a.plus <= ',
		'Jog A Minus':'net jog-a-minus halui.axis.a.minus <= ',
		'Jog B Plus':'net jog-b-plus halui.axis.b.plus <= ',
		'Jog B Minus':'net jog-b-minus halui.axis.b.minus <= ',
		'Jog C Plus':'net jog-c-plus halui.axis.c.plus <= ',
		'Jog C Minus':'net jog-c-minus halui.axis.c.minus <= ',
		'Jog U Plus':'net jog-u-plus halui.axis.u.plus <= ',
		'Jog U Minus':'net jog-u-minus halui.axis.u.minus <= ',
		'Jog V Plus':'net jog-v-plus halui.axis.v.plus <= ',
		'Jog V Minus':'net jog-v-minus halui.axis.v.minus <= ',
		'Jog W Plus':'net jog-w-plus halui.axis.w.plus <= ',
		'Jog W Minus':'net jog-w-minus halui.axis.w.minus <= ',


		'Probe Input':'net probe-input motion.probe-input <= ',
		'Digital 0':'net digital-0-input motion.digital-in-00 <= ',
		'Digital 1':'net digital-1-input motion.digital-in-01 <= ',
		'Digital 2':'net digital-2-input motion.digital-in-02 <= ',
		'Digital 3':'net digital-3-input motion.digital-in-03 <= ',

		'Flood':'net coolant-flood iocontrol.0.coolant-flood <= ',
		'Mist':'net coolant-mist iocontrol.0.coolant-mist <= ',
		'Lube Level':'net lube-level iocontrol.0.lube_level <= ',
		'Tool Changed':'net tool-changed iocontrol.0.tool-changed <= ',
		'Tool Prepared':'net tool-prepared iocontrol.0.tool-prepared <= '
		}

	# build the inputs

	invert = {True:'-not', False:''}
	for i, (k, v) in enumerate(parent.p1inBtns.items()):
		if v.text() in input_dict:
			sense = invert[parent.p1inCkBxs[f'p1InCB_{i}'].isChecked()]
			contents.append(f'{input_dict[v.text()]} parport.0.pin-{inPins[i]}-in{sense}\n')
		#if parent.p1inCkBxs[f'p1InCB_{i}'].isChecked():
		#	contents.append(f'setp parport.0.pin-{inPins[i]}-in-reset 1\n')

	for i, (k, v) in enumerate(parent.p2inBtns.items()):
		if v.text() in input_dict:
			sense = parent.p1inCkBxs[f'p2InCB_{i}'].isChecked()
			contents.append(f'{input_dict[v.text()]} parport.1.pin-{inPins[i]}-in{sense}\n')
		#if parent.p1inCkBxs[f'p2InCB_{i}'].isChecked():
		#	contents.append(f'setp parport.1.pin-{inPins[i]}-in-reset 1\n')


	'''
	# build inputs from qpushbutton menus
	for i in range(11):
		key = getattr(parent, 'inputPB_' + str(i)).text()
		invert = '_not' if getattr(parent, 'inputInvertCB_' + str(i)).isChecked() else ''
		if input_dict.get(key, False): # return False if key is not in dictionary
			contents.append(input_dict[key] + f'hm2_7i96.0.gpio.{i:03}.in{invert}\n')
		else: # handle special cases
			if key == 'Home All':
				contents.append('\n# Home All Joints\n')
				contents.append('net home-all ' + f'hm2_7i96.0.gpio.{i:03}.in{invert}\n')
				for i in range(5):
					if getattr(parent, 'axisCB_' + str(i)).currentData():
						contents.append('net home-all ' + f'joint.{i}.home-sw-in\n')
			elif key == 'External E Stop':
				contents.append('\n# External E-Stop\n')
				contents.append('loadrt estop_latch\n')
				contents.append('addf estop-latch.0 servo-thread\n')
				contents.append('net estop-loopout iocontrol.0.emc-enable-in <= estop-latch.0.ok-out\n')
				contents.append('net estop-loopin iocontrol.0.user-enable-out => estop-latch.0.ok-in\n')
				contents.append('net estop-reset iocontrol.0.user-request-enable => estop-latch.0.reset\n')
				contents.append(f'net remote-estop estop-latch.0.fault-in <= hm2_7i96.0.gpio.{i:03}.in{invert}\n\n')
	'''

	output_dict = {
	'Coolant Flood': 'net flood-output iocontrol.0.coolant-flood =>',
	'Coolant Mist': 'net mist-output iocontrol.0.coolant-mist =>',
	'Spindle On': 'net spindle-on spindle.0.on =>',
	'Spindle CW': 'net spindle-cw spindle.0.forward =>',
	'Spindle CCW': 'net spindle-ccw spindle.0.reverse =>',
	'Spindle Brake': 'net spindle-brake spindle.0.brake =>',
	'E-Stop Out': 'net estop-loop',
	'Digital Out 0': 'net digital-out-0 motion.digital-out-00 =>',
	'Digital Out 1': 'net digital-out-1 motion.digital-out-01 =>',
	'Digital Out 2': 'net digital-out-2 motion.digital-out-02 =>',
	'Digital Out 3': 'net digital-out-3 motion.digital-out-03 =>',
	'Drive Enable': 'net enable =>'
	}

	# build the outputs

	for i, (k, v) in enumerate(parent.p1outBtns.items()):
		if v.text() in output_dict:
			contents.append(f'{output_dict[v.text()]} parport.0.pin-{outPins[i]}-out\n')
		if parent.p1outCkBxs[f'p1OutCB_{i}'].isChecked():
			contents.append(f'setp parport.0.pin-{outPins[i]}-out-reset 1\n')

	for i, (k, v) in enumerate(parent.p2outBtns.items()):
		if v.text() in output_dict:
			contents.append(f'{output_dict[v.text()]} parport.1.pin-{outPins[i]}-out\n')
		if parent.p1outCkBxs[f'p2OutCB_{i}'].isChecked():
			contents.append(f'setp parport.1.pin-{outPins[i]}-out-reset 1\n')

	'''
	for i in range(6):
		key = getattr(parent, 'outputPB_' + str(i)).text()
		if output_dict.get(key, False): # return False if key is not in dictionary
			contents.append(output_dict[key] + f'hm2_7i96.0.ssr.00.out-0{i}\n')
		else: # handle special cases
			if key == 'E Stop Out':
				contents.append(f'net estop-loopin hm2_7i96.0.ssr.00.out-0{i}\n')
	'''

	try:
		with open(filePath, 'w') as f:
			f.writelines(contents)
			return True
	except OSError:
		parent.machinePTE.appendPlainText(f'OS error\n {traceback.print_exc()}')
		return False
