
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# def home(request):
#     return render(request, 'home.html')
@login_required
def user_dashboard_view(request):
    return render(request, 'user/dashboard.html')