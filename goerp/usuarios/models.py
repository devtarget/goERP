from django.db import models

# Create your models here.
class Usuarios(models.Model):   
	login = models.CharField(max_length=100)    
	nome = models.CharField(max_length=100)    
	senha = models.CharField(max_length=20, null=True, blank=True)
    
	def __str__(self):
		return self.nome

	def salvar(self):
		self.save() 