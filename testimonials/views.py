from django.shortcuts import render
from django.utils import timezone
from .models import Testimonials

def testimonials(request):
    """ adding date and time to each testimonial  """
    testimonial_posts = Testimonials.objects.filter(date_created_at__lte = timezone.now()).order_by('-date_created_at')
    return render(request, "testimonials.html", {"blog_posts": blog_posts})
