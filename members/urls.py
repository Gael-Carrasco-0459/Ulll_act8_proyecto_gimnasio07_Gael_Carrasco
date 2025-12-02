# members/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_gimnasio, name='inicio'),

    # --- MEMBRESIA ---
    path('membresia/agregar/', views.agregar_membresia, name='agregar_membresia'),
    path('membresia/ver/', views.ver_membresias, name='ver_membresias'),
    path('membresia/actualizar/<int:id>/', views.actualizar_membresia, name='actualizar_membresia'),
    path('membresia/actualizar/realizar/<int:id>/', views.realizar_actualizacion_membresia, name='realizar_actualizacion_membresia'),
    path('membresia/borrar/<int:id>/', views.borrar_membresia, name='borrar_membresia'),

    # --- SOCIO ---
    path('socio/agregar/', views.agregar_socio, name='agregar_socio'),
    path('socio/ver/', views.ver_socios, name='ver_socios'),
    path('socio/actualizar/<int:id>/', views.actualizar_socio, name='actualizar_socio'),
    path('socio/actualizar/realizar/<int:id>/', views.realizar_actualizacion_socio, name='realizar_actualizacion_socio'),
    path('socio/borrar/<int:id>/', views.borrar_socio, name='borrar_socio'),

    # --- ENTRENADOR ---
    path('entrenador/agregar/', views.agregar_entrenador, name='agregar_entrenador'),
    path('entrenador/ver/', views.ver_entrenadores, name='ver_entrenadores'),
    path('entrenador/actualizar/<int:id>/', views.actualizar_entrenador, name='actualizar_entrenador'),
    path('entrenador/actualizar/realizar/<int:id>/', views.realizar_actualizacion_entrenador, name='realizar_actualizacion_entrenador'),
    path('entrenador/borrar/<int:id>/', views.borrar_entrenador, name='borrar_entrenador'),

    # --- CLASE ---
    path('clase/agregar/', views.agregar_clase, name='agregar_clase'),
    path('clase/ver/', views.ver_clases, name='ver_clases'),
    path('clase/actualizar/<int:id>/', views.actualizar_clase, name='actualizar_clase'),
    path('clase/actualizar/realizar/<int:id>/', views.realizar_actualizacion_clase, name='realizar_actualizacion_clase'),
    path('clase/borrar/<int:id>/', views.borrar_clase, name='borrar_clase'),

    # --- RESERVA CLASE ---
    path('reserva/agregar/', views.agregar_reserva_clase, name='agregar_reserva_clase'),
    path('reserva/ver/', views.ver_reservas_clase, name='ver_reservas_clase'),
    path('reserva/actualizar/<int:id>/', views.actualizar_reserva_clase, name='actualizar_reserva_clase'),
    path('reserva/actualizar/realizar/<int:id>/', views.realizar_actualizacion_reserva_clase, name='realizar_actualizacion_reserva_clase'),
    path('reserva/borrar/<int:id>/', views.borrar_reserva_clase, name='borrar_reserva_clase'),

    # --- PAGO ---
    path('pago/agregar/', views.agregar_pago, name='agregar_pago'),
    path('pago/ver/', views.ver_pagos, name='ver_pagos'),
    path('pago/actualizar/<int:id>/', views.actualizar_pago, name='actualizar_pago'),
    path('pago/actualizar/realizar/<int:id>/', views.realizar_actualizacion_pago, name='realizar_actualizacion_pago'),
    path('pago/borrar/<int:id>/', views.borrar_pago, name='borrar_pago'),

    # --- RUTINA PERSONALIZADA ---
    path('rutina/agregar/', views.agregar_rutina_personalizada, name='agregar_rutina_personalizada'),
    path('rutina/ver/', views.ver_rutinas_personalizadas, name='ver_rutinas_personalizadas'),
    path('rutina/actualizar/<int:id>/', views.actualizar_rutina_personalizada, name='actualizar_rutina_personalizada'),
    path('rutina/actualizar/realizar/<int:id>/', views.realizar_actualizacion_rutina_personalizada, name='realizar_actualizacion_rutina_personalizada'),
    path('rutina/borrar/<int:id>/', views.borrar_rutina_personalizada, name='borrar_rutina_personalizada'),
]