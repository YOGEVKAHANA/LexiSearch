from django import forms
from .models import Document, Metadata, WordGroup, LinguisticExpression


class DocumentUploadForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = Document
        fields = ['file_name', 'title', 'artist', 'album', 'release_year', 'genre', 'description']


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
