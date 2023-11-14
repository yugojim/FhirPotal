from django.contrib import admin

from .models import Permission,fhirip
#admin.site.register(Permission)
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    #list display
    list_display = ['user', 'patient', 'emergency', 'outpatient', 'inpatient', 'medication', 'report', 'administrative', 'up']
    #list Filter
    list_filter = ('user','dateTimeOfUpload')
    
#admin.site.register(fhirip)
@admin.register(fhirip)
class fhiripAdmin(admin.ModelAdmin):
    #list display
    list_display = ['location', 'ip', 'token', 'dateTimeOfUpload']
    #list Filter
    list_filter = ('location','dateTimeOfUpload')