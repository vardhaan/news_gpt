import news_api_wrapper as news
import url_scraper as scraper
from gpt_wrapper import GPT

'''
Returns a list of News objects of the latest breaking news. Each News
object has a content summary added to it.
'''
def extract_summarize():
    gpt = GPT()
    prompt = ""
    with open("prompts/extract_news_summary.txt") as f:
        prompt = f.read()
    breaking_news = news.get_breaking_news()[:5]
    for news_item in breaking_news:
        text = scraper.scrape_url(news_item.url)
        text = ''.join(text.split())
        completed_prompt = prompt.format(news_item.title, text)
        completion = gpt.send_completion_request(completed_prompt)
        news_item.add_summary(completion)
    return breaking_news


'''
#Test
x = extract_summarize()
for y in x:
    print(y)
'''
