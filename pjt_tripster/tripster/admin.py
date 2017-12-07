from django.contrib import admin
from tripster.models import Tripster

class TripsterAdmin(admin.ModelAdmin):
    list_display=('title','author','created',)

admin.site.register(Tripster, TripsterAdmin)