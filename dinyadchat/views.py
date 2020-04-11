from django.shortcuts import render

def welcome(request):
	return render(request,'dinyadchat/welcome.html',{})

# Create your views here.
