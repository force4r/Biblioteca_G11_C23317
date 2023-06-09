from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth.models import Group
from .models import Usuario



def login_user(request):
        context={}
        if request.method == "POST":
          username = request.POST["username"]
          password = request.POST["password"]
          user = authenticate(request, username=username, password=password)
          if user is not None:
            login(request, user)
            return redirect('index')
          else:
            messages.error(request, "Hubo un error al ingresar, verifique y vuelva a intentar")
            return redirect('login')
        else:
            return render(request, 'authenticate/login.html', context)
        

def logout_user(request):
        logout(request)
        messages.success(request, ("Haz cerrado sesion correctamente"))
        return redirect('index')    


def register_user(request):
    
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            #Intento de asignar automaticamente a Grupos
            #grupo = Group.objects.get(name='Lector')
            #user = Usuario.objects.get(username="username")
            #user.groups.add(grupo)
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registro realizado con exito"))
            return redirect('index')
    else:
        form = RegisterUserForm()


        
        
        
    return render (request, 'authenticate/register_user.html',{'form':form})





