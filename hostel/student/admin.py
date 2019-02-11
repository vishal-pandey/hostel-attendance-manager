from django.contrib import admin
from .models import Student

# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	model = Student
	list_display = ['id', 'hostel_id', 'roll_no', 'name', 'phone_no', 'room_no']

admin.site.register(Student, StudentAdmin)

# Register your models here.
