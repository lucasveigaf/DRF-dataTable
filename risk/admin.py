from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin
#from mptt.admin import DraggableMPTTAdmin


from risk.models import Risk, Responses, Country




class CountryAdmin(DjangoMpttAdmin):
    pass
    
admin.site.register(Country, CountryAdmin)



class RiskAdmin(DjangoMpttAdmin):
    pass
    
admin.site.register(Risk, RiskAdmin)



class ResponsesAdmin(admin.ModelAdmin):
    list_display = ('risk', 'responsesCategory', 'description')

admin.site.register(Responses, ResponsesAdmin)

