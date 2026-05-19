from django.db import models

# Create your models here.

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

class Authors(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}" 
    
class Articles(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    dateTime = models.DateTimeField()
