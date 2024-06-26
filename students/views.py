from django.shortcuts import render, get_object_or_404, redirect
from users.permissions import StudentRequiredMixin
from django.views import View
from users.models import Student, Team
from .forms import HomeworkFrom
from .models import Lesson, Homework

class StudentDashboardView(StudentRequiredMixin, View):
    def get(self, request):
        return render(request, 'students/dashboard.html')

class StudentGroupView(StudentRequiredMixin, View):
    def get(self,request):
        student = Student.objects.get(user=request.user)
        return render(request, 'students/guruhlarim.html', {'student': student})


class StudentLessonView(StudentRequiredMixin, View):
    def get(self, request, group_id):
        team = get_object_or_404(Team, id=group_id)
        lessons = team.lessons.all()
        return render(request, 'students/guruh.html', {'lessons': lessons})


class HomeworkView(StudentRequiredMixin, View):
    def get(self, request, lesson_id):
        form = HomeworkFrom()
        return render(request, 'students/homework.html', {'form':form})

    def post(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, id=lesson_id)
        student = get_object_or_404(Student, user=request.user)

        form = HomeworkFrom(request.POST, request.FILES)
        if form.is_valid():
            homework = Homework()
            homework.student = student
            homework.lesson = lesson
            homework.description = form.cleaned_data['description']
            homework.homework_file = form.cleaned_data['homework_file']
            homework.save()

            lesson.homework_status = True
            lesson.save()

            return redirect('students/dashboard')



class HomeworkDetailView(StudentRequiredMixin, View):
    def get(self, request, lesson_id):
        student = get_object_or_404(Student, user=request.user)
        lesson = get_object_or_404(Lesson, id=lesson_id)
        homework = Homework.objects.filter(lesson=lesson, student=student).first()
        return render(request, 'students/homework_detail.html', {'homework': homework})









