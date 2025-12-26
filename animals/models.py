from django.db import models

# Create your models here.

class Hayvon(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    yesa_boladi = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Pet(models.Model):
    hayvon = models.ForeignKey(Hayvon, on_delete=models.CASCADE)
    parrandami = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hayvon