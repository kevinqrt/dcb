from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import pandas as pd
from DCB_Backend import config, settings


# functions no views


class Helper:
    def add_pdf_to_vectorstore(
        vectorstore: config.STORECOMPONENT, path: str, source_id: str
    ):
        loader = PyPDFLoader(path)
        pages = loader.load_and_split()
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        docs = text_splitter.split_documents(pages)
        for doc in docs:
            doc.metadata = {"source_id": source_id}
        extension = config.STORECOMPONENT.from_documents(docs, config.EMBEDDINGS)
        vectorstore.merge_from(extension)
        vectorstore.save_local(settings.VECTORSTOREPATH)

    def delete_document(vectorstore: config.STORECOMPONENT, source_id):
        vector_df = Helper.store_to_df(vectorstore)
        chunks_list = vector_df.loc[
            vector_df["metadata"].apply(lambda x: x.get("source_id") == source_id)
        ]["chunk_id"].tolist()
        vectorstore.delete(chunks_list)
        vectorstore.save_local(settings.VECTORSTOREPATH)

    def store_to_df(store):
        v_dict = store.docstore._dict
        data_rows = []
        for k in v_dict.keys():
            metadata = v_dict[k].metadata
            content = v_dict[k].page_content
            data_rows.append({"chunk_id": k, "metadata": metadata, "content": content})
        vector_df = pd.DataFrame(data_rows)
        return vector_df

    def show_vstore(store):
        vector_df = Helper.store_to_df(store)
        print(vector_df)
