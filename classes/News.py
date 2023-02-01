from utils import convert_datetime_to_utc_string


class News:
    def __init__(self, title, description, url, published_at):
        self.title = title
        self.description = description
        self.url = url
        self.published_at = published_at
        self.summary = None

    def __str__(self):
        published_at_string = convert_datetime_to_utc_string(self.published_at)
        return 'Title: ' + self.title + 'Published At: ' + published_at_string
    
    def add_summary(self, summary):
        self.summary = summary