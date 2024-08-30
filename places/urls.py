from django.urls import path

from places import views

app_name = 'places'

urlpatterns = [
    path('/<slug:category_slug>/', views.categories, name='places'),
]