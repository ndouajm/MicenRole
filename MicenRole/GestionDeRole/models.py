from django.db import models
from django import forms
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Roles(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    TYPE_DOCUMENT_CHOICES = [
        ('projet_de_loi_ordinaire', 'PROJET DE LOI ORDINAIRE'),
        ('projet_de_loi_organique', 'PROJET DE LOI ORGANIQUE'),
        ('projet_ordonnance', "PROJET D'ORDONNANCE"),
        ('projet_decret', 'PROJET DE DECRET'),
        ('projet_communication', 'PROJET DE COMMUNICATION')
    ]
    
    nom = models.CharField(("Nom"), max_length=30)
    
    date_echeance = models.DateField(("Date d'écheance"))
    
    type_document = models.CharField(
        max_length=70,
        choices=TYPE_DOCUMENT_CHOICES,
        default='projet_de_loi_ordinaire',
        verbose_name='Type Document',
        null=True,
        blank=True
    )
    
    objet = models.CharField(("Objet"), max_length=500, null=True)
    
    date_conseil = models.DateTimeField()
    
    etats = models.CharField(max_length=20, choices=[
        ('N/D', ' Nom demarrer'), 
        ('ENCOURS', 'En cours'), 
        ('TERMINER', 'Terminer'),
        ('ANNULER', 'Annuler')
        ],
        default='N/D',
        null=True
    )
    
    
    economie = models.TextField(("Economie"), max_length=2000, null=True)
    observation_ct = models.TextField(("Observation"), max_length=2000, null=True)
    recommandation = models.TextField(("Recommandation"), max_length=2000, null=True)
    alert_impact = models.TextField(("Alert / Impact"), max_length=2000, null=True)
    commentaire = models.TextField(('COmmentaire Du CT GOORE BI'), max_length=2000, null=True)

    document = models.FileField(
        upload_to='documents/',
        verbose_name='Document',
        null=True,
        blank=True
    )
    
    def get_document_url(self):
        if self.document:
            return settings.MEDIA_URL + str(self.document)
        return None
    
    def get_absolute_url(self):
        return reverse('role_detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = ("Role")
        verbose_name_plural = ("Roles")
        
    def __str__(self):
        return self.nom
    
    
    
   
    
   
    
    
    
        