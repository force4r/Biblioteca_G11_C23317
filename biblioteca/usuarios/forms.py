from django.contrib.auth.forms import UserCreationForm
from django import forms
from usuarios.models import Usuario

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class':'form-control'}),
        required=True
    )
    first_name = forms.CharField(
        min_length= 3, 
        label="Nombre",
        widget= forms.TextInput(attrs={'class':'form-control'}),
        required=True
    )
    
    last_name = forms.CharField(
        min_length= 3, 
        label="Apellido",
        widget= forms.TextInput(attrs={'class':'form-control'}),
        required=True
        )
    
    class Meta:
        model = Usuario 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'