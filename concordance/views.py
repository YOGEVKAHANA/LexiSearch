from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Document, Word, WordOccurrence, WordGroup, LinguisticExpression
from .forms import DocumentUploadForm, MetadataForm, WordGroupForm, LinguisticExpressionForm
from django.shortcuts import render, redirect
from .forms import DocumentUploadForm
from .models import Document, Word, WordOccurrence
# from .database_utils import execute_sql
import re
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import DocumentUploadForm
from .models import Document
from .database_utils import execute_sql
from django.conf import settings
import os

def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            if form.is_valid():
                document = form.save(commit=False)

                # Handle file upload
                file = request.FILES['file']
                file_name = file.name
                file_path = os.path.join(settings.MEDIA_ROOT, file_name)

                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

                document.file_path = file_path
                # document.save()
            # Save the document metadata to Oracle database
            sql = '''
                INSERT INTO documents (file_name, title, artist, album, release_year, genre, description, file_path)
                VALUES (:file_name, :title, :artist, :album, :release_year, :genre, :description, :file_path)
            '''
            params = {
                'file_name': document.file_name,
                'title': document.title,
                'artist': document.artist,
                'album': document.album,
                'release_year': document.release_year,
                'genre': document.genre,
                'description': document.description,
                'file_path': document.file_path
            }
            execute_sql(sql, params)

            return redirect('document_list')
    else:
        form = DocumentUploadForm()
    return render(request, 'concordance/upload_document.html', {'form': form})

"""
def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            file = request.FILES['file']

            # Read and decode the file content
            content = file.read().decode('utf-8')

            # Create and save the document
            document = Document.objects.create(title=title, content=content)

            # Process the document
            process_document(document)

            return redirect('document_list')
    else:
        form = DocumentUploadForm()
    return render(request, 'concordance/upload_document.html', {'form': form})


def process_document(document):
    # Tokenize the content into words
    words = re.findall(r'\b\w+\b', document.content.lower())

    # Count words and save occurrences
    word_count = len(words)
    for position, word_text in enumerate(words):
        word, _ = Word.objects.get_or_create(text=word_text)
        WordOccurrence.objects.create(word=word, document=document, position=position)

    # Update document word count
    document.word_count = word_count
    document.save()

    # Get top 5 words in the document
    top_words_sql = "
    SELECT w.text, COUNT(*) as count
    FROM concordance_wordoccurrence wo
    JOIN concordance_word w ON wo.word_id = w.id
    WHERE wo.document_id = :doc_id
    GROUP BY w.text
    ORDER BY count DESC
    FETCH FIRST 5 ROWS ONLY
    "
    # top_words = execute_sql(top_words_sql, {'doc_id': document.id})
    # print("Top 5 words:", top_words)
    #
    # return top_words
"""

class HomeView(TemplateView):
    template_name = 'concordance/home.html'


class DocumentListView(ListView):
    model = Document
    template_name = 'concordance/document_list.html'


class DocumentDetailView(DetailView):
    model = Document
    template_name = 'concordance/document_detail.html'


def word_list(request):
    words = Word.objects.all()
    return render(request, 'concordance/word_list.html', {'words': words})


def word_context(request, word_id):
    word = Word.objects.get(id=word_id)
    occurrences = WordOccurrence.objects.filter(word=word)
    return render(request, 'concordance/word_context.html', {'word': word, 'occurrences': occurrences})

# Add more views for other functionalities (e.g., word groups, linguistic expressions)
