from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.titre