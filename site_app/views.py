from django.conf import settings
from django.shortcuts import render

from .models import Product

BRAND = 'Дерзновение'

VALUES = [
    ('Вера', 'Каждый принт — цитата из Писания, молитвы или иконописной традиции, а не просто украшение.'),
    ('Качество', 'Плотные ткани, чистая вышивка и шелкография. Вещь, которую носят годами.'),
    ('Сдержанность', 'Никакого пафоса: тёмные цвета, строгий крой и аккуратные детали.'),
]


def index(request):
    return render(request, 'site_app/index.html', {
        'brand': BRAND,
        'products': Product.objects.filter(is_active=True),
        'values': VALUES,
        'telegram_url': settings.TELEGRAM_URL,
    })
