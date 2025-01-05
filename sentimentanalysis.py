# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 02:05:54 2025

@author: Abdul Majid
"""

import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
# URL of the web page
url = "https://www.bbc.com/news/articles/c205ek63433o"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from the web page
    text = soup.get_text()
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")


sentiment = analyzer.polarity_scores(text)
print(sentiment)