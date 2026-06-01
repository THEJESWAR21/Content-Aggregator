from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"), # HOME PAGE
    path("update-feeds/", views.update_feeds,name="update_feeds"), # UPDATE FEED REQUEST FOR THE BUTTON
    path("delete-feed/<int:feed_id>/", views.delete_feed, name="delete_feed"), # DELETE FEED REQUEST FOR THE LINKS
]