from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
]
