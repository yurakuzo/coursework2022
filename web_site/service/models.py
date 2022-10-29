from django.db import models
from django.forms import CharField


class Haircuts(models.Model):
    service = models.CharField(max_length=50)
    price = models.IntegerField()
    duration = models.DurationField()

    def __str__(self) -> str:
        return f"{self.service}"

    class Meta:
        verbose_name = 'Стрижка'
        verbose_name_plural = 'Стрижки'
    
class Facial(models.Model):
    service = models.CharField(max_length=50)
    price = models.IntegerField()
    duration = models.DurationField()

    def __str__(self) -> str:
        return f"{self.service}"

    class Meta:
        verbose_name = 'Догляд за обличчям'
        verbose_name_plural = 'Догляд за обличчям'

class Hand_FootCare(models.Model):
    service = models.CharField(max_length=50)
    price = models.IntegerField()
    duration = models.DurationField()

    def __str__(self) -> str:
        return f"{self.service}"

    class Meta:
        verbose_name = 'Догляд за руками та ногами'
        verbose_name_plural = 'Догляд за руками та ногами'