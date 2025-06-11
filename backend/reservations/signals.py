# lorsqu'une réservation est créée, la chambre liée passe automatiquement à "Occupée" (ou un autre statut que tu souhaites).
# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reservation

@receiver(post_save, sender=Reservation)
def update_chambre_status(sender, instance, created, **kwargs):
    if created:
        chambre = instance.chambre
        chambre.statut = "réservé"  # ou "Réservée", à toi de voir
        chambre.save()
