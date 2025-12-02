from django.shortcuts import render, redirect, get_object_or_404
from .models import Membresia, Socio, Entrenador, Clase, ReservaClase, Pago, RutinaPersonalizada
from django.utils import timezone

def inicio_gimnasio(request):
    return render(request, 'inicio.html')

# --- MEMBRESIA ---
def agregar_membresia(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo_membresia')
        desc = request.POST.get('descripcion')
        costo = request.POST.get('costo')
        duracion = request.POST.get('duracion_meses')
        beneficios = request.POST.get('beneficios')
        sesiones = request.POST.get('num_sesiones_incluidas')
        # Checkbox devuelve 'on' si está marcado, o nada.
        activa = True if request.POST.get('es_activa') else False
        
        Membresia.objects.create(
            tipo_membresia=tipo, descripcion=desc, costo=costo,
            duracion_meses=duracion, beneficios=beneficios,
            num_sesiones_incluidas=sesiones, es_activa=activa
        )
        return redirect('ver_membresias')
    return render(request, 'membresia/agregar_membresia.html')

def ver_membresias(request):
    membresias = Membresia.objects.all()
    return render(request, 'membresia/ver_membresias.html', {'membresias': membresias})

def actualizar_membresia(request, id):
    membresia = get_object_or_404(Membresia, id=id)
    return render(request, 'membresia/actualizar_membresia.html', {'membresia': membresia})

def realizar_actualizacion_membresia(request, id):
    if request.method == 'POST':
        m = get_object_or_404(Membresia, id=id)
        m.tipo_membresia = request.POST.get('tipo_membresia')
        m.descripcion = request.POST.get('descripcion')
        m.costo = request.POST.get('costo')
        m.duracion_meses = request.POST.get('duracion_meses')
        m.beneficios = request.POST.get('beneficios')
        m.num_sesiones_incluidas = request.POST.get('num_sesiones_incluidas')
        m.es_activa = True if request.POST.get('es_activa') else False
        m.save()
        return redirect('ver_membresias')

def borrar_membresia(request, id):
    m = get_object_or_404(Membresia, id=id)
    m.delete()
    return redirect('ver_membresias')

# --- SOCIO (Ejemplo con Llave Foránea) ---
def agregar_socio(request):
    # Necesitamos enviar las membresías para el <select>
    membresias = Membresia.objects.filter(es_activa=True)
    if request.method == 'POST':
        Socio.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            genero=request.POST.get('genero'),
            direccion=request.POST.get('direccion'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            membresia_id=request.POST.get('membresia'), # _id para asignar FK directo
            fecha_vencimiento_membresia=request.POST.get('fecha_vencimiento_membresia')
        )
        return redirect('ver_socios')
    return render(request, 'socio/agregar_socio.html', {'membresias': membresias})

def ver_socios(request):
    socios = Socio.objects.all()
    return render(request, 'socio/ver_socios.html', {'socios': socios})

def actualizar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    membresias = Membresia.objects.all()
    return render(request, 'socio/actualizar_socio.html', {'socio': socio, 'membresias': membresias})

def realizar_actualizacion_socio(request, id):
    if request.method == 'POST':
        s = get_object_or_404(Socio, id=id)
        s.nombre = request.POST.get('nombre')
        s.apellido = request.POST.get('apellido')
        s.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        s.genero = request.POST.get('genero')
        s.direccion = request.POST.get('direccion')
        s.telefono = request.POST.get('telefono')
        s.email = request.POST.get('email')
        s.membresia_id = request.POST.get('membresia')
        s.fecha_vencimiento_membresia = request.POST.get('fecha_vencimiento_membresia')
        s.save()
        return redirect('ver_socios')

def borrar_socio(request, id):
    s = get_object_or_404(Socio, id=id)
    s.delete()
    return redirect('ver_socios')

# --- ENTRENADOR ---
def agregar_entrenador(request):
    if request.method == 'POST':
        Entrenador.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            especialidad=request.POST.get('especialidad'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            fecha_contratacion=request.POST.get('fecha_contratacion'),
            salario=request.POST.get('salario'),
            certificado=request.POST.get('certificado')
        )
        return redirect('ver_entrenadores')
    return render(request, 'entrenador/agregar_entrenador.html')

def ver_entrenadores(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'entrenador/ver_entrenadores.html', {'entrenadores': entrenadores})

def actualizar_entrenador(request, id):
    entrenador = get_object_or_404(Entrenador, id=id)
    return render(request, 'entrenador/actualizar_entrenador.html', {'entrenador': entrenador})

def realizar_actualizacion_entrenador(request, id):
    if request.method == 'POST':
        e = get_object_or_404(Entrenador, id=id)
        e.nombre = request.POST.get('nombre')
        e.apellido = request.POST.get('apellido')
        e.especialidad = request.POST.get('especialidad')
        e.telefono = request.POST.get('telefono')
        e.email = request.POST.get('email')
        e.fecha_contratacion = request.POST.get('fecha_contratacion')
        e.salario = request.POST.get('salario')
        e.certificado = request.POST.get('certificado')
        e.save()
        return redirect('ver_entrenadores')

def borrar_entrenador(request, id):
    get_object_or_404(Entrenador, id=id).delete()
    return redirect('ver_entrenadores')

# --- CLASE ---
def agregar_clase(request):
    entrenadores = Entrenador.objects.all()
    if request.method == 'POST':
        Clase.objects.create(
            nombre_clase=request.POST.get('nombre_clase'),
            descripcion=request.POST.get('descripcion'),
            horario=request.POST.get('horario'),
            duracion_minutos=request.POST.get('duracion_minutos'),
            entrenador_id=request.POST.get('entrenador'),
            cupo_maximo=request.POST.get('cupo_maximo'),
            costo_clase=request.POST.get('costo_clase'),
            nivel_dificultad=request.POST.get('nivel_dificultad')
        )
        return redirect('ver_clases')
    return render(request, 'clase/agregar_clase.html', {'entrenadores': entrenadores})

def ver_clases(request):
    clases = Clase.objects.all()
    return render(request, 'clase/ver_clases.html', {'clases': clases})

def actualizar_clase(request, id):
    clase = get_object_or_404(Clase, id=id)
    entrenadores = Entrenador.objects.all()
    return render(request, 'clase/actualizar_clase.html', {'clase': clase, 'entrenadores': entrenadores})

def realizar_actualizacion_clase(request, id):
    if request.method == 'POST':
        c = get_object_or_404(Clase, id=id)
        c.nombre_clase = request.POST.get('nombre_clase')
        c.descripcion = request.POST.get('descripcion')
        c.horario = request.POST.get('horario')
        c.duracion_minutos = request.POST.get('duracion_minutos')
        c.entrenador_id = request.POST.get('entrenador')
        c.cupo_maximo = request.POST.get('cupo_maximo')
        c.costo_clase = request.POST.get('costo_clase')
        c.nivel_dificultad = request.POST.get('nivel_dificultad')
        c.save()
        return redirect('ver_clases')

def borrar_clase(request, id):
    get_object_or_404(Clase, id=id).delete()
    return redirect('ver_clases')
# --- RESERVA CLASE ---
def agregar_reserva_clase(request):
    socios = Socio.objects.all()
    clases = Clase.objects.all()
    if request.method == 'POST':
        ReservaClase.objects.create(
            socio_id=request.POST.get('socio'),
            clase_id=request.POST.get('clase'),
            estado_reserva=request.POST.get('estado_reserva'),
            comentarios=request.POST.get('comentarios')
        )
        return redirect('ver_reservas_clase')
    return render(request, 'reserva_clase/agregar_reserva_clase.html', {'socios': socios, 'clases': clases})

def ver_reservas_clase(request):
    reservas = ReservaClase.objects.all()
    return render(request, 'reserva_clase/ver_reservas_clase.html', {'reservas': reservas})

def actualizar_reserva_clase(request, id):
    reserva = get_object_or_404(ReservaClase, id=id)
    socios = Socio.objects.all()
    clases = Clase.objects.all()
    return render(request, 'reserva_clase/actualizar_reserva_clase.html', {'reserva': reserva, 'socios': socios, 'clases': clases})

def realizar_actualizacion_reserva_clase(request, id):
    if request.method == 'POST':
        r = get_object_or_404(ReservaClase, id=id)
        r.socio_id = request.POST.get('socio')
        r.clase_id = request.POST.get('clase')
        r.estado_reserva = request.POST.get('estado_reserva')
        r.comentarios = request.POST.get('comentarios')
        r.save()
        return redirect('ver_reservas_clase')

def borrar_reserva_clase(request, id):
    get_object_or_404(ReservaClase, id=id).delete()
    return redirect('ver_reservas_clase')

# --- PAGO ---
def agregar_pago(request):
    socios = Socio.objects.all()
    membresias = Membresia.objects.all()
    if request.method == 'POST':
        Pago.objects.create(
            socio_id=request.POST.get('socio'),
            monto=request.POST.get('monto'),
            metodo_pago=request.POST.get('metodo_pago'),
            concepto=request.POST.get('concepto'),
            membresia_pagada_id=request.POST.get('membresia_pagada'),
            estado_pago=request.POST.get('estado_pago')
        )
        return redirect('ver_pagos')
    return render(request, 'pago/agregar_pago.html', {'socios': socios, 'membresias': membresias})

def ver_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'pago/ver_pagos.html', {'pagos': pagos})

