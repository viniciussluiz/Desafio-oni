# Generated by Django 4.1.7 on 2023-03-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0013_alter_artista_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='artistas/'),
        ),
    ]
