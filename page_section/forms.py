from django import forms
from page_section.models_1_psicologico import NegativeAttitudesAging, CognitionDeficit, Depression, PsychologicalAspects
from page_section.models_2_Biologicos import BiologicalAspects, SensoryDeficit, FunctionalDisability, Malnutrition, CardiovascularFactors, MisuseMedications
from page_section.models_3_sociais import SocialAspects, LowSocialSupport, EnvironmentalProblems, Violence
from page_section.models_4_multidimensional import MultidisciplinaryDomain, Falls
from page_section.models_0_page import Page



class CognitionDeficitForms(forms.ModelForm):
    class Meta:
        model = CognitionDeficit
        fields = '__all__'

class  NegativeAttitudesAgingForms(forms.ModelForm):
    class Meta:
        model= NegativeAttitudesAging
        fields = '__all__'

class DepressionForm(forms.ModelForm):
    class Meta:
        model = Depression
        fields = '__all__'


class PsychologicalAspectsForm(forms.ModelForm):
    class Meta:
        model = PsychologicalAspects
        fields = '__all__'

class SensoryDeficitForm(forms.ModelForm):
    class Meta:
        model = SensoryDeficit
        fields = '__all__'

class FunctionalDisabilityForm(forms.ModelForm):
    class Meta:
        model= FunctionalDisability
        fields = '__all__'

class MalnutritionForm(forms.ModelForm):
    class Meta:
        model= Malnutrition
        fields = '__all__'

class CardiovascularFactorsForm(forms.ModelForm):
    class Meta:
        model= CardiovascularFactors
        fields = '__all__'

class MisuseMedicationsForm(forms.ModelForm):
    class Meta:
        model= MisuseMedications
        fields = ['q44_amount_diagnostics','q45_medicines','q46_medicines_increase','q47_know_medicines',
                  'q48_medications_prescribed','q49_medicine_medical_advice','q50_already_stopped_medicines',
                  'q51_self_medication','q52_inappropriate_medication','q53_risk_adverse_reaction',
                  'need_investigation', 'max_score']

class MisuseMedicationsForm42(forms.ModelForm):
    class Meta:
        model= MisuseMedications
        fields = ['q42_diseases_last_5_years_a', 'q42_diseases_last_5_years_b', 'q42_diseases_last_5_years_c',
                  'q42_diseases_last_5_years_d', 'q42_diseases_last_5_years_e', 'q42_diseases_last_5_years_f',
                  'q42_diseases_last_5_years_g', 'q42_diseases_last_5_years_h', 'q42_diseases_last_5_years_i',
                  'q42_diseases_last_5_years_j', 'q42_diseases_last_5_years_k', 'q42_diseases_last_5_years_l']

class MisuseMedicationsForm43(forms.ModelForm):
    class Meta:
        model= MisuseMedications
        fields = ['q43_health_problems_a', 'q43_health_problems_b', 'q43_health_problems_c', 'q43_health_problems_d',
                  'q43_health_problems_e', 'q43_health_problems_f',  'q43_health_problems_g','q43_health_problems_h']

class BiologicalAspectsForm(forms.ModelForm):
    class Meta:
        model= BiologicalAspects
        fields = '__all__'

class LowSocialSupportForm(forms.ModelForm):
    class Meta:
        model= LowSocialSupport
        fields = '__all__'

class EnvironmentalProblemsForm (forms.ModelForm):
    class Meta:
        model= EnvironmentalProblems
        fields = '__all__'

class ViolenceForm (forms.ModelForm):
    class Meta:
        model= Violence
        fields = '__all__'

class SocialAspectsForm (forms.ModelForm):
    class Meta:
        model= SocialAspects
        fields = '__all__'

class FallsForm (forms.ModelForm):
    class Meta:
        model= Falls
        fields = '__all__'

class MultidisciplinaryDomainForm (forms.ModelForm):
    class Meta:
        model= MultidisciplinaryDomain
        fields = '__all__'

class PageForm:
    class Meta:
        model= Page
        fields = '__all__'