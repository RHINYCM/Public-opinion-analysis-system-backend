import requests
import json

def get_text():
    news = "people said china is a great place.everyone say china is a great place"

    apiurl = "http://10.201.104.231:5000/api"

    response = requests.post(url=apiurl,data={'news':news})
    resultlist = json.loads(response.text)

    for result in resultlist:
        print(result["ARG0"]+"****"+result["PRED"]+"****"+result["ARG1"])

    #print(response.text)
    return response.text