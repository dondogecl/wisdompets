from django.contrib import admin

from .models import Pet

#decorator
@admin.register(Pet)

class PetAdmin(admin.ModelAdmin):
    pass
