# Generated by Django 5.0.6 on 2024-06-08 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_homework_lesson'),
        ('users', '0013_alter_studenthomework_vazifa'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('team', 'title')},
        ),
    ]
