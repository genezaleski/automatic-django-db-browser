#!/usr/bin/python
import mysql.connector
from os import listdir
from sys import argv
import djangoConversions 

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
	tables.append(cur[0])

#For each table in DB, get all fields and their data types
#Then, re-write models.py to include our new tables
djangoImport = "from django.db import models\n"
djangoModelMap = djangoConversions.modelDict
with open("./models.py","w") as djangoModels:
	djangoModels.write(djangoImport)
	djangoModels.write("\n")
	djangoModels.write("\n")
	for t in tables:
		if t in djangoConversions.djangoTables:
			continue
		djangoModels.write("class " + t + "(models.Model):\n")
		mycursor.execute("DESCRIBE " + t + ";")
		for f in mycursor:
			fieldName = f[0]
			primaryKeyFlag = False
			if "-" in fieldName:
				print(fieldName + " contains a '-', and is illegal as a variable name in Python. Skipping...")
				continue
			elif " " in fieldName:
				fieldName = fieldName.replace(" ","")
			elif fieldName == "id" or fieldName == "ID":
				primaryKeyFlag = True
			dataType  = f[1].decode("utf-8")
			variableLength = False
			if "varchar" in dataType:
				length = dataType.replace("varchar(","")
				length = length.replace(")","")
				dataType = "varchar(X)"
				variableLength = True
			elif "datetime" in dataType:
				dataType = "datetime"
			elif "tinyint" in dataType:
				dataType = "smallint"
			dModel = djangoModelMap[dataType]
			if variableLength:
				dModel = dModel.replace("X",length)
			if primaryKeyFlag:
				if dModel.find("()") > 0:
					dModel = dModel.replace("()","(primary_key=True)")
				else:
					dModel = dModel.replace(")",",primary_key=True)")
			line = "\t" + fieldName + " = " + dModel + "\n"
			djangoModels.write(line)
		djangoModels.write("\n")
		djangoModels.write("\tclass Meta:\n")
		djangoModels.write("\t\tdb_table = '" + t + "'\n")
		djangoModels.write("\n")
		djangoModels.write("\t" + "def __str__(self):\n")
		djangoModels.write("\t\treturn self.name\n")
		djangoModels.write("\n")
