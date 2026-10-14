from django.test import TestCase

from .models import Product


class SiteSmokeTests(TestCase):
    def test_index_shows_active_products_only(self):
        Product.objects.create(name='Видимый', price=1000)
        Product.objects.create(name='Скрытый', price=2000, is_active=False)
        response = self.client.get('/')
        self.assertContains(response, 'Видимый')
        self.assertNotContains(response, 'Скрытый')

    def test_robots_and_sitemap(self):
        self.assertContains(self.client.get('/robots.txt'), 'Sitemap:')
        self.assertEqual(self.client.get('/sitemap.xml').status_code, 200)
