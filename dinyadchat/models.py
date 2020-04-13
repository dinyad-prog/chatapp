from django.db import models
from django.conf import settings
from django.utils import timezone


class personne(models.Model):
	nom=models.CharField(max_length=30)
	prenom=models.CharField(max_length=30)
	pseudo=models.CharField(max_length=30)
	pwd=models.CharField(max_length=30)
	amis=models.ManyToManyField('self',blank=True)

	def __unicode__(self):
		return self.prenom+" "+self.nom
		
class recepteur(models.Model):
	recpt=models.ForeignKey(personne,on_delete=models.CASCADE)

	


class message(models.Model):
	contenu=models.TextField()
	date=models.DateTimeField(default=timezone.now)
	auteur=models.ForeignKey(personne,on_delete=models.CASCADE)
	recpt=models.ForeignKey(recepteur,on_delete=models.CASCADE)

	def __unicode__(self):
		if len(self.contenu) > 20:
			return self.contenu[:19]+"..."
		else:
			return self.contenu

# Create your models here.
