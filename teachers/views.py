from django.shortcuts import render, get_object_or_404, redirect
from users.permissions import TeacherRequiredMixin
from django.views import View


class TeacherDashboardView(TeacherRequiredMixin, View):
    def get(self, request):
        return render(request, 'teachers/teacher_dashboard.html')