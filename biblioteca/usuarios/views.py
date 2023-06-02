from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



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
            messages.success(request, ("Hubo un error al ingresar, verifique y vuelva a intentar"))
            return redirect('login')
        else:
            return render(request, 'authenticate/login.html', context)
        

def logout_user(request):
        logout(request)
        messages.success(request, ("Haz cerrado sesion correctamente"))
        return redirect('index')    


def register_user(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registro realizado con exito"))
            return redirect('index')
    else:
        form = UserCreationForm()


        
        
        
    return render (request, 'authenticate/register_user.html',{'form':form})





