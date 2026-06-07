from django.db import models

# Create your models here.

class Status(models.TextChoices):
    INITIAL="Initial"
    COMPLETED="Completed"
    PENDING="Pending"
    USER_CANCELED="User canceled"

class TXN(models.Model):
    member=models.ForeignKey('member.Member',on_delete=models.RESTRICT)
    name=models.CharField(max_length=100,blank=True)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=20,choices=Status.choices,default=Status.INITIAL)
    txn_id=models.CharField(max_length=50,blank=True,null=True)
    pidx=models.CharField(max_length=30,null=True,blank=True)
    loaction=models.TextField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
