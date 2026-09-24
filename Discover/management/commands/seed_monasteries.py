from django.core.management.base import BaseCommand

from Discover.models import Monastery


MONASTERIES = [
    {
        'name': 'Holy Cross Monastery',
        'slug': 'holy-cross-nteje',
        'order_name': 'Congregation of the Holy Cross',
        'location': 'Nteje, Anambra State',
        'region': 'Anambra East',
        'summary': 'A prayerful monastic community rooted in mission, silence, and service.',
        'description': 'Holy Cross Monastery is a peaceful sanctuary where contemplative life and community service meet. The brothers are known for disciplined prayer, pastoral outreach, and serene hospitality for pilgrims and visitors.',
        'directions': 'From Nteje, follow the road toward the parish church and continue until you see the monastic enclosure at the hilltop approach.',
        'image_url': 'https://images.unsplash.com/photo-1507692049790-de58290a4334',
        'is_published': True,
    },
    {
        'name': 'St. Benedict Monastery',
        'slug': 'st-benedict-ozubulu',
        'order_name': 'Order of Saint Benedict',
        'location': 'Ozubulu, Anambra State',
        'region': 'Ekwusigo',
        'summary': 'A Benedictine haven of prayer, work, and balanced monastic living.',
        'description': 'St. Benedict Monastery offers a rhythm of chapel prayer, manual work, and quiet reflection. It is valued for its strong Benedictine rule, disciplined hospitality, and carefully nurtured communal life.',
        'directions': 'At Ozubulu, follow the road toward the central church junction and turn toward the monastic grounds beside the old farm entrance.',
        'image_url': 'https://images.unsplash.com/photo-1470770841072-f978cf4d019e',
        'is_published': True,
    },
    {
        'name': 'Carmelite Monastery',
        'slug': 'carmelite-holy-family',
        'order_name': 'Carmelite Order',
        'location': 'Awka, Anambra State',
        'region': 'Awka South',
        'summary': 'A Carmelite refuge of silent prayer, reflection, and devotion to Mary.',
        'description': 'The Carmelite Monastery is known for its deep love of prayer, the rosary, and contemplative life. Visitors find a serene atmosphere ideal for reflection, spiritual guidance, and quiet renewal.',
        'directions': 'Proceed toward the Carmelite lane in the Awka area and follow the signs to the monastery chapel and guest house.',
        'image_url': 'https://images.unsplash.com/photo-1494526585095-c41746248156',
        'is_published': True,
    },
]


class Command(BaseCommand):
    help = 'Seed the database with the default monastery records for Discover Monasteries.'

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for data in MONASTERIES:
            obj, created = Monastery.objects.update_or_create(
                slug=data['slug'],
                defaults=data,
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        total = Monastery.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f'Created {created_count} new monasteries, updated {updated_count}, total records: {total}.'
            )
        )
