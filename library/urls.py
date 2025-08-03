from django.urls import path
from .views import books_list, book_detail, base


app_name = 'library'

urlpatterns = [
    path('books_list/', books_list, name='books_list'),
    path("book_detail/<int:book_id>", book_detail, name='book_detail'),
    path('base/', base, name='base'),
]