from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} - {self.price}'


class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateField()

    class Meta:
        verbose_name = 'Закуп'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f'{self.item.name} bought {self.name}'
