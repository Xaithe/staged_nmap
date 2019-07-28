#!/bin/python3
import os
import argparse
import subprocess
import xml.etree.ElementTree as ET

# sort out command line args
parser = argparse.ArgumentParser()
parser.add_argument("host", help="The IP address or hostname of the scan target")
args = parser.parse_args()

host = args.host
wd = os.getcwd()
filename = wd + "/stagednmap.txt"
# run initial nmap scan and get the output

print("Running initial scan on {}".format(host))

initialscan = subprocess.run(["nmap","-T4","-p-","-oX","-",host], stdout=subprocess.PIPE)
initialresult = initialscan.stdout.decode("utf-8")

# parse the output and grab open ports

root = ET.fromstring(initialresult)
openports = list()

for port in root.findall(".//port"):
	 openports.append(port.attrib["portid"])

portparam = "-p{}".format(",".join(openports))

# Run deep scan
print("Running final scan on {}".format(host))

finalscan = subprocess.run(["nmap","-A",portparam,"-oN","-",host], stdout=subprocess.PIPE)
result = finalscan.stdout.decode("utf-8")

with open(filename, "w") as textout:
	textout.write(result)

print("Output saved to {}".format(filename))
