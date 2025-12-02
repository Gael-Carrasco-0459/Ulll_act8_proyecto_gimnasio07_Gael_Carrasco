from django.db import models

# --- MEMBRESIA ---
class Membresia(models.Model):
    tipo_membresia = models.CharField(max_length=50, verbose_name="Tipo de Membresía")
    descripcion = models.TextField(verbose_name="Descripción")
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_meses = models.IntegerField(verbose_name="Duración (Meses)")
    beneficios = models.TextField()
    num_sesiones_incluidas = models.IntegerField(verbose_name="Número de Sesiones")
    es_activa = models.BooleanField(default=True, verbose_name="¿Está activa?")

    def __str__(self):
        return f"{self.tipo_membresia} - ${self.costo}"

    class Meta:
        verbose_name = "Membresía"
        verbose_name_plural = "Membresías"

# --- SOCIO ---
class Socio(models.Model):
    GENERO_CHOICES = [('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)
    membresia = models.ForeignKey(Membresia, on_delete=models.SET_NULL, null=True, related_name="socios")
    fecha_vencimiento_membresia = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# --- ENTRENADOR ---
class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    certificado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    class Meta:
        verbose_name_plural = "Entrenadores"

# --- CLASE ---
class Clase(models.Model):
    nombre_clase = models.CharField(max_length=100)
    descripcion = models.TextField()
    horario = models.CharField(max_length=100, help_text="Ej: Lunes y Miércoles 10:00 AM")
    duracion_minutos = models.IntegerField()
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True, related_name="clases")
    cupo_maximo = models.IntegerField()
    costo_clase = models.DecimalField(max_digits=10, decimal_places=2)
    nivel_dificultad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_clase

# --- RESERVA CLASE ---
class ReservaClase(models.Model):
    ESTADO_CHOICES = [('Confirmada', 'Confirmada'), ('Pendiente', 'Pendiente'), ('Cancelada', 'Cancelada')]
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name="reservas")
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name="reservas")
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado_reserva = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='Confirmada')
    fecha_cancelacion = models.DateTimeField(null=True, blank=True)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reserva: {self.socio} - {self.clase}"
    class Meta:
        verbose_name = "Reserva de Clase"
        verbose_name_plural = "Reservas de Clases"

# --- PAGO ---
class Pago(models.Model):
    METODO_PAGO_CHOICES = [('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta de Crédito/Débito'), ('Transferencia', 'Transferencia')]
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name="pagos")
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO_CHOICES)
    concepto = models.CharField(max_length=100)
    membresia_pagada = models.ForeignKey(Membresia, on_delete=models.SET_NULL, null=True, blank=True)
    estado_pago = models.CharField(max_length=50, default='Pagado')

    def __str__(self):
        return f"Pago #{self.id} - {self.socio} - ${self.monto}"

# --- RUTINA PERSONALIZADA ---
class RutinaPersonalizada(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name="rutinas")
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True, related_name="rutinas_asignadas")
    fecha_creacion = models.DateField(auto_now_add=True)
    objetivo = models.CharField(max_length=100)
    descripcion_ejercicios = models.TextField()
    frecuencia = models.CharField(max_length=50, help_text="Ej: 3 veces por semana")
    duracion_semanas = models.IntegerField()

    def __str__(self):
        return f"Rutina para {self.socio} - {self.objetivo}"
    class Meta:
        verbose_name = "Rutina Personalizada"
        verbose_name_plural = "Rutinas Personalizadas"
