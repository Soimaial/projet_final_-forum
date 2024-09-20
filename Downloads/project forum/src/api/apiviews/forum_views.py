from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from forum.models.forum_model  import ForumModel
from api.serializers.forum_serializer import ForumSerializer




@csrf_exempt
def forum_list(request):
    if request.method == "GET":
       forum = ForumModel.objects.all()
       serializer = ForumSerializer( forum , many=True)
       return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
         data = JSONParser().parse(request)
         serializer = ForumSerializer(data=data)
         if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data, status=201)
         return JsonResponse(serializer.errors, status=201)
    
@csrf_exempt
def student_detail(request, id):
    try:
        forum  = ForumModel.objects.get(id=id)
    except ForumModel.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ForumSerializer(forum)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data =  JSONParser().parse(request)
        serializer = ForumSerializer(forum , data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.errors, status=400)
        
    
