from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Book, Author, Review
from registration_app.models import User

def index(request):
    context = {
        "user": User.objects.get(id = request.session['user_id']),
        "book": Book.objects.all(),
    }
    return render(request, "books_home.html", context)