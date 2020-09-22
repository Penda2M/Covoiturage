from django.contrib import admin

from .models import *

admin.site.register(Person)
admin.site.register(Conducteur)
admin.site.register(Passager)
admin.site.register(Trajet)