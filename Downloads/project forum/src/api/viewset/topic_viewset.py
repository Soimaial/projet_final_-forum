from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from topic.models.topic_model import TopicModel
from api.serializers.topic_serializer import TopicSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets







class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = TopicModel.objects.all()
    
        