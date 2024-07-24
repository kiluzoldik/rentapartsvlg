from django.contrib import admin

from places.models import Categories, Places


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    pass