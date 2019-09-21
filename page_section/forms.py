from django import forms
from .models import *

class CognitionDeficitForms(forms.ModelForm):
    class Meta:
        model = CognitionDeficit
        fields = ["q1_memory_good_like_before","q2_memory_test","q3_language_function_attention","q4_visospatial_ability","q4_visospatial_ability_score","q5_praxia",\
                  "q6_memory_test"]


class CognitionDeficitForms2(forms.ModelForm):
    class Meta:
        model = CognitionDeficit
        fields = ["need_investigation"]


class  NegativeAttitudesAgingForms(forms.ModelForm):
    class Meta:
        model= NegativeAttitudesAging
        fields = ["q7_age_self_perception","q7_age_self_perception_why","q7_age_self_perception_analyze","q8_aging_positive_points","q8_aging_negative_points", \
                  "q8_aging_analyse"]


class NegativeAttitudesAgingForms2(forms.ModelForm):
    class Meta:
        model = NegativeAttitudesAging
        fields = ["need_investigation"]


class DepressionForm(forms.ModelForm):
    class Meta:
        model = Depression
        fields = ["q9_satisfied_with_life","q10_frequently_sad","q11_stopped_doing_things","q12_fear_bad_things_happen","q13_impatient_disquiet","q14_concentration_problem"]


class DepressionForm2(forms.ModelForm):
    class Meta:
        model = Depression
        fields = ["need_investigation"]

class PsychologicalAspectsForm(forms.ModelForm):
    class Meta:
        model = PsychologicalAspects
        fields = ["comments"]


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ["date","p1_self_health_report"]


