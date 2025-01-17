from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('identification', views.identification, name='identification'),
    path('logout', views.logout, name='logout'),
]