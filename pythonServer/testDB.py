#!/usr/bin/python
import mysql.connector
from os import listdir

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root"
)

mycursor = mydb.cursor()

mycursor.execute("use nba;")
mycursor.execute("show tables;")

for cur in mycursor:
    print(cur)
