from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Jar


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def jars_index(request):
  jars = Jar.objects.all()
  return render(request, 'jars/index.html', { 'jars': jars})

def jars_detail(request, jar_id):
  jar = Jar.objects.get(id=jar_id)
  return render(request, 'jars/detail.html', { 'jar': jar })

class JarCreate(CreateView):
  model = Jar
  fields = '__all__'
  success_url = '/jars/'

class JarUpdate(UpdateView):
  model = Jar
  fields = ['contents', 'description', 'quantity']

class JarDelete(DeleteView):
  model = Jar
  success_url = '/jars/'