from django.shortcuts import render
from django.http import HttpResponse
from modules.fetchDBDict import fetch
from os import listdir

db = fetch("nba")
fields = list(db.keys())

# Create your views here.
def table0(request):
	context = {
		'data': db,
		'field': fields[0] 
	}
	return render(request, "nba/table0.html", context) 

def table1(request):
	context = {
		'data': db,
		'field': fields[1] 
	}
	return render(request, "nba/table0.html", context) 

def table2(request):
	context = {
		'data': db,
		'field': fields[2] 
	}
	return render(request, "nba/table0.html", context) 

def table3(request):
	context = {
		'data': db,
		'field': fields[3] 
	}
	return render(request, "nba/table0.html", context) 

def table4(request):
	context = {
		'data': db,
		'field': fields[4] 
	}
	return render(request, "nba/table0.html", context) 
