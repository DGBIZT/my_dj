from django.urls import path
from .views import BooksListView, BookUpdateView, BookCreateView, BookDeleteView, BookDetailView


app_name = 'library'

urlpatterns = [
    path('books/', BooksListView.as_view(), name='books_list'),
    path('book/new/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),

]