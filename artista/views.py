from django.shortcuts import render, redirect
from .forms import ArtistaForm, MusicaForm
from .models import Artista, Musica

def list_artista(request):
    artistas = Artista.objects.all()
    return render(request, 'artista.html', {'artistas': artistas})


def create_artista(request):
    form = ArtistaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_artista')

    return render(request, 'artista-form.html', {'form': form})


def update_artista(request, id):
    artista = Artista.objects.get(id=id)
    form = ArtistaForm(request.POST or None, instance=artista)

    if form.is_valid():
        form.save()
        return redirect('list_artista')

    return render(request, 'artista-form.html', {'form': form, 'artista': artista})


def delete_artista(request, id):
    artista = Artista.objects.get(id=id)

    if request.method == 'POST':
        artista.delete()
        return redirect('list_artista')

    return render(request, 'artista-delete-confirm.html', {'artista': artista})


def list_musicas(request):
    musicas = Musica.objects.all()
    return render(request, 'musica.html', {'musicas': musicas})


def list_musica(request, artista_id):
    artistas = Artista.objects.get(id=artista_id)
    musicas = Musica.objects.filter(artista_id=artista_id)
    return render(request, 'musica.html', {'artistas': artistas , 'musicas': musicas})


def create_musica(request):
    form = MusicaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_musicas')

    return render(request, 'musica-form.html', {'form': form})


def editar_musica(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    form = MusicaForm(request.POST or None, instance=musica)

    if form.is_valid():
        form.save()
        return redirect('list_musicas')

    return render(request, 'musica-form.html', {'form': form, 'musica': musica})


def delete_musica(request, musica_id):
    musica = Musica.objects.get(id=musica_id)

    if request.method == 'POST':
        musica.delete()
        return redirect('list_musicas')

    return render(request, 'musica-delete-confirm.html', {'musica': musica})
    
