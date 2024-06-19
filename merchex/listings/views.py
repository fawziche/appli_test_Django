from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm
from django.core.mail import send_mail


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands' : bands})


def band_detail(request, id):
    # L'id en paramètre est celui envoyé par l'url 
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band':band})


def band_add(request):

    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
           band = form.save()
           return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request, 'listings/band_add.html', {'form':form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    

    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
           band = form.save()
           return redirect('band-detail', band.id)

    else:
        form = BandForm(instance=band)  # on pré-remplit le formulaire avec un group    

    return render(request, 'listings/band_update.html', {'form':form})


def band_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        return redirect('band-list')
    
    return render(request, 'listings/band_delete.html', {'band':band})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings' : listings})


def contact(request):
    print("la méthode de requete est : ", request.method)
    print("Les données du post sont", request.POST)

    if request.method == "POST":
        # Si on vient sur cette page avec un POST ...
        # ... on remplit le formulaire avec les données du POST
        form = ContactUsForm(request.POST)

        # ... si le formulaire a été validé, on traite ces données
        if form.is_valid():
            send_mail (
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['fc_03@laposte.net'],
            )        
            return redirect("email-sent")
        
    else:
        #sinon on vient d'un GET. Dans ce cas, on veut un formulaire vierge
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form':form})