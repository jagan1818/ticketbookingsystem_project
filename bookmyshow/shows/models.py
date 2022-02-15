from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        abstract = True


class Cities(BaseModel):
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return self.city_name

    class Meta:
        db_table = 'shows_cities'


class Theatres(BaseModel):
    theatre_name = models.CharField(max_length=255)
    city = models.ForeignKey('Cities', on_delete=models.CASCADE)

    def __str__(self):
        return self.theatre_name

    class Meta:
        db_table = 'shows_theatres'


class Screens(BaseModel):
    screen_name = models.CharField(max_length=255)
    theatre = models.ForeignKey('Theatres', on_delete=models.CASCADE)

    def __str__(self):
        return self.screen_name

    class Meta:
        db_table = 'shows_screens'


class Movies(BaseModel):
    movie_name = models.CharField(max_length=255)
    release_date = models.DateField()
    screen = models.ForeignKey('Screens', on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_name

    class Meta:
        db_table = 'shows_movies'