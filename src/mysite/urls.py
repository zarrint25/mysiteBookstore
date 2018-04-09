from django.conf.urls import url
from .views import home, register,profile

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^register/', register, name='register'),
    url(r'^profile/', profile, name='profile'),
]
