from django.contrib import admin
from .models import *


class HousingAdmin(admin.ModelAdmin):
    list_display = ["name", "housing_type", "address"]
    ordering = ["housing_type", "name"]

class Housing_PeopleAdmin(admin.ModelAdmin):
    list_display = ['people']

class Housing_BedAdmin(admin.ModelAdmin):
    list_display = ['beds']

class Housing_BathAdmin(admin.ModelAdmin):
    list_display = ['baths']

class StyleAdmin(admin.ModelAdmin):
    list_display = ["name", "people", "beds", "baths", "rent"]
    ordering = ['name', "people", "beds", "baths", "rent"]

class AmenityAdmin(admin.ModelAdmin):
    list_display = ['name']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["housing", "review", "rating", "active"]
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ["name", "pic1", "pic2", "pic3"]

# Register your models here.
admin.site.register(Housing, HousingAdmin)
admin.site.register(Housing_People, Housing_PeopleAdmin)
admin.site.register(Housing_Bed, Housing_BedAdmin)
admin.site.register(Housing_Bath, Housing_BathAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Images, ImagesAdmin)
