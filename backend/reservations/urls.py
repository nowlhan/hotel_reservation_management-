from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChambreViewSet, ReservationViewSet, DashboardView

router = DefaultRouter()
router.register(r'chambres', ChambreViewSet)
router.register(r'reservations', ReservationViewSet)


urlpatterns = [
    path('', include(router.urls)),
   
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]