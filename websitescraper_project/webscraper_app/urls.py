from django.contrib import admin
from django.urls import path, include

from webscraper_app import views

urlpatterns = [

    path('',views.home,name='home'),
    path('clear-table/', views.clear_table, name='clear_table'),
    # path('delete/',views.delete,name='delete')
]