# Build AI Chatbot with error handling

import os
import openai
from dotenv import load_dotenv

# Load .env from parent folder
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise EnvironmentError("Missing OPENAI_API_KEY in environment variables.")

def classify_query(query):
    keywords = ['news', 'headline', 'update', 'latest']
    if any(word in query.lower() for word in keywords):
        return "news"
    return "general"

def get_completion(prompt):
    if not prompt or not prompt.strip():
        return "Error: Empty prompt provided."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4.1",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            timeout=15  # Optional: add timeout for robustness
        )
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as oe:
        return f"OpenAI API error: {str(oe)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"