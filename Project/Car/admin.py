from django.contrib import admin
from django.utils.html import format_html

from .models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    
    def image_tag(self,obj):
        return format_html('<img src="{}" width="40  style="border-radius: 50px;" />'.format(obj.car_photo.url))    
    image_tag.short_description = 'Thumbnail'
    
    list_display = ('id','image_tag','car_title','state','model','year','is_featured')
    list_display_links = ('id','image_tag','car_title')
    search_fields = ('car_title','model',)
    list_filter = ('model',)
    
admin.site.register(Car,CarAdmin)
