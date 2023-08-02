from django.db import models


# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True)
    newspaper = models.CharField(max_length=30, default="", blank=True, null=True)
    date = models.DateTimeField()
    link = models.CharField(max_length=2083, default="")
    language = models.CharField(max_length=20)
    dattion = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    description = models.CharField(max_length=20000, default="")
    sentiment = models.CharField(max_length=20)
