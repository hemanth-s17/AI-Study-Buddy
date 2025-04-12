#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:34:04 2025

@author: hemanthsanisetty
"""

import re
from typing import List

def clean_text(text: str) -> str:
    """
    Basic cleaning of text: remove excessive whitespace and special characters.
    """
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def chunk_text(text: str, max_tokens: int = 500) -> List[str]:
    """
    Splits the text into chunks of approximately `max_tokens` words.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_tokens):
        chunk = " ".join(words[i:i+max_tokens])
        chunks.append(chunk)
    return chunks
