from django.urls import path, include
from .views import index, PriceAPI, PricesilverAPI, latest
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'goldprices', PriceAPI)
router.register(r'silverprices', PricesilverAPI)

urlpatterns = [
    path('', index, name="index"),
    path('', include(router.urls)),
    path('latest', latest, name="latest"),
]
