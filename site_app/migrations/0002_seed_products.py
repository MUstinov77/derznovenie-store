from django.db import migrations

PRODUCTS = [
    ('Худи «Покров»', 'Плотный футер, вышитый крест на груди', 6900, 'Худи'),
    ('Футболка «Ныне и присно»', 'Органический хлопок, принт на спине', 3200, 'Футболка'),
    ('Свитшот «Господи, помилуй»', 'Свободный крой, минималистичная вышивка', 5400, 'Свитшот'),
    ('Лонгслив «Свет Фаворский»', 'Мягкий трикотаж, тонкий принт на рукаве', 3900, 'Лонгслив'),
    ('Шапка «Крест»', 'Акрил с шерстью, вышивка по краю', 2100, 'Аксессуары'),
    ('Шоппер «Благодать»', 'Плотная хлопковая ткань, шелкография', 1500, 'Аксессуары'),
]


def seed(apps, schema_editor):
    Product = apps.get_model('site_app', 'Product')
    if Product.objects.exists():
        return
    for i, (name, desc, price, cat) in enumerate(PRODUCTS):
        Product.objects.create(name=name, description=desc, price=price, category=cat, order=i)


class Migration(migrations.Migration):
    dependencies = [('site_app', '0001_product')]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
