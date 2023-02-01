import os
import requests
from utils import convert_utc_string_to_datetime
import classes.News as News

API_KEY = os.environ.get('NEWS_API_KEY')

# function that gets the breaking news for the US from https://newsapi.org/docs/get-started#top-headlines
def get_breaking_news(datetime_string=None):
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + API_KEY
    response = requests.get(url)
    print(response)
    python_object_news_list = parse_news_list(response.json()['articles'])
    if datetime_string:
        datetime_object = convert_utc_string_to_datetime(datetime_string)
        python_object_news_list = filter_news_by_datetime(python_object_news_list, datetime_object)
    return python_object_news_list


# function that parses out each article's title, description, and content from a JSON object array
def parse_news_list(news_json_arr):
    news_list = []
    for news_json in news_json_arr:
        published_at = convert_utc_string_to_datetime(news_json['publishedAt'])
        news = News.News(news_json['title'], news_json['description'], news_json['url'], published_at)
        news_list.append(news)
    return news_list


def filter_news_by_datetime(news_list, datetime):
    filtered_news_list = []
    for news in news_list:
        if news.published_at > datetime:
            filtered_news_list.append(news)
    return filtered_news_list