from django.contrib import admin
from .models import Cabinet, Company, AdditionalOffice, Collaborator


admin.site.register(Cabinet)
admin.site.register(AdditionalOffice)
admin.site.register(Collaborator)
admin.site.register(Company)
