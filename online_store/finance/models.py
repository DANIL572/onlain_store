from django.db import models
from django.core.validators import MinValueValidator
from core.models import Users



class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='account')
    balance = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    class CurrencyChoices(models.TextChoices):
        RUB = 'RUB', 'Рубль'
        USD = 'USD', 'Доллар США'
        EUR = 'EUR', 'Евро'
    currency = models.CharField(max_length=3, choices=CurrencyChoices.choices, default=CurrencyChoices.RUB)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'account'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.name} - {self.balance}{self.currency}'











