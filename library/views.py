from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Books,Author
from .serializer import BooksSerializer
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt



def home_page(request):
    book_query_set = Books.objects.all()
    resp = []

    for book in book_query_set:
        book_entry = {}
        book_entry['name'] = book.name
        book_entry['genre'] = book.genre
        book_entry['is_available'] = book.is_available
        authors_list = []
        print("Book: " + book.name)
        for author in  book.author_set.all():
            authors_list.append(author.first_name +" " + author.last_name)
        print("---------------------------------")
        book_entry['authors'] = authors_list
        resp.append(book_entry)

    print("Called Homepage succesfully")
    return JsonResponse(resp,safe=False)

@csrf_exempt
def add_book(request):
    active_user = request.user
    qs = active_user.groups.all()
    for group in qs:
        if(group.name == "Librarian"):
            print("API Access Permission granted")
            book_name = request.POST.get('name')
            genre = request.POST.get('genre')
            is_available = request.POST.get('is_available')
            book = Books.objects.create(name=book_name, genre=genre, is_available= is_available)
            return HttpResponse("Success... Book added")
        
    return HttpResponse("You dont have the permission to access this API. Contact admin for more details")
    
    
