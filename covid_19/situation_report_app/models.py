from django.db import models
# from django.contrib.auth.models import User
from users_app.models import AppUser


# abstract class
class IsApprovedMixin(models.Model):
    is_approved = models.BooleanField(default=False)

    class Meta:
        abstract = True


class ApprovedManager(models.Manager):

    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_approved=True)


# abstract class Date (changed class Article(Date): and class Statistic(Date):)
class Date(models.Model):
    date = models.DateField(null=True)

    class Meta:
        abstract = True


# Create your models here.
class Place(models.Model):
    place_name = models.CharField(max_length=16, unique=True, verbose_name='название страны или места')
    country = models.BooleanField(default=True, verbose_name='отметка, если страна')
    notes = models.TextField(blank=True, verbose_name='примечания')

    class Meta:
        verbose_name = 'страна или место'
        verbose_name_plural = 'places'

    def __str__(self):
        return self.place_name


class Source(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Article(Date):
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Statistic(Date):
    country_name = models.ForeignKey(Place, on_delete=models.CASCADE)
    total_cases = models.CharField(max_length=32, null=True)
    new_cases = models.CharField(max_length=32, null=True)
    total_deaths = models.CharField(max_length=32, null=True)
    new_deaths = models.CharField(max_length=32, null=True)
    total_recovered = models.CharField(max_length=32, null=True)

    # def __str__(self):
    #     return self.name


class Post(IsApprovedMixin):
    objects = models.Manager()
    approved_objects = ApprovedManager()
    name = models.CharField(max_length=64, unique=True)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    # user = models.ForeignKey(User)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    def has_image(self):
        return bool(self.image)

    def __str__(self):
        return self.name
