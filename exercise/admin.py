from django.contrib import admin

# Register your models here.
from .models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "muscle_group",
        "difficulty",
        "equipment",
        "created_at",
    )

    list_filter = (
        "difficulty",
        "muscle_group",
    )

    search_fields = (
        "name",
        "muscle_group",
        "equipment",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )