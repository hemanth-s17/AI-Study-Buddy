#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:31:30 2025

@author: hemanthsanisetty
"""
from transformers import pipeline

# Use the same Mistral pipeline from llm_utils if needed, or redefine here
from llm_utils import generator

def generate_quiz(text, num_questions=5):
    """
    Generates quiz questions from the input text using the LLM.
    """
    prompt = (
        f"Create a quiz with {num_questions} multiple choice questions based on the following content.\n"
        "Each question should have 4 options and clearly mark the correct one.\n\n"
        f"Content: {text[:2000]}"
    )

    output = generator(prompt)[0]['generated_text']
    return output.replace(prompt, "").strip()

