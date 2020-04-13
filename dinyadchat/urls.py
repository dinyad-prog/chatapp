from django.conf.urls import url
from django.contrib import admin
from dinyadchat.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^yeto/',welcome),
    url(r'^register/',register),
    url(r'^connexion/',connexion),
    url(r'^home/',home),
    url(r'^messag/',messag),
    
]