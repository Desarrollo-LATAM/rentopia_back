from django.contrib import admin

from .models import Tenant


class TenantAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "name",
        "last_name",
        "rating_user",
        "phone",
    )
    search_fields = ("name", "last_name", "phone")
    ordering = ("user_id",)


admin.site.register(Tenant, TenantAdmin)
