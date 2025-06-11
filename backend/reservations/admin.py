from django.contrib import admin

from .models import Reservation
from .models import Chambre

admin.site.register(Reservation)
admin.site.register(Chambre)