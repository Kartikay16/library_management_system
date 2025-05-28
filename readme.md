# 📚 Library Management System

A full-stack Library Management System built with **Django**, **React.js**, and **MySQL** that enables efficient book inventory management, user handling, and seamless book issuance/return tracking.

---

## 🚀 Features

- 🔐 **User Authentication & Role Management**
  - User registration, login, and logout
  - Role-based permissions: Reader vs Librarian

- 📚 **Book & Author Management**
  - Add, edit, and view books and authors
  - Filter books by author, genre, and availability

- 🔄 **Book Issuing & Returning**
  - Order (issue) and return books
  - Track user-specific borrowing history
  - View book-specific issue history (Librarian only)

- 🛠️ **Admin Dashboard**
  - Django Admin panel

- 🌐 **RESTful APIs**
  - 15+ endpoints supporting CRUD operations and data retrieval

---

## 🛠️ Tech Stack

| Layer           | Technology                     |
|------------------|-------------------------------|
| Frontend         | React.js, Bootstrap           |
| Backend          | Django, Django REST Framework |
| Database         | MySQL                         |
| Authentication   | Django built-in auth system   |
| Admin Panel      | Django Admin                  |


API Endpoints:

GET Homepage - Display all books, along with its authors and availability. Accept filters like filter by author, genre, availability
POST book/add - Add a new book to database (Only accessible to Librarians)
POST accounts/register - Create a new account
POST accounts/login - Login
GET accounts/logout - Logout
POST author/add -  Add a new author to the database (Only accessible to Librarians)
GET author/get - Get all authors in database
POST book/edit - Edit a book details (Only accessible to Librarians)
POST author/edit - Edit a author details (Only accessible to Librarians)
POST /order - Order a book
POST /return - Return a ordered book
GET /order/history - A logged in user can request to see its order history
GET /book/history - Librarian can see the order history of a book (Only accessible to Librarians)


## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kartikay16/library_management_system


