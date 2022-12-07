from django.contrib import admin

# Register your models here.
from .models import Play

class CustomPlayAdmin(admin.ModelAdmin):
    model = Play
    list_display=('name','desc','purchaser','img')
    list_filter=('name','desc')
    
    search_fields=('name','desc')
    fieldsets=(('Owner',{'fields':('purchaser',)}),('play info',{'fields':('name','desc','img')}),)

admin.site.register(Play,CustomPlayAdmin)