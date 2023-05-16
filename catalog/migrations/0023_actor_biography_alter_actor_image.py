# Generated by Django 4.0.2 on 2023-05-14 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_alter_actor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='biography',
            field=models.TextField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.ImageField(default=' ', upload_to='catalog/static/catalog/img/personality'),
        ),
    ]