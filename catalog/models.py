from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=255, default=' ')
    last_name = models.CharField(max_length=255, default=' ')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Writer(models.Model):
    first_name = models.CharField(max_length=255, default=' ')
    last_name = models.CharField(max_length=255, default=' ')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=255, default=' ')
    last_name = models.CharField(max_length=255, default=' ')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s review for {self.movie.title}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.ManyToManyField(Director)
    writer = models.ManyToManyField(Writer)
    actor = models.ManyToManyField(Actor)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    rating = models.FloatField()
    release_date = models.DateField()
    runtime = models.PositiveIntegerField()
    cover_image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



