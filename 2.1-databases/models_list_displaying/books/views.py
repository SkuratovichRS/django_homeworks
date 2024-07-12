from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.all()
    context = {"books": books_objects}
    return render(request, template, context)


def pub_date_view(request, pub_date):
    template = 'books/books_pub_date.html'
    book_object = Book.objects.get(pub_date=pub_date)
    books_objects = Book.objects.all().order_by('pub_date')
    paginator = Paginator(books_objects, 1)
    current_page_number = [index + 1 for index, data in enumerate(books_objects)
                           if data.pub_date == book_object.pub_date][0]
    page = paginator.get_page(current_page_number)
    previous_page_number = page.previous_page_number() if page.has_previous() else None
    next_page_number = page.next_page_number() if page.has_next() else None

    previous_book = books_objects[previous_page_number - 1] if previous_page_number else None
    next_book = books_objects[next_page_number - 1] if next_page_number else None

    context = {
        "book": book_object,
        "page": page,
        "previous_book": previous_book,
        "next_book": next_book,
    }

    return render(request, template, context)
