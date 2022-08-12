from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task


class DueList(ListView):
  model = Task
  context_object_name = 'tasks'

class DueDetail(DetailView):
  model = Task
  context_object_name = 'task'
  template_name = 'main_app/task.html'

class DueCreate(CreateView):
  model = Task
  fields = '__all__'
  success_url = '/'

class DueUpdate(UpdateView):
  model = Task
  fields = '__all__'
  success_url = '/'

class DueDelete(DeleteView):
  model = Task
  context_object_name = 'task'
  success_url = '/'
