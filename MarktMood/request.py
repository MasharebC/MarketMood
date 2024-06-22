from newsapi import NewsApiClient

# Initialize the client with your API key
newsapi = NewsApiClient(api_key='656efde4fcbc4bcb9ede7c882c39e9dd')

# Fetch top headlines about the stock market
top_headlines = newsapi.get_top_headlines(q='stock market',
                                          language='en',
                                          country='us')

# Fetch all articles about a specific topic
all_articles = newsapi.get_everything(q='stock market',
                                      from_param='2024-05-22',
                                      to='2024-05-22',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# Print the articles to the console
print(top_headlines)
print(all_articles)
