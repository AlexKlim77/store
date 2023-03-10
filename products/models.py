from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Назва категорії', max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Найменування продукта', max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукти'

    def __str__(self):
        return f'{self.name} | {self.category.name}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    creates_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    # def total_sum(self):
    #     baskets = Basket.objects.filter(user=self.user)
    #     return sum(basket.sum() for basket in baskets)
    #
    # def total_quantity(self):
    #     baskets = Basket.objects.filter(user=self.user)
    #     return sum(basket.quantity for basket in baskets)
