#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:25:11 2025

@author: hemanthsanisetty
"""

import streamlit as st
from pdf_utils import extract_text_from_pdf
from llm_utils import summarize_text
from rag_utils import create_vector_store, query_vector_store
from quiz_utils import generate_quiz
from flashcard_utils import generate_flashcards
from youtube_utils import get_transcript
from text_utils import clean_text

st.set_page_config(page_title="AI Study Buddy", page_icon="🧠")
st.title("🧠 AI Study Buddy")
st.write("Upload a PDF or enter a YouTube link to get simplified explanations, flashcards, and quizzes.")

# Sidebar for inputs
source_type = st.sidebar.radio("Select Input Type", ["PDF Upload", "YouTube Link"])

pdf_text = ""
youtube_url = ""
vector_store = None
source_text = ""

if source_type == "PDF Upload":
    uploaded_pdf = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_pdf:
        with st.spinner("Extracting text from PDF..."):
            pdf_text = extract_text_from_pdf(uploaded_pdf)
            source_text = pdf_text
        st.subheader("Extracted Text Preview")
        st.text_area("First 1000 characters", pdf_text[:1000], height=200)

elif source_type == "YouTube Link":
    youtube_url = st.sidebar.text_input("Enter YouTube Video URL")
    if youtube_url:
        try:
            with st.spinner("Fetching and cleaning transcript..."):
                transcript = get_transcript(youtube_url)
                source_text = clean_text(transcript)
            st.subheader("Transcript Preview")
            st.text_area("First 1000 characters", source_text[:1000], height=200)
        except Exception as e:
            st.error(f"Failed to fetch transcript: {e}")

# Main action
st.sidebar.markdown("---")
action = st.sidebar.radio("What would you like to do?", ["Explain Simply", "Generate Flashcards", "Quiz Me"])

custom_query = ""
if action == "Explain Simply":
    custom_query = st.text_input("Ask a question or leave blank for general explanation", "Explain this content simply")

if st.sidebar.button("Run AI 🤖"):
    if source_text:
        with st.spinner("Creating vector store..."):
            vector_store = create_vector_store(source_text)

        with st.spinner("Processing with AI..."):
            if action == "Explain Simply":
                if vector_store:
                    relevant_chunks = query_vector_store(vector_store, custom_query)
                    combined_text = "\n\n".join(relevant_chunks)
                    summary = summarize_text(combined_text)
                    st.subheader("🧾 Simplified Explanation")
                    st.write(summary)

            elif action == "Generate Flashcards":
                if vector_store:
                    relevant_chunks = query_vector_store(vector_store, "Create flashcards from this content")
                    combined_text = "\n\n".join(relevant_chunks)
                    flashcards = generate_flashcards(combined_text)
                    st.subheader("🗂️ Flashcards")
                    st.text_area("Generated Flashcards", flashcards, height=400)

            elif action == "Quiz Me":
                if vector_store:
                    relevant_chunks = query_vector_store(vector_store, "Create a quiz from this content")
                    combined_text = "\n\n".join(relevant_chunks)
                    quiz = generate_quiz(combined_text)
                    st.subheader("📝 Quiz")
                    st.text_area("Generated Questions", quiz, height=400)
    else:
        st.error("Please upload a valid input before running the AI.")
