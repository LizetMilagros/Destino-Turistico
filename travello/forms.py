#crear html basandonos en modelo
from django import forms
from .models import Destination

class DestinoTuristico(forms.ModelForm):
    class Meta:
        model =Destination
        #para hacer referencia a los campos
        fields ='__all__'
