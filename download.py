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
sqlCliCmd = ["sudo","apt-get","install","python3-dev","default-libmysqlclient-dev","build-essential"]
subprocess.run(sqlCliCmd)

if "django" in modules:
    print("Requirement satisfied: Python Django is already installed.") 
else:
    downloadCommand = ["sudo","pip3","install","django"]
    subprocess.run(downloadCommand)
    downloadCommand = ["sudo","pip3","install","django-extensions"]
    subprocess.run(downloadCommand)
sqlCliPy = ["sudo","pip3","install","mysqlclient"]
subprocess.run(sqlCliPy)

if "progressbar2" in modules:
    print("Requirement satisfied: Python progressbar2 is already installed.")
else:
    downloadCommand = ["sudo","pip3","install","progressbar2"]
    subprocess.run(downloadCommand)
