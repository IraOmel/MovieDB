# Generated by Django 4.0.2 on 2023-03-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_movie_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover_image',
            field=models.CharField(max_length=255),
        ),
    ]