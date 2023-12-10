from dotenv import load_dotenv
#from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from django.conf import settings
import os

load_dotenv(dotenv_path=settings.BASE_DIR / ".env")

def get_vectorstore():
        embeddings = EMBEDDINGS
        store_path = settings.VECTORSTOREPATH

        try:
            vectorstore = STORECOMPONENT.load_local(store_path, embeddings)
        except:
            vectorstore = STORECOMPONENT.from_texts(texts=[""] , embedding=embeddings)
            vectorstore.save_local(store_path)
        
        return vectorstore


STORECOMPONENT = FAISS

#EMBEDDINGS = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl") #OpenAIEmbeddings()
EMBEDDINGS = OpenAIEmbeddings(
    openai_api_key=os.environ["OPENAI_API_KEY"],
    model="text-embedding-ada-002",
)

#LLM = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.5, "max_length": 512}) # ChatOpenAI()
LLM = ChatOpenAI(
    openai_api_key=os.environ["OPENAI_API_KEY"],
    model_name="gpt-3.5-turbo",
)

VECTORSTORE = get_vectorstore()