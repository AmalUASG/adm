from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import *


admin.site.register(Manufact)


# admin.site.register(Maintenance)
# admin.site.register(Variant)


class ModelAdmin(admin.ModelAdmin):
    list_display = ["model", "manufact","description"]
    search_fields = ["model", "manufact","description"]

class VariantAdmin(admin.ModelAdmin):
    list_display = ["model", "manufact","variant","locator","cc","description"]
    search_fields = ["model", "manufact","variant","locator","cc","description"]

class PriceAdmin(admin.ModelAdmin):
    list_display = ["model", "manufact","variant","pricelist","price"]
    search_fields = ["model", "manufact","variant","pricelist","price"]


admin.site.register(Model,ModelAdmin)

admin.site.register(Variant,VariantAdmin)
admin.site.register(Price,PriceAdmin)
admin.site.register(VM_10_VSPEC)
