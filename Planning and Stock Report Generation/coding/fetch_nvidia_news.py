# filename: fetch_nvidia_news.py
from newsapi import NewsApiClient
import pandas as pd

# Initialize the client with your API key
newsapi = NewsApiClient(api_key='your_api_key_here')

# Fetch news for Nvidia around April 19, 2024
all_articles = newsapi.get_everything(q='Nvidia',
                                      from_param='2024-04-17',
                                      to='2024-04-21',
                                      language='en',
                                      sort_by='relevancy')

# Create a DataFrame for easy viewing
articles_df = pd.DataFrame(all_articles['articles'])

# Select relevant columns if necessary
articles_df = articles_df[['publishedAt', 'title', 'description', 'url']]

# Save the news data to a CSV file for further analysis
articles_df.to_csv('nvidia_news_around_significant_drop.csv')

# Show the DataFrame
print(articles_df)

# Optionally, you can plot a timeline with news titles if you integrate with a visualization tool or library.