
from django.contrib import admin
from .models import ServiceCategory, ServiceProduct

# ============================================================
# SERVICE CATEGORY ADMIN
# ============================================================

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "slug",
        "display_order",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "category",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "slug",
        "description",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "display_order",
        "name",
    )

    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "slug", "description", "category")
        }),
        ("Media & Display", {
            "fields": ("image", "display_order")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
    )
# ============================================================
# SERVICE PRODUCT ADMIN
# ============================================================

@admin.register(ServiceProduct)
class ServiceProductAdmin(admin.ModelAdmin):
    list_display = ("Product", "SC", "slug", "price", "is_active", "created_at")
    list_filter = ("SC", "is_active")
    search_fields = ("Product__model_name", "SC__name", "slug")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("Product__model_name",)
