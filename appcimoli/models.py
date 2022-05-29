from django.db import models

# Create your models here.
class Deporte(models.Model):
    deporte=models.CharField(max_length=50)
    categoria=models.CharField(max_length=50)

    def __str__(self):
        return self.deporte, self.categoria

         