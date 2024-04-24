from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Adres(models.Model):
    zoeknaam = models.CharField(max_length=255)
    bedrijfsnaam = models.CharField(max_length=255)
    straat = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    plaats = models.CharField(max_length=100)
    land = models.CharField(max_length=100)
    koordinaten = models.CharField(max_length=255, blank=True, null=True)  # Assuming coordinates are stored as string

    def __str__(self):
        return self.zoeknaam + ' - ' + self.bedrijfsnaam
    
    class Meta:
        verbose_name = "Adres"
        verbose_name_plural = "Adressen"

class Klant(models.Model):
    zoeknaam = models.CharField(max_length=255)
    bedrijfsnaam = models.CharField(max_length=255)
    hoofdadres = models.ForeignKey(Adres, on_delete=models.CASCADE)
    FIN = models.CharField(max_length=50)
    kontaktpersoon = models.CharField(max_length=255)
    telefoon = models.CharField(max_length=20)
    email = models.EmailField()
    bank = models.CharField(max_length=100)
    iban = models.CharField(max_length=34)
    bic = models.CharField(max_length=11)
    betalingsvoorwaarden = models.TextField()
    
    def __str__(self):
        return self.zoeknaam + ' - ' + self.bedrijfsnaam
    
    class Meta:
        verbose_name = "Klant"
        verbose_name_plural = "Klanten"

class Factuur(models.Model):
    class FactuurStatus(models.TextChoices):
        OPEN = 'OPEN', _('Open')
        BETAALD = 'BETAALD', _('Betaald')
        VERVALLEN = 'VERVALLEN', _('Vervallen')

    factuurnummer = models.CharField(max_length=50, editable=False)
    klant = models.ForeignKey(Klant, on_delete=models.CASCADE)
    factuurdatum = models.DateField(auto_now=True)
    verzenddatum = models.DateField(null=True, blank=True)
    betaaldatum = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=FactuurStatus.choices, default=FactuurStatus.OPEN)
    annulering = models.BooleanField(default=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    bedrag = models.DecimalField(max_digits=10, decimal_places=2)
    btw = models.DecimalField(max_digits=10, decimal_places=2)
    totaalbedrag = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.factuurnummer:
            self.factuurnummer = 'T-' + str(uuid.uuid4().int)[:6]  # Randomly generate number
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.factuurnummer
    
    class Meta:
        verbose_name = "Factuur"
        verbose_name_plural = "Facturen"

class FactuurRegel(models.Model):
    factuur = models.ForeignKey(Factuur, on_delete=models.CASCADE, related_name='regel_factuur')
    uitvoerdatum = models.DateField()
    uitvoerreferentie = models.CharField(max_length=255)
    opmerking = models.TextField(blank=True, null=True)
    subbedrag = models.DecimalField(max_digits=10, decimal_places=2)
    extra = models.DecimalField(max_digits=10, decimal_places=2)
    regelbedrag = models.DecimalField(max_digits=10, decimal_places=2)
    

class Annulering(models.Model):
    factuur = models.ForeignKey(Factuur, on_delete=models.CASCADE, related_name='annulering_factuur')
    datum = models.DateField()
    reden = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    volbedrag = models.BooleanField()
    bedrag = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if self.bedrag > 0:
            self.bedrag *= -1  # Ensure the amount is always negative
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.factuur + ' - ' + self.bedrag + ' - ' + self.reden
    
    class Meta:
        verbose_name = "Annulering"
        verbose_name_plural = "Annuleringen"
        
    
