from django.contrib import admin

from dietPlan.models import DietPlan

# Register your models here.

@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "member",
        "plan_name",
        "total_calories",
        "is_active",
    )