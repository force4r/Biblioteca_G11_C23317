from django import forms
from typing import Any, Dict 
DESTINO_CHOICES = (
    ("informacion_personal", "Información general"),
    ("recomendacion_libro", "Recomendación de libro"),
    ("prestamos", "Prestamos"),
)

class contactoForm(forms.Form):

    nombre = forms.CharField(
        min_length= 3,
        label='Nombre',
        widget= forms.TextInput(attrs={'class':'form-control'}),
        required=True
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class':'form-control'}),
        required=True
    )
    asunto = forms.CharField(
        label='Asunto',
        widget= forms.TextInput(attrs={'class':'form-control'})
    )
    destino = forms.ChoiceField(
        choices=DESTINO_CHOICES,
        label='Destino',
        widget= forms.Select(),
        required=True
    )

    mensaje = forms.CharField(
        label='Tu mensaje',
        widget=forms.Textarea(attrs={'class':'form-control'}),
        required=True
    )
    recibir_informacion = forms.BooleanField(
        label='Deseo recibir información sobre las actividades en la Biblioteca.',
        required=False
    )

    def clean(self) -> Dict[str, Any]:
        # Se buscan los datos del form
        super(contactoForm, self).clean()
        nombre = self.cleaned_data.get('nombre')
        asunto = self.cleaned_data.get('asunto')
        
        n=False
        for i in nombre:
            if i.isnumeric():
                n=True
        if n==True:
            self.add_error('nombre','El nombre no puede contener números') 
        a=False
        for i in asunto:
             if i.isnumeric():
                a=True
        if a==True:
            self.add_error('asunto', 'El asunto no puede contener números')
            
        return self.cleaned_data