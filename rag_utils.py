#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:30:09 2025

@author: hemanthsanisetty
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

# Use a small, performant embedding model
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

embedding_model = HuggingFaceEmbeddings(model_name=EMBED_MODEL_NAME)

def create_vector_store(text):
    """
    Splits text into chunks and creates a FAISS vector store with embeddings.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = [Document(page_content=chunk) for chunk in text_splitter.split_text(text)]
    vector_store = FAISS.from_documents(docs, embedding_model)
    return vector_store

def query_vector_store(vector_store, query, top_k=3):
    """
    Searches the FAISS store and returns top-k relevant documents for a query.
    """
    results = vector_store.similarity_search(query, k=top_k)
    return [doc.page_content for doc in results]
