from django.contrib import admin

from .models import Monastery, PrayerIntent, RetreatRequest


@admin.register(Monastery)
class MonasteryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_name', 'location', 'is_published')
    list_filter = ('is_published', 'order_name')
    search_fields = ('name', 'location', 'order_name')
    prepopulated_fields = {'slug': ('name',)}
list_editable = (
        "is_featured",
    )
fieldsets = (
        (
            "Basic information",
            {
                "fields": (
                    "name",
                    "slug",
                    "order_name",
                    "location",
                    "address",
                )
            }
        ),

        (
            "About the monastery",
            {
                "fields": (
                    "short_description",
                    "description",
                    "uniqueness",
                )
            }
        ),

        (
            "Visitor information",
            {
                "fields": (
                    "directions",
                    "dos",
                    "donts",
                    "visitor_notes",
                )
            }
        ),

        (
            "Contact & media",
            {
                "fields": (
                    "image_url",
                    "website_url",
                    "phone",
                )
            }
        ),

        (
            "Publishing",
            {
                "fields": (
                    "is_featured",
                )
            }
        ),
    )

@admin.register(PrayerIntent)
class PrayerIntentAdmin(admin.ModelAdmin):
    list_display = ('name', 'monastery', 'intention_type', 'created_at')
    list_filter = ('intention_type', 'monastery')
    search_fields = ('name', 'message', 'monastery__name')


@admin.register(RetreatRequest)
class RetreatRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'monastery', 'stay_type', 'arrival_date', 'duration_days')
    list_filter = ('stay_type', 'monastery')
    search_fields = ('name', 'notes', 'monastery__name')
