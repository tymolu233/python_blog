from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
import json


class DecoderMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method != 'GET' and  request.META['CONTENT_TYPE'] == 'application/json':
            data = json.loads(request.body)
            request.data = data

