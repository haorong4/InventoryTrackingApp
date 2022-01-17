from django.db import models

class Item(models.Model):
    name = models.CharField(max_length = 100, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name} : {self.quantity}'
