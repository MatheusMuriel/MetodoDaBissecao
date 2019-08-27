from django.db import models

# Create your models here.
class Calculo(models.Model):
    
    class Meta:
        db_table = 'calculo'

    funcao = models.CharField(max_length=200, null=True)
    x5 = models.IntegerField(null=True)
    x4 = models.IntegerField(null=True)
    x3 = models.IntegerField(null=True)
    x2 = models.IntegerField(null=True)
    x1 = models.IntegerField(null=True)
    xf = models.IntegerField(null=True)
    epsilon = models.IntegerField(null=True)
    criterioParada = models.IntegerField(null=True)

    def __str__(self):
        return self.funcao
