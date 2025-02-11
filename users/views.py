from rest_framework import viewsets
from .models import Task
from .permissions import CanAssignTask
from .serializers import TaskSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [CanAssignTask]

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.get_object()
        if task.assigned_to != request.user:
            return Response({'error': 'You are not assigned to this task.'}, status=status.HTTP_403_FORBIDDEN)
        
        points = request.data.get('points')
        if not points:
            return Response({'error': 'Points are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        task.completed = True
        task.points = points
        task.save()
        return Response({'status': 'Task completed', 'points': points}, status=status.HTTP_200_OK)