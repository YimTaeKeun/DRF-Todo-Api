from rest_framework import serializers
from .models import Todo

# todo를 리스트로 가져올 때 사용하는 시리얼라이저 입니다.
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'important', 'complete')

# todo의 상세정보를 가져올 때 사용하는 시리얼라이저 입니다.
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important', 'complete')

