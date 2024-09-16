from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .serializer import TodoListSerializer, TodoDetailSerializer
from .models import Todo


# Create your views here.
class TodoList(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete=False) # 완료하지 않은 할일 만 가져옵니다.
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TodoGetPost(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TodoDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        todo.complete = True
        todo.save()
        serializer = TodoDetailSerializer(todo)
        return Response(status=status.HTTP_200_OK)

class TodoAllGet(APIView):
    def get(self, request):
        todo = Todo.objects.all()
        serializer = TodoListSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


