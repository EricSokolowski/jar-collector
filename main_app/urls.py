from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('about/', views.about, name='about'),

  path('jars/', views.jars_index, name='jars_index'),

  path('jars/<int:jar_id>/', views.jars_detail, name='jars_detail')
]