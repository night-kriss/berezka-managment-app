from django.contrib import admin
from .models import *

from import_export.admin import ImportExportActionModelAdmin

admin.site.site_header = ' "Берёзка" Справка и Учёт'

@admin.register(Smena)
class SmenaModelAdmin(admin.ModelAdmin):
    list_filter = ["is_curent"]

@admin.register(Party)
class PartyModelAdmin(admin.ModelAdmin):
    list_filter = ["smena__is_curent"]

@admin.register(SocialOption)
class SocialOptionModelAdmin(admin.ModelAdmin):
    pass

@admin.register(StudyPlaceOption)
class StudyPlaceOptionModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Child)
class ChildModelAdmin(ImportExportActionModelAdmin):
    search_fields = ["second_name","first_name","third_name"]
    list_filter = ["party__smena__is_curent",  "sex", "region", "from_city", "social_type", "study_place_type", "party"]

    list_display = ["second_name","first_name","third_name", "sex", "social_type", "study_place_type" ]
    list_display_links = ["second_name","first_name","third_name"]

    fieldsets = [
        (
            None,
            {
                "fields": ["second_name","first_name","third_name", "party"],
            },
        ),
        (
            "Общие данные",
            {
                "fields": ["sex", "birth_date", "phone_number"],
            },
        ),
        (
            "Данные о месте жительства",
            {
                "fields": ["live_place_full", "region", "from_city"],
            },
        ),
        (
            "Данные о учереждении образования",
            {
                "fields": ["study_place_full", "study_place_type"],
            },
        ),
        (
            "Данные путёвке",
            {
                "fields": ["order_number", "order_state"],
            },
        ),
        (
            "Данные о социальном положении",
            {
                "fields": ["social_type"],
            },
        ),
        (
            "Данные о матери",
            {
                "fields": ["mother_full_name", "mother_birth_date", "mother_work", "mother_post", "mother_phone"],
            },
        ),
        (
            "Данные об отце",
            {
                "fields": ["father_full_name", "father_birth_date", "father_work", "father_post", "father_phone"],
            },
        ),
        (
            "Дополнительные данные",
            {
                "fields": ["comment"],
            },
        ),
    ]

    filter_horizontal = ["party"]