
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Complaint
from django.shortcuts import render, redirect

# def home(request):
#     return render(request, 'home.html')

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

        Complaint.objects.create(
            user=request.user,
            department=profile.department,
            name=name,
            cnic=cnic,
            category=category,
            description=description,
            evidence=evidence
        )

        return redirect('user_dashboard_view')

    return render(request, 'complaint/complain_form.html')

# track complaint
def track_complaint_view(request):
    # search complaint
    complaint = None
    
    if request.method == "POST":
        
        cnic=request.POST.get('cnic')
        complaint = Complaint.objects.filter(cnic=cnic).first()

    return render(request, 'complaint/track_complaint.html', {'complaint': complaint})
