from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(BotUsers)
class BotAdmin(admin.ModelAdmin):
    list_display =['name','t_id','language']
    list_filter = ['added','language']
    search_fields = ['name','t_id','language']