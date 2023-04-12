from django.contrib.auth.models import User
from rest_framework import serializers

from advert.models import Advertisement, Favorites


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
        # many=True
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', 'draft')

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        adverts = Advertisement.objects.filter(creator__id=self.context["request"].user.id).filter(status='OPEN')
        adverts_count = adverts.count()
        if adverts_count >= 10 and data['status'] != 'CLOSED':
            raise serializers.ValidationError("У пользователя не может быть больше 10 открытых объявлений")
        return data


class FavoritesSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = Favorites
        fields = ('user', 'advertisement')
