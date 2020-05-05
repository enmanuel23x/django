from django.contrib import admin
from .models import Carousel,JobOffer,Employees
# Titulo del panel
admin.site.site_header = 'Beconsult - Panel de administración'
class ListSniped(admin.ModelAdmin):
    list_display = ('Titulo','Creado','Actualizado')
    list_filter = ('Creado',)
    search_fields = ['Titulo']
    ordering = ['Actualizado', 'Creado']
class EmployeesSniped(admin.ModelAdmin):
    list_display = ('Nombre','Creado','Actualizado')
    list_filter = ('Creado','Titulo')
    search_fields = ['Nombre']
    ordering = ['Actualizado', 'Creado']
# Register your models here.
admin.site.register(Carousel, ListSniped)
admin.site.register(JobOffer, ListSniped)
admin.site.register(Employees, EmployeesSniped)
