from django.db import models

# Create your models here.

class Source(models.Model):
    site_name = models.CharField(max_length=100, default=None)
    site_link = models.URLField(unique=True)

    # Controls how each objects appears as a string
    def __str__(self):
        return self.site_name

class Authors(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name="authors")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Articles(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=500, unique=True) # Unique prevents 2 rows in the same coloumn to have the same values
    description = models.TextField(blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    all_tags = models.CharField(max_length=500, blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name="articles")
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        return self.title   
