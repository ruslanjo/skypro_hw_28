from django.db import models


class Locations(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lng = models.DecimalField(max_digits=8, decimal_places=6)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserChoices:
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    MEMBER = 'member'
    CHOICES = (
        ('Администратор', ADMIN),
        ('Модератор', MODERATOR),
        ('Участник', MEMBER)
    )


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=40)
    role = models.CharField(max_length=15, choices=UserChoices.CHOICES, default='member')
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Locations)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
