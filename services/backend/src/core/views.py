from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Test, Question, Result
from django.conf import settings

def home_view(request):
    return render(request, 'home.html')

@login_required
def test_view(request):
    if request.method == 'POST':
        score = calculate_score(request.POST)
        Result.objects.create(
            user=request.user,
            test=Test.objects.first(),
            score=score
        )
        return redirect('dashboard')
    question = Question.objects.first()
    return render(request, 'testing.html', {'question': question})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard_view(request):
    tests = Test.objects.filter(created_by=request.user) if request.user.is_teacher else Test.objects.all()
    return render(request, 'dashboard.html', {
        'dash_url': settings.DASH_URL + f"?user_id={request.user.id}",
        'tests': tests
    })

def calculate_score(post_data):
    return 85.0
