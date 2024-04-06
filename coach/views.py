from django.shortcuts import render, redirect, reverse

# Create your views here.

def login(request):
    return render(request, 'auth/login.html')

def register(request):
    return render(request, 'auth/reg.html')

def lock(request):
    return render(request, 'auth/lock_screen.html')

def dep(request):
    return render(request, 'dep.html')

def req(request):
    return render(request, 'client/req.html')

def coachDashboard(request):
    return render(request, 'coach/coachDashboard.html')

def dashboard(request):
    return render(request, 'dashboard.html')

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

def staff(request):
    staff = Staff.objects.all()
    return render(request, "staff.html", {'staff': staff})

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

