from django.urls import path
from game import views

urlpatterns = [
    path('', views.choose_game_mode, name='choose_game_mode'),
    path('play/', views.play_game, name='play_game'),
]
