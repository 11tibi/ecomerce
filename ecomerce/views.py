from django.shortcuts import render, redirect
from django.http import Http404


def index(request):
    return redirect('index')
