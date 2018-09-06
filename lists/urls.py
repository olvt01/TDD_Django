from django.urls import path, re_path

from lists import views

urlpatterns = [
    path('new', views.new_list, name='new_list'),
    path('<int:list_id>/', views.view_list, name='view_list'),
    path('users/<str:email>/', views.my_lists, name='my_lists'),
    #re_path(r'^lists/new$', views.new_list, name='new_list'),
]