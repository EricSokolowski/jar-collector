from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Jar, Sticker
from .forms import CleaningForm


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
  stickers_jar_doesnt_have = Sticker.objects.exclude(id__in = jar.stickers.all().values_list('id'))
  cleaning_form = CleaningForm()
  return render(request, 'jars/detail.html', {
    'jar': jar, 'cleaning_form': cleaning_form, 'stickers': stickers_jar_doesnt_have
  })

def add_cleaning(request, jar_id):
  form = CleaningForm(request.POST)
  if form.is_valid():
    new_cleaning = form.save(commit=False)
    new_cleaning.jar_id = jar_id
    new_cleaning.save()
  return redirect('jars_detail', jar_id = jar_id)

def assoc_sticker(request, jar_id, sticker_id):
  Jar.objects.get(id=jar_id).stickers.add(sticker_id)
  return redirect('jars_detail', jar_id=jar_id)

class JarCreate(CreateView):
  model = Jar
  fields = ['name', 'contents', 'description', 'quantity']
  success_url = '/jars/'

class JarUpdate(UpdateView):
  model = Jar
  fields = ['contents', 'description', 'quantity']

class JarDelete(DeleteView):
  model = Jar
  success_url = '/jars/'

class StickerCreate(CreateView):
  model = Sticker
  fields = '__all__'

class StickerList(ListView):
  model = Sticker

class StickerDetail(DetailView):
  model = Sticker

class StickerUpdate(UpdateView):
  model = Sticker
  fields = ['name', 'color']

class StickerDelete(DeleteView):
  model = Sticker
  success_url = '/stickers/'