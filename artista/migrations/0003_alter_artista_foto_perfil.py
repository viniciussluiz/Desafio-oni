# Generated by Django 4.1.7 on 2023-03-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0002_artista_ano_primeiro_lancamento_artista_foto_perfil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='artistas/'),
        ),
    ]
