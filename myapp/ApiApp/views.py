from django.shortcuts import render
from .models import *
from django.http import JsonResponse

from .serializers import tasksSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def task_url(request):
    Api_url ={
       'get_task/ get_task, name=get_task',
       'taskDetalis/<id>/, taskDetalis, name=taskDetalis',
       'taskCreate/, taskCreate, name=taskCreate',
        'taskUpdate/<id>/, taskUpdate, name=taskUpdate',
       'tast_delcet/<id>/, tast_delcet, name=tast_delcet',

    }
    return Response(Api_url)





@api_view(['GET'])
def get_task(request):
    task_ob = Tasks.objects.all()
    serilizer = tasksSerializer(task_ob, many=True)
    return Response( serilizer.data)


@api_view(['GET'])
def taskDetalis(request, id):
    task_ob = Tasks.objects.get(id=id)
    serilizer = tasksSerializer(task_ob, many=False)
    return Response( serilizer.data)


@api_view(['POST'])
def taskCreate(request):
    serilizer = tasksSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)

@api_view(['POST'])
def taskUpdate(request,id):
    task=Tasks.objects.get(id=id)
    serilizer=tasksSerializer(instance=task,data=request.data)

    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)

@api_view(['DELETE'])
def tast_delcet(request,id):
    task=Tasks.objects.get(id=id)
    task.delete()
    return Response('Item delete successfully')


