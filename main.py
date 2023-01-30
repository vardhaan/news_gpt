import news_api_wrapper as news
import url_scraper as scraper

breaking_news = news.get_breaking_news()
latest_news = breaking_news[0]
news_text = scraper.scrape_url(latest_news['url'])
print(news_text)