# Generated by Django 4.0.2 on 2023-05-16 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_director_biography_director_image_writer_biography_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='biography',
        ),
    ]
