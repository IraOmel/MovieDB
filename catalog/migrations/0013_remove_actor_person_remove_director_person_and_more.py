# Generated by Django 4.0.2 on 2023-04-15 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_movie_actor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='person',
        ),
        migrations.RemoveField(
            model_name='director',
            name='person',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='person',
        ),
        migrations.AddField(
            model_name='actor',
            name='first_name',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='actor',
            name='last_name',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='director',
            name='first_name',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='director',
            name='last_name',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='review',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.review'),
        ),
        migrations.AddField(
            model_name='writer',
            name='first_name',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='writer',
            name='last_name',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='Credit',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]