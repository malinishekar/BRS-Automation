from django.contrib import admin
from .models import Venu
from .models import Event
from .models import MyclubUsers

#admin.site.register(Venu)
#admin.site.register(Event)
admin.site.register(MyclubUsers)
@admin.register(Venu)
class VenueAdmin(admin.ModelAdmin):
   list_display = ('name', 'address', 'phone')
   ordering = ('name',)
   search_fields = ('name', 'address')

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
   fields = (('name', 'Venue'), 'date', 'description', 'manager')
   list_display = ('name', 'date', 'Venue')
   list_filter = ('date', 'Venue')
   ordering = ('-date', )