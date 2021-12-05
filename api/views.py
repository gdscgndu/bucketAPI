from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
import io
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
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

@csrf_exempt
def countwords(request):
    if(request.method=="GET"):
        json_data = request.body  # coming data
        stream = io.BytesIO(json_data)  # created io(input/output) stream
        textocheck = JSONParser().parse(stream)  # converted JSON to Python Data

        txt = textocheck['text']
        count=len(txt.split(' '))
        result = {'totalwords': count}
        return JsonResponse(result, safe=False)

@csrf_exempt
def viewInstaProfile(request, username):    
    if(request.method=="GET"):        
        import instaloader
        loader = instaloader.Instaloader()
        try:   
            profile = instaloader.Profile.from_username(loader.context,username)                 
            # returns link to the profile picture        
            profile_pic = profile.profile_pic_url
            return JsonResponse({'status':'success', 'url':profile_pic}, safe=False)
        except:
            return JsonResponse({'status':'failed', 'url':"null"}, safe=False)
