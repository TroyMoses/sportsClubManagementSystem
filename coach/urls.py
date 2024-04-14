from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('lock/', views.lock, name='register'),
    path('dep/', views.dep, name='dep'),
    path('',views.coachDashboard,name='coachDashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('coach_players/', views.coach_players, name="coach_players"),
    path('coach_add_player/', views.coach_add_player, name="coach_add_player"),
    path('coach_administrators/', views.coach_administrators, name="coach_administrators"),
    path('coach_staff/', views.coach_staff, name="coach_staff"),
    path('coach_add_staff/', views.coach_add_staff, name="coach_add_staff"),
    path('coach_teams/', views.coach_teams, name="coach_teams"),
    path('coach_add_team/', views.coach_add_team, name="coach_add_team"),
    path('coach_matches/', views.coach_matches, name="coach_matches"),
    path('coach_add_match/', views.coach_add_match, name="coach_add_match"),
    path('coach_sessions/', views.coach_sessions, name="coach_sessions"),
    path('coach_add_session/', views.coach_add_session, name="coach_add_session"),
    path('coach_player_team/', views.coach_player_team, name="coach_player_team"),
    path('coach_add_player_team/', views.coach_add_player_team, name="coach_add_player_team"),
    path('coach_player_matches/', views.coach_player_matches, name="coach_player_matches"),
    path('coach_player_injuries/', views.coach_player_injuries, name="coach_player_injuries"),
    path('coach_player_feedback_session/', views.coach_player_feedback_session, name="coach_player_feedback_session"),
    path('coach_player_feedback_match/', views.coach_player_feedback_match, name="coach_player_feedback_match"),
    path('coach_staff_feedback_session/', views.coach_staff_feedback_session, name="coach_staff_feedback_session"),
    path('coach_add_staff_feedback_session/', views.coach_add_staff_feedback_session, name="coach_add_staff_feedback_session"),
    path('coach_staff_feedback_match/', views.coach_staff_feedback_match, name="coach_staff_feedback_match"),
    path('coach_add_staff_feedback_match/', views.coach_add_staff_feedback_match, name="coach_add_staff_feedback_match"),
]