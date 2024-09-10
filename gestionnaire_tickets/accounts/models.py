from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profil(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE) 
    numero_employe = models.CharField(max_length=50, blank=True, null=True)

    def genere_numero_employe(self):
        prenom = self.utilisateur.first_name[:2].lower()
        nom = self.utilisateur.last_name[:2].lower()
        date = timezone.now().strftime("%d%m%Y")

        self.numero_employe = f'{prenom}{nom}{date}'

    def __str__(self):
        return self.utilisateur.username

