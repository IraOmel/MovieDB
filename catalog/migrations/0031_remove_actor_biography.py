# Generated by Django 4.0.2 on 2023-05-16 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0030_movie_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='biography',
        ),
    ]
