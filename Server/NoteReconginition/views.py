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
import wave as wavvv
import base64

def NoteReconginition(request):
    if request.method == 'GET':
        output = {'keys': "d/4", 'duration': "h"}
        context = json.dumps(output)
        
        return JsonResponse(context, safe = False)
        
    if request.method == 'POST':
        print(request.content_type)
        output = {'keys': "d/4", 'duration': "h"}
        context = json.dumps(output)
        nchannels = 2
        sampwidth = 2
        framerate = 8000
        nframes = 100
        decoded_data = base64.b64decode(request.body, ' /')

        pcmfile = "temp.file"
        wavfile = "output.wav"
        with open(pcmfile, 'wb') as pcm:
            pcm.write(decoded_data)
        with open(pcmfile, 'rb') as pcm:
            pcmdata = pcm.read()
        with wavvv.open(wavfile, 'wb') as wav:
            wav.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
            wav.writeframes(pcmdata)

        note_dict = {
            "C/3" : 13081,
            "C#/3" : 13859,
            "D/3" : 14683,
            "D#/3" : 15556,
            "E/3" : 16481,
            "F/3" : 17461,
            "F#/3" : 18500,
            "G/3" : 19600,
            "G#/3" : 20765,
            "A/3" : 22000,
            "A#/3" : 23308,
            "B/3" : 24694,
            "C/4" : 26163,
            "C#/4" : 27718,
            "D/4" : 29366,
            "D#/4" : 31113,
            "E/4" : 32963,
            "F/4" : 34923,
            "F#/4" : 36999,
            "G/4" : 39200,
            "G#/4" : 41530,
            "A/4" : 44000,
            "A#/4" : 46616,
            "B/4" : 49388,
            "C/5" : 52325,
            "C#/5" : 55436,
            "D/5" : 58733,
            "D#/5" : 62225,
            "E/5" : 65925,
            "F/5" : 69845,
            "F#/5" : 73999,
            "G/5" : 783991,
        }


        # In[17]:


        import parselmouth
        import math
        import os
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        import wave, struct
        from io import BytesIO
        import tempfile
        import scipy.signal as sg
        from scipy.signal import butter, lfilter


        # In[18]:


        log_dict = note_dict.copy()
        for key in log_dict:    
            log_dict[key] = math.log(log_dict[key])

        print(log_dict)




        from scipy.io import wavfile
        from scipy import signal
        import numpy as np

        sr, x = wavfile.read('Demo 2.wav')      # 16-bit mono 44.1 khz

        b = signal.firwin(31, cutoff=1000, fs=sr, pass_zero=False)

        x = signal.lfilter(b, [1.0], x)
        wavfile.write('test2.wav', sr, x.astype(np.int16))


        # In[9]:


        # sns.set() # Use seaborn's default style to make attractive graphs

        # Plot nice figures using Python's "standard" matplotlib library
        snd = parselmouth.Sound("output.wav")
        plt.figure()
        plt.plot(snd.xs(), snd.values.T)
        plt.xlim([snd.xmin, snd.xmax])
        plt.xlabel("time [s]")
        plt.ylabel("amplitude")
        plt.show() # or plt.savefig("sound.png"), or plt.savefig("sound.pdf")


        # In[10]:


        snd = parselmouth.Sound("test2.wav")
        plt.figure()
        plt.plot(snd.xs(), snd.values.T)
        plt.xlim([snd.xmin, snd.xmax])
        plt.xlabel("time [s]")
        plt.ylabel("amplitude")
        #plt.show() # or plt.savefig("sound.png"), or plt.savefig("sound.pdf")


        # In[11]:


        def draw_spectrogram(spectrogram, dynamic_range=70):
            X, Y = spectrogram.x_grid(), spectrogram.y_grid()
            sg_db = spectrogram.values
        #10 * np.log10(spectrogram.values)
            plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - dynamic_range, cmap='afmhot')
            plt.ylim([spectrogram.ymin, spectrogram.ymax])
            plt.xlabel("time [s]")
            plt.ylabel("frequency [Hz]")

        def draw_pitch(pitch):
            # Extract selected pitch contour, and
            # replace unvoiced samples by NaN to not plot
            pitch_values = pitch.selected_array['frequency']
            pitch_values[pitch_values==0] = np.nan
            plt.plot(pitch.xs(), pitch_values, 'o', markersize=5, color='w')
            plt.plot(pitch.xs(), pitch_values, 'o', markersize=2)
            plt.grid(False)
            plt.ylim(0, pitch.ceiling)
            plt.ylabel("fundamental frequency [Hz]")

            
        ##time step
        time_step = 0.05
        ##--------

        pre_emphasized_snd = snd.copy()
        pre_emphasized_snd.pre_emphasize()
        spectrogram = pre_emphasized_snd.to_spectrogram(window_length=time_step, maximum_frequency=1000)

        pitch = snd.to_pitch(time_step=time_step)

        pitch = parselmouth.Pitch.kill_octave_jumps(pitch)
        print(pitch)

        plt.figure()
        draw_spectrogram(spectrogram)

        draw_pitch(pitch)
        plt.xlim([snd.xmin, snd.xmax])

        #plt.show() # or plt.savefig("spectrogram.pdf")

        n_frames = parselmouth.Pitch.get_number_of_frames(pitch)


        # In[19]:


        n_frames = parselmouth.Pitch.get_number_of_frames(pitch)
        print("frames::" , n_frames)

        def match_hz_to_note(current_freq):
            last = log_dict["C/3"]
            last_note = "C/3"
            log_hz = math.log(current_freq * 100)
            if(log_hz < last):
                return "R"
            for note, freq in log_dict.items():    
                if(log_hz < freq):
                    if(log_hz - last > freq - log_hz):
                        return note
                    else:
                        return last_note
                last_note = note
                last = freq
            
        def find_max_count(d1):
            v=list(d1.values())
            k=list(d1.keys())
            return k[v.index(max(v))]

        note_count = dict()

        for i in range(1,n_frames):
            current_hz = parselmouth.Pitch.get_frame(pitch, i).as_array()[0][0]
            if(current_hz != 0):
                current_note = match_hz_to_note(current_hz)
                if(current_note in note_count):
                    note_count[current_note] += 1
                else:
                    note_count[current_note] = 1

        max_note = find_max_count(note_count)
        if(note_count[max_note] < n_frames * time_step / 2):
            result = "R"
        else:
            result = max_note
            
        print(result)

        output = {'update':  1, 'keys': result}
        context = json.dumps(output)
        print(context)
        
        return JsonResponse(context, safe = False)
