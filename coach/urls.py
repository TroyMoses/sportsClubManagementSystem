from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('lock/', views.lock, name='register'),
    path('dep/', views.dep, name='dep'),
    path('',views.coachDashboard,name='coachDashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('players/', views.players, name="coach_players"),
    path('add_player/', views.add_player, name="coach_add_players"),
    path('administrators/', views.administrators, name="coach_administrators"),
    path('staff/', views.staff, name="coach_staff"),
    path('teams/', views.teams, name="coach_teams"),
    path('add_team/', views.add_team, name="coach_add_team"),
    path('matches/', views.matches, name="coach_matches"),
    path('add_match/', views.add_match, name="coach_add_match"),
    path('sessions/', views.sessions, name="coach_sessions"),
    path('add_session/', views.add_session, name="coach_add_session"),
    path('player_team/', views.player_team, name="coach_player_team"),
    path('add_player_team/', views.add_player_team, name="coach_add_player_team"),
    path('player_matches/', views.player_matches, name="coach_player_matches"),
    path('player_injuries/', views.player_injuries, name="coach_player_injuries"),
    path('player_feedback_session/', views.player_feedback_session, name="coach_player_feedback_session"),
    path('player_feedback_match/', views.player_feedback_match, name="coach_player_feedback_match"),
    path('staff_feedback_session/', views.staff_feedback_session, name="coach_staff_feedback_session"),
    path('staff_feedback_match/', views.staff_feedback_match, name="coach_staff_feedback_match"),
]