from django.db import models
class Шаурма(models.Model):
    shawarma_name =  models.CharField(max_length=50, verbose_name="Название шаурмы",blank=True,null=True)
    shawarma_ingredients = models.CharField(max_length=250, verbose_name="Ингридиенты шаурмы",blank=True,null=True)
    shawarma_price = models.FloatField(verbose_name="Цена шаурмы",blank=True,null=True)
# Create your models here.
def __str__(self):
    return self.project_name
class Meta:
 verbose_name = 'Проект'
 verbose_name_plural = 'Проекты'