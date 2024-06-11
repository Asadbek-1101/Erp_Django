from django.urls import path
from .views import TeacherDashboardView, TeacherTeamsView

app_name = 'teachers'

urlpatterns = [
    path('dashboard/', TeacherDashboardView.as_view(), name='dashboard'),
    path('guruhlarim', TeacherTeamsView.as_view(), name='guruhlarim'),
]


