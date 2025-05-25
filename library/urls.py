from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('book/add',views.add_book),
    path('author/add',views.add_author),
    path('author/get',views.get_author),
    path('book/edit',views.edit_book),
    path('author/edit',views.edit_author),
    path('order',views.assign_book),
    path('return',views.return_book),
    path('order/history',views.get_order_history),
    path('book/history',views.get_book_history)
]