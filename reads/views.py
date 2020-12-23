from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

def index(request):
    return render(request, "books_home.html")