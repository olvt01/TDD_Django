from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/new', views.new_list, name='new_list'),
    path('lists/<int:list_id>/', views.view_list, name='view_list'),
    path('lists/<int:list_id>/add_item', views.add_item, name='add_item'),
    #re_path(r'^lists/new$', views.new_list, name='new_list'),
]