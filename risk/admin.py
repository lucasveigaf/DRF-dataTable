from django.contrib import admin


from risk.models import Risk




class RiskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Risk, RiskAdmin)

