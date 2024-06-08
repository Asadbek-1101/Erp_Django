# Generated by Django 5.0.6 on 2024-06-08 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_lesson_homework_status'),
        ('users', '0013_alter_studenthomework_vazifa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dascritption', models.TextField()),
                ('homework_file', models.FileField(blank=True, null=True, upload_to='homeworks/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lesson', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='homework', to='students.lesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='users.student')),
            ],
            options={
                'unique_together': {('lesson', 'student')},
            },
        ),
    ]
