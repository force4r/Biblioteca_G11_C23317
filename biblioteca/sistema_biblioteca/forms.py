from django import forms
from typing import Any, Dict 
from .models import Libro, Autor, Editorial, Genero
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
    


    """ class EditorialForm(forms.Form):
        editorial = forms.CharField(

        max_length=100,
        widget=forms.Select(choices=TITLE_CHOICES),
    ) """
    
    

    
    

class bibliotecaform(forms.Form):
    
    titulo = forms.CharField(
        
        label='Titulo',
        widget= forms.TextInput(),
        required=True
    )
    
    autor = forms.CharField(
        min_length= 3,
        label='Nombre del Autor',
        widget= forms.TextInput(),
        required=True 
    )

    genero = forms.CharField(
        min_length= 3,
        label='Genero',
        widget= forms.TextInput(),
        required=True 
    )

    # isbn = forms.CharField(
    #     min_length= 3,
    #     label='ISBN',
    #     widget= forms.CharField( widget=forms.TextInput(attrs={'type':'number'})),
    #     required=True 
    # )

    año_edicion = forms.IntegerField(
        
        label='Año de edicion',
        widget= forms.DateTimeInput(),
        required=True 
    )

    descripcion = forms.CharField(
        min_length= 3,
        label='Descripcion',
        widget= forms.TextInput(),
        required=True 
    )

    editoriales = forms.CharField(
        min_length= 3,
        label='Editoriales',
        widget= forms.TextInput(),
        required=True 
    )

    idiomas = forms.CharField(
        min_length= 3,
        label='Idiomas',
        widget= forms.TextInput(),
        required=True 
    )

class AltaLibro(forms.ModelForm):
   
    class Meta:
        model = Libro
        fields = '__all__'

    def __init__(self, *args, **kwargs ):
        super(AltaLibro, self).__init__(*args, **kwargs)
        # sin la siguiente línea label_from_instance NO funciona
        self.fields['editoriales'].queryset = Editorial.objects.all()
        self.fields['editoriales'].label_from_instance = lambda obj: "%s" % (obj.editorial)
        self.fields['autor'].queryset = Autor.objects.all()
        self.fields['autor'].label_from_instance = lambda obj: "%s %s" % (obj.nombre, obj.apellido)
        self.fields['genero'].queryset = Genero.objects.all()
        self.fields['genero'].label_from_instance = lambda obj: "%s" % (obj.genero)
    

    
    # autor = forms.ModelChoiceField(
    #    queryset=Autor.objects.values_list()
    # )
    # genero = forms.ModelChoiceField(
    #    queryset=Genero.objects.values()
    # )
    # editoriales = forms.MultipleChoiceField(
    #     choices=Editorial.objects.values_list()
    # )
    
        

    
        
        
        
        