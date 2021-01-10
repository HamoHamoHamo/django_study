from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Post

class PublicPostIndexView(generic.ListView):
    model = Post