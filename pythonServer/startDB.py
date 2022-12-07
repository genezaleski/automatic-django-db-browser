#!/usr/bin/python

import subprocess

checkCommand = 'ps -aux | grep -i "http.server"'

serverRunning = subprocess.getoutput(checkCommand)

if "python" in serverRunning:
    print("Requirement already satisfied: mySQL server is running!")
else:
    startServer = ['python','-m','http.server','8081','--bind','127.0.0.1']
    subprocess.Popen(startServer)
