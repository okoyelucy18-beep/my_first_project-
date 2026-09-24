from django.db import models
from django.urls import reverse


class Monastery(models.Model):
     name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    order_name = models.CharField(
        max_length=150,
        blank=True,
        help_text="e.g. Benedictine, Cistercian, Carmelite"
    )

    location = models.CharField(max_length=200)
    address = models.TextField(blank=True)

    short_description = models.TextField(
        help_text="Short description shown on the homepage."
    )

    description = models.TextField(
        help_text="Full description for the monastery page."
    )

    uniqueness = models.TextField(
        help_text="What makes this monastery distinctive?"
    )

    image_url = models.URLField(
        blank=True,
        help_text="URL for the monastery's main image."
    )

    directions = models.TextField(
        blank=True,
        help_text="Visitor directions."
    )

    dos = models.TextField(
        blank=True,
        help_text="One visitor guideline per line."
    )

    donts = models.TextField(
        blank=True,
        help_text="One visitor restriction per line."
    )

    visitor_notes = models.TextField(blank=True)

    website_url = models.URLField(blank=True)

    phone = models.CharField(max_length=50, blank=True)

    is_featured = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Monastery"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('monastery_detail', kwargs={'slug': self.slug})

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
            + query.replace(" ", "+") )