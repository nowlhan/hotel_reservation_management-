
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from .models import Chambre, Reservation
from .serializers import ChambreSerializer, ReservationSerializer

class ChambreViewSet(viewsets.ModelViewSet):
    queryset = Chambre.objects.all()
    serializer_class = ChambreSerializer
    permission_classes = [permissions.AllowAny]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.AllowAny] # tsy securisé fa mila mitady methode afa
    

    def perform_create(self, serializer):
        serializer.save()

class DashboardView(APIView):
    permission_classes = [permissions.AllowAny]  # Permet l'accès à tous, même aux non-authentifiés
    
    def get(self, request, *args, **kwargs):
        total_chambres = Chambre.objects.count()
        chambres_occupees = Chambre.objects.filter(statut='Occupée').count()
        chambres_disponibles = total_chambres - chambres_occupees
        reservations_encours = Reservation.objects.filter(statut='en attente').count()
        total_reservation = Reservation.objects.count()

        return Response({
            'total_chambres': total_chambres,
            'chambres_occupees': chambres_occupees,
            'chambres_disponibles': chambres_disponibles,
            'reservations_encours': reservations_encours,
            'total_reservation':total_reservation
        })



