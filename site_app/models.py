from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=120)
    description = models.CharField('Описание', max_length=255, blank=True)
    price = models.PositiveIntegerField('Цена, ₽')
    category = models.CharField('Категория', max_length=60, blank=True)
    image = models.ImageField('Фото', upload_to='products/', blank=True)
    is_active = models.BooleanField('Показывать на сайте', default=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name

    @property
    def price_display(self):
        return f'{self.price:,}'.replace(',', ' ') + ' ₽'
