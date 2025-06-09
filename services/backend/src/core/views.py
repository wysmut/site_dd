from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def home(request):
return render(request, 'home.html')

def testing(request):
return render(request, 'testing.html')

def dashboard(request):
if not request.user.is_authenticated:
return redirect('login')
return render(request, 'dashboard.html', {'DASH_URL': '/dash/'})

def login_view(request):
if request.method == 'POST':
form = AuthenticationForm(request, data=request.POST)
if form.is_valid():
username = form.cleaned_data.get('username')
password = form.cleaned_data.get('password')
user = authenticate(username=username, password=password)
if user is not None:
login(request, user)
return redirect('dashboard')
else:
form = AuthenticationForm()
return render(request, 'login.html', {'form': form})
