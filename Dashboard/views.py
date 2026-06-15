from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Citizen Complaint Portal!")

def user_dashboard_view(request):
    return render(request, 'user_dashboard.html')
def admin_dashboard_view(request):
    return render(request, 'admin_dashboard.html')
def login_view(request):
    return render(request, 'login.html')
def register_view(request):
    return render(request, 'register.html')