from django.contrib import admin
from institution_section.models import Cidade, Address, Locals, Professional, \
     Institution, AssistanceModality, WebAddress, Offers, Capacity

admin.site.register(Cidade)
admin.site.register(Address)
admin.site.register(Locals)
admin.site.register(Professional)
admin.site.register(Institution)
admin.site.register(AssistanceModality)
admin.site.register(WebAddress)
admin.site.register(Offers)
admin.site.register(Capacity)