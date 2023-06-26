from django.db import models


# Create your models here.
class Lender(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=3, unique=True)
    upfront_commission_rate = models.DecimalField(max_digits=9, decimal_places=8)
    trial_commission_rate = models.DecimalField(max_digits=9, decimal_places=8)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
