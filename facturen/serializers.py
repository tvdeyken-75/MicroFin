from rest_framework import serializers
from .models import Adres, Klant, Factuur, FactuurRegel, Annulering

class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = '__all__'

class KlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klant
        fields = '__all__'

class FactuurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factuur
        fields = '__all__'

class FactuurRegelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactuurRegel
        fields = '__all__'

class AnnuleringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annulering
        fields = '__all__'
