from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django import forms
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import matplotlib.pyplot as plt
from PIL import Image
import json
import random
import os

label_list = ['asymmetricLength', 'asymmetricNeck', 'balloonSleeve', 'bardotNeck', 'bellSleeve', 'capSleeve', 'capeSleeve', 'coldshoulder', 'coldshoulderSleeve', 'collarNeck', 'cowlNeck', 'cropLength', 'dolmanSleeve', 'fittedCut', 'flaredCut', 'halterNeck', 'highlowLength', 'jewelNeck', 'kimonoSleeve', 'kneeLength', 'longLength', 'longSleeve', 'maxiLength', 'mermaidCut', 'midLength', 'midSleeve', 'midiLength', 'offtheshoulderSleeve', 'oneshoulderSleeve', 'plungingNeck', 'raglanSleeve', 'roundNeck', 'ruffleSleeve', 'shortLength', 'shortSleeve', 'sleeveless', 'spaghettistrapSleeve', 'splitNeck', 'squareNeck', 'straightCut', 'straplessSleeve', 'surpliceNeck', 'sweethearNeck', 'sweetheartNeck', 'turtleNeck', 'vNeck']


label_type = {'Neck': ['jewelNeck', 'roundNeck', 'turtleNeck', 'bardotNeck', 'collarNeck', 'vNeck', 'plungingNeck', 'surpliceNeck', 'halterNeck',
                       'squareNeck', 'sweetheartNeck', 'asymmetricNeck', 'splitNeck', 'cowlNeck'],
              'SleeveStyle': ['oneshoulderSleeve', 'offtheshoulderSleeve', 'Coldshoulder', 'bellSleeve', 'raglanSleeve', 'dolmanSleeve', 'balloonSleeve', 'capeSleeve', 'kimonoSleeve', 'ruffleSleeve'],
              'Cut': ['fittedCut', 'straightCut', 'flaredCut', 'mermaidCut'],
              'SleeveLength': ['longSleeve', 'midSleeve', 'shortSleeve', 'capSleeve', 'sleeveless', 'spaghettistrapSleeve', 'straplessSleeve'],
              'Length': ['shortLength', 'kneeLength', 'midiLength', 'maxiLength', 'asymmetricLength', 'highlowLength', 'cropLength', 'midLength', 'longLength']}        
        
def process_image(request):

    if request.method == 'POST':
        #run requested pic in the NN, retrieve boolean list of labels

        print(request.FILES)
        
        img_name = request.FILES.get('image')
        fs = FileSystemStorage()
        filename = fs.save(img_name.name, img_name)
        uploaded_file_url = fs.url(filename)
        uploaded_file_url = uploaded_file_url[1:]

        uploaded_file_url = uploaded_file_url.replace('/', "\\")
        
        cur_dir = os.getcwd()
        print(os.path.join(cur_dir, uploaded_file_url))
        img = Image.open(os.path.join(cur_dir ,uploaded_file_url))
        
        print(img.size)
        
        #plt.imshow(img)
        #plt.show()
        
        label_bool = [0] * len(label_list)

        labels = []
        
        for i in range(0, len(label_list)-1):
            if label_bool[i] == 1:
                labels.append(label_list[i])
   
        output = {}
        #for i in labels:
        #    for j in label_type:
        #        if i in label_type[j]:
        #            output[j] = i
                       
        output = {'Neck': 'roundNeck', 'SleeveStyle': 'oneshoulderSleeve', 'Cut': 'flaredCut', 'SleeveLength': 'longSleeve', 'Length': 'maxiLength'}
        
        print(output)
        context = json.dumps(output)
        #print(context)
        
        return JsonResponse(context, safe = False)
