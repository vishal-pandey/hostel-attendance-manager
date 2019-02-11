from django.contrib import admin
from .models import MyHostel

class MyHostelAdmin(admin.ModelAdmin):
	model = MyHostel
	list_display = ['id', 'name']
	# list_editable = ['name']
admin.site.register(MyHostel, MyHostelAdmin)
# Register your models here.
