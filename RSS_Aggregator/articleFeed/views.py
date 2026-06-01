from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader


from .models import Articles
from .models import Source

from .feedParser import fetch_and_save_feed

# Create your views here.
def home(request):
    if request.method == "POST":
        rss_url = request.POST.get("rss_url")
        if rss_url:
            Source.objects.get_or_create(
                site_link = rss_url,
                defaults = {
                    "site_name": rss_url
                }
            )

        return redirect("home")

    source = Source.objects.all()

    articles = Articles.objects.all().order_by(
        '-published_at'
    )

    context = {
        "feeds": source,
        "articles": articles,
    }

    return render(request, 'articleFeed/index.html', context)

def update_feeds(request): # MAKE THE REQUEST TO UPDATE THE FEED
    if request.method == "POST":
        source = Source.objects.all()
        for feed in source:
            fetch_and_save_feed(
                feed.site_link
            )
    
    # AFTER MAKING THE REQUEST REDIRECT BACK TO HOME PAGE
    return redirect("home")

def delete_feed(request, feed_id): # MAKE THE REQUEST TO DELETE THE FEED
    if request.method == "POST":
        feed = get_object_or_404(Source, id=feed_id) # IF THE RECORD DIDN'T EXIST IT WILL THROW A 404 ERROR
        feed.delete()

    # AFTER MAKING THE REQUEST REDIRECT BACK TO HOME PAGE
    return redirect('home')
