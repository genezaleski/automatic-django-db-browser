#!/usr/bin/python
import mysql.connector
from os import listdir
from sys import argv

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root"
)

#Connect to local database and use parameter specified DB
mycursor = mydb.cursor()
mycursor.execute("use " + argv[1] + ";")

#Get all tables in database
tables = []
mycursor.execute("show tables;")
for cur in mycursor:
	print(cur)
