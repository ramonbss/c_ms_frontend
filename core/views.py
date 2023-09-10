from django.shortcuts import render
import requests
import json
# Create your views here.


def index(request):
    try:
        context = requests.get("http://127.0.0.1:8002/posts/").json()
    except requests.exceptions.ConnectionError:
        return render(request, 'index.html', context={})
    return render(request, 'index.html', context=context)
