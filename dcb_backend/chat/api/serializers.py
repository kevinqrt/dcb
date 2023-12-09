from rest_framework import serializers
from chat.models import ChatModel

class ChatSerializer(serializers.ModelSerializer):
    response = serializers.CharField(read_only=True)
    question = serializers.CharField(required=True)
    class Meta:
        model = ChatModel
        fields = ('question', 'response', 'new_conversation', 'created')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatModel
        fields = ('response', 'new_conversation')