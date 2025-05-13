from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuari

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            contrasenya = form.cleaned_data['contrasenya']
            try:
                usuari = Usuari.objects.get(email=email, contrasenya=contrasenya)
                return redirect('inici')
            except Usuari.DoesNotExist:
                return render(request, 'login.html', {'error': 'Credencials incorrectes'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def login_con_sessio(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            contrasenya = form.cleaned_data['contrasenya']
            try:
                usuari = Usuari.objects.get(email=email, contrasenya=contrasenya)
                request.session['usuari_id'] = usuari.id
                return redirect('inici')
            except Usuari.DoesNotExist:
                return render(request, 'login.html', {'error': 'Credencials incorrectes'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def inici(request):
    if 'usuari_id' not in request.session:
        return redirect('login')
    usuari = Usuari.objects.get(id=request.session['usuari_id'])
    return render(request, 'inici.html', {'usuari': usuari})

def logout(request):
    request.session.flush()  # Elimina totes les dades de sessió
    return redirect('login')


