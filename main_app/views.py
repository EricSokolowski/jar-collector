from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Jar, Sticker
from .forms import CleaningForm


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def jars_index(request):
  jars = Jar.objects.filter(user=request.user)
  return render(request, 'jars/index.html', { 'jars': jars})

@login_required
def jars_detail(request, jar_id):
  jar = Jar.objects.get(id=jar_id)
  stickers_jar_doesnt_have = Sticker.objects.exclude(id__in = jar.stickers.all().values_list('id'))
  cleaning_form = CleaningForm()
  return render(request, 'jars/detail.html', {
    'jar': jar, 'cleaning_form': cleaning_form, 'stickers': stickers_jar_doesnt_have
  })

@login_required
def add_cleaning(request, jar_id):
  form = CleaningForm(request.POST)
  if form.is_valid():
    new_cleaning = form.save(commit=False)
    new_cleaning.jar_id = jar_id
    new_cleaning.save()
  return redirect('jars_detail', jar_id = jar_id)

@login_required
def assoc_sticker(request, jar_id, sticker_id):
  Jar.objects.get(id=jar_id).stickers.add(sticker_id)
  return redirect('jars_detail', jar_id=jar_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)


class JarCreate(LoginRequiredMixin, CreateView):
  model = Jar
  fields = ['name', 'contents', 'description', 'quantity']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url = '/jars/'

class JarUpdate(LoginRequiredMixin, UpdateView):
  model = Jar
  fields = ['contents', 'description', 'quantity']

class JarDelete(LoginRequiredMixin, DeleteView):
  model = Jar
  success_url = '/jars/'

class StickerCreate(LoginRequiredMixin, CreateView):
  model = Sticker
  fields = '__all__'

class StickerList(LoginRequiredMixin, ListView):
  model = Sticker

class StickerDetail(LoginRequiredMixin, DetailView):
  model = Sticker

class StickerUpdate(LoginRequiredMixin, UpdateView):
  model = Sticker
  fields = ['name', 'color']

class StickerDelete(LoginRequiredMixin, DeleteView):
  model = Sticker
  success_url = '/stickers/'