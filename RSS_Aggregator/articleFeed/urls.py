from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("update-feeds/", views.update_feeds,name="update_feeds"),

    path("delete-feed/<int:feed_id>/", views.delete_feed, name="delete_feed"),
]