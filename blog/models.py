from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=120)
    summary = models.CharField(max_length=240)
    blog_body = models.TextField()
    date_created_at = models.DateTimeField(auto_now_add=True)
