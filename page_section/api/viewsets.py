from rest_framework.response import Response
from rest_framework import status

from experts_section.models import Expert
from page_section.models_1_psicologico import NegativeAttitudesAging, CognitionDeficit, Depression, PsychologicalAspects
from page_section.models_2_Biologicos import BiologicalAspects, SensoryDeficit, FunctionalDisability, Malnutrition, CardiovascularFactors, MisuseMedications
from page_section.models_3_sociais import SocialAspects, LowSocialSupport, EnvironmentalProblems, Violence
from page_section.models_4_multidimensional import MultidisciplinaryDomain, Falls
from page_section.models_0_page import Page
from page_section.api.serializers import NegativeAttitudesAgingSerializer, CognitionDeficitSerializer,\
    DepressionSerializer, PsychologicalAspectsSerializer, BiologicalAspectsSerializer, SensoryDeficitSerializer,\
    FunctionalDisabilitySerializer, MalnutritionSerializer, CardiovascularFactorsSerializer,\
    MisuseMedicationsSerializer, SocialAspectsSerializer, LowSocialSupportSerializer, EnvironmentalProblemsSerializer,\
    ViolenceSerializer, MultidisciplinaryDomainSerializer, FallsSerializer, PageSerializer
from utils.api.serializer import CustomModelViewSet, IsExpert
from assessment_section.models import DemandMap
from participant_section.models import ParticipantSituation, Participant
from datetime import datetime


class NegativeAttitudesAgingViewSet(CustomModelViewSet):
    queryset = NegativeAttitudesAging.objects.all()
    serializer_class = NegativeAttitudesAgingSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class CognitionDeficitViewSet(CustomModelViewSet):
    queryset = CognitionDeficit.objects.all()
    serializer_class = CognitionDeficitSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class DepressionViewSet(CustomModelViewSet):
    queryset = Depression.objects.all()
    serializer_class = DepressionSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class PsychologicalAspectsViewSet(CustomModelViewSet):
    queryset = PsychologicalAspects.objects.all()
    serializer_class = PsychologicalAspectsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class BiologicalAspectsViewSet(CustomModelViewSet):
    queryset = BiologicalAspects.objects.all()
    serializer_class = BiologicalAspectsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class SensoryDeficitViewSet(CustomModelViewSet):
    queryset = SensoryDeficit.objects.all()
    serializer_class = SensoryDeficitSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class FunctionalDisabilityViewSet(CustomModelViewSet):
    queryset = FunctionalDisability.objects.all()
    serializer_class = FunctionalDisabilitySerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MalnutritionViewSet(CustomModelViewSet):
    queryset = Malnutrition.objects.all()
    serializer_class = MalnutritionSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class CardiovascularFactorsViewSet(CustomModelViewSet):
    queryset = CardiovascularFactors.objects.all()
    serializer_class = CardiovascularFactorsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MisuseMedicationsViewSet(CustomModelViewSet):
    queryset = MisuseMedications.objects.all()
    serializer_class = MisuseMedicationsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class SocialAspectsViewSet(CustomModelViewSet):
    queryset = SocialAspects.objects.all()
    serializer_class = SocialAspectsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class LowSocialSupportViewSet(CustomModelViewSet):
    queryset = LowSocialSupport.objects.all()
    serializer_class = LowSocialSupportSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class EnvironmentalProblemsViewSet(CustomModelViewSet):
    queryset = EnvironmentalProblems.objects.all()
    serializer_class = EnvironmentalProblemsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class ViolenceViewSet(CustomModelViewSet):
    queryset = Violence.objects.all()
    serializer_class = ViolenceSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class MultidisciplinaryDomainViewSet(CustomModelViewSet):
    queryset = MultidisciplinaryDomain.objects.all()
    serializer_class = MultidisciplinaryDomainSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


class FallsViewSet(CustomModelViewSet):
    queryset = Falls.objects.all()
    serializer_class = FallsSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert]
    }


