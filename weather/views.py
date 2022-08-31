from django.shortcuts import render
import requests
import json

def index(request):
    app_id = '791a1e4a216bb844c0bc92e88d5b9609'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + app_id
    city = 'Minsk'
    res = requests.get(url.format(city))
    main = json.loads(res.text)['main']
    temp = main['temp']
    return render(request, 'weather/index.html', {'res':res, 'main': main, 'temp':temp})

def weather(request):
    return render(request, 'weather/weather.html')
# Create your views here.
