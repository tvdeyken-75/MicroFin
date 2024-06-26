from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Views import
from . import views

router = DefaultRouter()

urlpatterns = [
    # Token
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    
    path("adressen/", views.AdresList.as_view(), name="adressen"),
    path("adres/<int:pk>/", views.AdresDetail.as_view(), name="adres"),
    
    path("klanten/", views.KlantList.as_view(), name="klanten"),
    path("klant/<int:pk>/", views.KlantDetail.as_view(), name="klant"),
    
    path("facturen/", views.FactuurList.as_view(), name="facturen"),
    path("factuur/<int:pk>/", views.FactuurDetail.as_view(), name="factuur"),
    
    path("annuleren/", views.AnnuleringList.as_view(), name="annuleren"),
    path("annulering/<int:pk>/", views.AnnuleringDetail.as_view(), name="annulering"),

    path("factuurregels/", views.FactuurRegelList.as_view(), name="factuurregels"),
    path("factuurregel/<int:pk>/", views.FactuurRegelDetail.as_view(), name="factuurregel"),
]

