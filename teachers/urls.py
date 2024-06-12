from django.urls import path
from .views import TeacherDashboardView, TeacherTeamsView, TeacherLessonView, TeacherStudentsView

app_name = 'teachers'

urlpatterns = [
    path('dashboard/', TeacherDashboardView.as_view(), name='dashboard'),
    path('guruhlarim', TeacherTeamsView.as_view(), name='guruhlarim'),
    path('lessons/<int:group_id>/', TeacherLessonView.as_view(), name='lessons'),
    path('students/', TeacherStudentsView.as_view(), name='students'),
]


