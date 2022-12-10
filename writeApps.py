#!/usr/bin/python

from sys    import argv
from shutil import copyfile

if len(argv) < 3:
	print("USAGE: makeApps.py <projectName> <appName>")

projectName = argv[1]
appName     = argv[2]

with open("./apps.py","w") as djangoApps:
	djangoApps.write("from django.apps import AppConfig")
	djangoApps.write("\n")
	djangoApps.write("class " + appName + "Config(AppConfig):\n")
	djangoApps.write("\tdefault_auto_field = 'django.db.models.BigAutoField'\n")
	djangoApps.write("\tname = '" + appName + "'\n")

copyfile("./apps.py","./" + projectName + "/" + appName + "/apps.py")
