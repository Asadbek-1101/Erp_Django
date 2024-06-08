from django.urls import path
from .views import TeacherDashboardView

app_name = 'teachers'

urlpatterns = [
    path('teacher-dashboard/', TeacherDashboardView.as_view(), name='teacher_dashboard')
]