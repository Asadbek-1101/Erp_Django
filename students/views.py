from django.shortcuts import render
from users.permissions import StudentRequiredMixin
from django.views import View
from users.models import Student, StudentHomework

class StudentDashboardView(StudentRequiredMixin, View):
    def get(self, request):
        return render(request, 'students/dashboard.html')

class StudentGroupView(StudentRequiredMixin, View):
    def get(self,request):
        student = Student.objects.get(user=request.user)
        return render(request, 'students/guruhlarim.html', {'student': student})


class StudentHomeworkView(StudentRequiredMixin, View):
    def get(self,request):
        homeworks = StudentHomework.objects.all()
        return render(request, 'students/homework.html', {'homeworks': homeworks})



