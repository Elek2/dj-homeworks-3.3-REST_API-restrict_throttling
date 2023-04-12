from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.admin import User
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advert.filters import AdvertisementFilter
from advert.models import Advertisement, Favorites
# from rest_framework.permissions import IsAuthenticated
from advert.permissions import IsAuthenticated
from advert.serializers import AdvertisementSerializer, FavoritesSerializer



def index(request):
    return redirect('api/')


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AdvertisementFilter
    search_fields = ['title', 'description']
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]   # если не указано в settings.py

    # Доп задание - статус DRAFT
    def list(self, request, *args, **kwargs):

        current_user = request.user.id  # id пользователя, напр. 1
        other_users = [i['id'] for i in User.objects.exclude(id=current_user).values('id')]
        # id остальных пользователей, напр. [2,3]
        queryset = Advertisement.objects.exclude(creator__in=other_users, draft=True)
        serializer = AdvertisementSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return []

# Доп задание - избранные объявления
    @action(detail=True, methods=['post'])  # detail=True - действия для всей модели
    def favorites(self, request, pk):
        """Избранное."""
        user = request.user  # Текущий пользователь
        adv = self.get_object()  # Текущее объявление

        if user != adv.creator:  # Если текущий пользователь - не создатель объявления
            favors = Favorites.objects.create(user=user, advertisement=adv)
            serializer = FavoritesSerializer(favors)
            return Response(serializer.data)
        else:
            return Response(
                'Нельзя добавлять свои объявления в избранное',
                status=400
            )

# Проверка избранных объявлений
    @action(detail=False, methods=['get'])  # detail=False - действия для отдельных объектов
    def f(self, request):
        """Избранное."""
        favors = Favorites.objects.all()
        serializer = FavoritesSerializer(favors, many=True)

        return Response(serializer.data)
