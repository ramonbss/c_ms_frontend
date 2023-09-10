from django.shortcuts import render
import requests
import json
# Create your views here.


def index(request):
    context = requests.get("http://127.0.0.1:8002/posts/").json()
    return render(request, 'index.html', context=context)
