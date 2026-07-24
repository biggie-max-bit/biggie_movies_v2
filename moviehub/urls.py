from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),
    path('signup/', views.signup, name='signup'),
    path("movies/", views.movies, name="movies"),
    path("trending/", views.trending, name="trending"),
    path("favorite/<int:id>/", views.add_to_favorites, name="add_to_favorites"),
    path("my-list/", views.my_list, name="my_list"),
    path("category/<str:category_name>/", views.category, name="category"),
]