from django.db import models
from core.models import Users
# from products.models import Products


# Create your models here.
class SellerProfile(models.Model):
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, null=False, blank=False)
    total_sales = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Профиль продавца"
        verbose_name_plural = "Профили продавцов"