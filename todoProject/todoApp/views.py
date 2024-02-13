from .serializers import ToDoSerializer
from .models import ToDoTask
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json

# Create your views here.

class TodoTaskView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if request.method == 'GET':
            if pk==None:
                data = ToDoTask.objects.all().order_by('-id')
                serializer = ToDoSerializer(data, many=True)
                return Response(serializer.data) 
            else:
                task=ToDoTask.objects.filter(pk=pk)
                serializer = ToDoSerializer(task, many=True)
                return Response(serializer.data)
        else:
            response_data={
                    "state":"ERROR",
                    "description":"Wrong request method"
                }
            return HttpResponse(json.dumps(response_data), content_type='application/json', status=400)
        
    def post(self, request): # Post task
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data={
                    "state":"SUCCESS",
                    "description":"New task added succesfully",
                    "ser":str(serializer)

                }
            return HttpResponse(json.dumps(response_data), content_type='application/json', status=200) 

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        taskToupdate = ToDoTask.objects.get(pk=pk)
        serializer = ToDoSerializer(instance=taskToupdate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data={
                    "state":"SUCCESS",
                    "description":"Data updated successfully"
                }
            HttpResponse(json.dumps(response_data), content_type='application/json', status=200)
        response_data={
                    "state":"ERROR",
                    "description":"Data update failed",
                }
        return HttpResponse(json.dumps(response_data), content_type='application/json')

    
