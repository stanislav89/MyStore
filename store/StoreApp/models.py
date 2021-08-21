from django.db import models
from django.contrib.auth.models import AbstractUser


# My models
class Product(models.Model):
    SMARTPHONES = 'Smartphones'
    LAPTOPS = 'Laptops'
    GADGETS = 'Gadgets'
    AUDIO = 'Audio'
    PHOTO_VIDEO = 'Photo_Video'
    CATEGORY_CHOICES = [
        (SMARTPHONES, 'Smartphones'),
        (LAPTOPS, 'Laptops'),
        (GADGETS, 'Gadgets'),
        (AUDIO, 'Audio'),
        (PHOTO_VIDEO, 'Photo_Video'),
    ]
    # slug = models.SlugField(max_length=40, unique=True)
    product_category = models.CharField(choices=CATEGORY_CHOICES, max_length=25)
    image = models.ImageField(verbose_name='Product image')
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=120, verbose_name='Product name')
    text = models.TextField(max_length=999, verbose_name='Product description')
    price = models.PositiveIntegerField(verbose_name='Product price')
    amount = models.PositiveIntegerField(null=True, verbose_name='Amount of product')

    def __str__(self):
        return f'{self.product_category} ---  {self.name} ' \
               f'--- Price: {self.price} --- Amount: {self.amount}'

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
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    buy_time = models.DateTimeField(auto_now=True)
    input_amount = models.PositiveIntegerField(default=1, verbose_name='Amount of product for user')
    final_price = models.PositiveIntegerField(verbose_name='Final price')

    def __int__(self):
        return self.input_amount

    def __str__(self):
        return f'{self.product.name} --- Buyer: {self.buyer} --- Amount: {self.input_amount}  ' \
               f'--- Final price: {self.final_price} --- Buy time: {self.buy_time.strftime("%Y-%m-%d %H:%M:%S")}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
