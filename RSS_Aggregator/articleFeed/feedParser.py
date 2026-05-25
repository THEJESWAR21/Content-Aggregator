import feedParser
from .models import Source, Authors, Articles

def fetch_and_save_feed(feed_url):
    feed = feedParser.parse(feed_url)

    tag_list = []
    for entry in feed.entries:
        Articles.objects.create(
            title = entry.title(),
            link = entry.link(),
            description = entry.description(),
            published_at = entry.published(),
        )

        # TODO: Code to turn tags into strings
        
