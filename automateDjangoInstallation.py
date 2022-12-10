#!/usr/bin/python

from sys        import argv
from subprocess import Popen,run
from shutil     import copyfile
from time       import sleep
import os

def createDjangoApp(projectName,appName):
	#Create Django directory if it has not already been created
	createDjango = ["django-admin","startproject",projectName]
	
	firstTimeSetup = False
	if os.path.isdir(projectName):
		print("Local Django Project already exists!")
	else:
		firstTimeSetup = True
		run(createDjango)

	manage = "./" + projectName + "/manage.py"
	createCmd = ["python",manage,"startapp",appName]

	if os.path.isdir(createCmd[-1]):
		print("Local Django App has already been created!")
	else:
		run(createCmd)
		run(["mv",appName,projectName + "/."])
		print("Created local Django App!")

def connectDjangoToLocalhost(projectName,appName):
	#Write models.py file to import database in django
	makeModels(dbName)
	copyfile("./models.py","./" + projectName + "/" + appName + "/models.py")	

	#Migrate relevant packages in django on first time setup
	migrateCmd = ["python","./" + projectName + "/manage.py","makemigrations"]
	run(migrateCmd)
	migrateCmd = ["python","./" + projectName + "/manage.py","migrate"]
	run(migrateCmd)

def runDjango(projectName,appName):

	makeMigrations = ["python", "./" + projectName + "/manage.py","makemigrations"]	
	run(makeMigrations)
	migrate = ["python", "./" + projectName + "/manage.py","migrate"]	
	run(migrate)
	runserver = ["python", "./" + projectName + "/manage.py","runserver"]	
	Popen(runserver)

	sleep(10)
	openserver = ["firefox","http://127.0.0.1:8000/" + appName]	
	Popen(openserver)
	
if __name__ == "__main__":
	#Download Django and other packages with apt,pip, etc.
	print("Downloading Django!")
	cmd = ["python","download.py"]
	run(cmd)

	#Get Project and App name from user input
	projectName = input("Please enter the name of your Django Project.")
	projectName = projectName.strip()
	appName     = input("Please enter the name of your Django App.")
	appName     = appName.strip()

	#Create a Django app for use with your db
	createDjangoApp(projectName,appName)

	#Determine if user needs to create new database from .sql files
	# or specify a database name to use
	newDB = input("Would you like to create a new database? [Y/N]")
	if newDB.lower().strip() == "y":
		dbPath = input("Please enter a path to .sql files for inserting data.")
		insertDBData(appName,dbPath.strip())
	else: 
		dbName = input("Please input the name of the database you will be using.")

	#Write settings file to reference your database + config files
	cmd = ["python","writeApps.py",projectName,appName]
	run(cmd)
	cmd = ["python","makeSettings.py",projectName,appName]
	run(cmd)

	#Make views and apps for new project
	cmd = ["python","makeViews.py",dbName,projectName,appName]
	run(cmd)

	#With apps,settings, and views configured, start the database
	# open the home page
	runDjango(projectName,appName)
