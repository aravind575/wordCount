from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    all = request.GET['all']
    words = all.split()

    return render(request, 'count.html', {'count':len(words), 'words':words})
