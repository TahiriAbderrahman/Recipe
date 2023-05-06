from django import forms

from .models import Recette


class RecetteForm(forms.ModelForm):
    meta = Recette
    fields= ['categorie'] # or'__all__'
