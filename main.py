import news_api_wrapper as news
import url_scraper as scraper
import gpt_wrapper as gpt

'''
breaking_news = news.get_breaking_news()
latest = breaking_news[0]
text = scraper.scrape_url(latest.url)
text = ''.join(text.split())
with open("prompts/extract_news_summary.txt") as f:
    prompt = f.read()
    prompt = prompt.format(latest.title, text)
    print(prompt)
completion = gpt.send_completion_request(prompt)
print(completion)
'''
breaking_news = news.get_breaking_news()
for i in breaking_news:
    text = scraper.scrape_url(i.url)
    text = ''.join(text.split())
    print(len(text))