from django.db import models
from django.utils import timezone


class Users(models.Model):          # класс пользователя
    name = models.CharField(max_length=20)         # имя максимальной длиной в 20 символов
    email = models.EmailField(unique=True)          # уникальное значение email
    password = models.CharField(max_length=20)     # пароль максимальной длинной в 20

    Role = [                            # массив с доступными ролями
        ('Покупатель', 'Buyer'),
        ('Продавец', 'Seller')
    ]

    role = models.CharField(max_length=10, choices=Role)        # поле с выбором роли Покупатель/Продавец
    created_at = models.DateTimeField(default=timezone.now, auto_now_add=True)          #  дата и время регистрации пользователя в магазине с учётом тайм зоны


class Categories(models.Model):         # класс категорий
    name = models.CharField(max_length=50)          # имя категории с максимальной длиной 50 символов

    parent = models.ForeignKey(
        'self',                     # ссылка на ту же модель
        null=True,                     # позволяет быть корневой директорией
        blank=True,                     # разрешает пустое значение в админке
        on_delete=models.CASCADE,           # при удалении родителя - удалит потомка
        related_name='children'             # доступ к подкатегориям
    )

    def __str__(self):          # для читаемости имени категории в магазине
        return self.name


