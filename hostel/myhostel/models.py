from django.db import models

# Create your models here.
class MyHostel(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = True

    def __str__(self):
	    return self.name

    def __unicode__(self):
        return self.name