from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from chat.models import ChatModel
from core.models import ClientModel
from .serializers import ChatSerializer
from .serializers import AnswerSerializer
from .utils import Helper
import secrets


class ChatHistory(ListAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        
        session_id = self.request.COOKIES.get("conversation")
        client = ClientModel.objects.get(session_id=session_id)
        return ChatModel.objects.filter(client=client)


class ChatAsk(CreateAPIView):
    serializer_class = ChatSerializer

    def create(self, request, *args, **kwargs):

        session_id= request.COOKIES.get("conversation")
        start_new_conversation = request.data.get("new_conversation")
        if (session_id is None or session_id == "" or start_new_conversation == True):
            session_id=secrets.token_urlsafe(32)
        
        user_question = request.data.get("question")
        response = Helper.getAiAnswer(user_question, session_id)
        
        client, created = ClientModel.objects.get_or_create(
            session_id=session_id,
            remote_address=Helper.get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT"),
        )
        client.save()
        new_question_answer = ChatModel.objects.create(
            question=user_question,
            new_conversation = created,
            response=response, 
            client=client,
        )
        new_question_answer.save()

        answer = AnswerSerializer(new_question_answer).data
        response = Response(answer)
        response.set_cookie("conversation", session_id, 600, samesite="lax", httponly=True) #600->10min
        return response
