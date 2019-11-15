from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.views import View
import json
import logging
import os
import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,ParseError
# Create your views here.

class ApiView(generics.ListCreateAPIView):
    def post(self, request):
        # http://api.openweathermap.org/data/2.5/weather?q=Tokyo&APPID=af316dd0232f9ef28ddab86e99588e0c
        #https://openweathermap.org/api
    
        name = request.data['name']
    
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
            print(str(e))
            data = {
                'error': True,
                'message': 'The call api have issuse {}'.format(str(e)),
                'resp' : None
            }
            return Response(data)
        
        try:
            json_data = json.loads(response.text)
        except Exception as e:
            print(str(e))
            data = {
                'error': True,
                'message': str(e),
                'resp' : None
            }

            return Response(data)
        data = {
            'error': False,
            'message': 'Successfully',
            'resp': json_data
        }
        return Response(data)