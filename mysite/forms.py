from django import forms
from dinyadchat.models import *

class profileF(forms.ModelForm):
    class Meta:
        model=personne
        exclude=('amis',)

class loginF(forms.Form):
    pseudo=forms.CharField(label="Pseudo")
    pwd=forms.CharField(label="Mot de passe",widget=forms.PasswordInput)

    def clean(self):
    	clened_data=super(loginF,self).clean()
    	pseudo=clened_data.get("pseudo")
    	pwd=clened_data.get("pwd")
        if pseudo and pwd:
            result=personne.objects.filter(pseudo=pseudo,pwd=pwd)
            if len(result)!=1:
                raise forms.ValidationError("Pseudo ou mot de passe incorrect.")

        return clened_data