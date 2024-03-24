from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main.models import (
    MilitaryUnit,
    Application,
    Vehicles,
    Inspection,
    FuelType,
    Refuel,
    Add_fuels,

    
    
)

# class MilitaryUnitAdmin(UserAdmin):


# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(MilitaryUnit)
admin.site.register(FuelType)
admin.site.register(Vehicles)
admin.site.register(Application)
admin.site.register(Inspection)
admin.site.register(Refuel)
# admin.site.register(Add_fuels)




@admin.register(Add_fuels)
class Add_fuels(admin.ModelAdmin):
    list_display = (
        "yoq_nomi",
        "tank",
        "art",
        # "bmp",
        # "avto",
        # "uchuv",
        # "trak",
        # "maxs",
        # "ishab",
        "rim1",
        "rim2",
        "rim3",
        "rim4",
        "time",
    )

