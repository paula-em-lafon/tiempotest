from django.contrib import admin

from .models import CfdiModel

class CfdiAdmin(admin.ModelAdmin):
    pass
admin.site.register(CfdiModel, CfdiAdmin)
