from http.client import HTTPSConnection
from time import sleep as wait
def send(text):
    a=0
    while a!=200:
        cnx=HTTPSConnection("discordapp.com")
        url="/api/channels/561927065658458142/messages"
        body='{"content":"'+text+'","tts":false}'
        headers={}
        headers["Authorization"]="Bot MzU4NTc4OTc4OTMzNDQwNTEy.XNbA2A.8huvoJO6y8Vq8PqtZh0dZQd1fnU"
        headers["Content-Type"]="application/json"
        headers["Content-Lenght"]=str(len(body))
        headers["Host"]="discordapp.com"
        cnx.request("POST",url,body,headers)
        resp=cnx.getresponse()
        a=resp.getcode()
        if a!=200:
            wait(1)
        
