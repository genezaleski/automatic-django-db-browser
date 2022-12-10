#!/usr/bin/python

from sys    import argv
from os     import mkdir
from shutil import copyfile

if len(argv) < 2:
	print("USAGE: makeTemplates.py <projectName> <appName>")
	exit()

templateDir    = "./"+projectName+"/"+appName+"/templates"
templateTagDir = "./"+projectName+"/"+appName+"/templatetags"
mkdir(templateDir)
mkdir(templateDir + "/" + appName)
mkdir(templateTagDir)

copyfile("./djangoDependencies/app_dependencies/app_templates/default.html",templateDir + "/templates/.")
copyfile("./djangoDependencies/app_dependencies/app_template_tags/*",templateTagDir + "/.")
