from django.db import models
from django.urls import reverse


class Monastery(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order_name = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200)
    region = models.CharField(max_length=100, blank=True)
    summary = models.TextField(blank=True)
    description = models.TextField(blank=True)
    directions = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('monastery_detail', args=[self.slug])


class PrayerIntent(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    monastery = models.ForeignKey(Monastery, on_delete=models.SET_NULL, null=True, blank=True)
    intention_type = models.CharField(
        max_length=50,
        choices=[
            ('health', 'Health & healing'),
            ('thanksgiving', 'Thanksgiving'),
            ('family', 'Family harmony'),
            ('vocation', 'Vocation'),
            ('peace', 'Peace & country'),
            ('general', 'General intention'),
        ],
        default='general',
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.intention_type}'


class RetreatRequest(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    monastery = models.ForeignKey(Monastery, on_delete=models.SET_NULL, null=True, blank=True)
    stay_type = models.CharField(
        max_length=50,
        choices=[
            ('silent', 'Silent retreat'),
            ('guided', 'Guided retreat'),
            ('family', 'Family stay'),
            ('group', 'Group retreat'),
        ],
        default='silent',
    )
    arrival_date = models.DateField()
    duration_days = models.PositiveIntegerField(default=3)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.monastery or "General"}'
   
    @property
    def map_url(self):
        query = self.address or self.location
        return (
            "https://www.google.com/maps/search/"
            "?api=1&query="
            + query.replace(" ", "+")
        )