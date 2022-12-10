#!/usr/bin/python
import mysql.connector
from os import listdir
from sys import argv
import progressbar

# This function will return the contents of a passed db as a dictionary.
# @param database: name of the database to use
# @param dsTables: name of tables to retrieve (optional)
# @return parentDictionry: dictionary containing all fields as keys and
#	data as values (stored in lists)
def fetch(*args):

	mydb = mysql.connector.connect(
	  host="127.0.0.1",
	  user="root",
	  password="root"
	)
	
	mycursor = mydb.cursor(buffered=True)
	
	mycursor.execute("use " + args[0] + ";")

	if len(args) == 2:
		dbTables = args[1]
		if type(dbTables) == str:
			dbTables = [dbTables]
	else:
		djangoTables = ['auth_group',
			'auth_group_permissions',
			'auth_permission',
			'auth_user',
			'auth_user_groups',
			'auth_user_user_permissions',
			'django_admin_log',
			'django_content_type',
			'django_migrations',
			'django_session'
		]
		mycursor.execute("show tables;")
		dbTables = []
		for x in mycursor:
			tableName = x[0]
			if tableName not in djangoTables:
				dbTables.append(tableName)

	parentDict = {}
	for table in dbTables:
		print("Fetcing " + table + "...")
		mycursor.execute("DESCRIBE " + table + ";")
		fields = [x[0] for x in mycursor]
		mycursor.execute("SELECT count(*) FROM " + table + ";")
		totalData = [int(x[0]) for x in mycursor][0]
		mycursor.execute("SELECT * FROM " + table + ";")
		tableData = []
		bar = progressbar.ProgressBar(max_value=totalData)
		pbar = 0
		for row in mycursor:
			rowdict = {}
			for ii in range(0,len(fields)): 
				rowdict[fields[ii]] = row[ii]
			tableData.append(rowdict)
			pbar += 1
			bar.update(pbar)
		parentDict[table] = tableData
		print("\nComplete!\n")
	return parentDict

if __name__ == "__main__":
	if len(argv) < 3:
		fetch(argv[1])
	else:
		fetch(argv[1],argv[2::])
