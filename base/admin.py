from django.contrib import admin
from .models import (
    Alumno,
    Nota
)

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Nota)