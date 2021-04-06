from django.contrib import admin
from activities_section.models import Characteristic, Benefit, Restriction, Type, Activity


admin.site.register(Characteristic)
admin.site.register(Benefit)
admin.site.register(Restriction)
admin.site.register(Type)
admin.site.register(Activity)

