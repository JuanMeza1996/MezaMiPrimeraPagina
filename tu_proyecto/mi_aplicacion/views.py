from django.shortcuts import render, redirect
from .models import Producto
from .forms import CategoriaForm, ProductoForm, ClienteForm

def index(request):
    return render(request, 'mi_aplicacion/index.html')

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'mi_aplicacion/agregar_categoria.html', {'form': form})


def buscar(request):
    if request.method == 'POST':
        term = request.POST.get('termino_busqueda')
        resultados = Producto.objects.filter(nombre__icontains=term)
        return render(request, 'mi_aplicacion/resultados_busqueda.html', {'resultados': resultados})
    return render(request, 'mi_aplicacion/buscar.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = ProductoForm()
    return render(request, 'mi_aplicacion/agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = ClienteForm()
    return render(request, 'mi_aplicacion/agregar_cliente.html', {'form': form})

