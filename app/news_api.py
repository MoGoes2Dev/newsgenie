# Integrate News and Web Search APIs - with error handling

import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(category):
    if not NEWS_API_KEY:
        raise EnvironmentError("Missing NEWS_API_KEY in environment variables.")

    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={NEWS_API_KEY}&language=en"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if "articles" not in data:
            raise ValueError("Unexpected response structure: 'articles' key not found.")
        
        return data["articles"][:5]
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error connecting to News API.")
    except requests.exceptions.Timeout:
        print("Request to News API timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return []

if __name__ == "__main__":
    print("NEWS_API_KEY loaded:", bool(NEWS_API_KEY))

