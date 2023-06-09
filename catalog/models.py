from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from users.models import UserProfile


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=255, default=' ')
    last_name = models.CharField(max_length=255, default=' ')
    image = models.ImageField(default=' ')
    biography = models.TextField(max_length=1000, default=' ')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Actor(models.Model):
    first_name = models.CharField(max_length=255, default=' ')
    last_name = models.CharField(max_length=255, default=' ')
    image = models.ImageField()
    biography = models.TextField(max_length=1000, default=' ')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    rating = models.FloatField()
    release_date = models.CharField(max_length=255)
    runtime = models.PositiveIntegerField()
    cover_image = models.ImageField(default=' ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)


class Saved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
