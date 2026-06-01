from django.contrib import admin

from subscription.models import GymMembership, Subscription

# Register your models here.

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'days',
        'price',
        'is_active',
        'created_at',
    )

    list_filter = (
        'is_active',
        'created_at',
    )

    search_fields = (
        'name',
    )

    ordering = (
        '-created_at',
    )

    list_editable = (
        'price',
        'is_active',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )
from django.contrib import admin
@admin.register(GymMembership)
class GymMembershipAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "member",
        "trainer",
        "subscription",
        "days",
        "price",
        "created_at",
    )

    list_filter = (
        "trainer",
        "created_at",
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)