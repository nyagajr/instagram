from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)
    # image_location = models.ForeignKey(Location)
    image_path = models.ImageField(upload_to = 'gallery/')
    image_description = models.TextField()

class Comment(models.Model):
    comments = models.CharField(max_length =30)

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
