from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def root(request):
    return redirect("/blogs")

def create(request):
    return redirect("/")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog numero:{number}")

def edit(request, number):
    return HttpResponse(f"placeholder para editar el blog {number}")

def destroy(request, number):
    return redirect("/blogs")