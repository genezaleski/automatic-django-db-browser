#!/usr/bin/python

from sys    import argv
from shutil import copyfile

if len(argv) < 3:
	print("USAGE: makeSettings.py <projectName> <appName>")

projectName = argv[1]
appName     = argv[2]

projectDefaultSettings = "./" + projectName + "/" + projectName + "/settings.py"
appDependentSettings   = "djangoDependencies/project_dependencies/settings.py"

with open(appDependentSettings,"r") as appSettings:
	with open(projectDefaultSettings,"r") as defaultSettings:
		with open("./settings.py","w") as Settings:
			for line in appSettings.readlines():
				if "??projectName??" in line:
					line = line.replace("??projectName??",projectName)
				elif "??appName??" in line:
					line = line.replace("??appName??",appName) 
				elif "??SECRET_KEY??" in line:
					secretKey = ""
					for line2 in defaultSettings:
						if "SECRET_KEY" in line2:
							secretKey = line2.strip().split(" ")[-1].strip()
					line = "SECRET_KEY = " + secretKey + "\n"
				Settings.write(line)

copyfile("./settings.py",projectDefaultSettings) 
