# Generated by Django 4.1.7 on 2023-03-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0007_alter_artista_tipo_de_música'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='foto_de_perfil',
            field=models.ImageField(default='builtins', upload_to='artistas/'),
            preserve_default=False,
        ),
    ]