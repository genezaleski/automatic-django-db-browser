#!/usr/bin/python
import mysql.connector
from os import listdir
from sys import argv

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS " + argv[1])

datapath = argv[2] 

for sqlFile in listdir(datapath):
    #open formatted sql script and run all commands in the file
    sqlScript   = open(datapath + sqlFile,"r")
    sqlCommands = sqlScript.read().split(";")
    sqlScript.close()

    for cmd in sqlCommands:
        if not cmd.strip():
            continue
        mycursor.execute(cmd)
    mydb.commit()

mydb.close()
