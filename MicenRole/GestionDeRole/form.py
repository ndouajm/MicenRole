from django.forms import ModelForm
from .models import Roles
from django import forms

class RoleCreate(ModelForm):
    class Meta:
        model = Roles
        date_echeance = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
        
        fields = ('nom',
                'date_echeance',
                'type_document',
                'objet',
                'date_conseil',
                'etats',
                'economie',
                'observation_ct',
                'recommandation',
                'alert_impact',
                'commentaire',
                'document'
                )