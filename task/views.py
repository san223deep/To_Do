from rest_framework.views import APIView
from .models import Task
from django.db.models import Q
from .serializers import TaskSerializer, CreateTaskSerializer, UpdateTaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ToDoList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todo_list = Task.objects.filter(user=request.user)
        title = self.request.query_params.get('title')
        todo_status = self.request.query_params.get('status')
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        sort_by = self.request.query_params.get('sort_by')
        if title:
            todo_list = todo_list.filter(title__icontains=title)
        if todo_status:
            todo_list = todo_list.filter(status=todo_status)
        if from_date and to_date:
            todo_list = todo_list.filter(Q(due_date__gte=from_date) & Q(due_date__lte=to_date))
        if sort_by:
            try:
                todo_list = todo_list.order_by(sort_by)
            except:
                pass
        serializer = TaskSerializer(todo_list, many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            response = serializer.data
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoListUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def get_task(self, pk):
        for i in pk:
            if i not in '1234567890':
                return False
        task = Task.objects.filter(pk=pk).first()
        if task:
            return task
        else:
            return False

    def put(self, request, **kwargs):
        task_pk = kwargs['pk']
        task = self.get_task(task_pk)
        if not task:
            return Response({'message': 'Invalid todo ID'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateTaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        task_pk = kwargs['pk']
        task = self.get_task(task_pk)
        if not task:
            return Response({'message': 'Invalid todo ID'}, status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
