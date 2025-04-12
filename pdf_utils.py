#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:25:49 2025

@author: hemanthsanisetty
"""

import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    """
    Extracts and returns the full text from a PDF file using PyMuPDF.
    """
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text
