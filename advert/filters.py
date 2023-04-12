from django_filters import rest_framework as filters, DateFromToRangeFilter, ModelChoiceFilter

from advert.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    #  DateFromToRangeFilter() автоматически добавляет 'created_at' в fields
    created_at = DateFromToRangeFilter()
    #  Необязательная строчка (в DjangoFilterBackend уже реализована)
    creator = filters.CharFilter(field_name='creator')
    #  Доп задание (фильтр по связанному полю user в избранных объявлениях)
    favor = filters.CharFilter(field_name='f__user')

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'favor']

