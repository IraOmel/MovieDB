# Generated by Django 4.0.2 on 2023-05-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='image',
            field=models.ImageField(default=' ', upload_to='catalog/static/catalog/img/personality'),
        ),
    ]