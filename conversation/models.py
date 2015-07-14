from django.db import models
from django import forms


class Place(models.Model):
    title = models.CharField(max_length=20)
    def __unicode__(self):
        return self.title

class Conversation(models.Model):
    forum = models.ForeignKey(Place)
    title = models.CharField(max_length=50, blank=True)
    post_count = models.IntegerField()
    last_post_date = models.DateTimeField('date of last post')
    def __unicode__(self):
        return str(self.pk)

class Post(models.Model):
    author         = models.CharField(max_length=25)
    text           = models.TextField()
    date           = models.DateTimeField("date published")
    image          = models.ImageField(upload_to="img/%d", blank=True)
    conversation   = models.ForeignKey(Conversation)

    number_post_in_conversation = models.IntegerField()

    def __unicode__(self):
        return "Post: {0}".format(self.text[:20])
