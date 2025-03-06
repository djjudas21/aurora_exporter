import subprocess
import re
import argparse

# Read in args
parser = argparse.ArgumentParser()
parser.add_argument('-a', help="Inverter address", default='3')
parser.add_argument('-z', help="Serial Device", default='/dev/ttyUSB0')
parser.add_argument('-Y', help="Retry failed communications with inverter up to <num> times (1-100)", default='3')
args = parser.parse_args()

#result = subprocess.run(['aurora', '-a', args.a, '-d', '0', '-Y', args.Y, args.z], stdout=subprocess.PIPE)

# main output example
#Input 1 Voltage             =    202.644669 V
#Input 1 Current             =      0.468859 A
#Input 1 Power               =     95.011826 W
#
#Input 2 Voltage             =    201.899002 V
#Input 2 Current             =      0.446302 A
#Input 2 Power               =     90.108009 W
#
#Grid Voltage Reading        =    243.262344 V
#Grid Current Reading        =      0.854146 A
#Grid Power Reading          =    188.479767 W
#Frequency Reading           =     50.050049 Hz.
#
#DC/AC Conversion Efficiency =         101.8 %
#Inverter Temperature        =     29.993212 C
#Booster Temperature         =     28.770926 C

tmpoutput = """Input 1 Voltage             =    202.644669 V
Input 1 Current             =      0.468859 A
Input 1 Power               =     95.011826 W

Input 2 Voltage             =    201.899002 V
Input 2 Current             =      0.446302 A
Input 2 Power               =     90.108009 W

Grid Voltage Reading        =    243.262344 V
Grid Current Reading        =      0.854146 A
Grid Power Reading          =    188.479767 W
Frequency Reading           =     50.050049 Hz.

DC/AC Conversion Efficiency =         101.8 %
Inverter Temperature        =     29.993212 C
Booster Temperature         =     28.770926 C"""


#for line in result.stdout.splitlines():
for line in tmpoutput.splitlines():
    # convert bytes to str
#    line = line.decode()

    # skip empty lines
    if line == "":
        continue
    
    # parse the line
    pattern = '^\s*(.+)\s+=\s+(\d+\.\d+)\s([\w+%])'
    a = re.search(pattern, line)

    # slugify the key
    description = a.group(1).strip()
    key = description.replace(" ", "_").replace("/", "_").lower()
    val = a.group(2)
    unit = a.group(3)

    # prom output
    print(f"# HELP {key} {description}")
    print(f"# TYPE {key} gauge")
    print(f"{key} {val}")


# example prom output
# # HELP apt_upgrades_pending Apt package pending updates by origin.
# # TYPE apt_upgrades_pending gauge
# apt_upgrades_pending{origin="Ubuntu:20.04/focal-updates",arch="all"} 3
# apt_upgrades_pending{origin="Ubuntu:20.04/focal-updates",arch="arm64"} 2
# # HELP node_reboot_required Node reboot is required for software updates.
# # TYPE node_reboot_required gauge
# node_reboot_required 1
