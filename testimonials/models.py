from django.db import models


class Testimonials(models.Model):
    """ The model for Testimonials, showing title, testimonials_body, rating out of 5 and date created """
    title = models.CharField(max_length=120)
    testimonial_body = models.TextField()
    date_created_at = models.DateTimeField(auto_now_add=True)


# defining the rating choices
    def Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)
    is_favorite = models.IntegerField(choices=Rating_CHOICES, default=3)
