from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('about/', views.about, name='about'),

  path('jars/', views.jars_index, name='jars_index'),

  path('jars/<int:jar_id>/', views.jars_detail, name='jars_detail'),

  path('jars/create/', views.JarCreate.as_view(), name='jars_create'),

  path('jars/<int:pk>/update/', views.JarUpdate.as_view(), name='jars_update'),

  path('jars/<int:pk>/delete/', views.JarDelete.as_view(), name='jars_delete'),
]