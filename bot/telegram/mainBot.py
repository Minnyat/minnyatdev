import re
from django.http import HttpResponse,HttpResponseBadRequest
from .minyatBot import Telegram
import requests
import urllib

tokenSpoUpgradeBot = "5480809534:AAF8btQBrErseJ0Bu4ywOtvEScrvuKCsQt0"
idGroupsendLog = '-1001558578200'
def getChatId(request):
    response = HttpResponse()
    Bot = Telegram(tokenSpoUpgradeBot)
    response.writelines(Bot.getIdGroup())
    return response
def sendLog(request):
    response = HttpResponse()
    textRequest = ''
    if request.method == 'POST':
        try:
            for key in request.POST:
                print(str(key).title())
                textRequest += '*{}*:  {} \n '.format(key.title(), request.POST[key])
        except Exception:
            textRequest = "None"
    if request.method == 'GET':
        try:
            for key in request.GET:
                print(str(key).title())
                textRequest += '*{}*:  {} \n '.format(key.title(), request.GET[key])
        except Exception:
            textRequest = "None"
    if textRequest != '':
        Bot = Telegram(tokenSpoUpgradeBot)

        timeZone = requests.get("http://worldtimeapi.org/api/timezone/Asia/Ho_Chi_Minh").json()
        textSend = '{} \n Log: \n {}'.format(timeZone['datetime'],textRequest)
        textSend = urllib.parse.quote(textSend, safe='')

        result = Bot.sendText(id = idGroupsendLog, 
            text = textSend, 
            markdown = True
        )
    else:
        textRequest = "None"
    response.writelines(textRequest)
    return response


if __name__ == "__main__":
    sendLog('sdf')
