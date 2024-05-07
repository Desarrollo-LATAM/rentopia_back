from django.contrib import admin

from apps.properties.models import Apartment, House, Land


class ApartmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "location",
        "price",
        "size",
        "num_bedrooms",
        "num_bathrooms",
        "num_floors",
    )
    search_fields = ("location", "price", "num_floors")
    ordering = ("price",)


class LandAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "location",
        "price",
        "size",
        "num_bedrooms",
        "num_bathrooms",
        "area",
    )
    search_fields = ("location", "price", "area")
    ordering = ("price",)


class HouseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "location",
        "price",
        "size",
        "num_bedrooms",
        "num_bathrooms",
        "num_floors",
    )
    search_fields = ("location", "price", "num_floors")
    ordering = ("price",)


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Land, LandAdmin)
admin.site.register(House, HouseAdmin)
