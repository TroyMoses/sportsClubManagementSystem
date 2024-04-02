from django.urls import path
from . import views

urlpatterns = [
    # path('', views.account_login, name="account_login"),
    # path('register/', views.account_register, name="account_register"),
    # path('logout/', views.account_logout, name="account_logout"),
    path('dep/', views.create_department, name="create_department"),
    path('lock/', views.lock, name='register'),
    path('', views.dashboard, name="adminDashboard"),
    path('reqst/', views.reqStatus, name="reqst"),
    path('repst/', views.reportStatus, name="repst"),
    path('players/', views.players, name="players"),
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
]