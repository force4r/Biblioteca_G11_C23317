from django import forms
from .models import Libro, Autor, Editorial, Genero, Prestamo_Libro

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
        widget= forms.Select(attrs={'class':'form-select'}),
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

    def clean(self):
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
    

class AltaLibro(forms.ModelForm):

    class Meta:
        model = Libro
        fields = '__all__'
        
        widgets = {
            "titulo": forms.TextInput(attrs={'class':'form-control'}),
            "isbn": forms.TextInput(attrs={'class':'form-control'}),
            "idioma": forms.TextInput(attrs={'class':'form-control'}),
            "descripcion": forms.Textarea(attrs={'class':'form-control', 'placeholder':'Resumen del libro'}),
            "genero": forms.Select(attrs={'class':'form-select'}),
            "autor": forms.Select(attrs={'class':'form-select'}),
            "editoriales": forms.SelectMultiple(attrs={'class':'form-select'}),
            "año_ingreso": forms.TextInput(attrs={'class':'form-control'}),
            "año_edicion": forms.TextInput(attrs={'class':'form-control'}),
            "imagen":forms.ImageField(required=False)
        }

    def __init__(self, *args, **kwargs ):
        super(AltaLibro, self).__init__(*args, **kwargs)
        # sin la siguiente línea label_from_instance NO funciona
        self.fields['editoriales'].queryset = Editorial.objects.all()
        self.fields['editoriales'].label_from_instance = lambda obj: "%s" % (obj.editorial)
        self.fields['autor'].queryset = Autor.objects.all()
        self.fields['autor'].label_from_instance = lambda obj: "%s %s" % (obj.nombre, obj.apellido)
        self.fields['genero'].queryset = Genero.objects.all()
        self.fields['genero'].label_from_instance = lambda obj: "%s" % (obj.genero)
    

class AltaAutor(forms.ModelForm):
    
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            "nombre":forms.TextInput(attrs={'class':'form-control'}),
            "apellido":forms.TextInput(attrs={'class':'form-control'}),
            "nacionalidad":forms.TextInput(attrs={'class':'form-control'}),                  
        }

class AltaGenero(forms.ModelForm):
    
    class Meta:
        model = Genero
        fields = '__all__'
        widgets = {
            "genero":forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Género'} ),        
        }

class AltaEditorial(forms.ModelForm):
    
    class Meta:
        model = Editorial
        fields = '__all__'
        widgets = {
            "editorial":forms.TextInput(attrs={'class':'form-control', 'placeholder':'Editorial'}),        
        }

class Reservas(forms.ModelForm):
    
    class Meta:
        model = Prestamo_Libro
        fields = ["reserva", "libro"]
        exclude = ["fecha_prestamo_fin"]
        widgets={
            "libro": forms.Select(attrs={'class':'form-select'}),
        }
        
        
