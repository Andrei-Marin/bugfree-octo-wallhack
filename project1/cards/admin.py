from django.contrib import admin
from .models import Cards

# Register your models here.

class CardsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['owner']}),
        ('Card Name',        {'fields': ['card_name']}),
        ('URL Name',         {'fields': ['url_name']}),
        ('Image',             {'fields': ['image']}),
        ('Media Type',        {'fields': ['media_type']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]



admin.site.register(Cards, CardsAdmin)