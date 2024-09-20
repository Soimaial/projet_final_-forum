from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from forum.models.forum_model import ForumModel
from api.serializers.forum_serializer import ForumSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets







class ForumViewSet(viewsets.ModelViewSet):
    serializer_class = ForumSerializer
    queryset = ForumModel.objects.all()
   
        