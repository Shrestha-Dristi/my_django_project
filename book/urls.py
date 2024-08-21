from django.urls import path
from book.views import book_list, book_detail

urlpatterns = [
    path('', book_list, name="book-list"),
    path('<id>', book_detail, name="book-detail")
]
