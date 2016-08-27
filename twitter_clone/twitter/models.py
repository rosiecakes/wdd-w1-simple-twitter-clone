from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    username = models.CharField(max_length = 140)
    password = models.CharField(max_length = 25)
    email = models.EmailField(max_length=25)

    def __unicode__(self):
        return self.username
        

class Tweet(models.Model):
    tweet = models.CharField(max_length = 140)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.tweet
        
        
