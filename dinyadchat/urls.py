from django.conf.urls import url
from django.contrib import admin
from dinyadchat.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/',welcome),
    url(r'^register/',register),
    url(r'^connexion/',connexion),
]