from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task


class MyLoginView(LoginView):
  template_name = 'main_app/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self):
    return '/'

class SignUpPage(FormView):
  template_name = 'main_app/sign_up.html'
  form_class = UserCreationForm
  redirect_authenticated_user = True
  success_url = '/'

  def form_valid(self, form):
    user = form.save()
    if user is not None:
      login(self.request, user)
    return super(SignUpPage, self).form_valid(form)


class DueList(LoginRequiredMixin, ListView):
  model = Task
  context_object_name = 'tasks'


class DueDetail(LoginRequiredMixin, DetailView):
  model = Task
  context_object_name = 'task'
  template_name = 'main_app/task.html'

class DueCreate(LoginRequiredMixin, CreateView):
  model = Task
  fields = '__all__'
  success_url = '/'

class DueUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  fields = '__all__'
  success_url = '/'

class DueDelete(LoginRequiredMixin, DeleteView):
  model = Task
  context_object_name = 'task'
  success_url = '/'
