from django import forms
from .models import Artista
from .models import Musica

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nome', 'tipo_de_musica', 'quantidade_de_musicas_lancadas', 'ano_do_primeiro_lancamento', 'foto']
        
class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['nome_musica', 'estilo', 'tempo_duracao', 'artista']