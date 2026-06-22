from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    
    path('user/dashboard', views.user_dashboard_view, name='user_dashboard_view'),
    path('complain/complain_form', views.user_complain_view, name='user_complain_view'),
    path('complaint/track_complaint', views.track_complaint_view, name='track_complaint_view'),
    path('logout/', views.logout_view, name='logout'),
    path('complaint/track_history', views.track_history_view, name='track_history_view'),
    
    path('management/', views.profile_manage_view, name='profile_manage_view'),
    path('mark_notifications_read/', views.mark_notifications_read, name='mark_notifications_read'),
]