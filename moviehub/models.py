from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    video = models.FileField(upload_to='movies/')
    category = models.CharField(max_length=100, default="Action")
    release_year = models.IntegerField()

    rating = models.DecimalField(max_digits=2, decimal_places=1, default=8.0)
    duration = models.CharField(max_length=20, default="2h 00m")
    quality = models.CharField(max_length=20, default="1080p")
    language = models.CharField(max_length=50, default="English")

    favorites = models.ManyToManyField(
    "auth.User",
    blank=True,
    related_name="favorite_movies"
)

    def __str__(self):
        return self.title