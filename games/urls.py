from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.index, name="index"),
    path("registration", views.register, name="registration"),
    path("login", views.login_u, name="login"),
    path("logout", views.logout_u, name="logout"),
    path("menu", views.menu, name="menu"),
    path('treasure', views.treasure, name='treasure'),
]
