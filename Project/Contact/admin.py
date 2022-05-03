from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ('id','first_name','last_name','car_title','message')
        list_display_links = ('id','first_name')
        search_fields = ('first_name','car_title')
admin.site.register(Contact)
