from django.db import models

class Attendance(models.Model):
	hostel_id = models.ForeignKey('myhostel.MyHostel', on_delete=models.CASCADE,)
	student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE,)
	date = models.DateTimeField('date published')
	MY_STATUS = (('A', 'Absent'),('P', 'Present'),('L', 'Leave'),)
	status = models.CharField(max_length=1, choices=MY_STATUS)

# Create your models here.
