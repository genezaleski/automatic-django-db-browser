#!/usr/bin/python

from sys import argv
from subprocess import Popen,run
from shutil import copyfile

from . import download,insertDBData,makeModels

def downloadDjangoAndDependencies():
	download()

def createDjangoApp(projectName,appName):
	#Create Django directory if it has not already been created
	createDjango = ["django-admin","startproject",projectName]
	
	firstTimeSetup = False
	if os.path.isdir(projectName):
		print("Local Django Project already exists!")
	else:
		firstTimeSetup = True
		run(createDjango)

	#Change to django area to run relevant functions
	pwd = os.getcwd()
	os.chdir(createDjango[-1])

	manage = projectName + "/manage.py"
	createCmd = ["python",manage,"startapp",appName]

	if isdir(createCmd[-1]):
	    print("Local Django App has already been created!")
	else:
	    run(createCmd)
	    print("Created local Django App!")

def connectDjangoToLocalhost(projectName,appName):
	#Write Settings.py file to connect Django to your Database

	#Write models.py file to import database in django
	makeModels(dbName)
	copyfile("./models.py","./" + projectName + "/" + appName + "/models.py")	

	#Migrate relevant packages in django on first time setup
	migrateCmd = ["python","manage.py","makemigrations"]
	run(migrateCmd)
	migrateCmd = ["python","manage.py","migrate"]
	run(migrateCmd)
	
if __name__ == "__main__":
	#Download Django and other packages with apt,pip, etc.
	downloadDjangoAndDependencies()

	#Create a Django app for use with your db
	createDjangoApp(projectName,appName)