def actualizar_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    socios = Socio.objects.all()
    membresias = Membresia.objects.all()
    return render(request, 'pago/actualizar_pago.html', {'pago': pago, 'socios': socios, 'membresias': membresias})

def realizar_actualizacion_pago(request, id):
    if request.method == 'POST':
        p = get_object_or_404(Pago, id=id)
        p.socio_id = request.POST.get('socio')
        p.monto = request.POST.get('monto')
        p.metodo_pago = request.POST.get('metodo_pago')
        p.concepto = request.POST.get('concepto')
        p.membresia_pagada_id = request.POST.get('membresia_pagada')
        p.estado_pago = request.POST.get('estado_pago')
        p.save()
        return redirect('ver_pagos')

def borrar_pago(request, id):
    get_object_or_404(Pago, id=id).delete()
    return redirect('ver_pagos')

# --- RUTINA PERSONALIZADA ---
def agregar_rutina_personalizada(request):
    socios = Socio.objects.all()
    entrenadores = Entrenador.objects.all()
    if request.method == 'POST':
        RutinaPersonalizada.objects.create(
            socio_id=request.POST.get('socio'),
            entrenador_id=request.POST.get('entrenador'),
            objetivo=request.POST.get('objetivo'),
            descripcion_ejercicios=request.POST.get('descripcion_ejercicios'),
            frecuencia=request.POST.get('frecuencia'),
            duracion_semanas=request.POST.get('duracion_semanas')
        )
        return redirect('ver_rutinas_personalizadas')
    return render(request, 'rutina_personalizada/agregar_rutina_personalizada.html', {'socios': socios, 'entrenadores': entrenadores})

