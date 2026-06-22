from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.models import User

from . models import registration_details

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

# accounts login role

from accounts.models import UserProfile

from Dashboard.models import Complaint

from django.contrib.auth import logout
# function start
# Home 
@login_required
def home_page_view(request):
     return render(request, 'user/home_page.html')

# Home
def admin_dashboard_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    complaints = Complaint.objects.filter(
    department=profile.department
)
    pending_count = complaints.filter(status="Pending").count()
    resolved_count = complaints.filter(status="Resolved").count()
    return render(request, 'admin/home_page.html',{
        'complaints': complaints
     })
# Home
def update_complaint(request, id):
    from django.contrib import messages
    from Dashboard.models import Notification
    complaint = Complaint.objects.get(id=id)

    if request.method == "POST":
        complaint.status = request.POST['status']
        complaint.save()

        # Create Notification for the user
        Notification.objects.create(
            user=complaint.user,
            message=f"Your complaint #{complaint.id} status has been updated to {complaint.status}."
        )

        messages.success(request, f"Complaint #{complaint.id} status updated to {complaint.status}!")
        return redirect('admin_dashboard_view')

    return render(request, 'admin/home_page.html', {'complaint': complaint})

# Dashboard
def dashboardApp(request):
    return render(request, 'user/dashboard.html')

# Home
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

# Home
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard_view')

            profile, created = UserProfile.objects.get_or_create(user=user)

            if profile.role == 'admin':
                return redirect('admin_dashboard_view')
            else:
                return redirect('dashboardApp')
            
        else:
            return render(request, 'auth/login.html' , {
                'error': 'Invalid username or password'
            })

    return render(request, 'auth/login.html')

# logout
def logout_view(request):
    logout(request)
    return redirect('login_view')
