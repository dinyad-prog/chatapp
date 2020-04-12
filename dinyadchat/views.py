from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpResponseRedirect
from dinyadchat.forms import *

def welcome(request):
	return render(request,'dinyadchat/welcome.html',{})

def register(request):
	if len(request.GET) > 0:
		form = profileF(request.GET)
		
		if form.is_valid() :
			nom=form.cleaned_data['nom']
			prenom=form.cleaned_data['prenom']
			pseudo=form.cleaned_data['pseudo']
			pwd=form.cleaned_data['pwd']
			etud=personne(nom=nom,prenom=prenom,pseudo=pseudo,pwd=pwd)
			etud.save()

			return HttpResponseRedirect ('/welcome')

		else :
			form = profileF()
			return render_to_response ('dinyadchat/register.html',{'form' : form})
	else :
		form = profileF()
		return render_to_response ('dinyadchat/register.html', {'form' : form})

def connexion(request):
	if request.method=="POST":
		form=loginF(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/welcome')
		else:
			form=loginF()
			return render_to_response('dinyadchat/connexion.html',{"form":form})
	else:
		form=loginF()
		return render_to_response('dinyadchat/connexion.html',{"form":form})

# Create your views here.
