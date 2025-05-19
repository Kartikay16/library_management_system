from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('book/add',views.add_book),
    path('author/add',views.add_author),
]