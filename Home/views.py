from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.models import User

from . models import registration_details

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
# def home(request):
#     return HttpResponse("Welcome to the Citizen Complaint Portal!")
@login_required
def home_page_view(request):
     return render(request, 'user/home_page.html')

def admin_dashboard_view(request):
     return render(request, 'admin/home_page.html')
def dashboardApp(request):
    return render(request, 'user/dashboard.html')

def register_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')  
        cnic = request.POST.get('cnic')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'auth/register.html', {
                'error': 'username already exist'
            })
        # create secure user
        user = User.objects.create_user(
            email=email,
            username=username,
            password=password,
        )

        registration_details.objects.create(
            user=user,
            full_name=full_name,
            cnic=cnic
        )

        return redirect('login_view')
    return render(request, 'auth/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard_view')
            else:
                return redirect('dashboardApp')

            return redirect('home_page_view')
        else:
            return render(request, 'login.html' , {
                'error': 'Invalid username or password'
            })

    return render(request, 'auth/login.html')

