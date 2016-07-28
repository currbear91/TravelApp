from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.contrib  import messages
import re
import bcrypt 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def isValidReg(self, context):
		passflag = True
		errors = []
		password = context['password']
		if not EMAIL_REGEX.match(context['email']):
			passflag = False
		if len(context['first_name']) < 1:
			errors.append("firstname cannot be empty!")
			passflag = False
		if len(context['last_name']) < 1:
			errors.append("lastname cannot be empty!")
			passflag = False
		if len(context['username']) < 1:
			errors.append("username cannot be empty!")
			passflag = False
		if len(context['password']) < 3:
			errors.append("password cannot be less than 8 characters!")
			passflag = False
		if context['password'] != context['confirm']:
			errors.append("passwords do not match!")
			passflag = False
		if len(self.filter(username = context['username'])) > 0:
			errors.append("username already exists")
			passflag = False 
		if len(self.filter(email = context['email'])) >0:
			errors.append('email already exists')
			passflag = False 
  
		if passflag == True:
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			self.create(first_name = context['first_name'], last_name = context['last_name'], username = context['username'], email = context['email'], password = hashed)
		return [passflag, errors]


	def validlog(self, context):
 		errors = [] 
 		passflag = False
 		if len(self.filter(username = context['username'])) < 1:
 			errors.append('invalid login')
		if len(self.filter(username = context['username'])) > 0:
			guy = self.get(username = context['username'])
			hashed = guy.password
			hashed = hashed.encode('utf-8')
			password= context['password']
			password = password.encode('utf-8')
			if bcrypt.hashpw(password, hashed) == hashed:
				passflag = True
		if not passflag:
			return [passflag, errors]
		return [passflag, guy]





class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	username = models.CharField(max_length=200)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	created_at = models.DateField(auto_now_add = True)
	updated_at = models.DateField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()

class Activity(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

class Place(models.Model):
	location = models.CharField(max_length=255)
	image = models.ImageField(null = True, upload_to = "media/TravelApp")
	created_at = models.DateField(auto_now_add = True)
	updated_at = models.DateField(auto_now = True)
	travellers = models.ManyToManyField(User)
	activities = models.ManyToManyField(Activity)



class Season(models.Model):
	name = models.CharField(max_length=50)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	objects = models.Manager()




# for item in ('winter', 'summer', 'fall', 'spring'):
# 	if not Season.objects.filter(name = item):
# 		Season.objects.create(name = item)











