import feedparser

feed_url = "https://techcrunch.com/feed/"
blog_feed = feedparser.parse(feed_url)

# print(blog_feed.feed.title)
# print(blog_feed.feed.link)
# print(len(blog_feed.entries))

print()


for i in blog_feed.entries:

    tag_str = []

    print(i.title)
    for tag in i.tags:
        tag_str.append(tag["term"])

    tags = ", ".join(tag_str)
    print(tags)
    print()
    
    # print(i.title)
    # print(i.link)
    # print(i.author)
    # print(i.published)
    # print(i.description)
    # print(i.summary)
    # print(i.tags)




