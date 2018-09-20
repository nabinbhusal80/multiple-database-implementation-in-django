from django.db import models

# Create your models here.

class ModelApp2(models.Model):
	Name = models.CharField(max_length=25,blank=False)
	Roll = models.IntegerField(blank=False)

	class Meta:
		app_label = 'app2'

	def __str__(self):
		return self.Name