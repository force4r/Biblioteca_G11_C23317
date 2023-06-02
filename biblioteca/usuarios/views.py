from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


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





