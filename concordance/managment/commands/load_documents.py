import os
from django.core.management.base import BaseCommand
from concordance.models import Document, Word, WordOccurrence


class Command(BaseCommand):
    help = 'Load documents from a specified directory'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=str, help='Directory containing text files')

    def handle(self, *args, **options):
        directory = options['directory']
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                with open(os.path.join(directory, filename), 'r') as file:
                    content = file.read()
                    document = Document.objects.create(title=filename, content=content)
                    self.process_document(document)
                    self.stdout.write(self.style.SUCCESS(f'Successfully loaded {filename}'))

    def process_document(self, document):
        words = document.content.split()
        for position, word_text in enumerate(words):
            word, _ = Word.objects.get_or_create(text=word_text.lower())
            WordOccurrence.objects.create(word=word, document=document, position=position)
