from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('oldindex/', views.oldindex, name='oldindex'),
    path('listodo/', views.todohome, name='todohome'),
]
