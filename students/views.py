from django.shortcuts import render
from users.permissions import StudentRequiredMixin
from django.views import View
class StudentDashboardView(StudentRequiredMixin,View):
    def get(self, request, *args):
        return render(request, 'users/student_dashboard.html')
