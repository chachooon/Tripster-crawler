from django.contrib import admin
from tipster.models import Tipster

class TipsterAdmin(admin.ModelAdmin):
    list_display=('title','author','created',)

admin.site.register(Tipster, TipsterAdmin)