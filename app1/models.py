
from django.db import models

# Create your models here.

class ModelApp1(models.Model):
	Father = models.CharField(max_length=25,blank=False)
	num = models.IntegerField(blank=False)

	class Meta:
		app_label = 'app1'

	def __str__(self):
		return self.Father