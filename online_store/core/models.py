from django.db import models
from django.utils import timezone

class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    Role = [
        ('Покупатель', 'Buyer'),
        ('Продавец', 'Seller')
    ]

    role = models.CharField(max_length=10, choices=Role)
    created_at = models.DateTimeField(default=timezone.now)  # Убрать auto_now_add=True

class Categories(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )

    def __str__(self):
        return self.name