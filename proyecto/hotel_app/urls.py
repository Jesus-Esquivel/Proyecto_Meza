from django.urls import path
from hotel_app import views
urlpatterns = [
    path("",views.hotel,name="inicio_vista"),
]
