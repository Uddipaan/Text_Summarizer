from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
from . text_service import *
# Create your views here.


def conv(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


def summary(request):
    url = 'http://159.65.156.192/api/v1/news'
    headers = {'Authorization': 'insert_token_here'}
    response = requests.get(url, headers)
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
    # d = {}
    # d = conv(z, d)
    # str1 = str(d).replace("\'", "\"")
    # parsed = json.loads(str1)
    # json_str = json.dumps(parsed, sort_keys=True)

    return JsonResponse(str(z), safe=False)

    # return render(request, 'form.html', {
    #                 'news': z
    #
    #              })

