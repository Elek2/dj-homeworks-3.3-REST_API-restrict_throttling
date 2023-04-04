from django_filters import rest_framework as filters, DateFromToRangeFilter

from advert.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    #  DateFromToRangeFilter() автоматически добавляет 'created_at' в fields
    creator = filters.CharFilter(field_name='creator')
    #  Необязательная строчка (в DjangoFilterBackend уже реализована)

    class Meta:
        model = Advertisement
        fields = ['creator']

