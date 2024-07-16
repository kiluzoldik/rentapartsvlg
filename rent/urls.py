from django.urls import path

from rent import views

app_name = 'rent'

urlpatterns = [
    path('', views.rent, name='rent'),
]