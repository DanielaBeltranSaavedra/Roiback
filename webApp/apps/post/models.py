from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Category (models.Model):
	Category = models.CharField(max_length=150),

class Tag (models.Model):
	Tag = models.CharField(max_length=150)
	
class Post (models.Model):
	Title = models.CharField(max_length=50),
	Author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True), 
	Content = models.CharField(max_length=150),
	CantLikes = models.IntegerField(default=0),
	CantComments = models.IntegerField(default=0),
	Categories = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True),
	Tags= models.ForeignKey(Tag, on_delete=models.SET_NULL,null=True)

class Comment (models.Model):
	Post = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True), 
	Author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True), 
	Comment = models.CharField(max_length=1000)

