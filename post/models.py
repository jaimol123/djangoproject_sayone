from django.db import models

class Images(models.Model):
	name2=models.CharField(default="0",max_length=20)
	text1=models.CharField(default="0",max_length=20)
	image=models.FileField(null=True,blank=True,upload_to='media')
	status=models.IntegerField(default=0)
	
	class Meta:
		db_table="images"
class Validation(models.Model):
	username1=models.CharField(default="0",max_length=20)
	password1=models.CharField(default="0",max_length=20)
	likedname=models.CharField(default="0",max_length=20)
	
	class Meta:
		db_table="validation"
