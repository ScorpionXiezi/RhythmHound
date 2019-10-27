from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django import forms
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import matplotlib.pyplot as plt
import json
import random
import os

def NoteReconginition(request):
    if request.method == 'POST':
        
        audio_file = request.FILES.get('audio')
        print(audio_file)

        fs = FileSystemStorage()
        filename = fs.save(audio_name.name, audio_name)
        uploaded_file_url = fs.url(filename)
        uploaded_file_url = uploaded_file_url[1:]

        uploaded_file_url = uploaded_file_url.replace('/', "\\")
        
        cur_dir = os.getcwd()
        print(os.path.join(cur_dir, uploaded_file_url))

        output = {'update':  1, 'keys': "d/4"}
        context = json.dumps(output)
        print(context)
        
        return JsonResponse(context, safe = False)
