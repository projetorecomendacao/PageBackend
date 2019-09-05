from django.db import models


class Drinks(models.Model):
    description = models.CharField(max_length=30)
    measure = models.CharField(max_length=30)

    class Meta:
        ordering = ['id']


class IngestedDrinks (models.Model):
    drink = models.ForeignKey(Drinks, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        ordering = ['id']
