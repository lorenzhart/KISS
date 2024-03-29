from django.db import models
from mongoengine import *
from intro.settings import DATABASES

connect(DATABASES["default"]["NAME"])

class Post(models.Model):
    name = models.CharField(max_length=120, null=True)
    roman = models.CharField(max_length=120, null=True)
    project = models.TextField(max_length=120, null=True)
    subproject = models.CharField(max_length=120, null=True)
    subprojectDescription = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=200, null=True)
    background = models.CharField(max_length=200, null=True)
    studentassistant = models.CharField(max_length=200, null=True)
    skill = models.CharField(max_length=200, null=True)
    twitter = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True)
    subproject = models.CharField(max_length=200, null=True)
    subprojectdescription = models.CharField(max_length=200, null=True)
    interest = models.CharField(max_length=200, null=True)
    introduce = models.CharField(max_length=200, null=True)
    img = models.CharField(max_length=200, null=True)
    class Meta:
        db_table = 'persons'

