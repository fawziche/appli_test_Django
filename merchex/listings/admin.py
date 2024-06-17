from django.contrib import admin
from listings.models import Band, Listing

# Cette classe redefinit le tableau ds la gestion CRUD
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

admin.site.register(Band, BandAdmin)


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','description')

admin.site.register(Listing, ListingAdmin)
