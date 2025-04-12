#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:26:34 2025

@author: hemanthsanisetty
"""

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# Load model + tokenizer once
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto"
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=0,
    max_new_tokens=512,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1
)

def summarize_text(text):
    """
    Generates a simplified explanation of the provided text using Mistral-7B.
    """
    prompt = (
        "You are a helpful AI tutor. Explain the following content in simple terms, "
        "like you're teaching a 10th-grade student.\n\n"
        f"Content: {text[:2000]}"
    )

    output = generator(prompt)[0]['generated_text']
    return output.replace(prompt, "").strip()
