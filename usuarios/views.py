from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('lista_usuarios')
    return render(request, 'usuarios/login.html')

# LOGOUT
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# LISTAR USUARIOS
@login_required
def lista_usuarios(request):
    users = User.objects.all()
    return render(request, 'usuarios/lista.html', {'users': users})

# CREAR USUARIO (con correo)
@login_required
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('lista_usuarios')
    return render(request, 'usuarios/crear.html')

# ELIMINAR USUARIO
@login_required
def eliminar_usuario(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('lista_usuarios')

# CRÉDITOS
@login_required
def creditos(request):
    return render(request, 'usuarios/creditos.html')
