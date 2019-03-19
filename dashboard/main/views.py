from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .fusioncharts import FusionCharts
from django.shortcuts import render
from collections import OrderedDict
import requests
import json



def homepage(request):
    return render(request, template_name='main/index.html')

def get_economic_news(request):
    resp = requests.get('https://newsapi.org/v2/everything?q=economy&pageSize=100&apiKey=' + 'b9d10b8dcf8f440d90e024091b8429a1')
    j = resp.json()
    j = j['articles']
    print("The length of articles is: " + str(len(j)))
    return render(request,'main/dashboard.html',{'output': j})

# Include the `fusioncharts.py` file that contains functions to embed the charts.

def get_hist():
    resp = requests.get('https://api.iextrading.com/1.0/stock/aapl/chart/5y')
    resp = resp.json()
    pricelist = []
    for i in resp:
        #print(str(i) + '\n')
        data = {}
        data['label'] = i['date']
        data['value'] = i['close']
        json_data = json.dumps(data)
        pricelist.append(json_data)

    return (pricelist)

# Loading Data from a Ordered Dictionary
# Example to create a column 2D chart with the chart data passed as Dictionary format.
# The `chart` method is defined to load chart data from Dictionary.

def chart(request):
    data = str(get_hist())
    print(data)
    chartObj = FusionCharts(
        'line',
        'ex1',
        '600',
        '400',
        'chart-1',
        'json',
        """{
 "chart": {
   "caption": "Price Graph",
   "yaxisname": "Price",
   "subcaption": "",
   "numbersuffix": "",
   "rotatelabels": "1",
   "setadaptiveymin": "1",
   "theme": "fusion",
   "drawAnchors" : "0",
    "bgColor": "EEEEEE,CCCCCC",
        "bgratio": "60,40",
        "bgAlpha": "70,80",
        "bgAngle": "180",
    "exportEnabled": "1",
            "useRoundEdges":"1",
 },
 "data": """+data.replace("'","")+"""
}""")

    return render(request, 'main/index.html', {'output': chartObj.render()})

def dashboard(request):
    return render(request, template_name='main/index.html')

