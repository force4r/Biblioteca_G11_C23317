from django import forms

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

    