from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
import json
from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.core.files.base import ContentFile



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getSong(request):
    with open("dejavu.cnf.SAMPLE") as f:
        config = json.load(f)
    djv = Dejavu(config)

    results = djv.recognize(FileRecognizer, "mp3/Time.mp3")
    print(results)

    song = {
        'response': {
            results
        },
    }

    return Response(song)

@csrf_exempt
def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        # Save the file to the desired location
        with open('media/audio.mp3', 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)
        return HttpResponse(status=201)
    return HttpResponse(status=400)
