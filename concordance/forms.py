from django import forms
from .models import Document, Metadata, WordGroup, LinguisticExpression


class DocumentUploadForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = Document
        fields = ['file_name', 'title', 'artist', 'album', 'release_year', 'genre', 'description']


class DocumentSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False, label='Search')
    title = forms.CharField(max_length=255, required=False, label='Title')
    artist = forms.CharField(max_length=255, required=False, label='Artist')
    album = forms.CharField(max_length=255, required=False, label='Album')
    release_year = forms.IntegerField(required=False, label='Release Year')
    genre = forms.CharField(max_length=255, required=False, label='Genre')
    description = forms.CharField(max_length=255, required=False, label='Description')


class MetadataForm(forms.ModelForm):
    class Meta:
        model = Metadata
        fields = ['key', 'value']


class WordGroupForm(forms.ModelForm):
    class Meta:
        model = WordGroup
        fields = ['name', 'words']


class LinguisticExpressionForm(forms.ModelForm):
    class Meta:
        model = LinguisticExpression
        fields = ['expression', 'description']
