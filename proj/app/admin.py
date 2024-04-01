from django.contrib import admin

from . import models


class BreedAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "size", "friendliness", "trainability", "shedding_amount", "exercise_needs")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")
    search_help_text = "Поиска по ID или названию"
    list_filter = ("size", "friendliness", "trainability", "shedding_amount", "exercise_needs")

    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["name"],
            }
        ),
        (
            "Характеристики",
            {
                "fields": ["size", "friendliness", "trainability", "shedding_amount", "exercise_needs"],
            }
        )
    ]


class DogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "breed", "gender", "color")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")
    search_help_text = "Поиска по ID или названию"
    list_filter = ("age", "gender")


admin.site.register(models.Breed, BreedAdmin)
admin.site.register(models.Dog, DogAdmin)

admin.site.site_title = "Админ-панель"
admin.site.site_header = "Админ-панель"
