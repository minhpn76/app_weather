from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.views import View
import json
import logging
import os
import requests
# Create your views here.

class TemplateView(View):
    def get(self, request):
        return render(request, 'home.html')
        # return HttpResponse(json.dumps({"ok": "Home"}))