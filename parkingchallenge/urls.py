from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_car/', views.add_car, name='add_car'),
    path('upload_car_data/', views.upload_car_data, name='upload_car_data'),
]
