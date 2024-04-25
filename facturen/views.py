from django.shortcuts import render
from rest_framework import generics

# Serializers import
from .serializers import (
    AdresSerializer,
    KlantSerializer,
    FactuurSerializer,
    FactuurRegelSerializer,
    AnnuleringSerializer
)

# Models import
from .models import (
    Adres, 
    Klant, 
    Factuur, 
    FactuurRegel, 
    Annulering
    )

class AdresList(generics.ListCreateAPIView):
    queryset = Adres.objects.all()
    serializer_class = AdresSerializer
    
class AdresDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adres.objects.all()
    serializer_class = AdresSerializer
    
class KlantList(generics.ListCreateAPIView):
    queryset = Klant.objects.all()
    serializer_class = KlantSerializer
    
class KlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klant.objects.all()
    serializer_class = KlantSerializer
    
class FactuurList(generics.ListCreateAPIView):
    queryset = Factuur.objects.all()
    serializer_class = FactuurSerializer
    
class FactuurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factuur.objects.all()
    serializer_class = FactuurSerializer
    
class FactuurRegelList(generics.ListCreateAPIView):
    queryset = FactuurRegel.objects.all()
    serializer_class = FactuurRegelSerializer
    
class FactuurRegelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactuurRegel.objects.all()
    serializer_class = FactuurRegelSerializer
    
class AnnuleringList(generics.ListCreateAPIView):
    queryset = Annulering.objects.all()
    serializer_class = AnnuleringSerializer
    
class AnnuleringDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annulering.objects.all()
    serializer_class = AnnuleringSerializer


