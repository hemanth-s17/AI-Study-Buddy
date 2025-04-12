#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:32:40 2025

@author: hemanthsanisetty
"""

from llm_utils import generator

def generate_flashcards(text, num_flashcards=5):
    """
    Generates flashcards from the input text using the LLM.
    """
    prompt = (
        f"Generate {num_flashcards} flashcards from the following content.\n"
        "Each flashcard should be in Q&A format, short and easy to remember.\n\n"
        f"Content: {text[:2000]}"
    )

    output = generator(prompt)[0]['generated_text']
    return output.replace(prompt, "").strip()
