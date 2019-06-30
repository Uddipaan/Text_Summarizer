from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
from . text_service import *
# Create your views here.


def Convert(tup, di):
    di = dict(tup)
    return di


def summary(request):
    url1 = 'http://159.65.156.192/api/v1/phone/login'
    header1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    body1 = {'phone': '9706208886', 'deviceToken': 'adfsgfdgsfaafsf'}
    response1 = requests.post(url1, headers=header1, data=body1)
    rs = response1.json()

    test = rs['data']
    token = test.get('token')

    url = 'http://159.65.156.192/api/v1/news'
    header = {'Authorization': 'JWT ' + token}
    response = requests.get(url, headers=header)
    news = response.json()
    id_news_item = []
    desc = []
    res = []
    for items in news['data']:
        for n in items['news'].items():
            if n[0] == "_id":
                id_news_item.append(n[1])
            if n[0] == "fullDescription":
                desc.append(n[1])
                result_summary = summarizer(n[1])
                res.append(result_summary)

    # z = list(zip(id_news_item, res, desc))
    z = list(zip(id_news_item, res))
    dictionary = {}
    test = Convert(z, dictionary)
    # d = {}
    # d = conv(z, d)
    # str1 = str(d).replace("\'", "\"")
    # parsed = json.loads(str1)
    # json_str = json.dumps(parsed, sort_keys=True)

    # return JsonResponse(str(z), safe=False, json_dumps_params={'ensure_ascii': False})
    return JsonResponse(test, safe=False, json_dumps_params={'ensure_ascii': False})

    # return render(request, 'form.html', {
    #                 'news': z
    #
    #              })

