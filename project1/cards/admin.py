from django.contrib import admin
from .models import Cards

# Register your models here.

class CardsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('URL Name',         {'fields': ['url_name']}),
        ('Card Name',        {'fields': ['card_name']}),
        ('Media Type',        {'fields': ['media_type']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]



admin.site.register(Cards, CardsAdmin)