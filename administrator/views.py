from django.shortcuts import render, reverse, redirect
# from client.models import Voter, Position, Candidate, Votes
from .forms import DepartmentForm
# from client.forms import *
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .email_backend import EmailBackend
from django.contrib.auth import login, logout
from .forms import PlayerForm, AdministratorForm, StaffForm, TeamForm, MatchForm, TrainingSessionForm, PlayerTeamForm, PlayerGameForm, InjuryForm, PlayerFeedbackForm1, PlayerFeedbackForm2, StaffFeedbackForm1, StaffFeedbackForm2
from .models import Player, Administrator, Staff, Team, Match, TrainingSession, PlayerTeam, PlayerGame, Injury, PlayerFeedback1, PlayerFeedback2, StaffFeedback1, StaffFeedback2

def account_login(request):
    pass
    # if request.method == 'POST':
    #     user = EmailBackend.authenticate(request, username=request.POST.get(
    #         'email'), password=request.POST.get('password'))
    #     if user != None:
    #         login(request, user)
    #         if user.user_type == '1':
    #             return redirect(reverse("adminDashboard"))
    #         elif user.user_type == '2':
    #             return redirect(reverse("staffDashboard"))
    #         else:
    #             return redirect(reverse("cashierDashboard"))
    #     else:
    #         messages.error(request, "Invalid details")
    #         return redirect("adminDashboard")

    # return render(request, "auth/login.html")


def account_register(request):
    pass
    # userForm = CustomUserForm(request.POST or None)
    # context = {
    #     'form1': userForm,
    # }
    # if request.method == 'POST':
    #     if userForm.is_valid():
    #         user = userForm.save(commit=False)
    #         user.save()
    #         messages.success(request, "Account created. You can login now!")
    #         return redirect(reverse('account_login'))
    #     else:
    #         messages.error(request, "Provided data failed validation")
    #         # return account_login(request)
    # return render(request, "auth/reg.html", context)


def account_logout(request):
    pass
    # user = request.user
    # if user.is_authenticated:
    #     logout(request)
    #     messages.success(request, "Thank you for visiting us!")
    # else:
    #     messages.error(
    #         request, "You need to be logged in to perform this action")

    # return redirect(reverse("account_login"))

def lock(request):
    return render(request, 'auth/lock_screen.html')

def create_department(request):
    form = DepartmentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('account_login')  
    else:
        messages.error(request, "Provided data failed validation")
    return render(request, 'dep.html', {'form': form})

def dashboard(request):
    return render(request, "admin/dashboard.html")

def reqStatus(request):
    return render(request, "admin/reqstatus.html")

def reportStatus(request):
    return render(request, "admin/reportStatus.html")

def players(request):
    players = Player.objects.all()
    return render(request, "players.html", {'players': players})

def add_player(request):
    form = PlayerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('players'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "add_player.html", {'form': form})

def administrators(request):
    administrators = Administrator.objects.all()
    return render(request, "administrators.html", {'administrators': administrators})

def add_administrator(request):
    form = AdministratorForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('administrators'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "add_administrator.html", {'form': form})

def staff(request):
    staff = Staff.objects.all()
    return render(request, "staff.html", {'staff': staff})

def add_staff(request):
    form = StaffForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('staff'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "add_staff.html", {'form': form})

def teams(request):
    teams = Team.objects.all()
    return render(request, "teams.html", {'teams': teams})

def add_team(request):
    form = TeamForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('teams'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "add_team.html", {'form': form})

def matches(request):
    matches = Match.objects.all()
    return render(request, "matches.html", {'matches': matches})

def add_match(request):
    form = MatchForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('matches'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "add_match.html", {'form': form})

def sessions(request):
    sessions = TrainingSession.objects.all()
    return render(request, "sessions.html", {'sessions': sessions})

def add_session(request):
    form = TrainingSessionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('sessions'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "add_session.html", {'form': form})

def player_team(request):
    player_team = PlayerTeam.objects.all()
    return render(request, "player_team.html", {'player_team': player_team})

def add_player_team(request):
    form = PlayerTeamForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('player_team'))
    else:
        messages.error(request, "Provided data failed validation") 
    return render(request, "add_player_team.html", {'form': form})

def player_matches(request):
    player_matches = PlayerGame.objects.all()
    return render(request, "player_matches.html", {'player_matches': player_matches})

def player_injuries(request):
    player_injuries = Injury.objects.all()
    return render(request, "player_injuries.html", {'player_injuries': player_injuries})

def player_feedback_session(request):
    player_feedback_session = PlayerFeedback1.objects.all()
    return render(request, "player_feedback_session.html", {'player_feedback_session': player_feedback_session})

def player_feedback_match(request):
    player_feedback_match = PlayerFeedback2.objects.all()
    return render(request, "player_feedback_match.html", {'player_feedback_match': player_feedback_match})

def staff_feedback_session(request):
    staff_feedback_session = StaffFeedback1.objects.all()
    return render(request, "staff_feedback_session.html", {'staff_feedback_session': staff_feedback_session})

def staff_feedback_match(request):
    staff_feedback_match = StaffFeedback2.objects.all()
    return render(request, "staff_feedback_match.html", {'staff_feedback_match': staff_feedback_match})

