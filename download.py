#!/usr/bin/python

from sys import modules
import subprocess

verifyCommand = ["dpkg","--list","mysql-server"]

serverInstalled = subprocess.check_output(verifyCommand).decode('utf-8')

if "mysql-server" in serverInstalled:
    print("Requirement satisfied: mySQL Server is already installed.")
else:
    downloadCommand = ["sudo","apt","install","mysql","server"] 
    subprocess.run(downloadCommand)


if "django" in modules:
    print("Requirement satisfied: Python Django is already installed.") 
else:
    downloadCommand = ["sudo","pip3","install","django"]
    subprocess.run(downloadCommand)
