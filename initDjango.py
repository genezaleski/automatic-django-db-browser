#!/usr/bin/python

from subprocess import run,Popen
import os

#Create Django directory if it has not already been created
createDjango = ["django-admin","startproject","advDbPresentation"]

firstTimeSetup = False
if os.path.isdir(createDjango[-1]):
    print("Local Django Project already exists!")
else:
    firstTimeSetup = True
    run(createDjango)

#Change to django area to run relevant functions
pwd = os.getcwd()
os.chdir(createDjango[-1])

#Migrate relevant packages in django on first time setup
if firstTimeSetup:
    migrateCmd = ["python","manage.py","migrate"]
    run(migrateCmd)

#Start Django Server
startCmd = ["python","manage.py","runserver"]
djangoServer = Popen(startCmd)
print("Django Server Started!")

#Give the server 5 seconds to start before opening
run(["sleep","5"])

#Open page in firefox to show success
openCmd = ["firefox","http://127.0.0.1:8000/"]
ff = Popen(openCmd)
