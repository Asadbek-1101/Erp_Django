from django.shortcuts import render, get_object_or_404, redirect
from users.permissions import TeacherRequiredMixin
from django.views import View
from users.models import Teacher, Team



class TeacherDashboardView(TeacherRequiredMixin, View):
    def get(self, request):
        return render(request, 'students/dashboard.html')


class TeacherTeamsView(TeacherRequiredMixin, View):
    def get(self, request):
        teacher = Teacher.objects.get(user=request.user)
        teams = teacher.teams.all()
        return render(request, 'teachers/guruhlarim.html', {'teams': teams})



class TeacherGruopView(TeacherRequiredMixin, View):
    def get(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        lessons = team.lessons.all()
        return render(request, 'teachers/guruh.html', {'lessons': lessons})







































