from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    
    tp = (
        ("Banda", "Banda"),
        ("Coral", "Coral"),
        ("Solo", "Solo"),
    )

    tipo_de_música = models.CharField(max_length=30, choices=tp,default="Solo")
    quantidade_de_músicas_lançadas = models.IntegerField()
    ano_do_primeiro_lançamento = models.IntegerField()
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Musica(models.Model):
    nome_musica = models.CharField(max_length=100)
    e = (
        ("Rock", "Rock"),
        ("Gospel", "Gospel"),
        ("Pop", "Pop"),
    )
    estilo = models.CharField(max_length=50, choices=e,default="Gospel")
    tempo_duracao = models.FloatField()
    artista = models.ForeignKey(Artista, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.nome_musica

        
