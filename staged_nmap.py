#!/bin/python3

import argparse
import subprocess
import xml.etree.ElementTree as ET

# sort out command line args
parser = argparse.ArgumentParser()
parser.add_argument("host", help="The IP address or hostname of the scan target")
args = parser.parse_args()

host = args.host

# run initial nmap scan and get the output

initialscan = subprocess.run(['nmap', '-T4','-p-','-oX','-',host], stdout=subprocess.PIPE)
initialresult = initialscan.stdout.decode('utf-8')

# parse the output and grab open ports

root = ET.fromstring(initialresult)
openports = list()

for port in root.findall(".//port"):
	 openports.append(port.attrib["portid"])


