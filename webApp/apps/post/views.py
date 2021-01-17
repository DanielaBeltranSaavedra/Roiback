from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.http import HttpResponse
import os
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.forms import ModelForm

# Create your views here.
@login_required(login_url='/')
def UpPost(request):
		if request.method=='POST':
			postForm = postForm(request.POST)
			postFormCategory= postFormCategory(request.POST)
			postFormTag= postFormTag(request.POST)
			if postForm.is_valid():
				category=postFormCategory.save()
				tag=postFormTag.save()
				post=postForm.save(commit=False)
				post.Author=request.user
				post.Categories=category
				post.Tags=tag
				post.save()
				request HttpResponse("Submited")
			else:
				return HttpResponse("Fallo")
		else:
			postForm = postForm()
			postFormCategory= postFormCategory()
			postFormTag= postFormTag()

	return render(request,'UpPost.html',{'postForm':postForm,'postFormCategory':postFormCategory,'postFormTag':postFormCategory});


@login_required (login_url='/')
def EditPost(request,primaryKey):
	post = post.objects.get(pk=primaryKey)
	if post.user.pk!= request.user.pk:
		raise Http404
	else:
		if request.method =='POST':
			postForm = postForm(request.POST)
			postFormCategory= postFormCategory(request.POST)
			postFormTag= postFormTag(request.POST)
			if postForm.is_valid():
				category=postFormCategory.save()
				tag=postFormTag.save()
				post=postForm.save(commit=False)
				post.Author=request.user
				post.Categories=category
				post.Tags=tag
				post.save()
				request HttpResponse("Submited")
			else:
				return HttpResponse("Fallo")
	else:
			postForm = postForm()
			postFormCategory= postFormCategory()
			postFormTag= postFormTag()

	return render(request,'EditPost.html',{'postForm':postForm,'postFormCategory':postFormCategory,'postFormTag':postFormCategory});

			

@login_required (login_url='/')
def showPost(request):
	post = post.ovjects.all()
	context={'post':post}
	return render(request,'postCatalog')


@login_required(login_url='/')
def Comments(request,primaryKey):
	post=Post.objects.get(pk = primaryKey)
	user= Post.objects.get(user = primaryKey)
	if request.method == 'POST':
		com= commentPostFrom(request.POST)
		if com.is_valid():
			Comment= com.save(commit=False)
			Comment.Author= user
			Comment.Post = post
			Comment.save()
			post.CantComments = post.CantComments+1
			post.save()
	else:
		com = commentPostFrom()
    return render(request, 'commentPost.html',{'com':com,'Post':post})

@login_required(login_url='/')
def DeletePost (request,primaryKey):
	post=Post.objects.get(pk = primaryKey)
	user= Post.objects.get(user = primaryKey)
	if post.Author.pk!= request.user.pk:
		raise Http404
	else:
		post.delete()
	return render(request,'home.html')


@login_required(login_url='/')
def SearchByCategory (request,primaryKey):

@login_required(login_url='/')
def SearchByTag (request,primaryKey):

@login_required(login_url='/')
def LikePost(request,primaryKey):

@login_required(login_url='/')
def UnLikePost(request,primaryKey):