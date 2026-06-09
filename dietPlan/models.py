from django.db import models

# Create your models here.

class DietPlan(models.Model):
    member = models.ForeignKey('member.Member',on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    breakfast = models.TextField()
    lunch = models.TextField()
    dinner = models.TextField()
    total_calories = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "dietPlan"

    def __str__(self):
        return f"{self.member.first}"
