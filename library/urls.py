from django.urls import path
from .views import BooksListView, BookUpdateView, BookCreateView, BookDeleteView, BookDetailView, AuthorCreateView, AuthorListView, AuthorUpdateView, AuthorDeleteView, AuthorDetailView

app_name = 'library'

urlpatterns = [

    path('authors/', AuthorListView.as_view(), name='authors_list'),
    path('author/new/', AuthorCreateView.as_view(), name='author_create'),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),

    path('books/', BooksListView.as_view(), name='books_list'),
    path('book/new/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),

]