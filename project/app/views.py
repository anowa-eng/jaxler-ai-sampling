from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from . import serializers

# Create your views here.
def create_conversational_data(req):
    if req.method == 'POST':
        try:
            obj = ConversationalData.objects.create(
                prompt=req.POST.get('prompt'),
                response=req.POST.get('response')
            )
            serializer_data = serializers.ConversationalDataSerializer(obj).data
            return redirect('/', context={'passed': True})
        except Exception as e:
            return redirect('/', context={'error': str(e)})
    else:
        return JsonResponse({})

def home(req):
    return render(req, 'index.html')