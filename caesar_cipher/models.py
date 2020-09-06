from django.db import models


# Create your models here

class Article(models.Model):
    body = models.TextField(max_length=65536)
    uri = models.TextField(max_length=1024)

    def __str__(self):
        return self.uri


class CapitalWord(models.Model):
    word = models.TextField(max_length=1024)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.word


class Statistic(models.Model):
    uri = models.TextField(max_length=1024)

    def __str__(self):
        return self.uri
