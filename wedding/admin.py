from django.contrib import admin

from .models import Guest, ShuttleFrom, ShuttleTo

admin.site.register(Guest)
admin.site.register(ShuttleFrom)
admin.site.register(ShuttleTo)
