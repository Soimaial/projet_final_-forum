from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from message.models.message_model import MessageModel
from api.serializers.message_serializer import MessageSerializer 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets






class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = MessageModel.objects.all()
   
        