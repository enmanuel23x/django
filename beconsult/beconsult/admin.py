from django.contrib import admin

# Register your models here.
from beconsult.models import Mails, Tittle, Message

admin.site.register(Mails)
admin.site.register(Tittle)
admin.site.register(Message)
