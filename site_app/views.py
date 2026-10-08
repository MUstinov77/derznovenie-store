import json

from django.conf import settings
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.templatetags.static import static
from django.shortcuts import render

from .models import Product

BRAND = 'Дерзновение'

VALUES = [
    ('Вера', 'Каждый принт — цитата из Писания, молитвы или иконописной традиции, а не просто украшение.'),
    ('Качество', 'Плотные ткани, чистая вышивка и шелкография. Вещь, которую носят годами.'),
    ('Сдержанность', 'Никакого пафоса: тёмные цвета, строгий крой и аккуратные детали.'),
]


def index(request):
    canonical_url = request.build_absolute_uri('/')
    jsonld = json.dumps({
        '@context': 'https://schema.org',
        '@type': 'Organization',
        'name': BRAND,
        'url': canonical_url,
        'logo': request.build_absolute_uri(static('img/apple-touch-icon.png')),
        'sameAs': [settings.TELEGRAM_URL],
    }, ensure_ascii=False).replace('</', '<\\/')
    return render(request, 'site_app/index.html', {
        'canonical_url': canonical_url,
        'og_image_url': request.build_absolute_uri(static('img/og-image.png')),
        'jsonld': jsonld,
        'brand': BRAND,
        'products': Product.objects.filter(is_active=True),
        'values': VALUES,
        'telegram_url': settings.TELEGRAM_URL,
    })


def robots_txt(request):
    lines = [
        'User-agent: *',
        'Allow: /',
        f'Disallow: /{settings.ADMIN_URL}',
        f'Sitemap: {request.build_absolute_uri("/sitemap.xml")}',
    ]
    return HttpResponse('\n'.join(lines) + '\n', content_type='text/plain')


def sitemap_xml(request):
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f'<url><loc>{request.build_absolute_uri("/")}</loc></url>'
        '</urlset>\n'
    )
    return HttpResponse(xml, content_type='application/xml')


def favicon_ico(request):
    return HttpResponsePermanentRedirect(static('favicon.ico'))
