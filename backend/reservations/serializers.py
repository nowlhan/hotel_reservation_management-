from rest_framework import serializers
from .models import Chambre, Reservation

class ChambreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chambre
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    chambre = ChambreSerializer(read_only=True)
    chambre_id = serializers.PrimaryKeyRelatedField(
        queryset=Chambre.objects.all(), write_only=True, source='chambre'
    )



    class Meta:
        model = Reservation
        fields = ['id', 'chambre', 'chambre_id', 'client_nom', 'client_contact', 'date_debut', 'date_fin', 'statut']
        #read_only_fields = ['cree_par']
