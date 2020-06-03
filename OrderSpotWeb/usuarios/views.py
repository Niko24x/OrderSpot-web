#django
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

# def welcome(request):
# 	return render(request, "users/welcome.html")

# def register(request):
# 	return render(request, "users/register.html")

# def login_view(request):
#     # Creamos el formulario de autenticación vacío
#     form = AuthenticationForm()
#     if request.method == "POST":
#         # Añadimos los datos recibidos al formulario
#         form = AuthenticationForm(data=request.POST)
#         # Si el formulario es válido...
#         if form.is_valid():
#             # Recuperamos las credenciales validadas
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             # Verificamos las credenciales del usuario
#             user = authenticate(username=username, password=password)

#             # Si existe un usuario con ese nombre y contraseña
#             if user is not None:
#                 # Hacemos el login manualmente
#                 login(request, user)
#                 # Y le redireccionamos a la portada
#                 return redirect('/')

#     # Si llegamos al final renderizamos el formulario
#     return render(request, "usuarios/login.html", {'form': form})

# def logout_view(request):
# 	logout(request)
# 	return redirect('/')