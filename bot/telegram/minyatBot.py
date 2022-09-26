import re
import requests
import json
import datetime
update = 'getUpdates'

class Telegram():
    def __init__(self, token):
        self.token = token
        
    def getUrl(self,urlChildren):
        url = "https://api.telegram.org/bot{}/{}".format(self.token,urlChildren)
        return url
    
    def getIdGroup(self):
        url = self.getUrl(update)
        r = requests.get(url)
        result = r.json()
        return json.dumps(result)
    
    def sendText(self, **kwargs):
        id = kwargs.pop('id', None)
        text = kwargs.pop('text', None)
        markdown = kwargs.pop('markdown', None)

        if id is None or text is None:
            return False
        urlChildren ='sendMessage?chat_id={}&text={}'.format(id, text)
        if markdown is True:
            urlChildren = urlChildren+'&parse_mode=markdown'

        url = self.getUrl(urlChildren)
        




        r = requests.get(url)
        result = r.json()
        return json.dumps(result)
    

    
