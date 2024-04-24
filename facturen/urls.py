from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AdresViewSet, KlantViewSet, FactuurViewSet, FactuurRegelViewSet, AnnuleringViewSet

router = DefaultRouter()
router.register(r'adressen', AdresViewSet)
router.register(r'klanten', KlantViewSet)
router.register(r'facturen', FactuurViewSet)
router.register(r'factuurregels', FactuurRegelViewSet)
router.register(r'annuleringen', AnnuleringViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
