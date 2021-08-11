from django.contrib import admin
from institution_section.models import Cidade, AddressPlace, Professional, \
     Institution, ActingArea, Offers, Capacity, Cidade, \
     ExpertiseAreas, AcademicEducation, WebAddressInstitution, \
     PhoneInstitution, EmailInstitution, TargetAudience, \
     LegalNature, PeopleType, PeopleSex, PeopleRangeAge, PeopleIncapacity,\
     TypeDigitalAddress


admin.site.register(Cidade)
admin.site.register(AddressPlace)
admin.site.register(Professional)
admin.site.register(Institution)
admin.site.register(ActingArea)
admin.site.register(Offers)
admin.site.register(Capacity)
admin.site.register(ExpertiseAreas)
admin.site.register(AcademicEducation)
admin.site.register(WebAddressInstitution)
admin.site.register(PhoneInstitution)
admin.site.register(EmailInstitution)
admin.site.register(TargetAudience)
admin.site.register(LegalNature)
admin.site.register(PeopleType)
admin.site.register(PeopleSex)
admin.site.register(PeopleRangeAge)
admin.site.register(PeopleIncapacity)
admin.site.register(TypeDigitalAddress)