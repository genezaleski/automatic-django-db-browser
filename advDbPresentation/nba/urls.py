from django.urls import path
from . import views

urlpatterns = [
	path('Draft', views.Draft, name='nba-Draft'),
	path('Draft_Combine', views.Draft_Combine, name='nba-Draft_Combine'),
	path('Game', views.Game, name='nba-Game'),
	path('Game_Inactive_Players', views.Game_Inactive_Players, name='nba-Game_Inactive_Players'),
	path('Game_Officials', views.Game_Officials, name='nba-Game_Officials'),
	path('Player', views.Player, name='nba-Player'),
	path('Player_Attributes', views.Player_Attributes, name='nba-Player_Attributes'),
	path('Player_Bios', views.Player_Bios, name='nba-Player_Bios'),
	path('Player_Photos', views.Player_Photos, name='nba-Player_Photos'),
	path('Player_Salary', views.Player_Salary, name='nba-Player_Salary'),
	path('Team', views.Team, name='nba-Team'),
	path('Team_Attributes', views.Team_Attributes, name='nba-Team_Attributes'),
	path('Team_History', views.Team_History, name='nba-Team_History'),
	path('Team_Salary', views.Team_Salary, name='nba-Team_Salary'),
]
