from django.shortcuts import render
from django.http import HttpResponse
from modules.fetchDBDict import fetch

db = fetch("nba","Team")


# Create your views here. 
def home(request):
	context = {
		'data': db,
		'fields': db.keys,
		'title': "NBA HOME"
	}
	return render(request, "nba/home.html", context) 
