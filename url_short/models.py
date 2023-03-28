from django.db import models
import pyshorteners


# 
class URLShort(models.Model):
    url = models.URLField()
    short_url = models.URLField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def save(self,*args,**kwargs):
        shortener = pyshorteners.Shortener()
        self.short_url = shortener.tinyurl.short(self.url)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.short_url
    
    