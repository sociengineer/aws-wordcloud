from django.contrib import admin

# Register your models here.
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
	list_display = ['categories', 'city', 'country','name','date','rating','tokens']
	list_per_page = 20
admin.site.register(Review, ReviewAdmin)