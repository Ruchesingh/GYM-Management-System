from django.db import models

# Create your models here.

class Exercise(models.Model):
    DIFFICULTY_CHOICES = (
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    )

    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=50)
    equipment = models.CharField(max_length=100, blank=True)
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES
    )
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
    class WorkoutPlan(models.Model):
        
     member = models.ForeignKey(
        "member.Member",
        on_delete=models.CASCADE
    )

     trainer = models.ForeignKey(
        "trainer.Trainer",
        on_delete=models.CASCADE
    )

    plan_name = models.CharField(max_length=100)

    start_date = models.DateField()
    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plan_name
    
    
    