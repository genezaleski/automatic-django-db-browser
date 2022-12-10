from django.urls import path
from . import views

urlpatterns = [
    path('table0', views.table0, name='nba-table0'),
    path('table1', views.table1, name='nba-table1'),
    path('table2', views.table2, name='nba-table2'),
    path('table3', views.table3, name='nba-table3'),
    path('table4', views.table4, name='nba-table4')
]
