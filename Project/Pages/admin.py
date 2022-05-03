from django.contrib import admin
from django.utils.html import format_html

from .models import Team

# Register your models here.
# @admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def image_tag(self,obj):
        return format_html('<img src="{}" width="40  style="border-radius: 50px;" />'.format(obj.photo.url))
    
    image_tag.short_description = 'Thumbnail'
    
    
    list_display = ('id','image_tag','first_name','last_name','designation')
    list_display_links = ('id','image_tag','first_name')
    search_fields = ('first_name','last_name','designation')
    list_filter = ('designation',)

admin.site.register(Team,TeamAdmin)

