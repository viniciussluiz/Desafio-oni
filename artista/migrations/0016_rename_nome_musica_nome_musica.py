# Generated by Django 4.1.7 on 2023-03-28 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0015_alter_artista_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musica',
            old_name='nome',
            new_name='nome_musica',
        ),
    ]
