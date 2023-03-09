from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductoForm
from .models import Producto
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db.models import Q

# Create your views here.
def inicio(request):
        productos = Producto.objects.all()
        return render(request, 'AppCrud/index.html', {'productos': productos})

def modificar(request):
    productos=Producto.objects.all()
    return render(request, 'AppCrud/modificar.html', {'productos': productos})
    
def modificar_producto(request,producto_id):
  
    
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            
            return redirect('modificar')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'AppCrud/modificar_producto.html', {'form': form, 'producto': producto})
def eliminar(request):
    productos = Producto.objects.all()
    return render(request, 'AppCrud/eliminar.html', {'productos': productos})

def eliminar_producto(request,producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('eliminar')

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto guardado exitosamente')
            form = ProductoForm() #se crea uno vacio
    else:
        form = ProductoForm()
    return render(request, 'AppCrud/crear_producto.html', {'form': form})

def filtrar_productos2(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        productos = Producto.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppCrud/filtrar_productos.html', {'productos': productos})
    else:
        return render(request, 'AppCrud/filtrar_productos.html')
    
def filtrar_productos(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        productos = Producto.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
        return render(request, 'AppCrud/filtrar_productos.html', {'productos': productos, 'query': query})
    else:
        return render(request, 'AppCrud/filtrar_productos.html')
    
