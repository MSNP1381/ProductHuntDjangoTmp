from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    pub_date = models.DateTimeField(auto_now=True)
    vote_tot = models.PositiveSmallIntegerField(default=1)
    image = models.ImageField(upload_to='media/')
    icon = models.ImageField(upload_to='media/')
    body = models.TextField(blank=True)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:75]
