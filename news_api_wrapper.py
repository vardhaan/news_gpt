import os
import requests

API_KEY = os.environ.get('NEWS_API_KEY')

# function that gets the breaking news for the US from https://newsapi.org/docs/get-started#top-headlines
def get_breaking_news():
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + API_KEY
    response = requests.get(url)
    python_object_news_list = parse_news_list(response.json()['articles'])
    return python_object_news_list

# function that parses out each article's title, description, and content from a JSON object array
def parse_news_list(news_json_arr):
    news_list = []
    for news_json in news_json_arr:
        news = {}
        news['title'] = news_json['title']
        news['description'] = news_json['description']
        news['url'] = news_json['url']
        news_list.append(news)
    return news_list