# TODO - When deleting a page, the aspects altogether with participant_situation and so on must be deleted as well
class PageViewSet (CustomModelViewSet):
    serializer_class = PageSerializer
    permission_classes_by_action = {
        'create': [IsExpert],
        'partial_update': [IsExpert],
        'destroy': [IsExpert]
    }

    
    def get_queryset(self):
        # Define um filtro para retornar apenas os pages do gerontologista logado
        gerontologist = Expert.objects.get(email=self.request.user.email)
        return Page.objects.filter(gerontologist=gerontologist)

    # o PAGe é gravado inteiro, o front envia um objeto com todos os campos..
    def create(self,request, *args, **kwargs):
        print('Entrou...')
        
        # Aspectos psicológicos
        dados= request.data["psychologicalAspectsForm"]['cognitiveDeficitForm']
        cognitionDeficit = CognitionDeficit.objects.create(
            q1_memory_good_like_before= dados['q1_memory_good_like_before'],
            q2_memory_test= dados['q2_memory_test'],
            q2_memory_test_score= dados['q2_memory_test_score'],
            q3_language_function_attention= dados['q3_language_function_attention'],
            q3_language_function_attention_score= dados['q3_language_function_attention_score'],
            q3_language_function_attention_15= dados['q3_language_function_attention_15'],
            q3_language_function_attention_30= dados['q3_language_function_attention_30'],
            q3_language_function_attention_45= dados['q3_language_function_attention_45'],
            q3_language_function_attention_60= dados['q3_language_function_attention_60'],
            q4_visospatial_ability= dados['q4_visospatial_ability'],
            q4_visospatial_ability_score= dados['q4_visospatial_ability_score'],
            q5_praxia= dados['q5_praxia'],
            q5_praxia_score= dados['q5_praxia_score'],
            q6_memory_test= dados['q6_memory_test'],
            q6_memory_test_score= dados['q6_memory_test_score'],
            need_investigation_cognition= dados['need_investigation_cognition'],
            score = dados['score'],
            max_score_cognition=6
        )
                                                    
        dados= request.data["psychologicalAspectsForm"]['negativeAttitudesAgingForm']
        negativeAttitudesAging = NegativeAttitudesAging.objects.create(
            q7_age_self_perception= dados['q7_age_self_perception'],
            q7_age_self_perception_why= dados['q7_age_self_perception_why'],
            q7_age_self_perception_analyze= dados['q7_age_self_perception_analyze'],
            q8_aging_positive_points= dados['q8_aging_positive_points'],
            q8_aging_negative_points= dados['q8_aging_negative_points'],
            q8_aging_analyse= dados['q8_aging_analyse'],
            need_investigation_negative= dados['need_investigation_negative'],
            score= dados['score'],
            max_score_negative=2
        )


        dados= request.data["psychologicalAspectsForm"]['depressionForm']
        depression_ = Depression.objects.create(
            q9_satisfied_with_life= dados['q9_satisfied_with_life'],
            q10_frequently_sad= dados['q10_frequently_sad'],
            q11_stopped_doing_things= dados['q11_stopped_doing_things'],
            q12_fear_bad_things_happen= dados['q12_fear_bad_things_happen'],
            q13_impatient_disquiet= dados['q13_impatient_disquiet'],
            q14_concentration_problem= dados['q14_concentration_problem'],
            need_investigation_depression= dados['need_investigation_depression'],
            score= dados['score'],
            max_score_depression=6
        )

        dados= request.data["psychologicalAspectsForm"]["commentsForm"]
        psychologicalAspects_ = PsychologicalAspects.objects.create(
            cognition_deficit=cognitionDeficit,
            negative_attitudes_aging=negativeAttitudesAging,
            depression=depression_,
            comments_psico=dados['comments'],
            max_score_psico=14
        )

        # Biologicos
        dados = request.data["biologicalAspectsForm"]["sensoryDeficitForm"]
        sensoryDeficit_ = SensoryDeficit.objects.create(
            q15_vision_problems= dados['q15_vision_problems'],
            q16_hearing_problems= dados['q16_hearing_problems'],
            q17_taste_problems= dados['q17_taste_problems'],
            q18_senses_problems= dados['q18_senses_problems'],
            q19_interaction_problems= dados['q19_interaction_problems'],
            need_investigation_sensory= dados['need_investigation_sensory'],
            score= dados['score'],
            max_score_sensory=5
        )

        dados = request.data["biologicalAspectsForm"]["functionalDisabilityForm"]
        functionalDisability_ = FunctionalDisability.objects.create(
            q20_to_shop= dados['q20_to_shop'],
            q21_use_transport= dados['q21_use_transport'],
            q22_to_cook= dados['q22_to_cook'],
            q23UseTelephone= dados['q23UseTelephone'],
            q24_dress_up= dados['q24_dress_up'],
            q25TakeShower= dados['q25TakeShower'],
            need_investigation_functional= dados['need_investigation_functional'],
            score= dados['score'],
            max_score_functional=6
        )

        dados = request.data["biologicalAspectsForm"]["malnutritionForm"]
        malnutrition_ = Malnutrition.objects.create(
            q26_yourself_malnourished= dados['q26_yourself_malnourished'],
            q27_chewing_mouth_problems= dados['q27_chewing_mouth_problems'],
            q28_less3_meal_daily= dados['q28_less3_meal_daily'],
            q29_decreases_amount_food= dados['q29_decreases_amount_food'],
            q30_lost_weight_no_reason= dados['q30_lost_weight_no_reason'],
            q30_lost_weight_no_reason_amount= dados['q30_lost_weight_no_reason_amount'],
            q31_stress_illness_hospitalization= dados['q31_stress_illness_hospitalization'],
            q31_stress= dados['q31_stress'],
            q31_illnes= dados['q31_illnes'],
            q31_hospital= dados['q31_hospital'],
            q32_bmi_less22= dados['q32_bmi_less22'],
            score = dados['score'],
            need_investigation_malnutrition= dados['need_investigation_malnutrition'],
            max_score_malnutrition=7
        )

        dados = request.data["biologicalAspectsForm"]["cardiovascularFactorsForm"]
        cardiovascularFactors_ = CardiovascularFactors.objects.create (
            q33_dcv_familiar_history= dados['q33_dcv_familiar_history'],
            q34_hypertension= dados['q34_hypertension'],
            q34_hypertension_unknow= dados['q34_hypertension_unknow'],
            q35_uncontrolled_diabetes= dados['q35_uncontrolled_diabetes'],
            q35_unknown_value_glycemia= dados['q35_unknown_value_glycemia'],
            q36_cholesterol= dados['q36_cholesterol'],
            q36_unknown_value_ct_hdl= dados['q36_unknown_value_ct_hdl'],
            q37_smoker= dados['q37_smoker'],
            q38_practice_150_minutes_exercises= dados['q38_practice_150_minutes_exercises'],
            q39_healthy_eating= dados['q39_healthy_eating'],
            q40_alcohol_Ingested_last_week= dados['q40_alcohol_Ingested_last_week'],
            q40_alcohol_Ingested_last_week_amount= dados['q40_alcohol_Ingested_last_week_amount'],
            q41_bmi_obesity= dados['q41_bmi_obesity'],
            need_investigation_cardio= dados['need_investigation_cardio'],
            score = dados['score'],
            max_score_cardio=9
        )

        dados = request.data["biologicalAspectsForm"]["misuseMedicationsForm"]
        misuseMedications_ = MisuseMedications.objects.create(
            q42_diseases_last_5_years_a= dados['q42_diseases_last_5_years_a'],
            q42_diseases_last_5_years_b= dados['q42_diseases_last_5_years_b'],
            q42_diseases_last_5_years_c= dados['q42_diseases_last_5_years_c'],
            q42_diseases_last_5_years_d= dados['q42_diseases_last_5_years_d'],
            q42_diseases_last_5_years_e= dados['q42_diseases_last_5_years_e'],
            q42_diseases_last_5_years_f= dados['q42_diseases_last_5_years_f'],
            q42_diseases_last_5_years_g= dados['q42_diseases_last_5_years_g'],
            q42_diseases_last_5_years_h= dados['q42_diseases_last_5_years_h'],
            q42_diseases_last_5_years_i= dados['q42_diseases_last_5_years_i'],
            q42_diseases_last_5_years_j= dados['q42_diseases_last_5_years_j'],
            q42_diseases_last_5_years_k= dados['q42_diseases_last_5_years_k'],
            q42_diseases_last_5_years_l= dados['q42_diseases_last_5_years_l'],
            q43_health_problems_a= dados['q43_health_problems_a'],
            q43_health_problems_b= dados['q43_health_problems_b'],
            q43_health_problems_c= dados['q43_health_problems_c'],
            q43_health_problems_d= dados['q43_health_problems_d'],
            q43_health_problems_e= dados['q43_health_problems_e'],
            q43_health_problems_f= dados['q43_health_problems_f'],
            q43_health_problems_g= dados['q43_health_problems_g'],
            q43_health_problems_h= dados['q43_health_problems_h'],
            q44_amount_diagnostics= dados['q44_amount_diagnostics'],
            q45_medicines= dados['q45_medicines'],
            q46_medicines_increase= dados['q46_medicines_increase'],
            q47_know_medicines= dados['q47_know_medicines'],
            q48_medications_prescribed= dados['q48_medications_prescribed'],
            q49_medicine_medical_advice= dados['q49_medicine_medical_advice'],
            q50_already_stopped_medicines= dados['q50_already_stopped_medicines'],
            q51_self_medication= dados['q51_self_medication'],
            q52_inappropriate_medication= dados['q52_inappropriate_medication'],
            q53_risk_adverse_reaction= dados['q53_risk_adverse_reaction'],
            need_investigation_misuse= dados['need_investigation_misuse'],
            score = dados['score'],
            max_score_misuse=9
        )

        dados = request.data["biologicalAspectsForm"]["commentsForm"]
        biologicalAspects_ = BiologicalAspects.objects.create(sensoryDeficit=sensoryDeficit_,
                                            functionalDisability=functionalDisability_,
                                            malNutrition = malnutrition_,
                                            cardiovascularFactors = cardiovascularFactors_,
                                            misuseMedications = misuseMedications_,
                                            comments_bio = dados['comments'],
                                            max_score_bio=36)


        # Social Aspects
        dados = request.data["socialAspectsForm"]["lowSocialSupportForm"]
        lowSocialSupport_ = LowSocialSupport.objects.create(
            q54_spouse= dados['q54_spouse'],
            q54_mother= dados['q54_mother'],
            q54_father= dados['q54_father'],
            q54_brothers= dados['q54_brothers'],
            q54_children= dados['q54_children'],
            q54_gran_children= dados['q54_gran_children'],
            q55_meet_family_friends= dados['q55_meet_family_friends'],
            q56_participate_family_decisions= dados['q56_participate_family_decisions'],
            q57_satisfied_family_relationship= dados['q57_satisfied_family_relationship'],
            q58_helped_if_need_money= dados['q58_helped_if_need_money'],
            q59_someone_helps_if_need= dados['q59_someone_helps_if_need'],
            q60_someone_to_have_fun= dados['q60_someone_to_have_fun'],
            q61_participate_social_events= dados['q61_participate_social_events'],
            q62_regulary_healt_services= dados['q62_regulary_healt_services'],
            need_investigation_low= dados['need_investigation_low'],
            score = dados['score'],
            max_score_low=8
        )

        dados = request.data["socialAspectsForm"]["environmentalProblemsForm"]
        environmentalProblems_ = EnvironmentalProblems.objects.create(
            q63_estable_furniture= dados['q63_estable_furniture'],
            q64_loose_objects_carpets= dados['q64_loose_objects_carpets'],
            q65_slippery_floor= dados['q65_slippery_floor'],
            q66_handrail_on_stairs= dados['q66_handrail_on_stairs'],
            q67_lighted_stairs= dados['q67_lighted_stairs'],
            q68_suitable_stairs_steps= dados['q68_suitable_stairs_steps'],
            q69_non_slippery_carpet= dados['q69_non_slippery_carpet'],
            q70_get_on_stool= dados['q70_get_on_stool'],
            q71_turn_lights_off= dados['q71_turn_lights_off'],
            q72_safe_shoes= dados['q72_safe_shoes'],
            q73_manicure_sidewalks= dados['q73_manicure_sidewalks'],
            q74_public_transport_access= dados['q74_public_transport_access'],
            q75_commerce_access= dados['q75_commerce_access'],
            q76_ease_plasewalking= dados['q76_ease_plasewalking'],
            q77_fun_access= dados['q77_fun_access'],
            q78_safety= dados['q78_safety'],
            score = dados['score'],
            max_score_env=16
        )

        dados = request.data["socialAspectsForm"]["violenceForm"]
        violence_ = Violence.objects.create(
            q79_afraid_close_person= dados['q79_afraid_close_person'],
            q80_feels_abandoned= dados['q80_feels_abandoned'],
            q81_forced= dados['q81_forced'],
            q82_assauteld= dados['q82_assauteld'],
            q83_in_need= dados['q83_in_need'],
            q84_someone_used_money= dados['q84_someone_used_money'],
            q85_touched_without_permission= dados['q85_touched_without_permission'],
            q86_dont_take_care_health= dados['q86_dont_take_care_health'],
            need_investigation_violence= dados['need_investigation_violence'],
            score= dados['score'],
            max_score_violence=8
        )

        dados = request.data["socialAspectsForm"]["commentsForm"]
        socialAspects_ = SocialAspects.objects.create(lowSocialSupport=lowSocialSupport_,
                                    environmentalProblems=environmentalProblems_,
                                    violence=violence_,
                                    comments_social = dados['comments'],
                                    maxScore_social=32)

        # multidimensional
        dados = request.data["multidimensionalAspectsForm"]["fallsForm"]
        falls_ = Falls.objects.create(
            q87_falls_last_year= dados['q87_falls_last_year'],
            q87_amount_falls_last_year= dados['q87_amount_falls_last_year'],
            q88_fractures_due_to_falls= dados['q88_fractures_due_to_falls'],
            q88_fractures_due_to_falls_list= dados['q88_fractures_due_to_falls_list'],
            q89_fractures_list= dados['q89_fractures_list'],
            q90_strength_mmii= dados['q90_strength_mmii'],
            q91_equilibrium= dados['q91_equilibrium'],
            q92_older_than75= dados['q92_older_than75'],
            q93_female= dados['q93_female'],
            q94_cognitive_alterations= dados['q94_cognitive_alterations'],
            q95_av_ds_commitment= dados['q95_av_ds_commitment'],
            q96_visual_deficit= dados['q96_visual_deficit'],
            q97_domestic_risks= dados['q97_domestic_risks'],
            q98_behavior_risk= dados['q98_behavior_risk'],
            q99_inactivity= dados['q99_inactivity'],
            q100_prior_ave= dados['q100_prior_ave'],
            q101_psychotropic_medications_use= dados['q101_psychotropic_medications_use'],
            q102_has_diseases= dados['q102_has_diseases'],
            need_investigation_falls= dados['need_investigation_falls'],
            score= dados['score'],
            max_score_falls=16
        )

        dados = request.data["multidimensionalAspectsForm"]["commentsForm"]
        multidisciplinaryDomain_ =  MultidisciplinaryDomain.objects.create(
            falls=falls_,
            comments_multi = dados['comments'],
            maxScore_multi=16
        )

        #Situação participant
        dados = request.data["participantFormForm"]
        participanteSituation_ = ParticipantSituation.objects.create(   
            p02_address= dados['p02_address'],
            p03_communication= dados['p03_communication'],
            p07_marital_status= dados['p07_marital_status'],
            p08_schooling= dados['p08_schooling'],
            p09_study_time= dados['p09_study_time'],
            p10_is_retired= dados['p10_is_retired'],
            p10_actual_profession= dados['p10_actual_profession'],
            p11_retire_more_time_activity= dados['p11_retire_more_time_activity'],
            p12_is_working_professionals_activities= dados['p12_is_working_professionals_activities'],
            p12_professional_activities= dados['p12_professional_activities'],
            p13_income_I= dados['p13_income_I'],
            p13_income_F= dados['p13_income_F'],
            p14_lives_with= dados['p14_lives_with'],
            p15_has_religion= dados['p15_has_religion'],
            p15_religion= dados['p15_religion'],
            p16_health_self_report= dados['p16_health_self_report'],
            p20_weight= dados['p20_weight'],
            p20_height= dados['p20_height'],
            p20_IMC= dados['p20_IMC'],
            p30_car= dados['p30_car'],
            p30_bus= dados['p30_bus'],
            p30_uber= dados['p30_uber'],
            p30_ride= dados['p30_ride'],
            p30_ride_with= dados['p30_ride_with'],
            p31_comments= dados['p31_comments'],
        )

        #demand map
        demand_map_ = DemandMap.objects.create(
            dm3_unmet_demands = '',
            gerontologist_assessment =  '',
            demands_problems = '',
            goals = '',
            actions_organization = '',
            coordenation_implementation = '',
            control = '',
        )

        # Dados do cabecalho do page
        dados = request.data["cabecaPageForm"]

        #participant
        participant_ = Participant.objects.get(id = dados["participant_id"])

        #especialista
        gerontologist_ = Expert.objects.get(id = dados["geronto_id"])

        page = Page.objects.create(
            service=dados['service'],
            entrance=datetime.strptime(dados['entrance'],'%Y-%m-%d'),
            interviewed=dados['interviewed'],
            interviewer=dados['interviewer'],
            avaliation_date=datetime.strptime(dados['avaliation_date'],'%Y-%m-%d'),
            gerontologist=gerontologist_,
            participant=participant_,
            participant_situation=participanteSituation_ ,
            psychologicalAspects=psychologicalAspects_ ,
            biologicalAspects = biologicalAspects_,
            socialAspects = socialAspects_,
            multidisciplinaryDomain = multidisciplinaryDomain_,
            demandMap= demand_map_
        )
        
        return Response ({'service': page.service,
            'entrance' : page.entrance,
            'interviewed' : page.interviewed,
            'interviewer' : page.interviewer,
            'avaliation_date' : page.avaliation_date,
            'gerontologist' : gerontologist_.pk,
            'participant' : participant_.pk,
            'participant_situation' : participanteSituation_.pk,
            'psychologicalAspects' : psychologicalAspects_.pk,
            'biologicalAspects' : biologicalAspects_.pk,
            'socialAspects' : socialAspects_.pk,
            'multidisciplinaryDomain' : multidisciplinaryDomain_.pk,
            'demandMap' : demand_map_.pk})

