from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from app.models import SolicitudArriendo , Inmueble, Usuario
from .forms import RegistroUsuarioForm,SolicitudArriendoForm,InmuebleForm



# Create your views here.

def index(request):
    inmuebles = Inmueble.objects.all()
    usuario = request.user
    return render(request, 'index.html',{'inmuebles': inmuebles})



@login_required
def detalle_inmueble(request, id):
    inmueble = Inmueble.objects.get (pk=id)
    return render(request,'detalle_inmueble.html',{'inmuebles':inmueble})




def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            password = form.cleaned_data['password']
            usuario.set_password(password)
            usuario.save()
            # Autenticar al usuario después del registro
            usuario_autenticado = authenticate(username=usuario.username, password=password)
            if usuario_autenticado is not None:
                login(request, usuario_autenticado)
                return redirect('index')  
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro_usuario.html', {'form': form})

@login_required
def generar_solicitud_arriendo(request, id):
    # Obtener el inmueble por su ID
    inmueble = get_object_or_404(Inmueble, pk=id)
    
    # Verificar si el usuario está autenticado y es un arrendatario
    if request.user.is_authenticated and request.user.usuario.tipo_usuario == 'arrendatario':
        if request.method == 'POST':
            form = SolicitudArriendoForm(request.POST)
            if form.is_valid():
                solicitud = form.save(commit=False)
                solicitud.arrendatario = request.user.usuario  # Asignar el usuario arrendatario
                solicitud.inmueble = inmueble
                solicitud.save()
                return redirect('detalle', id=inmueble.id)
        else:
            # Inicializar el formulario con el inmueble correspondiente
            form = SolicitudArriendoForm(initial={'inmueble': inmueble})
        return render(request, 'generar_solicitud_arriendo.html', {'form': form})
    else:
        return redirect('index')
    
    
    
@login_required
def solicitudes_arrendador(request):
    # Verificar si el usuario es un arrendador
    if request.user.usuario.tipo_usuario == 'arrendador':
        # Obtener todas las solicitudes recibidas por el arrendador
        solicitudes = SolicitudArriendo.objects.filter(inmueble__propietario=request.user)
        return render(request, 'solicitudes_arrendador.html', {'solicitudes': solicitudes})
    else:
        # Redirigir a otra página si el usuario no es un arrendador
        return redirect('index')  
  
  
@login_required
def alta_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        print(form)
        if form.is_valid():
            
            inmueble = form.save(commit=False)
            inmueble.propietario = request.user
            inmueble.save()
            return redirect('inicio') 
    else:
        form = InmuebleForm()
    return render(request, 'alta_inmueble.html', {'form': form})