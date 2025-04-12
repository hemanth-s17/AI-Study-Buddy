#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:28:32 2025

@author: hemanthsanisetty
"""

from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(youtube_url):
    """
    Extracts the video ID from a standard YouTube URL.
    """
    pattern = r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, youtube_url)
    return match.group(1) if match else None

def get_transcript(youtube_url):
    """
    Fetches and returns the transcript as a string from the given YouTube video URL.
    """
    video_id = extract_video_id(youtube_url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry['text'] for entry in transcript])
    return full_text
