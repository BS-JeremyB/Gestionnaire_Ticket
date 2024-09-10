from django.urls import path
from . import views

urlpatterns = [
    path('creation_ticket/', views.creer_ticket, name='creation_ticket'),
    path('liste_tickets/', views.liste_tickets, name='liste_tickets'),
    path('modifier_ticket/<int:pk>/', views.modifier_ticket, name='modifier_ticket'),
    path('supprimer_ticket/<int:pk>/', views.supprimer_ticket, name='supprimer_ticket'),
]
