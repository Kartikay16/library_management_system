from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Books,Author
from .serializer import BooksSerializer
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt



def home_page(request):
    book_query_set = Books.objects.all()
    books_dict = BooksSerializer(book_query_set,many=True)

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
def register(request):
    if(request.method == 'GET'):
        return HttpResponse("Welcome")
    if(request.method == 'POST'):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, email=email,password=password,first_name = first_name,last_name=last_name)
        user.save()
        return JsonResponse({'message':"User Inserted Succesfully"})
    

@csrf_exempt
def login_it(request):
    if(request.method == 'POST'):
        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponse("Login Succesfull")
        else:
            return HttpResponse("Login Failed")
    
    
