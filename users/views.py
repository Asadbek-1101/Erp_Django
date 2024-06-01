from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm, ProfileEditForm
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:profile')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            return redirect('/')

        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html')

class EditProfileView(LoginRequiredMixin,View):
    def get(self,request):
        form = ProfileEditForm(instance=request.user)
        return render(request, 'users/edit_profile.html', {'form': form})

    def post(self, request):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')

        form = ProfileEditForm(instance=request.user)
        return render(request, 'users/edit_profile.html', {'form': form})
