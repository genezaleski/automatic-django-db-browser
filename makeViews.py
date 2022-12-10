#!/usr/bin/python
import mysql.connector
from os import listdir
from sys import argv
from shutil import copyfile
import djangoConversions 

if len(argv) < 3:
	print("USAGE: makeViews.py <Database Name> <Project Name> <App Name>")
	exit()

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root"
)

#Connect to local database and use parameter specified DB
dbName      = argv[1]
projectName = argv[2]
appName     = argv[3]
mycursor    = mydb.cursor()
mycursor.execute("use " + dbName + ";")

#Get all tables in database
tables = []
mycursor.execute("show tables;")
for cur in mycursor:
	tables.append(cur[0])

#Write views.py file to represent your database as html pages
with open("./views.py","w") as djangoViews:
	djangoViews.write("from django.shortcuts import render\n")
	djangoViews.write("from django.http import HttpResponse\n")
	djangoViews.write("from modules.fetchDBDict import fetch\n")
	djangoViews.write("\n")	
	djangoViews.write("db = fetch('" + dbName + "')\n")
	djangoViews.write("\n")
	for t in tables:
		if t in djangoConversions.djangoTables:
			continue
		djangoViews.write("def " + t + "(request):\n")	
		djangoViews.write("\tcontext = {\n")
		djangoViews.write("\t\t'data' : db,\n")
		djangoViews.write("\t\t'field' : '" + t + "'\n")
		djangoViews.write("\t}\n")
		djangoViews.write("\treturn render(request, '" + appName + "/default.html', context)\n") 
		djangoViews.write("\n")

#Once views are written, it is necessary to re-write the project urls.py file 
# to reference your app urls
with open("./project_urls.py","w") as projectURLs:
	projectURLs.write("from django.contrib import admin\n")
	projectURLs.write("from django.urls import path, include\n")
	projectURLs.write("urlpatterns = [\n")
	projectURLs.write("\tpath('admin/', admin.site.urls),\n")
	projectURLs.write("\tpath('" + appName + "/', include('" + appName + ".urls'))\n")
	projectURLs.write("]\n")

#Now write urls.py for your app
with open("./app_urls.py","w") as appURLs:
	appURLs.write("from django.urls import path\n")
	appURLs.write("from . import views\n")
	appURLs.write("\n")
	appURLs.write("urlpatterns = [\n")
	for t in tables:
		if t in djangoConversions.djangoTables:
			continue
		appURLs.write("\tpath('" + t + "', views." + t + ", name='" + appName + "-" + t + "'),\n")
	appURLs.write("]\n")	

#With the relevant url and view files written,
#copy the url files and view file to the django project for use. 
projectUrlDest = "./" + projectName + "/" + projectName + "/urls.py"
copyfile("./project_urls.py",projectUrlDest)
appUrlDest = "./" + projectName + "/" + appName + "/urls.py"
copyfile("./app_urls.py",appUrlDest)
