from django.urls import path
from .views import (LoginView, RegisterView, ProfileView, EditProfileView, LogoutView,
                    GroupsView, team_students)
from . import views

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
    path('groups/', GroupsView.as_view(), name='groups'),
    path('team/<int:pk>/', views.team_students, name='team_students'),
]