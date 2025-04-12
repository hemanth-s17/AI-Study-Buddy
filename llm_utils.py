#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:26:34 2025

@author: hemanthsanisetty
"""

import os
import requests

GROQ_API_KEY = "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"  # Set this in your environment or .env file
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
DEFAULT_MODEL = "mistral-saba-24b"  # or "llama3-70b-8192", etc.

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}



from groq import Groq



def generator(prompt, system_prompt="You are a helpful assistant.", model=DEFAULT_MODEL, temperature=0.7):

    client = Groq(
        # This is the default and can be omitted
        api_key=GROQ_API_KEY,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model= DEFAULT_MODEL
    )

    return chat_completion.choices[0].message.content



def summarize_text(text):
    """
    Generates a simplified explanation of the provided text using Mistral-7B.
    """
    prompt = (
        "You are a helpful AI tutor. Explain the following content in simple terms, "
        "like you're teaching a 10th-grade student.\n\n"
        f"Content: {text[:2000]}"
    )

    output = generator(prompt)
    return output.replace(prompt, "").strip()
