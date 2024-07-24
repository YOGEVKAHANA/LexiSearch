from django.urls import path
from . import views

urlpatterns = [
    path('', views.DocumentListView.as_view(), name='document_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('document/<int:pk>/', views.DocumentDetailView.as_view(), name='document_detail'),
    path('words/', views.word_list, name='word_list'),
    path('word/<int:word_id>/context/', views.word_context, name='word_context'),
    # Add more URL patterns for other views
]
