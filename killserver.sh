#!/usr/bin/sh

kill -9 $(ps -aux | grep runserver | awk '{print $2}')
