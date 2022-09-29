from distutils.log import INFO
from django.shortcuts import render
from calendar import c
from django.http import HttpResponse
from django.template import Template,  Context
from AppCoder.models import Family3, entregable, profesor, estudiate
from AppCoder.forms import *
# Create your views here.
def inicio(request): 

	return render(request, "AppCoder/inicio.html")

def estudiantes(request):
	
	return render(request, "AppCoder/estudiantes.html")

def profesores(request): 
	
	return render(request, "AppCoder/profesores.html")

def Family(request):

	mama = Family3(nombre = "Ivana", edad = 48, fechaNac="1974-06-19")
	mama.save()
	papa = Family3(nombre = "Miguel", edad = 50, fechaNac="1972-03-26")
	papa.save()
	hermana = Family3(nombre = "Guadalupe", edad = 23, fechaNac="1999-05-06" )
	hermana.save()
	
	miHtml = open("C:/Users/Equipo/Desktop/trabajo django/ProyectoCoder/AppCoder/plantilla/family20.html")
	
	plantilla = Template(miHtml.read())
	
	miHtml.close()

	miContexto = Context()

	documento = plantilla.render(miContexto)
	
	return render(request, "family20.html",{"mama":mama,"papa":papa,"hermana":hermana})

def entregables(request):
	
	ente1 = entregable(nombre="examen 1", fechaDeEntrega="2022-03-30")
	ente1.save()
	
	return render(request, "AppCoder/entregables.html")

def formulario1(request):
	
	if request.method=="POST":

		formulario1 = FormularioProfesor(request.POST)

		if formulario1.is_valid(): #manera de ver si tenemos errores
		
			info = formulario1.cleaned_data

			ProfeF = profesor(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"], profesion=info["profesion"])

			ProfeF.save() #se realiza el guardado en la base de datos

			return render(request, "AppCoder/inicio.html") #nos vuelve a mostrar la pagina del formulario vacia o la podemos redireccionar a otra parte de la pagina

	else: 
		
		formulario1=FormularioProfesor() #muestra el formulario vacio
	
	return render(request, "AppCoder/formu1.html", {"form1":formulario1}) #entero añ url y me muestra esta plantilla
	
def fromulario2(request):
	
	if request.method=="POST":

		formulario2 = FormularioEstudainte(request.POST)

		if formulario2.is_valid(): #manera de ver si tenemos errores
		
			info = formulario2.cleaned_data

			estdianteF = estudiate(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"])

			estdianteF.save() #se realiza el guardado en la base de datos

			return render(request, "AppCoder/inicio.html") #nos vuelve a mostrar la pagina del formulario vacia o la podemos redireccionar a otra parte de la pagina

	else: 
		
		formulario2=FormularioEstudainte() #muestra el formulario vacio
	
	return render(request, "AppCoder/formu2.html", {"form2":formulario2}) #entero añ url y me muestra esta plantilla


def busquedaProfes(requst):

	return render(requst, "AppCoder/busquedaProfes.html")

def buscar(request):

	if request.GET["nombre"]:

		nombre = request.GET["nombre"]
		
		profes = profesor.objects.filter(nombre__icontains=nombre)
		
		
		return render(request, "AppCoder/resultados.html", {"profes":profes, "nombre":nombre})
	
	else:
		
		mensaje = "No enviaste los datos"

	return HttpResponse(mensaje)