from django.shortcuts import render
from book.models import Book

# Create your views here.
def book_list(request):
    book = Book.objects.all()
    context = {
        "book":book
    }
    return render(request, 'book/index.html', context)

def book_detail(request, id):
    book = Book.objects.get(id=id)
    context = {
        "book":book
    }
    return render(request, 'book/details.html', context)