from django import forms
from django.forms import modelformset_factory
from .models import Factuur, FactuurRegel, Annulering, Klant, Adres

class FactuurForm(forms.ModelForm):
    class Meta:
        model = Factuur
        fields = '__all__'
        exclude = ['user']
        
        # Datum should be datefield
        widgets = {
            'factuurdatum': forms.DateInput(attrs={'type': 'date'}),
            'verzenddatum': forms.DateInput(attrs={'type': 'date'}),
            'betaaldatum': forms.DateInput(attrs={'type': 'date'}),
        }
        

class FactuurRegelForm(forms.ModelForm):
    class Meta:
        model = FactuurRegel
        fields = '__all__'
        exclude = ['factuur']
        
        # Field Opmerking should be textfield
        widgets = {
            'opmerking': forms.Textarea(attrs={'rows': 3}),
            'uitvoerdatum': forms.DateInput(attrs={'type': 'date'}),
        }

FactuurRegelFormSet = modelformset_factory(
    FactuurRegel,
    form=FactuurRegelForm,
    extra=1,  # Aantal extra lege forms om te tonen
    can_delete=True  # Voeg een optie toe om factuurregels te verwijderen
)

# Uitbreiden met Adres en Klant forms

class AdresForm(forms.ModelForm):
    class Meta:
        model = Adres
        fields = '__all__'
        
class KlantForm(forms.ModelForm):
    class Meta:
        model = Klant
        fields = '__all__'
        
