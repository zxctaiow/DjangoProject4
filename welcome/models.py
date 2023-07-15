from django.db import models
from datetime import datetime

# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published', default=datetime.now, blank=True)

    def __str__(self):
        return self.news_title[:40]+'...'
    
class Comments(models.Model):
    topic = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=250)
    sent_date = models.DateField('date sent', default=datetime.now, blank=True)

    def __str__(self):
        return self.topic.news_title

class NewsComments(models.Model):
    topic = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=250)
    sent_date = models.DateField('date sent', default=datetime.now, blank=True)

    def __str__(self):
        return self.topic.news_title