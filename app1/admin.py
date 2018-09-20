from django.contrib import admin

# Register your models here.
from .models import ModelApp1

class ModelApp1Admin(admin.ModelAdmin):
	list_display = ["Father", "num"]
	class Meta:
		model = ModelApp1

admin.site.register(ModelApp1, ModelApp1Admin)