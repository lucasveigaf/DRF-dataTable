from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin
#from mptt.admin import DraggableMPTTAdmin


from risk.models import Risk#, Hazard



"""
class RiskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Risk, RiskAdmin)
"""

class RiskAdmin(DjangoMpttAdmin):
    pass
    
admin.site.register(Risk, RiskAdmin)

