from django.urls import path
from .views import list_artista, create_artista, update_artista, delete_artista, list_musica, create_musica, editar_musica, delete_musica, list_musicas

urlpatterns = [
    path('', list_artista, name='list_artista'),
    path('update/<int:id>/', update_artista, name='update_artista'),
    path('new', create_artista, name='create_artista'),
    path('delete/<int:id>/', delete_artista, name='delete_artista'),
    path('musica.html', list_musicas, name='list_musicas'),
    path('nova',create_musica, name='create_musica'),
    path('edit/<int:musica_id>/', editar_musica, name='editar_musica'),
    path('delmusic/<int:musica_id>/', delete_musica, name='delete_musica'),
    path('delete/<int:id>/', delete_artista, name='delete_artista'),
    path('artistas/<int:artista_id>/', list_musica, name='list_musica'),
]
