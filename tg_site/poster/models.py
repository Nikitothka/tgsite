from django.db import models

class Category(models.Model):
    name = models.TextField()
    posts= models.ManyToManyField(to='Post')


class Post(models.Model):
    views = models.IntegerField()
    categories = models.ManyToManyField(to='Category')


class Channel(models.Model):
    name = models.TextField()