from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.views import View
import json
import logging
import os
import requests
from django.views.decorators.csrf import csrf_protect
# Create your views here.

class ApiView(View):
    @csrf_protect
    def post(self, request):
        # http://api.openweathermap.org/data/2.5/weather?q=Tokyo&APPID=af316dd0232f9ef28ddab86e99588e0c
        name = request.POST.get('name')
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": name,
            'APPID': settings.API_KEY_WEATHER
        }
        try:
            response = requests.get(
                url, params
            )
        except Exception as e:
            data = {
                'error': True,
                'message': 'The call api have issuse {}'.format(str(e)),
                'resp' : None
            }
            return HttpResponse(json.dumps(data))
        
        try:
            json_data = json.loads(response.text)
        except Exception as e:
            data = {
                'error': True,
                'message': str(e),
                'resp' : None
            }

            return HttpResponse(json.dumps(data))
        
        data = {
            'error': False,
            'message': 'Successfully',
            'resp': json_data
        }
        return HttpResponse(json.dumps(data))