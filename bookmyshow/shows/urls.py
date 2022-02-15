from django.urls import path
from shows import views


urlpatterns = [
    path('api/movie_save', views.AddMovies.as_view()),
    path('api/movies_list', views.MoviesList.as_view()),
    path('api/update_movie/<int:id>', views.UpdateMovies.as_view())
]