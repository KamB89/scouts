from django.contrib import admin

# Register your models here.

from .models import Skaut, Oddil
class SkautAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("prezdivka",) } 
    list_display = ["jmeno", "prezdivka", "splneno", "vek"]
    list_filter =  ["splneno", "vek"]
    
    class Oddiladmin(admin.ModelAdmin):
        list_display = ["jmeno", "heslo"]
admin.site.register(Skaut, SkautAdmin)
admin.site.register(Oddil)