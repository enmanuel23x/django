from django.contrib import admin
from .models import Carousel,JobOffer,Employees,Banner
# Titulo del panel
admin.site.site_header = 'Beconsult - Panel de administración'
class ListSniped(admin.ModelAdmin):
    list_display = ('Title','Created','Updated')
    list_filter = ('Created',)
    search_fields = ['Title']
    ordering = ['Updated', 'Created']
class EmployeesSniped(admin.ModelAdmin):
    list_display = ('Name','Created','Updated')
    list_filter = ('Created','Title')
    search_fields = ['Name']
    ordering = ['Updated', 'Created']
# Register your models here.
admin.site.register(Banner, ListSniped)
admin.site.register(Carousel, ListSniped)
admin.site.register(JobOffer, ListSniped)
admin.site.register(Employees, EmployeesSniped)
