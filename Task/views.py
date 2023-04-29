from django.shortcuts import render
from .serializers import TaskSerializer
from django.http.response import JsonResponse
from django.http import Http404
from .models import Task
from rest_framework.response import Response
from rest_framework import status , viewsets , filters
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.

#1-Get and Post
@api_view(['GET','POST'])
def task_List(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#---------------------------------------------------------------------------    
#2- Get and Put and Delete
class Task_pk(APIView):
    def get_object(self,pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    def put(self, request,pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
#---------------------------------------------------------------------------
# retrieve list filtered by status
class Viewset_task_status(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['status']

## retrieve list filtered by priority
class Viewset_task_priority(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['priority']



