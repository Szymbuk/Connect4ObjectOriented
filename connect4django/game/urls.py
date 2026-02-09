from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='game-home'),
    path('instruction/', views.instruction, name='game-about'),
    path('play/', views.play, name='game-play'),
    path('leaderboard/', views.leaderboard, name='game-leaderboard'),
]