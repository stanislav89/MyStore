from django.db import models
from django.contrib.auth.models import AbstractUser


# My models
class Articles(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=120, verbose_name='Product name')
    text = models.TextField(max_length=250, verbose_name='Product description')
    price = models.PositiveIntegerField(verbose_name='Product price')
    amount = models.PositiveIntegerField(null=True, verbose_name='Amount of product')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'


class User(AbstractUser):
    money = models.PositiveIntegerField(default=10000)
    # orders = models.ManyToManyField('Purchase', verbose_name='User purchases', related_name='related_user')

    def __int__(self):
        return self.money

    class Meta:
        verbose_name = 'Profile'


class Purchase(models.Model):
    buyer = models.ForeignKey(User, related_name='buyer', on_delete=models.CASCADE)
    product = models.ForeignKey(Articles, related_name='product', on_delete=models.CASCADE)
    buy_time = models.DateTimeField(auto_now=True)
    input_amount = models.PositiveIntegerField(default=1, verbose_name='Amount of product for user')
    final_price = models.PositiveIntegerField(verbose_name='Final price')

    def __int__(self):
        return self.input_amount

    def __str__(self):
        return f'Product: {self.product.name} --- Buyer: {self.buyer} --- Buy time: {self.buy_time}'

    def save(self, *args, **kwargs):
        # self.final_price = self.input_amount * self.product.price
        super().save(*args, **kwargs)
