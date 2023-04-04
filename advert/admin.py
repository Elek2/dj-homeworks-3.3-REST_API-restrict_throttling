from django.contrib import admin

# Register your models here.
from advert.models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    # pass
    list_display = ['id', 'title', 'status', 'creator']
