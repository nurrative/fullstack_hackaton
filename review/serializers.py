from rest_framework.serializers import ModelSerializer
from .models import Comment, Rating, Like

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('user',)

        #так как наше поле user должен автоматичеки заполняться, то надо включить его в переменную exclude
    def validate(self, attrs):
        # но нам нужно добавить поле user в наш словарь с данными, поэтому переопределяем функцию validate
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance):
        #хотим внести доп инфу в блок user
        rep = super().to_representation(instance)
        rep['user'] = {
            'id': instance.user.id,
            'email': instance.user.email,
        }
        return rep

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        exclude = ('user',)

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return  attrs

    def create(self, validated_data): #хотим обновлять иди создавать новый рейтинг
        value = validated_data.pop('value')
        obj, created = Rating.objects.update_or_create(**validated_data, defaults={'value': value})
        return obj

    # def to_representation(self, instance):
    #     from playlists.serializers import PlaylistSerializer
    #
    #     rep = super().to_representation(instance)
    #     rep['playlist'] = PlaylistSerializer(instance.playlist).data
    #     return rep
