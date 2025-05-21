from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Books,Author,Order
from .serializer import BooksSerializer
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
import json

def home_page(request):
    book_query_set = Books.objects.all()
    filter_genre = request.GET.get('genre')
    if(filter_genre != None):
        book_query_set = book_query_set.filter(genre = filter_genre)
    
    filter_availability = request.GET.get('Available')
    if(filter_availability != None):
        book_query_set = book_query_set.filter(is_available = filter_availability)

    filter_author = request.GET.get('author_id')
    if(filter_author != None):
        book_query_set = book_query_set.filter(author__id = filter_author)


    resp = []

    for book in book_query_set:
        book_entry = {}
        book_entry['name'] = book.name
        book_entry['genre'] = book.genre
        book_entry['is_available'] = book.is_available
        authors_list = []
        print("Book: " + book.name)
        for author in  book.author.all():
            authors_list.append(author.first_name +" " + author.last_name)
        print("---------------------------------")
        book_entry['authors'] = authors_list
        resp.append(book_entry)

    print("Called Homepage succesfully")
    return JsonResponse(resp,safe=False)


# API to get all authors in database
def get_author(request):
    resp = []
    author_query_set = Author.objects.all()
    for author in author_query_set:
        author_entry = {}
        author_entry['id'] = author.id
        author_entry['name'] = author.first_name +" "+ author.last_name
        resp.append(author_entry)

    print("Fetched all authors succesfully")
    return JsonResponse(resp,safe=False)
    

# API to add a book to database
@csrf_exempt
def add_book(request):
    active_user = request.user
    qs = active_user.groups.all()
    for group in qs:
        if(group.name == "Librarian"):
            print("API Access Permission granted")
            book_name = request.POST.get('name')
            genre = request.POST.get('genre')
            author_id = request.POST.get('author_id')
            is_available = request.POST.get('is_available')

            book = Books.objects.create(name=book_name, genre=genre, is_available= is_available)
            print(author_id)
            author = Author.objects.get(id = author_id)
            book.author.add(author)

            return HttpResponse("Success... Book added")
    return HttpResponse("You dont have the permission to access this API. Contact admin for more details")

@csrf_exempt
def edit_book(request):
    active_user = request.user
    if(active_user.groups.all().filter(name = "librarian").exists()):
        book_id = request.POST.get('book_id')
        print(book_id)
        book = Books.objects.get(id = book_id)

        if(request.POST.get('name') != None):
            book.name = request.POST.get('name')

        if(request.POST.get('genre') != None):
            book.genre = request.POST.get('genre') 
        
        if(request.POST.get('is_available') != None):
            book.is_available = request.POST.get('is_available')

        if(request.POST.get('add_authors') != None):
            authors_to_be_added_str = request.POST.get('add_authors')
            authors_to_be_added = json.loads(authors_to_be_added_str)
            book.author.add(*authors_to_be_added)

        if (request.POST.get('remove_authors') != None):
            authors_to_be_removed_str = request.POST.get('remove_authors')
            authors_to_be_removed = json.loads(authors_to_be_removed_str)
            book.author.remove(*authors_to_be_removed)
            

        book.save()
        return HttpResponse("Book updated")
           
    else:
        return HttpResponse("Access denied...Contact admin")

@csrf_exempt
def edit_author(request):
    active_user = request.user
    if(active_user.groups.all().filter(name = "Librarian").exists()):
        author = Author.objects.get(id = request.POST.get('author_id'))
        if(request.POST.get('first_name') != None):
            author.first_name = request.POST.get('first_name')

        if(request.POST.get('last_name') != None):
            author.last_name = request.POST.get('last_name')
        author.save()
        return HttpResponse("Author updated succesfully")
    else:
        return HttpResponse("403 Forbidden to access the API. Contact admin")
        




@csrf_exempt
def add_author(request):
    if(request.user.groups.all().filter(name = 'librarian').exists()):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Author.objects.create(first_name=first_name,last_name=last_name)
        return HttpResponse("Author Added Succesfully")
    else: 
        return HttpResponse("Forbidden..Contact Admin")
    

@csrf_exempt
def assign_book(request):

    book_to_be_assigned  = request.POST.get("book_id")
    book = Books.objects.get(id = book_to_be_assigned)
    user_booking = request.POST.get("user_id")
    user = User.objects.get(id = user_booking)
    Order.objects.create(book = book , user = user)
    return HttpResponse("Book issued to requested user succesfully")
    
    
    
