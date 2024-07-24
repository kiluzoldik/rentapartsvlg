from django.urls import path

from places import views

app_name = 'places'

urlpatterns = [
    path('', views.categories, name='places'),
]