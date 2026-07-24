from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Movie

def home(request):
    query = request.GET.get("q")

    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()

    featured_movie = Movie.objects.order_by("-id").first()

    context = {
        "featured_movie": featured_movie,
        "action_movies": movies.filter(category="Action"),
        "comedy_movies": movies.filter(category="Comedy"),
        "horror_movies": movies.filter(category="Horror"),
        "romance_movies": movies.filter(category="Romance"),
        "scifi_movies": movies.filter(category="Sci-Fi"),
    }

    return render(request, "home.html", context)

def trending(request):
    movies = Movie.objects.order_by("-release_year", "-rating")[:20]

    return render(request, "trending.html", {
        "movies": movies
    })

def category(request, category_name):
    movies = Movie.objects.filter(category=category_name)

    return render(request, "movies.html", {
        "movies": movies,
    })

def movies(request):
    movies = Movie.objects.all().order_by("-release_year")

    return render(request, "movies.html", {
        "movies": movies
    })


@login_required
def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)

    related_movies = Movie.objects.filter(
        category=movie.category
    ).exclude(id=movie.id)[:4]

    return render(request, "movie_detail.html", {
        "movie": movie,
        "related_movies": related_movies,
    })

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def add_to_favorites(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.user in movie.favorites.all():
        movie.favorites.remove(request.user)
    else:
        movie.favorites.add(request.user)

    return redirect("movie_detail", id=id)

@login_required
def my_list(request):
    movies = request.user.favorite_movies.all()

    return render(request, "my_list.html", {
        "movies": movies,
    })

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})