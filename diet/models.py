from django.db import models

# Create your models here.
class DietPlan(models.Model):
    GOAL_CHOICES = (
        ("Weight Loss", "Weight Loss"),
        ("Weight Gain", "Weight Gain"),
        ("Muscle Gain", "Muscle Gain"),
    )

    member = models.ForeignKey(
        "member.Member",
        on_delete=models.CASCADE
    )

    trainer = models.ForeignKey(
        "trainer.Trainer",
        on_delete=models.CASCADE
    )

    goal = models.CharField(
        max_length=50,
        choices=GOAL_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)
    
    
