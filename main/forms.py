from django import forms
from main.models import Trajet

class TrajetForm(forms.ModelForm):
   class Meta:
        model = Trajet
        fields = '__all__'