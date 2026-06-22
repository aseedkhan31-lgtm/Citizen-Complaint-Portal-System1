# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from .models import Complaint

# def home(request):
#     return render(request, 'home.html')

@login_required
def user_dashboard_view(request):
    return render(request, 'user/dashboard.html')

@login_required
def user_complain_view(request):

    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        name = request.POST.get('name')
        cnic = request.POST.get('cnic')
        category = request.POST.get('category')
        description = request.POST.get('description')
        evidence = request.FILES.get('evidence')

        # Create complaint. Department can be assigned later by admins or automatically
        Complaint.objects.create(
            user=request.user,
            name=name,
            cnic=cnic,
            category=category,
            description=description,
            evidence=evidence
        )

        return redirect('user_dashboard_view')

    return render(request, 'complaint/complain_form.html')

# track complaint
@login_required
def track_complaint_view(request):
    # search complaint
    complaint = None
    
    if request.method == "POST":
        cnic = request.POST.get('cnic')
        # Only allow user to track their own complaints by cnic, or allow general search
        complaint = Complaint.objects.filter(cnic=cnic, user=request.user).first()

    return render(request, 'complaint/track_complaint.html', {'complaint': complaint})

@login_required
def track_history_view(request):
    # Fetch all complaints for the logged in user
    complaints = Complaint.objects.filter(user=request.user).order_by('-id')
    return render(request, 'complaint/track_history.html', {'complaints': complaints})

@login_required
def profile_manage_view(request):
    from accounts.models import UserProfile
    from Home.models import registration_details
    from django.contrib.auth import update_session_auth_hash
    from django.contrib import messages
    
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    try:
        reg_details = registration_details.objects.get(user=request.user)
    except registration_details.DoesNotExist:
        reg_details = None

    if request.method == "POST":
        if 'update_picture' in request.POST:
            if 'profile_picture' in request.FILES:
                user_profile.profile_picture = request.FILES['profile_picture']
                user_profile.save()
                messages.success(request, "Profile picture updated successfully!")
        elif 'update_details' in request.POST:
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            cnic = request.POST.get('cnic')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            # Update User
            request.user.email = email
            if new_password and new_password == confirm_password:
                request.user.set_password(new_password)
            request.user.save()

            # Update Registration Details
            if reg_details:
                reg_details.full_name = full_name
                reg_details.cnic = cnic
                reg_details.save()
            else:
                registration_details.objects.create(user=request.user, full_name=full_name, cnic=cnic)

            # Keep user logged in if password changes
            if new_password and new_password == confirm_password:
                update_session_auth_hash(request, request.user)
                
            messages.success(request, "Account details updated successfully!")

        return redirect('profile_manage_view')

    return render(request, 'management/profile.html', {
        'profile': user_profile,
        'reg_details': reg_details
    })

# logout
def logout_view(request):
    logout(request)
    return redirect('login_view')
