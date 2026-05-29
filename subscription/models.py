from django.db import models

# Create your models here.
class Subscription(models.Model):
    name=models.CharField(max_length=30)
    days=models.PositiveBigIntegerField(default=0)
    price=models.PositiveBigIntegerField(default=0)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
def __str__(self):
        return self.full_name
    