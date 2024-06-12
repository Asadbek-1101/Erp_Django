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



class TeacherLessonView(TeacherRequiredMixin, View):
    def get(self, request, group_id):
        team = get_object_or_404(Team, id=group_id)
        lessons = team.lessons.all()
        return render(request, 'teachers/lessons.html', {'lessons': lessons})

class TeacherStudentsView(TeacherRequiredMixin, View):
    def get(self, request):
        teacher = get_object_or_404(Teacher, user=request.user)
        students = teacher.students.all()
        return render(request, 'teachers/students.html', {'students': students})


















