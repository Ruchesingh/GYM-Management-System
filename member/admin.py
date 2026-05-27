from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "gender",
        "blood_group",
        "is_active",
        "joined_at",
        "created_at",
        "updated_at",   # ✅ added
    )

    list_filter = (
        "gender",
        "blood_group",
        "is_active",
        "joined_at",
    )

    search_fields = (
        "first_name",
        "last_name",
        "phone",
        "email",
    )

    ordering = ("-created_at",)

    # ✅ important: prevent manual editing of timestamps
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Personal Info", {
            "fields": ("first_name", "middle_name", "last_name", "dob", "gender")
        }),
        ("Contact Info", {
            "fields": ("phone", "email", "address", "emergency_contact")
        }),
        ("Health Info", {
            "fields": ("height_cm", "weight_kg", "blood_group", "medical_conditions")
        }),
        ("Membership Info", {
            "fields": ("joined_at", "is_active")
        }),
        ("System Info (Timestamps)", {   # ✅ new section
            "fields": ("created_at", "updated_at"),
        }),
    )