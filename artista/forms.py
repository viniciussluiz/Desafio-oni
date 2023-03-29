from django import forms
from .models import Artista
from .models import Musica

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nome', 'tipo_de_música', 'quantidade_de_músicas_lançadas', 'ano_do_primeiro_lançamento', 'foto']
        
class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['nome_musica', 'estilo', 'tempo_duracao', 'artista']