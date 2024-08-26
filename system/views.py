from django.shortcuts import render
import requests

# Create your views here.

def homepage(request):
    return render(request,'index.html')

def fetch_data(request):
    url = "https://api.waziup.io/api/v2/devices/kofikofi"
    response = requests.get(url)


    data = response.json()
    sensors = data['sensors']

    # humidity
    humidity = sensors[0]['quantity_kind'] #1st data
    sensor_values = sensors[0]['value']

    hum_value = sensor_values['value'] #2nd data
    hum_date = sensor_values['timestamp'] #3rd data

    # temprature

    temprature = sensors[1]['quantity_kind'] #1st data
    sensor_values = sensors[1]['value']

    temp_value = sensor_values['value'] #2nd data
    temp_date = sensor_values['timestamp'] #3rd data

    # air quality
    Air = sensors[2]['quantity_kind'] #1st data
    sensor_values = sensors[2]['value']

    Air_value = sensor_values['value'] #2nd data
    Air_date = sensor_values['timestamp'] #3rd data




    #  Air qaulity
    context1 = {
    'Air':Air,
    'Air_value':Air_value,
    'Air_date':Air_date,
    }

     # noise level

    #  TEmprature
    context3 = {
    'temp':temprature,
    'temp_value':temp_value,
    'temp_date':temp_date,
    }

    # humidity
    context4 = {
    'humidity':humidity,
    'hum_value':hum_value,
    'hum_date':hum_date,
    }



    context={**context1,**context3,**context4}

    return render(request, 'sensor_data.html', context)
