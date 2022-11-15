from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),

  path('about/', views.about, name='about'),

  path('jars/', views.jars_index, name='jars_index'),

  path('jars/<int:jar_id>/', views.jars_detail, name='jars_detail'),

  path('jars/create/', views.JarCreate.as_view(), name='jars_create'),

  path('jars/<int:pk>/update/', views.JarUpdate.as_view(), name='jars_update'),

  path('jars/<int:pk>/delete/', views.JarDelete.as_view(), name='jars_delete'),

  path('jars/<int:jar_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),

  path('jars/<int:jar_id>/assoc_sticker/<int:sticker_id>/', views.assoc_sticker, name='assoc_sticker'),

  path('stickers/create/', views.StickerCreate.as_view(), name='stickers_create'),

  path('stickers/<int:pk>/', views.StickerDetail.as_view(), name='stickers_detail'),

  path('stickers/', views.StickerList.as_view(), name='stickers_index'),

  path('stickers/<int:pk>/update/', views.StickerUpdate.as_view(), name='stickers_update'),

  path('stickers/<int:pk>/delete/', views.StickerDelete.as_view(), name='stickers_delete'),

  path('accounts/signup/', views.signup, name='signup'),
]