import feedparser

from datetime import datetime
from .models import Source, Authors, Articles

def fetch_and_save_feed(feed_url):
    blog_feed = feedparser.parse(feed_url)

    # Crates a Source object
    source, created = Source.objects.get_or_create(
        site_link=feed_url,
        defaults={
            "site_name": blog_feed.feed.get("title", feed_url)
        }
    )

    for entry in blog_feed.entries:

        # Reset the tags for each article
        tag_list = []

        # Checking Whether tags exist
        if hasattr(entry, "tags"):
            for tag in entry.tags:
                tag_list.append(tag["term"])

        tags = ", ".join(tag_list)


        # Prevents program from crashing if author didn't exist
        author_name = entry.get("author", "Unknown Author")


        # prevent duplicates
        # Creates a Author Object
        author, created = Authors.objects.get_or_create(
            source = source,
            name = author_name
        )

        # Parasing Datatime string to datetime object
        published_date = None
        if entry.get('published_parsed'):
            try:
                published_date = datetime(*entry.published_parsed[:6])
            except Exception:
                published_date = None
                
            # Only want 6 units

        # Creates a Article Object
        Articles.objects.get_or_create(
            link = entry.get("link"),
            defaults={
                "title" : entry.get("title", "No Title"),
                "description": entry.get("description", ""),
                "published_at": published_date,
                "all_tags": tags,
                "source": source,
                "author": author
            }
        )
