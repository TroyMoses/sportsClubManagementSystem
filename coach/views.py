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

def coach_players(request):
    coach_players = Player.objects.all()
    return render(request, "coach_players.html", {'coach_players': coach_players})

def coach_add_player(request):
    form = PlayerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach_players'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach_add_player.html", {'form': form})

def coach_administrators(request):
    coach_administrators = Administrator.objects.all()
    return render(request, "coach_administrators.html", {'coach_administrators': coach_administrators})

def coach_staff(request):
    coach_staff = Staff.objects.all()
    return render(request, "coach_staff.html", {'coach_staff': coach_staff})

def coach_add_staff(request):
    form = StaffForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach_staff'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach_add_staff.html", {'form': form})

def coach_teams(request):
    coach_teams = Team.objects.all()
    return render(request, "coach_teams.html", {'coach_teams': coach_teams})

def coach_add_team(request):
    form = TeamForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach_teams'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach_add_team.html", {'form': form})

def coach_matches(request):
    coach_matches = Match.objects.all()
    return render(request, "coach_matches.html", {'coach_matches': coach_matches})

def coach_add_match(request):
    form = MatchForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach_matches'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach_add_match.html", {'form': form})

def coach_sessions(request):
    coach_sessions = TrainingSession.objects.all()
    return render(request, "coach_sessions.html", {'coach_sessions': coach_sessions})

def coach_add_session(request):
    form = TrainingSessionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach_sessions'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach_add_session.html", {'form': form})

def coach_player_team(request):
    coach_player_team = PlayerTeam.objects.all()
    return render(request, "coach_player_team.html", {'coach_player_team': coach_player_team})

def coach_add_player_team(request):
    form = PlayerTeamForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach_player_team'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach_add_player_team.html", {'form': form})

def coach_player_matches(request):
    coach_player_matches = PlayerGame.objects.all()
    return render(request, "coach_player_matches.html", {'coach_player_matches': coach_player_matches})

def coach_add_player_match(request):
    form = PlayerGameForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach_player_matches'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach_add_player_match.html", {'form': form})

def coach_player_injuries(request):
    coach_player_injuries = Injury.objects.all()
    return render(request, "coach_player_injuries.html", {'coach_player_injuries': coach_player_injuries})

def coach_player_feedback_session(request):
    coach_player_feedback_session = PlayerFeedback1.objects.all()
    return render(request, "coach_player_feedback_session.html", {'coach_player_feedback_session': coach_player_feedback_session})

def coach_player_feedback_match(request):
    coach_player_feedback_match = PlayerFeedback2.objects.all()
    return render(request, "coach_player_feedback_match.html", {'coach_player_feedback_match': coach_player_feedback_match})

def coach_staff_feedback_session(request):
    coach_staff_feedback_session = StaffFeedback1.objects.all()
    return render(request, "coach_staff_feedback_session.html", {'coach_staff_feedback_session': coach_staff_feedback_session})

def coach_staff_feedback_match(request):
    coach_staff_feedback_match = StaffFeedback2.objects.all()
    return render(request, "coach_staff_feedback_match.html", {'coach_staff_feedback_match': coach_staff_feedback_match})

def coach_add_staff_feedback_session(request):
    form = StaffFeedbackForm1(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach_staff_feedback_session'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach_add_staff_feedback_session.html", {'form': form})

def coach_add_staff_feedback_match(request):
    form = StaffFeedbackForm2(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('coach_staff_feedback_match'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "coach_add_staff_feedback_match.html", {'form': form})

