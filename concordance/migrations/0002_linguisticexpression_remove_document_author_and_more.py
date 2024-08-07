# Generated by Django 5.0.6 on 2024-07-24 17:44

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concordance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinguisticExpression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='author',
        ),
        migrations.RemoveField(
            model_name='document',
            name='date_written',
        ),
        migrations.RemoveField(
            model_name='document',
            name='file',
        ),
        migrations.RemoveField(
            model_name='document',
            name='text_type',
        ),
        migrations.RemoveField(
            model_name='word',
            name='document',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word',
        ),
        migrations.AddField(
            model_name='document',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='document',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='word',
            name='text',
            field=models.CharField(default='default_text', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=255)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concordance.document')),
            ],
        ),
        migrations.CreateModel(
            name='WordGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('words', models.ManyToManyField(to='concordance.word')),
            ],
        ),
        migrations.CreateModel(
            name='WordOccurrence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concordance.document')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concordance.word')),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
