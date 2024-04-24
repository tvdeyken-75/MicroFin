from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from . import models

class FactuurForm(ModelForm):
    class Meta:
        model = models.Factuur
        fields = '__all__'
        
FactuurRegelFormSet = inlineformset_factory(
    models.Factuur,
    models.FactuurRegel,
    fields=['uitvoerdatum', 'uitvoerreferentie', 'opmerking', 'subbedrag', 'extra', 'regelbedrag'],
    extra=1,
    can_delete=True
)

# Formset voor Annulering welke een 1 op 1 relatie met Factuur heeft
AnnuleringFormSet = inlineformset_factory(
    models.Factuur,
    models.Annulering,
    fields=['datum', 'reden', 'volbedrag', 'bedrag'],
    extra=1,
    can_delete=True
) 
        
class AdresForm(ModelForm):
    class Meta:
        model = models.Adres
        fields = '__all__'
        
        
class KlantForm(ModelForm):
    class Meta:
        model = models.Klant
        fields = '__all__'

 