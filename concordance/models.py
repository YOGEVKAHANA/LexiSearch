from django.db import models
from django.utils import timezone


class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='')  # Provide a default value here
    upload_date = models.DateTimeField(default=timezone.now)  # Provide a default value here


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
