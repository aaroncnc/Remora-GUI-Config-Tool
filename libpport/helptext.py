"""
Return text based on the tab number passed
"""

def descriptions(index):
	if index == 0:   # Machine Tab
		return text_0
	elif index == 1: # Options Tab
		return text_1
	elif index == 2: # Parallel Port 1
		return text_2
	elif index == 3: # Parallel Port 2
		return text_3
	elif index == 4: # Axes
		return text_4
	elif index == 5: 
		return text_5
	elif index == 6: 
		return text_6

	elif index == 8:
		return text_8
	elif index == 9: # PLC Tab
		return text_9
	elif index == 10: # Pins Tab
		return text_10
	elif index == 11: # Info Tab
		return text_11
	elif index == 12: # PC Tab
		return text_12
	elif index == 20:
		return text_20
	elif index == 30:
		return text_30
	else:
		return text_no

text_0 = """
Help Text for Machine Tab

Maximum Linear Velocity is in User Units per second.

Manual Tool Change
	This option is if you run G code with more than one tool and the tools can be
	preset like BT and Cat holders. If you have collet type like ER and R8 you
	should not check this and you should only use one tool per G code program and
	touch it off before running the program.

PyVCP Panel
	This option adds the connections and a basic PyVCP panel.

Debug Options
	This sets the debug level that is used when an error happens. When an error
	occours the error information is sent to dmesg. Open a terminal and clear
	dmesg with sudo dmesg -c then run your configuration and to view the error
	in a terminal type dmesg.

"""

text_1 = """
Help Text for Outputs Tab

Axis Display Standard is Mill Lathe is XZ only

Thread Timing is usually not changed

Hal Files
Custom Hal is loaded after the main hal file
Post GUI Hal is loaded after the GUI has loaded
Shutdown Hal is only ran during shutdown
"""

text_2 = """
Help Text for Parallel Port 1 Tab

Select Port Type In or Out to get pins.

Port Address is usually 0

Step and Direction Joints must start at 0 and not skip
a joint. They can be in any order.
"""

text_3 = """
Help Text for Parallel Port 2 Tab

Select Port Type In or Out to get pins.

Port Address is usually 1

Step and Direction Joints must start at 0 and not skip
a joint. They can be in any order.
"""

text_4 = """
Help Text for Axes Tab

Select Step and Direction for an Axis and that tab will
be enabled
"""

text_5 = """
Help Text for PLC Tab

Classicladder PLC will add a basic PLC to the configuration. You can also set
the number of components that Classicladder starts with.
"""



text_6 = """
Help Text for Tool Changer Tab

"""

text_70 = """
Help Text for SS Cards Tab
"""

text_71 = """
Help Text for 7i64 Tab
"""
text_72 = """
Help Text for 7i69 Tab
"""
text_73 = """
Help Text for 7i70 Tab
"""
text_74 = """
Help Text for 7i71 Tab
"""
text_75 = """
Help Text for 7i72 Tab
"""
text_76 = """
Help Text for 7i73 Tab

Powered up no config running CR1 is solid red and CR2 is off
Powered up and LinuxCNC running CR1 is off and CR2 is blinking green

"""
text_77 = """
Help Text for 7i84 Tab
"""
text_78 = """
Help Text for 7i87 Tab
"""


text_8 = """
Help Text for Options Tab



Hal User Interface
	This option enables halui which exports hal pins so they can be connected to
	physical or VCP or used in your hal configuration. These include pins related
	to abort, tool, spindle, program, mode, mdi, coolant, max velocity, machine,
	lube, joint, jog, feed override, rapid override, e stop, axis and home.



GladeVCP Panel
	Not functioning at this point.


"""

text_9 = """
Help Text for PLC Tab


"""
text_10 = """
Help Text for Pins Tab

If you have the 7i96 connected press get pins to get the current pinout
"""

text_11 = """
Help Text for Info Tab

Get CPU information and NIC information
"""

text_12 = """
Help Text for PC Tab

To check if the network packet time is ok get the CPU speed from the Info Tab.
Then get the tmax time and put those values into the boxes then hit calculate.
Make sure you select if the CPU speed is gHz or mHz.

To get tMax you must have the 7i96 connected to the PC and be running the
configuration with LinuxCNC.
"""

text_20 = """
Help Text for Building the Configuration

Opening the sample ini file and modifying is the fastest way to get a working configuration.
Check Configuration will scan the configuration for errors
Build Configuration will build all the configuration files needed.
	The ini file is always overwritten.
	The configName.hal file will always be overwritten.
	The tool table, variable file, postgui.hal, custom.hal, configName.clp,
	configName.xml files are never overwritten if present. To get a new one delete
	the file and a new one will be created when you build the configuration.
"""

text_30 = """
Help Text for PC Setup

7i96 card requires the Master Branch of LinuxCNC

Mesa Ethernet Cards require LinuxCNC Uspace and the PREEMPT kernel.

Instructions to download and install Debian 9 and LinuxCNC Uspace with the
desktop of your choice

https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/
drill down to the latest version of the nonfree amd64 iso-cd netinst.iso

Burn to a CD if you have a PCI Ethernet card remove it, setup with the on board LAN only
Boot from the CD
Graphical Install, Do Not enter a Root Password! Just hit enter
Debian desktop environment, Mate, SSH server,Print server, standard system utilities

after booting to Debian 9 open a terminal
sudo nano /etc/lightdm/lightdm.conf
to log in without your user name a password uncomment and add your user name
autologin-user=yourusername
autologin-user-timeout=0
CTRL X and yes to save and exit.

Open the Synaptic Package Manager
search for linux-image and install linux-image-latest.version-rt

reboot the pc

in a terminal
uname -a     # it should report back PREEMT RT
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install dirmngr
sudo apt-get install software-properties-common
*** to get the buildbot current build
sudo apt-key adv --keyserver hkp://keys.gnupg.net --recv-key E0EE663E
sudo add-apt-repository "deb http://buildbot.linuxcnc.org/ stretch master-rtpreempt"
sudo apt-get update
sudo apt-get install linuxcnc-uspace

Configure the network adapter to work with an Ethernet card
To find the Ethernet adapter name
ip link show

sudo nano /etc/network/interfaces
auto enp0s25 << change to match your interface name
  iface enp0s25 inet static
    address 10.10.10.1
    netmask 255.255.255.0

shutdown and install a second LAN card if you need to connect to the internet

for git and programming tools
sudo apt-get install git-core git-gui make gcc

to add open in terminal to caja
sudo apt-get install caja-open-terminal

to be able to edit the menu add mozo
sudo apt-get install mozo
You will find it in System > Control Center > Main Menu
"""

text_no = """
No Help is found for this tab
"""

