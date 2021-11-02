# Remora-GUI-Config-Tool
This is a GUI config tool for Remora for use with linux cnc.

This is in alpha for the moment. not feature complete but a proof of concept.

Things still missing
Encoder support
Thermistors
PWM
Servo

The Save and load function of the tool only saves/loads the items needed for the config file. i need to add the rest of the new inputs.

Spindle is setup only for pwm to dac control. more options to come later.

Inputs missing the option for home+limit combo.

.
To run the tool you will need to have PyQt5 installed.

This can be done with the following command

python -m pip install PyQt5

To run the tool you must have both the .py and .ui file in the same folder and then run the .py file

.

The tool will generate 2 files when the save button is selected.

A config.txt and save.txt hal file and ini file

The config.txt file is put on the micro sd card and inserted into your main board.

The save.txt is used to save the gui config so it can be reloaded via the load config button, the save.txt must be in the same folder as the program.



.
If you find any errors or feed back please create an issue. 

