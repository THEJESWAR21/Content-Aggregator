from django.db import models

# Create your models here.

# Class BlogSource

# Class Authors
    # FIRST NAME
    # LAST 
# Class Articles
    # TITLE
    # LINK
    # AUTHOR
    # time published
    # AUTHOR
    # Description

class Source(models.Model):
    siteName = models.CharField(max_length=100, default=None)
    siteLink = models.URLField(max_length=500)

class Authors(models.Model):
    siteName = models.ForeignKey(Source, on_delete=models.CASCADE,)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}" 
    
class Articles(models.Model):
    siteName = models.ForeignKey(Source, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=500)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    dateTime = models.DateTimeField()
    tags = models.CharField(max_length=500)