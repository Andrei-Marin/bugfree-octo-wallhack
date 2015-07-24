from rest_framework import serializers, viewsets

from .models import Cards

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards

class CardsViewSet(viewsets.ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
