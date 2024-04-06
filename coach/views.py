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


#===========Francis calling the dashbourd==============
def coachDashboard(request):
    return render(request, 'client/coachDashboard.html')

def client(request):
    return render(request, 'client.html')


