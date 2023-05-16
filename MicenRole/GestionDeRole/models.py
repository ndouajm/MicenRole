from django.db import models
from django import forms
from django.urls import reverse

# Create your models here.

class Roles(models.Model):
    
    nom = models.CharField(("Nom"), max_length=30)
    
    date = models.DateField(("Date d'ajout"))
    
    enfants = models.IntegerField(("Nombres d'enfants"))
    
    date_conseil = models.DateTimeField()
    
    etats = models.CharField(max_length=20, choices=[
        ('N/D', ' Nom demarrer'), 
        ('ENCOURS', 'En cours'), 
        ('TERMINER', 'Terminer'),
        ('ANNULER', 'Annuler')
        ])
    
    objet = models.CharField(("Objet"), max_length=500, null=True)
    economie = models.TextField(("Economie"), max_length=2000, null=True)
    recommandation = models.TextField(("Recommandation"), max_length=2000, null=True)
    observation_ct = models.TextField(("Observation"), max_length=2000, null=True)
    order_jour = models.CharField(("Ordre Du Jour"), max_length=100, null=True)
    
    document = models.FileField(
        upload_to='./static/img',
        verbose_name='Document',
        null=True,
        blank=True
    )
    
    def get_absolute_url(self):
        return reverse('role_detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = ("Role")
        verbose_name_plural = ("Roles")
        
    def __str__(self):
        return self.nom
    
    
    
    # TYPE_DOCUMENT_CHOICES = [
    #     ('projet_de_loi_ordinaire', 'PROJET DE LOI ORDINAIRE'),
    #     ('projet_de_loi_organique', 'PROJET DE LOI ORGANIQUE'),
    #     ('projet_ordonnance', "PROJET D'ORDONNANCE"),
    #     ('projet_decret', 'PROJET DE DECRET'),
    #     ('projet_communication', 'PROJET DE COMMUNICATION')
    # ]
    # type_document = models.CharField(
    #     max_length=70,
    #     choices=TYPE_DOCUMENT_CHOICES,
    #     default='projet_de_loi_ordinaire',
    #     verbose_name='Type Document',
    #     null=True,
    #     blank=True
    # )
    
   
    
    
    
        