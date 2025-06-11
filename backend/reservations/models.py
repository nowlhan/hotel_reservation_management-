from django.db import models
from django.contrib.auth.models import AbstractUser

class Administrateur(AbstractUser):
    # Hérite de User (avec username, password, email...)
    poste = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username


class Chambre(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=50)
    statut = models.CharField(max_length=20, choices=[('Libre', 'Libre'), ('Occupée', 'Occupée')], default='Libre')  # libre / occupée / maintenance
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Chambre {self.numero} ({self.type})"


class Reservation(models.Model):
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    client_nom = models.CharField(max_length=100)
    client_contact = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=50)
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('CONFIRMEE', 'Confirmée'),
        ('ANNULEE', 'Annulée'),
    ]
   
   

    def __str__(self):
        return f"{self.client_nom} - {self.chambre.numero} ({self.date_debut} à {self.date_fin})"
