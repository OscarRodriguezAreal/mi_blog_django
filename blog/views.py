from django.shortcuts import render, redirect
from .models import Post
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm

def home(request):
    return render(request, "blog/base.html")

def agregar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AutorForm()
    return render(request, "blog/formulario.html", {"form": form, "titulo": "Agregar Autor"})

def agregar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoriaForm()
    return render(request, "blog/formulario.html", {"form": form, "titulo": "Agregar Categoría"})

def agregar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blog/formulario.html", {"form": form, "titulo": "Agregar Post"})

def buscar_post(request):
    form = BuscarPostForm(request.GET)
    posts = []
    if form.is_valid():
        titulo = form.cleaned_data.get("titulo")
        if titulo:
            posts = Post.objects.filter(titulo__icontains=titulo)
    return render(request, "blog/buscar.html", {"form": form, "posts": posts})