def ver_rutinas_personalizadas(request):
    rutinas = RutinaPersonalizada.objects.all()
    return render(request, 'rutina_personalizada/ver_rutinas_personalizadas.html', {'rutinas': rutinas})

def actualizar_rutina_personalizada(request, id):
    rutina = get_object_or_404(RutinaPersonalizada, id=id)
    socios = Socio.objects.all()
    entrenadores = Entrenador.objects.all()
    return render(request, 'rutina_personalizada/actualizar_rutina_personalizada.html', {'rutina': rutina, 'socios': socios, 'entrenadores': entrenadores})

def realizar_actualizacion_rutina_personalizada(request, id):
    if request.method == 'POST':
        r = get_object_or_404(RutinaPersonalizada, id=id)
        r.socio_id = request.POST.get('socio')
        r.entrenador_id = request.POST.get('entrenador')
        r.objetivo = request.POST.get('objetivo')
        r.descripcion_ejercicios = request.POST.get('descripcion_ejercicios')
        r.frecuencia = request.POST.get('frecuencia')
        r.duracion_semanas = request.POST.get('duracion_semanas')
        r.save()
        return redirect('ver_rutinas_personalizadas')

def borrar_rutina_personalizada(request, id):
    get_object_or_404(RutinaPersonalizada, id=id).delete()
    return redirect('ver_rutinas_personalizadas')