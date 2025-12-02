from django.contrib import admin
from .models import Membresia, Socio, Entrenador, Clase, ReservaClase, Pago, RutinaPersonalizada

admin.site.register(Membresia)
admin.site.register(Socio)
admin.site.register(Entrenador)
admin.site.register(Clase)
admin.site.register(ReservaClase)
admin.site.register(Pago)
admin.site.register(RutinaPersonalizada)