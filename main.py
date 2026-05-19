import feedparser

feed_url = "https://techcrunch.com/feed/"
blog_feed = feedparser.parse(feed_url)

# print(blog_feed.feed.title)
# print(len(blog_feed.entries))

for i in range(len(blog_feed.entries)):

    print()

    print(blog_feed.entries[i].title)
    print(blog_feed.entries[i].link)
    print(blog_feed.entries[i].author)
    print(blog_feed.entries[i].published)

    print()


