from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.index, name="index"),
    path("registration", views.register, name="registration"),
    path("login", views.login_u, name="login"),
    path("logout", views.logout_u, name="logout"),
    path("menu", views.menu, name="menu"),
    path('treasure', views.treasure, name='treasure'),
    path('memory', views.memory, name='memory'),
    path('weather', views.weather, name='weather'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)