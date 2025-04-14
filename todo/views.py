from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/tasks/'},
        {'GET': '/api/tasks/<id>/'},
        {'POST': '/api/tasks/'},
        {'PUT': '/api/tasks/<id>/'},
        {'DELETE': '/api/tasks/<id>/'},
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def getTasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('-created_at')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def getTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTask(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return Response({'message': 'Task deleted successfully!'})
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)


@api_view(['PUT'])
def updateTask(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)

    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
