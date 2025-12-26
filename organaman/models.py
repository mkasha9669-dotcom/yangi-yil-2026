from django.db import models

# Create your models here.
class Organdik(models.Model):
    mavzu = models.CharField(max_length=255)
    vaqt = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mavzu

class Tushundim(models.Model):
    organdik = models.ForeignKey(Organdik, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    vaqt = models.DateField()

    def __str__(self):
        return self.name