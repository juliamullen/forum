from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=20)
    def __unicode__(self):
        return self.title

class Conversation(models.Model):
    forum = models.ForeignKey(Place)
    last_post_date = models.DateTimeField('date of last post')
    title = models.CharField(max_length=50, blank=True)
    @property
    def op(self):
        """ Return the first post """
        return self.post_set.order_by('date')[0]
    @property
    def post_latest(self):
        """ Return up to the three most recent posts """
        last = self.post_set.order_by('-date')[:(3 if (self.post_count > 3) else (self.post_count - 1))]
        return last
   def __unicode__(self):
        return str(self.pk)

class Post(models.Model):
    author         = models.CharField(max_length=25)
    text           = models.TextField()
    date           = models.DateTimeField("date published")
    image          = models.ImageField(upload_to="img/%d", blank=True)
    conversation   = models.ForeignKey(Conversation)
    def __unicode__(self):
        return self.text[:20]
