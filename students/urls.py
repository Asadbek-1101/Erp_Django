from django.urls import path
from .views import StudentDashboardView, StudentGroupView, StudentLessonView, HomeworkView


app_name = 'students'

urlpatterns = [
    path('dashboard/', StudentDashboardView.as_view(), name='dashboard'),
    path('guruhlarim/', StudentGroupView.as_view(), name='guruhlarim'),
    path('lesson/<int:group_id>/', StudentLessonView.as_view(), name='lesson'),
    path('homework/<int:lesson_id>/', HomeworkView.as_view(), name='homework'),
]