from django.forms import ModelForm
from .models import Roles
from django import forms

class RoleCreate(ModelForm):
    class Meta:
        model = Roles
        date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
        
        fields = ('nom',
                'date',
                'enfants',
                'date_conseil',
                'etats',
                'objet',
                'economie',
                'recommandation',
                'observation_ct',
                'order_jour',
                'document'
                )