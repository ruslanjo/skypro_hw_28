from django.db import models

from users.models import Users


class Categories(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ads(models.Model):
    name = models.CharField(max_length=400)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='ad')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, related_name='ad')

    class Meta:
        verbose_name = 'Обявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name
