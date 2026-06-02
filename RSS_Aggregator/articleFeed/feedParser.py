import feedparser

from datetime import datetime
from .models import Source, Authors, Articles

def fetch_and_save_feed(feed_url):

    # Parsing the URL
    blog_feed = feedparser.parse(feed_url)

    source_title = getattr(blog_feed.feed, "title", "Unknown Source")
    source_link = getattr(blog_feed.feed, "link", feed_url)

    # Creating a Source object
    source, created = Source.objects.get_or_create(
        site_link = source_link,
        defaults={
            "site_name": source_title
        }
    )

    for entry in blog_feed.entries:

        # 1. TURNING THE TAGS INTO LISTS

        # Reset the tags for each article
        tag_list = []

        # Checking Whether tags exist
        if hasattr(entry, "tags"):
            for tag in entry.tags:
                tag_list.append(tag.get("term", ""))

        # turn the list into a string
        tags = ", ".join(tag_list)


        # Prevents program from crashing if author didn't exist
        author_name = getattr(entry, "author", "Unknown Author")


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
            title= getattr(entry, "title", "No Title"),
            link = getattr(entry, "link", None),
            defaults={
                "description": getattr(entry, "description", ""),
                "published_at": published_date,
                "all_tags": tags,
                "source": source,
                "author": author
            }
        )
