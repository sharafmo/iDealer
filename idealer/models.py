from django.db import models
from datetime import datetime
import re


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.first_name +" "+ self.last_name +" - "+ self.email




class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        email_check = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            
        if len(postData['f_n']) < 2:
            errors["f_n"] = "User First name should be at least 2 characters"
        if len(postData['l_n']) < 2:
            errors["l_n"] = "User last name should be at least 2 characters"
        
        if not email_check.match(postData['email']):
            errors['email'] = 'email must be valid format'
        if len(postData['pw']) < 8:
            errors["pw"] = "Password should be at least 8 characters"
        if postData['pw'] != postData['conf_pw']:
            errors['conf_pw'] = 'Password and confirm password must match!'
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()




class AddManager(models.Manager):
    def validator(self, postdata):
        errors={}
        if len(postdata['make']) == 0:
            errors['make'] = 'Make field can not be empty!'
        if len(postdata['model']) == 0:
            errors['model'] = ' Model field can not be empty!'
        if len(postdata['year']) == 0:
            errors['year'] = ' Year field can not be empty!'
        if len(postdata['color']) == 0:
            errors['color'] = ' Color field can not be empty!'
        return errors


class Add(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name="add")
    creator = models.ForeignKey(User, related_name='created_adds', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AddManager()
