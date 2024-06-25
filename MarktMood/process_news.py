import json
from newsapi import NewsApiClient

def clean_text(text):
    """Simple function to clean text data."""
    if text:
        return ' '.join(text.split())
    return ""

def fetch_and_process_data(api_key, query='appl'):
    """Fetch news data and preprocess it."""
    newsapi = NewsApiClient(api_key=api_key)
    all_articles = newsapi.get_everything(q=query,
                                          language='en',
                                          sort_by='relevancy')
    
    processed_articles = []
    for article in all_articles['articles']:
        processed_article = {
            'title': clean_text(article['title']),
            'description': clean_text(article['description']),
            'content': clean_text(article['content'])
        }
        processed_articles.append(processed_article)
    
    return processed_articles

if __name__ == '__main__':
    # Replace 'your_api_key' with your actual NewsAPI key
    api_key = '656efde4fcbc4bcb9ede7c882c39e9dd'
    results = fetch_and_process_data(api_key)
    print(json.dumps(results, indent=2))
