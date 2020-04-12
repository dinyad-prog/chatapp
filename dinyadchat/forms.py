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
        cleaned_data=super(loginF,self).clean()
        pseudo=cleaned_data.get("pseudo")
        pwd=cleaned_data.get("pwd")
        if pseudo and pwd:
            result=personne.objects.filter(pseudo=pseudo,pwd=pwd)
            if len(result)!=1:
                raise forms.ValidationError("Pseudo ou mot de passe incorrect.")

        return cleaned_data