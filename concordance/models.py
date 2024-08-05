from django.db import models
from django.utils import timezone


class Document(models.Model):
    file_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, null=True, blank=True)
    album = models.CharField(max_length=255, null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Metadata(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)


class Word(models.Model):
    text = models.CharField(max_length=100, unique=True, default='default_text')  # Provide a default value here


class WordOccurrence(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    position = models.IntegerField()


class WordGroup(models.Model):
    name = models.CharField(max_length=100)
    words = models.ManyToManyField(Word)


class LinguisticExpression(models.Model):
    expression = models.CharField(max_length=255)
    description = models.TextField()
