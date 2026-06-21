from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('dashboard', views.user_dashboard_view, name='user_dashbaord_view'),
]