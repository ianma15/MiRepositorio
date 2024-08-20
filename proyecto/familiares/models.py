from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre


