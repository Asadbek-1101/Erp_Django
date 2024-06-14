from django.urls import path
from .views import TeacherDashboardView, TeacherTeamsView, TeacherGruopView

app_name = 'teachers'

urlpatterns = [
    path('dashboard/', TeacherDashboardView.as_view(), name='dashboard'),
    path('guruhlarim', TeacherTeamsView.as_view(), name='guruhlarim'),
    path('guruh/<int:team_id>/', TeacherTeamsView.as_view(), name='guruh')

]


