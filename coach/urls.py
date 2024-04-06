from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('lock/', views.lock, name='register'),
    path('dep/', views.dep, name='dep'),
    path('',views.coachDashboard,name='coachDashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('players/', views.players, name="players"),
    path('administrators/', views.administrators, name="administrators"),
    path('staff/', views.staff, name="staff"),
    path('teams/', views.teams, name="teams"),
    path('add_team/', views.add_team, name="add_team"),
    path('matches/', views.matches, name="matches"),
    path('add_match/', views.add_match, name="add_match"),
    path('sessions/', views.sessions, name="sessions"),
    path('add_session/', views.add_session, name="add_session"),
    path('player_team/', views.player_team, name="player_team"),
    path('player_matches/', views.player_matches, name="player_matches"),
    path('player_injuries/', views.player_injuries, name="player_injuries"),
    path('player_feedback_session/', views.player_feedback_session, name="player_feedback_session"),
    path('player_feedback_match/', views.player_feedback_match, name="player_feedback_match"),
    path('staff_feedback_session/', views.staff_feedback_session, name="staff_feedback_session"),
    path('staff_feedback_match/', views.staff_feedback_match, name="staff_feedback_match"),
]