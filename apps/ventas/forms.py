# apps/ventas/forms.py
from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto', 'cantidad']  # Asegúrate de que estos campos existan en el modelo
