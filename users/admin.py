from django.contrib import admin
from .models import User, Student, Team, StudentHomework

# Register your models here.
admin.site.register(User)
admin.site.register([Student, Team])
admin.site.register(StudentHomework)