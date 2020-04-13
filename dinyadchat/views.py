#-*- encoding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpResponseRedirect
from dinyadchat.forms import *
import os



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

			return HttpResponseRedirect ('/connexion')

		else :
			 
			return render_to_response ('dinyadchat/register.html',{'form' : form})
	else :
		form = profileF()
		return render_to_response ('dinyadchat/register.html', {'form' : form})

def connexion(request):
	if request.method=="POST":
		form=loginF(request.POST)
		if form.is_valid():
			pseudo = form.cleaned_data['pseudo'] 
			logged_user = personne.objects.get(pseudo=pseudo) 
			request.session['logged_user_id'] = logged_user.id
			return HttpResponseRedirect('/home')
		else:
			
			return render_to_response('dinyadchat/connexion.html',{"form":form})
	else:
		form=loginF()
		return render_to_response('dinyadchat/connexion.html',{"form":form})

def home(request):
	if 'logged_user_id' in request.session:
		logged_user_id=request.session['logged_user_id']
		logged_user=personne.objects.get(id=logged_user_id)
		personnes=personne.objects.all()
		messages=logged_user.message_set.all()

		if 'ajouter' in request.GET:
			logged_user_id=request.session['logged_user_id']
			logged_user=personne.objects.get(id=logged_user_id)
			ajouter=request.GET['ajouter']
			ami=personne.objects.get(id=ajouter)
			logged_user.amis.add(ami)
			logged_user.save()

			return render_to_response('dinyadchat/home.html',{"logged_user":logged_user,"personnes":personnes,"messages":messages})
		else:
			return render_to_response('dinyadchat/home.html',{"logged_user":logged_user,"personnes":personnes,"messages":messages})


	else:
		return HttpResponseRedirect('/connexion')




# Create your views here.
