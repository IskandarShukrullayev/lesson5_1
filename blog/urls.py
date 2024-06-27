from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('lazy/', home, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),

]