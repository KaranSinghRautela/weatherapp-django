from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
import datetime 

def get_context(location):
    
    api_result = requests.get("http://api.weatherstack.com/current?access_key=b6240781df6928d2240e462cdc039030"+"&query="+location)
    api_response = api_result.json()
    date=api_response['location']['localtime'].split()[0].replace('-',' ')
  
    day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    day = day_name[datetime.datetime.strptime(date, '%Y %m %d').weekday()]
    data = {
        'location':api_response['location']['region'],
        'cur_temp':api_response['current']['temperature'],
        'day':day,
        'date':api_response['location']['localtime'].split()[0],
        'wind_speed':api_response['current']['wind_speed'],
        'wind_dir':api_response['current']['wind_dir'],
        'desc':api_response['current']['weather_descriptions'][0],
        'lat':api_response['location']['lat'],
        'lon':api_response['location']['lon'],
        "pressure":api_response['current']['pressure'],
        "precip": api_response['current']['precip'],
        "humidity": api_response['current']['humidity'],
        "cloudcover": api_response['current']['cloudcover'],
        "feelslike": api_response['current']['feelslike'],
        "uv_index": api_response['current']['uv_index'],
        "visibility":api_response['current']['visibility']
        
    }
    return data

def home(request):
    if request.method == "POST":
        location = request.POST['location']
        data = get_context(location)
        return  render(request, 'index.html',context=data)
    else:
        location = "fetch:ip"
        data = get_context(location)
        return render(request, 'index.html',context=data)