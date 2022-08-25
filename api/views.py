from django.shortcuts import render

# Create your views here.

import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    response = HttpResponse()
    response.writelines("test")
    return response

def binCheck(request):
    response = HttpResponse()
    dataDict = request.GET
    try:
        bin = dataDict['bin']
        binCheckUrl = "https://lookup.binlist.net/"
        res = requests.get(binCheckUrl + bin )
        if res.status_code == 200:
            response.writelines(res.text)
            return response

    except:
        bin = ''
    
    response.writelines(bin)
    return response



