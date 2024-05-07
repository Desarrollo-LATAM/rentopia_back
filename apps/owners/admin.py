from django.contrib import admin

from .models import Owner


class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "name",
        "last_name",
        "address",
        "photo",
        "rating_user",
        "phone",
    )
    search_fields = ("name", "last_name", "phone")
    ordering = ("user_id",)


admin.site.register(Owner, OwnerAdmin)
