from django import forms
from .models import Document, Metadata, WordGroup, LinguisticExpression


class DocumentUploadForm(forms.Form):
    title = forms.CharField(max_length=255)
    file = forms.FileField()


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
