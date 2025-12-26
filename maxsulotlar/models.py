from django.db import models

# Create your models here.

class Narsa(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class KerakliNarsa(models.Model):
    narsa = models.ForeignKey(Narsa, on_delete=models.CASCADE)
    discount = models.IntegerField(default=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.narsa.name