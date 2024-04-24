from django.urls import path
from facturen.views import (
        home,
        klanten_lijst,
        facturen_lijst,
        adressen_lijst,
        create_factuur,
        create_adres,
        create_klant,
        delete_adres,
        delete_klant
    )

app_name = 'facturen'

urlpatterns = [
    path('', home, name='home'),
    path('klanten-lijst/', klanten_lijst, name='klanten-lijst'),
    path('facturen-lijst/', facturen_lijst, name='facturen-lijst'),
    path('adressen-lijst/', adressen_lijst, name='adressen-lijst'),
    
    path('maak-factuur/', create_factuur, name='maak-factuur'),
    path('maak-adres/', create_adres, name='maak-adres'),
    path('maak-klant/', create_klant, name='maak-klant'),
    
    path('delete-adres/<int:pk>/', delete_adres, name='delete-adres'),
    path('delete-klant/<int:pk>/', delete_klant, name='delete-klant'),
]


