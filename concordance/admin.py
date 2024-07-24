# admin.py

from django.contrib import admin
from concordance.models import Document, Word

admin.site.register(Document)
admin.site.register(Word)

# Customize admin views as needed