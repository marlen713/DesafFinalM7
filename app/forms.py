from django import forms
from .models import Usuario, SolicitudArriendo,Inmueble

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'nombres', 'apellidos', 'rut', 'direccion', 'telefono', 'correo_electronico', 'tipo_usuario']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        exclude = ('propietario',)  # Excluimos el campo 'propietario' del formulario

    

class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = ['inmueble', 'mensaje']
    