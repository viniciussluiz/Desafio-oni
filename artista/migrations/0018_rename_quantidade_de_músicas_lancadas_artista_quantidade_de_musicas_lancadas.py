# Generated by Django 4.1.7 on 2023-03-31 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0017_rename_ano_do_primeiro_lançamento_artista_ano_do_primeiro_lancamento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artista',
            old_name='quantidade_de_músicas_lancadas',
            new_name='quantidade_de_musicas_lancadas',
        ),
    ]
