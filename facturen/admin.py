from django.contrib import admin
from . import models
# Register your models here.

register = admin.site.register

# Zet factuur en factuurregel als formset in de admin

class FactuurRegelInline(admin.TabularInline):
    model = models.FactuurRegel
    extra = 1
    
class FactuurAdmin(admin.ModelAdmin):
    inlines = [FactuurRegelInline]

register(models.Factuur, FactuurAdmin)
register(models.Annulering)
register(models.Klant)
register(models.Adres)

