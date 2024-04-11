from django import forms
from .models import Rider

class riderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ['riderid','username','name','location','availability','contactnum','password']
