from django.shortcuts import render, redirect
from .forms import FactuurForm, FactuurRegelFormSet, AdresForm, KlantForm
from .models import Factuur, FactuurRegel, Annulering, Klant, Adres


# Create a home page view

def home(request):
    return render(request, 'facturen/index.html')

def facturen_lijst(request):
    facturen = Factuur.objects.all()
    return render(request, 'facturen/facturen-lijst.html', {
        'facturen': facturen
    })

def klanten_lijst(request):
    klanten = Klant.objects.all()
    return render(request, 'facturen/klanten-lijst.html', {
        'klanten': klanten
    })

def adressen_lijst(request):
    adressen = Adres.objects.all()
    return render(request, 'facturen/adressen-lijst.html', {
        'adressen': adressen
    })

def create_factuur(request):
    if request.method == 'POST':
        form = FactuurForm(request.POST)
        formset = FactuurRegelFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            factuur = form.save(commit=False)
            factuur.user = request.user
            factuur.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.factuur = factuur
                instance.save()
            formset.save_m2m()
            return redirect('facturen:home')  # Verander naar een geldige redirect URL
        else:
            print(form.errors, formset.errors)  # Dit zal helpen om te zien wat er mis gaat als er iets niet valideert
    else:
        form = FactuurForm()
        formset = FactuurRegelFormSet(queryset=FactuurRegel.objects.none())

    return render(request, 'facturen/maak-factuur.html', {
        'form': form,
        'formset': formset
    })



def create_adres(request):
    if request.method == 'POST':
        form = AdresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturen:home')
    else:
        form = AdresForm()

    return render(request, 'facturen/maak-adres.html', {
        'form': form
    })


def create_klant(request):
    if request.method == 'POST':
        form = KlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturen:home')
    else:
        form = KlantForm()

    return render(request, 'facturen/maak-klant.html', {
        'form': form
    })
    
def delete_adres(request, pk):
    adres = Adres.objects.get(id=pk)
    adres.delete()
    return redirect('facturen:home')

def delete_klant(request, pk):
    klant = Klant.objects.get(id=pk)
    klant.delete()
    return redirect('facturen:home')


