from django.contrib import admin
from .models import Attendance

# @admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
	model = Attendance
	list_display = ['id', 'date', 'hostel_id', 'student_id', 'status']

admin.site.register(Attendance, AttendanceAdmin)

# Register your models here.
