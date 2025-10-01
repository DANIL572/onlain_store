from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from products.models import Products

# Create your models here.
class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    STATUS_CHOICES = [
        # Предзаказ
        ('cart', 'В корзине'),
        ('pending', 'Ожидает подтверждения'),

        # Оплата
        ('awaiting_payment', 'Ожидает оплаты'),
        ('paid', 'Оплачен'),
        ('payment_failed', 'Ошибка оплаты'),

        # Обработка
        ('confirmed', 'Подтвержден'),
        ('processing', 'В обработке'),
        ('ready_for_shipment', 'Готов к отправке'),

        # Доставка
        ('shipped', 'Отправлен'),
        ('in_transit', 'В пути'),
        ('out_for_delivery', 'У курьера'),

        # Завершение
        ('delivered', 'Доставлен'),
        ('received', 'Получен покупателем'),

        # Проблемы
        ('cancelled', 'Отменен'),
        ('refunded', 'Возврат оформлен'),
        ('returned', 'Товар возвращен'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='cart')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        order_name = 'заказ'
        orders_name = 'заказы'
        ordering = ['-created_at']

class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    added_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('buyer_id', 'product_id') # Чтобы товар не дублировался
        ordering = ['-added_at']


class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2) # Цена на момент заказа
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('order', 'product') # Чтобы товар не дублировался в заказе