from django.contrib import admin

# Register your models here.

from .models import Skaut
class SkautAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("prezdivka",) } 
    list_display = ["jmeno", "prezdivka", "splneno", "vek"]
    list_filter =  ["splneno", "vek"]
admin.site.register(Skaut, SkautAdmin)
