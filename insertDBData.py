#!/usr/bin/python
import mysql.connector
from os import listdir
from sys import argv
import progressbar

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS " + argv[1])
mycursor.execute("use " + argv[1])

datapath = argv[2] 

for sqlFile in listdir(datapath):
	#open formatted sql script and run all commands in the file
	sqlScript   = open(datapath + "/" + sqlFile,"r")
	cmds = ""
	delimiterSection = False
	for line in sqlScript.readlines():
		if line.startswith("--") or line.startswith("/"):
			continue
		cmds += line
	sqlCommands = cmds.split(";")
	sqlScript.close()

	print("Inserting " + sqlFile + " to database " + argv[1] + "\n")
	bar = progressbar.ProgressBar(max_value=len(sqlCommands))
	pBar = 0
	for cmd in sqlCommands:
		if not cmd.strip():
			continue
		mycursor.execute(cmd.strip())
		pBar += 1
		bar.update(pBar)
	mydb.commit()
	print("\n")
	print("Complete!\n")

mydb.close()
