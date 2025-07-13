#Integrate News and Web Search APIs - no error handling

import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(category):
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={NEWS_API_KEY}&language=en"
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return articles[:5]  # Return top 5


print("NEWS_API_KEY loaded:", os.getenv("NEWS_API_KEY"))

