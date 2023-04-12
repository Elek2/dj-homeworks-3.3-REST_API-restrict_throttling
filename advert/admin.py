from django.contrib import admin

# Register your models here.
from advert.models import Advertisement, Favorites

class FavoriresInline(admin.TabularInline):
    model = Favorites


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'creator', 'draft']
    inlines = [
        FavoriresInline,
        ]

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ['user', 'advertisement']


