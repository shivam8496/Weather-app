from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        jason_data=json.loads(res)
        data={
            "city":city,
            "country_code" : str(jason_data['sys']['country']),
            "coordinate": str(jason_data['coord']['lon'])+"  "+str(jason_data['coord']['lat']),
            "temp": str(jason_data['main']['temp'])+" K",
            "pressure": str(jason_data['main']['pressure']+" P"),
            "humidity" : str(jason_data['main']['humidity'])
        }
    else:
        city=' '
   
    return render(request,"index.html",data)