from django.shortcuts import render
from django.http import HttpResponse
from . import telegram as telegramBot
from .config import *
# Create your views here.

def index(request):
    response = HttpResponse()
    response.writelines("main web")
    return response


def telegram(request):
    requestPath = str(request.path)
    for i in range(len(urlsTelegram)):
        if urlsTelegram[i] in requestPath:
            return acctionsTelegram[i](request)
    return HttpResponse.writelines(None)


