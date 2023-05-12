from django.urls import path
from . import views


urlpatterns = [
    path('<str:username>/', views.user_profile, name = 'user_profile'),
    path('<str:username>/favourites/', views.favourites, name='favourites'),
]


