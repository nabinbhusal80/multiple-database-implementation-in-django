from django.contrib import admin

# Register your models here.
from .models import ModelApp2

class ModelApp2Admin(admin.ModelAdmin):
	list_display = ["Name", "Roll"]
	class Meta:
		model = ModelApp2

admin.site.register(ModelApp2, ModelApp2Admin)