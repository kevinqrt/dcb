from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import RedisChatMessageHistory
from langchain.chains import ConversationalRetrievalChain
from django.conf import settings
from DCB_Backend import config


class Helper:
    def getAiAnswer(user_question, session_id):
        message_history = RedisChatMessageHistory(
            url=settings.REDISPATH,
            ttl=600,  # 10 minutes in seconds
            session_id=session_id,
        )
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            chat_memory=message_history,
            return_messages=True,
        )
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=config.LLM,
            retriever=config.VECTORSTORE.as_retriever(),
            memory=memory,
        )
        response = conversation_chain({"question": user_question}).get("answer")
        return response

    def get_client_ip(request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
