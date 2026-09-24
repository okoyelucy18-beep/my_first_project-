from django.test import TestCase
from django.urls import reverse

from .forms import PrayerIntentForm, RetreatRequestForm
from .models import Monastery


class MonasterySiteTests(TestCase):
    def setUp(self):
        self.monastery = Monastery.objects.create(
            name='St. Benedict Monastery',
            slug='st-benedict-monastery',
            order_name='Order of Saint Benedict',
            location='Ozubulu, Anambra State',
            summary='A living beacon of Benedictine prayer and work.',
            description='Calm place of prayer and hospitality.',
            directions='Turn left at the main roundabout.',
        )

    def test_home_page_lists_monasteries(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'St. Benedict Monastery')

    def test_monastery_detail_page_works(self):
        response = self.client.get(reverse('monastery_detail', args=[self.monastery.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.monastery.name)

    def test_prayer_form_validates_required_fields(self):
        form = PrayerIntentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_retreat_form_validates_required_fields(self):
        form = RetreatRequestForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
from django.urls import reverse


class DiscoveryPagesTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Discover Monasteries')

    def test_monastery_pages_load(self):
        for route_name, heading in (
            ('holy-cross', 'Holy Cross Monastery'),
            ('st-benedict', 'St. Benedict Monastery'),
            ('carmelite', 'Carmelite Monastery'),
        ):
            with self.subTest(route_name=route_name):
                response = self.client.get(reverse(route_name))

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, heading)

    def test_support_pages_load(self):
        for route_name, page_title in (
            ('retreats', 'Plan a Sacred Retreat'),
            ('guidelines', 'Visitor Guidelines and Liturgy Hours'),
            ('prayer-intentions', 'Prayer Intentions'),
        ):
            with self.subTest(route_name=route_name):
                response = self.client.get(reverse(route_name))

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, page_title)
