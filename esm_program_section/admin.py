from django.contrib import admin

from esm_program_section.models import ActiveEvent, Event, Program, ActionsEsm, Intervention, EditorProgram

admin.site.register(Program)
admin.site.register(ActionsEsm)
admin.site.register(ActiveEvent)
admin.site.register(Intervention)
admin.site.register(EditorProgram)
admin.site.register(Event)

# Register your models here.
