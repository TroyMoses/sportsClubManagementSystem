from django.shortcuts import render, reverse, redirect
# from client.models import Voter, Position, Candidate, Votes
from .forms import DepartmentForm
# from client.forms import *
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .email_backend import EmailBackend
from django.contrib.auth import login, logout

def account_login(request):
    # if request.user.is_authenticated:
    #     if user.user_type == '1':
    #         return redirect(reverse("adminDashboard"))
    #     elif user.user_type == '2':
    #         return redirect(reverse("staffDashboard"))
    #     else:
    #         return redirect(reverse("cashierDashboard"))

    # context = {}
    if request.method == 'POST':
        user = EmailBackend.authenticate(request, username=request.POST.get(
            'email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            if user.user_type == '1':
                return redirect(reverse("adminDashboard"))
            elif user.user_type == '2':
                return redirect(reverse("staffDashboard"))
            else:
                return redirect(reverse("cashierDashboard"))
        else:
            messages.error(request, "Invalid details")
            return redirect("adminDashboard")

    return render(request, "auth/login.html")


def account_register(request):
    userForm = CustomUserForm(request.POST or None)
    context = {
        'form1': userForm,
    }
    if request.method == 'POST':
        if userForm.is_valid():
            user = userForm.save(commit=False)
            user.department = userForm.cleaned_data['department']
            user.save()
            messages.success(request, "Account created. You can login now!")
            return redirect(reverse('account_login'))
        else:
            messages.error(request, "Provided data failed validation")
            # return account_login(request)
    return render(request, "auth/reg.html", context)


def account_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        messages.success(request, "Thank you for visiting us!")
    else:
        messages.error(
            request, "You need to be logged in to perform this action")

    return redirect(reverse("account_login"))

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
    return render(request, "admin/reqStatus.html")

def reportStatus(request):
    return render(request, "admin/reportStatus.html")