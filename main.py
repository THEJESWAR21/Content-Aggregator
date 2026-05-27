import feedparser

feed_url = "https://techcrunch.com/feed/"
blog_feed = feedparser.parse(feed_url)


print()


for i in blog_feed.entries:

    tag_str = []

    print(i.title)
    for tag in i.tags:
        tag_str.append(tag["term"])

    tags = ", ".join(tag_str)
    print(tags)
    print()
    




