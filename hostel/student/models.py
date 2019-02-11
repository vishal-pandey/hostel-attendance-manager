from django.db import models

class Student(models.Model):
	hostel_id = models.ForeignKey('myhostel.MyHostel', on_delete=models.CASCADE,)
	roll_no = models.CharField(max_length=15)
	name = models.CharField(max_length=200)
	phone_no = models.CharField(max_length=15)
	room_no = models.CharField(max_length=10)


	def __str__(self):
	    return  self.roll_no

# Create your models here.
