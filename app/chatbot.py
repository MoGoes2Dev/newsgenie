#Build AI Chatbot

import os
import openai
from dotenv import load_dotenv

# Load .env from parent folder
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_query(query):
    keywords = ['news', 'headline', 'update', 'latest']
    if any(word in query.lower() for word in keywords):
        return "news"
    return "general"

def get_completion(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4.1",  # or "gpt-3.5-turbo" if using free tier
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"