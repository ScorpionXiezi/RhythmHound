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
import wave

def NoteReconginition(request):
    if request.method == 'POST':
        print(request.content_type)

        output = {'update':  1, 'keys': "d/4"}
        context = json.dumps(output)
        print(context)
        nchannels = 2
        sampwidth = 2
        framerate = 8000
        nframes = 100
        
        name = 'output.wav'
        audio = wave.open(name, 'wb')
        audio.setnchannels(nchannels)
        audio.setsampwidth(sampwidth)
        audio.setframerate(framerate)
        audio.setnframes(nframes)

        blob = request.body # such as `blob.read()`
        audio.writeframes(blob)

        return JsonResponse(context, safe = False)

        fs = FileSystemStorage()
        filename = fs.save("audio_clip", request.body)
        uploaded_file_url = fs.url(filename)
        uploaded_file_url = uploaded_file_url[1:]

        uploaded_file_url = uploaded_file_url.replace('/', "\\")

        return JsonResponse(context, safe = False)
        cur_dir = os.getcwd()
        print(os.path.join(cur_dir, uploaded_file_url))

        output = {'update':  1, 'keys': "d/4"}
        context = json.dumps(output)
        print(context)
        
        return JsonResponse(context, safe = False)
