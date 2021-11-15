from django.db import models

#เก็บ user profile
from django.contrib.auth.models import User
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	#photo = models.ImageField(upload_to="gallery_photo_profile",null=True,blank=True,default='dafaultprofile.png')
	usertype = models.CharField(max_length=100,default='member') 

	def __str__(self):
		return self.user.first_name
class Allproduct(models.Model):
	name = models.CharField(max_length=100)  #text
	price = models.CharField(max_length=100)
	detail = models.TextField(null=True,blank=True)
	imageurl = models.CharField(max_length=200,null=True,blank=True)
	
	
	def __str__(self):
		return self.name