from django.shortcuts import render, redirect, reverse
from administrator.forms import PlayerForm, AdministratorForm, StaffForm, TeamForm, MatchForm, TrainingSessionForm, PlayerTeamForm, PlayerGameForm, InjuryForm, PlayerFeedbackForm1, PlayerFeedbackForm2, StaffFeedbackForm1, StaffFeedbackForm2
from administrator.models import Player, Administrator, Staff, Team, Match, TrainingSession, PlayerTeam, PlayerGame, Injury, PlayerFeedback1, PlayerFeedback2, StaffFeedback1, StaffFeedback2
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request, 'auth/login.html')

def register(request):
    return render(request, 'auth/reg.html')

def lock(request):
    return render(request, 'auth/lock_screen.html')

def dep(request):
    return render(request, 'dep.html')

def coachDashboard(request):
    return render(request, 'coach/coachDashboard.html')

def dashboard(request):
    return render(request, 'dashboard.html')

