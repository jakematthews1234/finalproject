from django.shortcuts import render
from django.utils import timezone
from .models import Blog

def blog(request):
    """ adding date and time to each blog post """
    blog_posts = Blog.objects.filter(date_created_at__lte = timezone.now()).order_by('-date_created_at')
    """ Testing blog_posts """
    print(blog_posts)
    return render(request, "blog.html", {"blog_posts": blog_posts})
