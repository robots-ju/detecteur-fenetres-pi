from http.client import HTTPConnection
def send(fnt,id,state):
    cnx=HTTPConnection("192.168.2.98:8080")
    url="/api/windows"
    body='{"id":'+str(id)+',"name":"'+fnt+'","state":"'+state+'"}'
    print(body)
    headers={}
    headers["Content-Type"]="application/json"
    cnx.request("POST",url,body,headers)
    resp=cnx.getresponse()
    a=resp.read()
    if a!=b'"Succesful"':
        raise ConnectionError(str(type(a))+" "+str(a))