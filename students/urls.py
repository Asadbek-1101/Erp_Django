from django.urls import path
from .views import StudentDashboardView, StudentGroupView, StudentHomeworkView

app_name = 'students'

urlpatterns = [
    path('dashboard/', StudentDashboardView.as_view(), name='dashboard'),
    path('guruhlarim/', StudentGroupView.as_view(), name='guruhlarim'),
    path('homework/', StudentHomeworkView.as_view(), name='homework'),
]