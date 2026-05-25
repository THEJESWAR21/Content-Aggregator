import feedParser
from .models import Source, Authors, Articles

def fetch_and_save_feed(feed_url):
    blog_feed = feedParser.parse(feed_url)

    tag_list = []

    source = Source.objects.create(
        site_name = blog_feed.feed.title,
        site_link = blog_feed.feed.link
    )
    

    for entry in blog_feed.entries:

        for tag in entry.tags:
            tag_list.append(tag["term"])

        tags = ", ".join(tag_list)


        author = Authors.objects.create(
            source = source,
            name = entry.author
        )

        article = Articles.objects.create(
            title = entry.title,
            link = entry.link,
            description = entry.description,
            published_at = entry.published,
            all_tags = tags
        )

fetch_and_save_feed("https://techcrunch.com/feed/")