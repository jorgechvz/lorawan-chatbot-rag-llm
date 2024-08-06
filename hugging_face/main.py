import os
from pinecone import Pinecone
import gradio as gr
from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import (
    VectorStoreIndex,
    Settings,
    SimpleDirectoryReader,
    PromptTemplate,
    get_response_synthesizer,
    Document,
)
import pandas as pd

load_dotenv()

pinecone_client = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
pinecone_index = pinecone_client.Index("lorawan-rag")

llm = Gemini(api_key=os.getenv("GOOGLE_API_KEY"), model="models/gemini-1.5-flash")
embed_model = GeminiEmbedding(model_name="models/embedding-001")
Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 768

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
retriever = VectorIndexRetriever(index=index, similarity_top_k=5)
query_engine = RetrieverQueryEngine(retriever=retriever)

prompt_template = (
    "Given the context that I will provide you, answer the questions.\n"
    "Context:\n"
    "#####################################\n"
    "{context_str}\n"
    "Answer: {query_str}\n"
)

qa_template = PromptTemplate(template=prompt_template)
chain_type_kwargs = {"prompt": qa_template}
response_synthesizer = get_response_synthesizer(
    llm=llm, text_qa_template=qa_template, response_mode="compact"
)
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
)


with gr.Blocks() as app:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Enter your query here")
    clear = gr.Button("Clear")

    def respond(message, chat_history):
        response = query_engine.query(message).response
        chat_history.append((message, response))
        return "", chat_history  

    msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

app.launch(share=True)