from django.urls import path
from . import views

urlpatterns = [
    # path('', views.account_login, name="account_login"),
    # path('register/', views.account_register, name="account_register"),
    # path('logout/', views.account_logout, name="account_logout"),
    path('dep/', views.create_department, name="create_department"),
    path('lock/', views.lock, name='register'),
    path('/adminDashboard', views.dashboard, name="adminDashboard"),
    path('', views.login, name="adminlogin"),
    path('reqst/', views.reqStatus, name="reqst"),
    path('repst/', views.reportStatus, name="repst"),
    path('players/', views.players, name="players"),
    path('player_attendance_session/', views.player_attendance_session, name="player_attendance_session"),
    path('add_player/', views.add_player, name="add_player"),
    path('administrators/', views.administrators, name="administrators"),
    path('add_administrator/', views.add_administrator, name="add_administrator"),
    path('staff/', views.staff, name="staff"),
    path('add_staff/', views.add_staff, name="add_staff"),
    path('teams/', views.teams, name="teams"),
    path('add_team/', views.add_team, name="add_team"),
    path('matches/', views.matches, name="matches"),
    path('add_match/', views.add_match, name="add_match"),
    path('sessions/', views.sessions, name="sessions"),
    path('add_session/', views.add_session, name="add_session"),
    path('player_team/', views.player_team, name="player_team"),
    path('add_player_team/', views.add_player_team, name="add_player_team"),
    path('player_matches/', views.player_matches, name="player_matches"),
    path('player_injuries/', views.player_injuries, name="player_injuries"),
    path('player_feedback_session/', views.player_feedback_session, name="player_feedback_session"),
    path('player_feedback_match/', views.player_feedback_match, name="player_feedback_match"),
    path('staff_feedback_session/', views.staff_feedback_session, name="staff_feedback_session"),
    path('staff_feedback_match/', views.staff_feedback_match, name="staff_feedback_match"),
]