from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login_con_sessio/', views.login_con_sessio, name='login_con_sessio'),
    path('inici/', views.inici, name='inici'),
    path('logout/', views.logout, name='logout')
]
