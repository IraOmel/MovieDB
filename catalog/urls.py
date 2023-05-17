from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:id>/', views.movie, name='movie'),
    path('actor-info/<int:actor_id>/', views.actor, name='actor'),
    path('director-info/<int:id>/', views.director, name='director'),
    path('writer-info/<int:id>/', views.writer, name='writer'),
    path('<int:movie_id>/add-to-fav/', views.add_to_fav, name='add-to-fav'),
    path('<int:movie_id>/remove-from-fav/', views.remove_from_fav, name='remove-from-fav'),
    path('<int:movie_id>/add-to-saved/', views.add_to_saved, name='add-to-saved'),
    path('<int:movie_id>/remove-from-saved/', views.remove_from_saved, name='remove-from-saved'),
    path('<int:movie_id>/delete-review/<int:review_id>/', views.delete_review, name='delete-review'),
    path('save/', views.save, name='m'),
]