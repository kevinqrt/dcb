from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.vectorstores import FAISS
from django.conf import settings

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
EMBEDDINGS = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl") #OpenAIEmbeddings()
LLM = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.5, "max_length": 512}) # ChatOpenAI()
VECTORSTORE = get_vectorstore()