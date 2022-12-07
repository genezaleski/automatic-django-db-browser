#!/usr/bin/python

from subprocess import run
from os.path import isdir

createCmd = ["python","advDbPresentation/manage.py","startapp","nba"]

if isdir(createCmd[-1]):
    print("Local Django App has already been created!")
else:
    run(createCmd)
    print("Created local Django App!")


