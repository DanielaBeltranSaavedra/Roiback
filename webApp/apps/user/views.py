from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.http import HttpResponse
import os
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.forms import ModelForm
from apps.user.forms import *
# Create your views here.

def index(request):
	if(request.user.pk is not None):
		return redirect('HomePage')
	form = logInForm(request.POST or None)
	print("Inicio de sesion")
	if form.is_valid():
		print("forma valida")
		data= form.cleaned_data
		userName=data.get("nombreUsuario")
		password= data.get("contraseniaUsuario")
		print("\n")
		print(userName)
		print(password)
		acceso= authenticate(username=userName, password=password)
		if acceso is not None:
			sesionPotencial= User.objects.get(username =userName)
			print("Cuenta cerrada? "+ str(infousuario.objects.get(user =sesionPotencial).cuantaCerrada)  )
			if infousuario.objects.get(user =sesionPotencial).cuantaCerrada:
			    msj="La cuenta de la que está tratando de acceder esta cerrada"
			    return render(request, 'paginaInicio.html',{'form':form,"msj":msj})
			if infousuario.objects.get(user =sesionPotencial).tieneCuentaActivada:
				login(request,acceso)
				return redirect('/')#TODO: return pagina de inicio despues de iniciar sesion
			else:
				msj="La cuenta todavia no ha sido activada, por favor revisar correo"
				return render(request, 'paginaInicio.html',{'form':form,"msj":msj})

		else:
			msj="Usuario o contraseña no coincide/existe"
			return render(request, 'paginaInicio.html',{'form':form,"msj":msj})
	else:
		form=logInForm()
	return render(request, 'paginaInicio.html',{'form':form})

def SinUp (request):

	if request.method =='POST':
		User_Form= RegistroForm(request.POST)
		if User_Form.is_valid():
			user=User_Form.save(commit=False)
			user.save()
			return render(request,'paginaInicio.html')
	else:
		User_Form= RegistroForm()
	return render(request, 'Registro.html', {'user_form':User_Form})



