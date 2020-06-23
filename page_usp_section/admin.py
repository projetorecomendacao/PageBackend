from django.contrib import admin
from page_usp_section.models_0_page_usp import PageUsp
from page_usp_section.models_1_psicologico_usp import CognitionDeficitUsp, DepressionUsp, NegativeAttitudesAgingUsp, PsychologicalAspectsUsp
from page_usp_section.models_2_Biologicos_usp import BiologicalAspectsUsp, CardiovascularFactorsUsp, FunctionalDisabilityUsp, MalnutritionUsp, Medicines, MisuseMedicationsUsp, SensoryDeficitUsp
from page_usp_section.models_3_sociais_usp import EnvironmentalProblemsUsp, LowSocialSupportUsp, SocialAspectsUsp, ViolenceUsp
from page_usp_section.models_4_multidimensional_usp import FallsUsp, MultidisciplinaryDomainUsp

admin.site.register(PageUsp)
admin.site.register(CognitionDeficitUsp)
admin.site.register(NegativeAttitudesAgingUsp)
admin.site.register(DepressionUsp)
admin.site.register(PsychologicalAspectsUsp)
admin.site.register(SensoryDeficitUsp)
admin.site.register(FunctionalDisabilityUsp)
admin.site.register(MalnutritionUsp)
admin.site.register(CardiovascularFactorsUsp)
admin.site.register(MisuseMedicationsUsp)
admin.site.register(BiologicalAspectsUsp)
admin.site.register(LowSocialSupportUsp)
admin.site.register(EnvironmentalProblemsUsp)
admin.site.register(ViolenceUsp)
admin.site.register(SocialAspectsUsp)
admin.site.register(FallsUsp)
admin.site.register(MultidisciplinaryDomainUsp)
