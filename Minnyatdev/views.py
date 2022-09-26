from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
    response = HttpResponse()
    urls = {
        'admin': '/admin',
        'api': '/api',
        'bot': '/bot',
    }
    response.writelines(json.dumps(urls))
    return response



