from rest_framework import viewsets
from .models import Adres, Klant, Factuur, FactuurRegel, Annulering
from .serializers import AdresSerializer, KlantSerializer, FactuurSerializer, FactuurRegelSerializer, AnnuleringSerializer


def index(request):
    return render(request, 'facturen/index.html')

def klanten_lijst(request):
    klanten = Klant.objects.all()
    return render(request, 'facturen/klanten-lijst.html', {'klanten': klanten})

def facturen_lijst(request):
    facturen = Factuur.objects.all()
    return render(request, 'facturen/facturen-lijst.html', {'facturen': facturen})

def adressen_lijst(request):
    adressen = Adres.objects.all()
    return render(request, 'facturen/adressen-lijst.html', {'adressen': adressen})

class AdresViewSet(viewsets.ModelViewSet):
    queryset = Adres.objects.all()
    serializer_class = AdresSerializer


class KlantViewSet(viewsets.ModelViewSet):
    queryset = Klant.objects.all()
    serializer_class = KlantSerializer

class FactuurViewSet(viewsets.ModelViewSet):
    queryset = Factuur.objects.all()
    serializer_class = FactuurSerializer

class FactuurRegelViewSet(viewsets.ModelViewSet):
    queryset = FactuurRegel.objects.all()
    serializer_class = FactuurRegelSerializer

class AnnuleringViewSet(viewsets.ModelViewSet):
    queryset = Annulering.objects.all()
    serializer_class = AnnuleringSerializer



# create views for templates use template names: edit-adres.html, lijst-adressen.html, detail-adres.html, delete-adres.html

# Adressen CRUD
def maak_adres(request):
    return render(request, 'facturen/edit-adres.html')

def delete_adres(request):
    return render(request, 'facturen/delete-adres.html')

def detail_adres(request):
    return render(request, 'facturen/detail-adres.html')

def lijst_adressen(request):
    return render(request, 'facturen/lijst-adressen.html')

def edit_adres(request):
    return render(request, 'facturen/edit-adres.html')

# Klanten CRUD
def maak_klant(request):
    return render(request, 'facturen/edit-klant.html')

def delete_klant(request):
    return render(request, 'facturen/delete-klant.html')

def detail_klant(request):
    return render(request, 'facturen/detail-klant.html')

def lijst_klanten(request):
    return render(request, 'facturen/lijst-klanten.html')

# Facturen CRUD

def maak_factuur(request):
    return render(request, 'facturen/edit-factuur.html')

def delete_factuur(request):
    return render(request, 'facturen/delete-factuur.html')

def detail_factuur(request):
    return render(request, 'facturen/detail-factuur.html')

def lijst_facturen(request):
    return render(request, 'facturen/lijst-facturen.html')

# FactuurRegels CRUD

def maak_factuurregel(request):
    return render(request, 'facturen/edit-factuurregel.html')

def delete_factuurregel(request):
    return render(request, 'facturen/delete-factuurregel.html')

def detail_factuurregel(request):
    return render(request, 'facturen/detail-factuurregel.html')

def lijst_factuurregels(request):
    return render(request, 'facturen/lijst-factuurregels.html')

# Annuleringen CRUD

def maak_annulering(request):
    return render(request, 'facturen/edit-annulering.html')

def delete_annulering(request):
    return render(request, 'facturen/delete-annulering.html')

def detail_annulering(request):
    return render(request, 'facturen/detail-annulering.html')

def lijst_annulerings(request):
    return render(request, 'facturen/lijst-annulerings.html')


