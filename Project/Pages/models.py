from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='Photos/Team')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    gmail_link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.designation}"
    
    
    