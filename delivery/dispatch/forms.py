from django import forms
from .models import Dispatch

class dispatchriderForm(forms.ModelForm):
    class Meta:
        model = Dispatch
        fields = ['dispatchrider','status','complete']