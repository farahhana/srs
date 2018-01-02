from django.db import models

# Create your models here.

class student(models.Model):

	PROGRAMMING = 'PR'
	NETWORKING = 'NT'
	PCTECH = 'PC'
	COURSE_CHOICES = (
		(PROGRAMMING, 'Programming'),
		(NETWORKING, 'Networking'),
		(PCTECH, 'PC Technichian'),

	)

	icnum = models.CharField('IC Number',max_length=12,unique=True,blank=False,null=False)
	name = models.CharField('Name',max_length=300,blank=False,null=False)
	Course = models.CharField('coursework',max_length=2,choices=COURSE_CHOICES,default=PCTECH)
	creatby = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	created_date = models.DateTimeField('Created DateTimeField',auto_now_add=True)

	def __str__(self):
		return self.icnum

