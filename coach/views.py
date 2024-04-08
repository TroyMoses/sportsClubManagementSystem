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

def players(request):
    players = Player.objects.all()
    return render(request, "coach/players.html", {'players': players})

def add_player(request):
    form = PlayerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach/players'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach/add_player.html", {'form': form})

def administrators(request):
    administrators = Administrator.objects.all()
    return render(request, "coach/administrators.html", {'administrators': administrators})

def staff(request):
    staff = Staff.objects.all()
    return render(request, "coach/staff.html", {'staff': staff})

def teams(request):
    teams = Team.objects.all()
    return render(request, "coach/teams.html", {'teams': teams})

def add_team(request):
    form = TeamForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach/teams'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach/add_team.html", {'form': form})

def matches(request):
    matches = Match.objects.all()
    return render(request, "coach/matches.html", {'matches': matches})

def add_match(request):
    form = MatchForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach/matches'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach/add_match.html", {'form': form})

def sessions(request):
    sessions = TrainingSession.objects.all()
    return render(request, "coach/sessions.html", {'sessions': sessions})

def add_session(request):
    form = TrainingSessionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach/sessions'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach/add_session.html", {'form': form})

def player_team(request):
    player_team = PlayerTeam.objects.all()
    return render(request, "coach/player_team.html", {'player_team': player_team})

def add_player_team(request):
    form = PlayerTeamForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach/player_team'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach/add_player_team.html", {'form': form})

def player_matches(request):
    player_matches = PlayerGame.objects.all()
    return render(request, "coach/player_matches.html", {'player_matches': player_matches})

def player_injuries(request):
    player_injuries = Injury.objects.all()
    return render(request, "coach/player_injuries.html", {'player_injuries': player_injuries})

def player_feedback_session(request):
    player_feedback_session = PlayerFeedback1.objects.all()
    return render(request, "coach/player_feedback_session.html", {'player_feedback_session': player_feedback_session})

def player_feedback_match(request):
    player_feedback_match = PlayerFeedback2.objects.all()
    return render(request, "coach/player_feedback_match.html", {'player_feedback_match': player_feedback_match})

def staff_feedback_session(request):
    staff_feedback_session = StaffFeedback1.objects.all()
    return render(request, "coach/staff_feedback_session.html", {'staff_feedback_session': staff_feedback_session})

def staff_feedback_match(request):
    staff_feedback_match = StaffFeedback2.objects.all()
    return render(request, "coach/staff_feedback_match.html", {'staff_feedback_match': staff_feedback_match})

