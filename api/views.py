from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
import io
from django.http import JsonResponse

def countchar(request):
    if (request.method == 'GET'):
        json_data = request.body  # coming data
        stream = io.BytesIO(json_data)  # created io(input/output) stream
        textocheck = JSONParser().parse(stream)  # converted JSON to Python Data

        chartocount=textocheck['text']
        count={}
        for i in chartocount:
            if(i in count):
                count[i]+=1
            else:
                count[i]=1
        result = {'result': count}
        return JsonResponse(result, safe=False)
