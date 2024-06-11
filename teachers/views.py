from django.shortcuts import render, get_object_or_404, redirect
from users.permissions import TeacherRequiredMixin
from django.views import View
from users.models import Teacher


class TeacherDashboardView(TeacherRequiredMixin, View):
    def get(self, request):
        return render(request, 'students/dashboard.html')


class TeacherTeamsView(TeacherRequiredMixin, View):
    def get(self, request):
        teacher = Teacher.objects.get(user=request.user)
        teams = teacher.teams.all()
        return render(request, 'teachers/guruhlarim.html', {'teams': teams})












