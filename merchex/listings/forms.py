from django import forms
from listings.models import Band


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


# permet de transformer un "modele" en objet "formulaire"
class BandForm(forms.ModelForm):
   class Meta:
     model = Band
     fields = '__all__'
     # exclude = ('active', 'official_homepage')  si on veut exclure des champs du formulaire