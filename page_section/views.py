from django.shortcuts import render
from django.http import HttpResponse

from experts_section.models import Gerontologist, Expert
from .forms import *
from datetime import datetime
from .lista_atividades import ListaAtividades
from .recommender import Recommender



def testar(request):
    depressionForm = DepressionForm()
    cognitionDeficitForms = CognitionDeficitForms ()
    negativeAttitudesAgingForms = NegativeAttitudesAgingForms ()
    psychologicalAspectsForm = PsychologicalAspectsForm()
    sensoryDeficitForm = SensoryDeficitForm()
    functionalDisabilityForm = FunctionalDisabilityForm()
    malnutritionForm = MalnutritionForm()
    cardiovascularFactorsForm = CardiovascularFactorsForm()
    misuseMedicationsForm = MisuseMedicationsForm()
    misuseMedicationsForm42 = MisuseMedicationsForm42()
    misuseMedicationsForm43 = MisuseMedicationsForm43()
    biologicalAspectsForm = BiologicalAspectsForm()
    lowSocialSupportForm = LowSocialSupportForm()
    environmentalProblemsForm = EnvironmentalProblemsForm()
    violenceForm = ViolenceForm()
    socialAspectsForm = SocialAspectsForm ()
    fallsForm = FallsForm()
    multidisciplinaryDomainForm = MultidisciplinaryDomainForm()
    pageForm = PageForm()
    participantForm = ParticipantForm()
    participantSituationForm = ParticipantSituationForm()

    return render(request, 'page.html', {'cognition':cognitionDeficitForms,'depression': depressionForm, 'negative':
                  negativeAttitudesAgingForms, 'psychological': psychologicalAspectsForm,
                  'sensory' : sensoryDeficitForm, 'functional' : functionalDisabilityForm, 'malnutrition': malnutritionForm,
                  'cardiovascular' : cardiovascularFactorsForm, 'biological':biologicalAspectsForm,
                  'low_social' : lowSocialSupportForm, 'environmental': environmentalProblemsForm,
                  'violence' : violenceForm, 'social' : socialAspectsForm, 'falls' : fallsForm,
                  'multidisciplinary': multidisciplinaryDomainForm, 'page' : pageForm, 'misuse42' : misuseMedicationsForm42,
                   'misuse43': misuseMedicationsForm43, 'misuse' : misuseMedicationsForm, 'participant': participantForm,'participant_situation':participantSituationForm })

def abas(request):
    return render(request,'abas.html',{'texto':'Um texto qualquer'})

def monta_vet(q,m):
    qi = int(q)
    lista =['[5]','[10]','[20]','[20,10]','[20,20]','[20,20,10]','[20,20,20]','[20,20,20,10]','[20,20,20,20]','[20,20,20,20,10]','[20,20,20,20,20]']
    pos = int((100/m*qi)/10)
    return lista[pos]

def cria_vet(obj):
    pala = '[' + str(obj['Cognition']) + ',' + \
            str(obj['Attitude']) + ',' + \
            str(obj['Depression']) + ',' + \
            str(obj['Sensorial']) + ',' + \
            str(obj['Functional']) + ',' + \
            str(obj['Nutrition']) + ',' + \
            str(obj['Cardiovascular']) + ',' + \
            str(obj['Prescriptions']) + ',' + \
            str(obj['SocialSupport']) + ',' +  \
            str(obj['Environment']) + ',' + \
            str(obj['Violence']) + ',' + \
            str(obj['Falls']) + ']'
    return pala

def grava_page(request):
    data = request.POST
    cria_page(data)

    psico = int(data['c1']) + int(data['c2']) + int(data['c3'])
    biolo = int(data['c4']) + int(data['c5']) + int(data['c6']) + int(data['c7']) + int(data['c8'])
    socia = int(data['c9']) + int(data['c10']) + int(data['c11'])
    multi = int(data['c12'])
    total = psico + biolo + socia + multi
    data2 = {
        'psico': psico,
        'biolo': biolo,
        'socia': socia,
        'multi': multi,
        'total': total,
        'v1': monta_vet(data['c1'],6),
        'v2': monta_vet(data['c2'],2),
        'v3': monta_vet(data['c3'],6),
        'v4': monta_vet(data['c4'],5),
        'v5': monta_vet(data['c5'],6),
        'v6': monta_vet(data['c6'],7),
        'v7': monta_vet(data['c7'],9),
        'v8': monta_vet(data['c8'],9),
        'v9': monta_vet(data['c9'],8),
        'v10': monta_vet(data['c10'],16),
        'v11': monta_vet(data['c11'],8),
        'v12': monta_vet(data['c12'],16),
        'v_psico': monta_vet(psico,14),
        'v_biolo': monta_vet(biolo, 36),
        'v_socia': monta_vet(socia, 32),
        'v_multi': monta_vet(multi, 16)
    }

    patient = {
        'PatientID': '1',
        'PatientName': data['p01_name'],
        'Cognition': int((100/6)*int(data['c1'])),
        'Attitude': int((100/2)*int(data['c2'])),
        'Depression': int((100/6)*int(data['c3'])),
        'Sensorial': int((100/5)*int(data['c4'])),
        'Functional': int((100/6)*int(data['c5'])),
        'Nutrition': int((100/7)*int(data['c6'])),
        'Cardiovascular': int((100/9)*int(data['c7'])),
        'Prescriptions': int((100/9)*int(data['c8'])),
        'SocialSupport': int((100/8)*int(data['c9'])),
        'Environment': int((100/16)*int(data['c10'])),
        'Violence': int((100/8)*int(data['c11'])),        
        'Falls': int((100/16)*int(data['c12'])),
    }

    patient['Pala'] = cria_vet(patient)

    offerings = ListaAtividades.offerings
    threshold = -5.0
    o = Recommender(offerings, threshold)
    volta = {}
    # sample call for the scorer method
    print('Recommended offerings for the patient {0}:'.format(patient['PatientID']))
    for (offerID, score) in o.scorer(patient):
        dic_loc = offerings[int(offerID)-1]
        dic_loc["Scor"] = score
        dic_loc["Pala"] = cria_vet(dic_loc)
        volta['ofe' + str(offerID)] = dic_loc
        print('-- {0} (with matching score of {1:4.2f})'.format(offerID, score))

    #print(volta)
    #print(patient)

    demandMapForm = DemandMapForm()
    return render(request,'demandas_tab.html',{'page': data ,'mapa': demandMapForm,'page2': data2, 'offerings' : volta, 'patient' : patient})

def grava_demanda(request):
    data= request.POST
    return render(request,'fim.html')

def testa_grafico(request):
    data= request.POST
    return render(request,'grafico.html')

def grava_page_banco(dados):
    for k in dados:
        pass

def cria_page(dados):
#psicologico
    cognitionDeficit = CognitionDeficit.objects.create(q1_memory_good_like_before=dados['q1_memory_good_like_before'],
                                                   q2_memory_test=dados['q2_memory_test'],
                                                   q3_language_function_attention=dados['q3_language_function_attention'],
                                                   q4_visospatial_ability=dados['q4_visospatial_ability'],
                                                   q4_visospatial_ability_score=dados['q4_visospatial_ability_score'],
                                                   q5_praxia=dados['q5_praxia'],
                                                   q6_memory_test=dados['q6_memory_test'],
                                                   need_investigation_cognition=dados['need_investigation_cognition'],
                                                   max_score_cognition=6)

    negativeAttitudesAging = NegativeAttitudesAging.objects.create(q7_age_self_perception=dados['q7_age_self_perception'],
                                                               q7_age_self_perception_why=dados['q7_age_self_perception_why'],
                                                               q7_age_self_perception_analyze=dados['q7_age_self_perception_analyze'],
                                                               q8_aging_positive_points=dados['q8_aging_positive_points'],
                                                               q8_aging_negative_points=dados['q8_aging_negative_points'],
                                                               q8_aging_analyse=dados['q8_aging_analyse'],
                                                               need_investigation_negative=dados['need_investigation_negative'],
                                                               max_score_negative=2)

    depression_ = Depression.objects.create(q9_satisfied_with_life=dados['q9_satisfied_with_life'],
                                        q10_frequently_sad=dados['q10_frequently_sad'],
                                        q11_stopped_doing_things=dados['q11_stopped_doing_things'],
                                        q12_fear_bad_things_happen=dados['q12_fear_bad_things_happen'],
                                        q13_impatient_disquiet=dados['q13_impatient_disquiet'],
                                        q14_concentration_problem=dados['q14_concentration_problem'],
                                        need_investigation_depression=dados['need_investigation_depression'],
                                        max_score_depression=6)

    psychologicalAspects_ = PsychologicalAspects.objects.create(cognition_deficit=cognitionDeficit,
                                             negative_attitudes_aging=negativeAttitudesAging,
                                             depression=depression_,
                                             comments_psico=dados['comments_psico'],
                                             max_score_psico=14)

# Biologicos

    sensoryDeficit_ = SensoryDeficit.objects.create(q15_vision_problems=dados['q15_vision_problems'],
                                 q16_hearing_problems=dados['q16_hearing_problems'],
                                 q17_taste_problems=dados['q17_taste_problems'],
                                 q18_senses_problems=dados['q18_senses_problems'],
                                 q19_interaction_problems=dados['q19_interaction_problems'],
                                 need_investigation_sensory=dados['need_investigation_sensory'],
                                 max_score_sensory=5)

    functionalDisability_ = FunctionalDisability.objects.create(q20_to_shop=dados['q20_to_shop'],
                                             q21_use_transport=dados['q21_use_transport'],
                                             q22_to_cook=dados['q22_to_cook'],
                                             q23UseTelephone=dados['q23UseTelephone'],
                                             q24_dress_up=dados['q24_dress_up'],
                                             q25TakeShower=dados['q25TakeShower'],
                                             need_investigation_functional=dados['need_investigation_functional'],
                                             max_score_functional=6)

    malnutrition_ = Malnutrition.objects.create(d26_yourself_malnourished=dados['d26_yourself_malnourished'],
                                 d27_chewing_mouth_problems = dados['d27_chewing_mouth_problems'],
                                 d28_less3_meal_daily = dados['d28_less3_meal_daily'],
                                 d29_decreases_amount_food = dados['d29_decreases_amount_food'],
                                 d30_lost_weight_no_reason = dados['d30_lost_weight_no_reason'],
                                 d31_stress_illness_hospitalization = dados['d31_stress_illness_hospitalization'],
                                 q32_bmi_less22 = dados['q32_bmi_less22'],
                                 need_investigation_malnutrition = dados['need_investigation_malnutrition'],
                                 max_score_malnutrition=7)

    cardiovascularFactors_ = CardiovascularFactors.objects.create (q33_dcv_familiar_history = dados['q33_dcv_familiar_history'],
                                                    q34_hypertension = dados['q34_hypertension'],
                                                    q34_hypertension_unknow = dados['q34_hypertension_unknow'],
                                                    q35_uncontrolled_diabetes = dados['q35_uncontrolled_diabetes'],
                                                    q35_unknown_value_glycemia = dados['q35_unknown_value_glycemia'],
                                                    q36_cholesterol = dados['q36_cholesterol'],
                                                    q36_unknown_value_ct_hdl = dados['q36_unknown_value_ct_hdl'],
                                                    q37_smoker = dados['q37_smoker'],
                                                    q38_practice_150_minutes_exercises = dados['q38_practice_150_minutes_exercises'],
                                                    q39_healthy_eating = dados['q39_healthy_eating'],
                                                    q40_alcohol_Ingested_last_week =  dados['q40_alcohol_Ingested_last_week'],
                                                    q40_alcohol_Ingested_last_week_amount = dados['q40_alcohol_Ingested_last_week_amount'],
                                                    q41_bmi_obesity = dados['q41_bmi_obesity'],
                                                    need_investigation_cardio = dados['need_investigation_cardio'],
                                                    max_score_cardio=9)

    misuseMedications_ = MisuseMedications.objects.create(q42_diseases_last_5_years_a=dados['q42_diseases_last_5_years_a'],
                                       q42_diseases_last_5_years_b=dados['q42_diseases_last_5_years_b'],
                                       q42_diseases_last_5_years_c=dados['q42_diseases_last_5_years_c'],
                                       q42_diseases_last_5_years_d=dados['q42_diseases_last_5_years_d'],
                                       q42_diseases_last_5_years_e=dados['q42_diseases_last_5_years_e'],
                                       q42_diseases_last_5_years_f=dados['q42_diseases_last_5_years_f'],
                                       q42_diseases_last_5_years_g=dados['q42_diseases_last_5_years_g'],
                                       q42_diseases_last_5_years_h=dados['q42_diseases_last_5_years_h'],
                                       q42_diseases_last_5_years_i=dados['q42_diseases_last_5_years_i'],
                                       q42_diseases_last_5_years_j=dados['q42_diseases_last_5_years_j'],
                                       q42_diseases_last_5_years_k=dados['q42_diseases_last_5_years_k'],
                                       q42_diseases_last_5_years_l=dados['q42_diseases_last_5_years_l'],
                                       q43_health_problems_a=dados['q43_health_problems_a'],
                                       q43_health_problems_b=dados['q43_health_problems_b'],
                                       q43_health_problems_c=dados['q43_health_problems_c'],
                                       q43_health_problems_d=dados['q43_health_problems_d'],
                                       q43_health_problems_e=dados['q43_health_problems_e'],
                                       q43_health_problems_f=dados['q43_health_problems_f'],
                                       q43_health_problems_g=dados['q43_health_problems_g'],
                                       q43_health_problems_h=dados['q43_health_problems_h'],
                                       q44_amount_diagnostics=dados['q44_amount_diagnostics'],
                                       q45_medicines=dados['q45_medicines'],
                                       q46_medicines_increase=dados['q46_medicines_increase'],
                                       q47_know_medicines=dados['q47_know_medicines'],
                                       q48_medications_prescribed=dados['q48_medications_prescribed'],
                                       q49_medicine_medical_advice=dados['q49_medicine_medical_advice'],
                                       q50_already_stopped_medicines=dados['q50_already_stopped_medicines'],
                                       q51_self_medication=dados['q51_self_medication'],
                                       q52_inappropriate_medication=dados['q52_inappropriate_medication'],
                                       q53_risk_adverse_reaction=dados['q53_risk_adverse_reaction'],
                                       need_investigation_misuse=dados['need_investigation_misuse'],
                                       max_score_misuse=9)

    biologicalAspects_ = BiologicalAspects.objects.create(sensoryDeficit=sensoryDeficit_,
                                        functionalDisability=functionalDisability_,
                                        malNutrition = malnutrition_,
                                        cardiovascularFactors = cardiovascularFactors_,
                                        misuseMedications = misuseMedications_,
                                        comments_bio = dados['comments_bio'],
                                        max_score_bio=36)


# Social Aspects

    lowSocialSupport_ = LowSocialSupport.objects.create(q54_spouse=dados['q54_spouse'],
                                     q54_mother=dados['q54_mother'],
                                     q54_father=dados['q54_father'],
                                     q54_brothers=dados['q54_brothers'],
                                     q54_children=dados['q54_children'],
                                     q54_gran_children=dados['q54_gran_children'],
                                     q55_meet_family_friends=dados['q55_meet_family_friends'],
                                     q56_participate_family_decisions=dados['q56_participate_family_decisions'],
                                     q57_satisfied_family_relationship=dados['q57_satisfied_family_relationship'],
                                     q58_helped_if_need_money=dados['q58_helped_if_need_money'],
                                     q59_someone_helps_if_need=dados['q59_someone_helps_if_need'],
                                     q60_someone_to_have_fun=dados['q60_someone_to_have_fun'],
                                     q61_participate_social_events=dados['q61_participate_social_events'],
                                     q62_regulary_healt_services=dados['q62_regulary_healt_services'],
                                     need_investigation_low=dados['need_investigation_low'],
                                     max_score_low=8)

    environmentalProblems_ = EnvironmentalProblems.objects.create(q63_estable_furniture=dados['q63_estable_furniture'],
                                    q64_loose_objects_carpets = dados['q64_loose_objects_carpets'],
                                    q65_slippery_floor = dados['q65_slippery_floor'],
                                    q66_handrail_on_stairs = dados['q66_handrail_on_stairs'],
                                    q67_lighted_stairs = dados['q67_lighted_stairs'],
                                    q68_suitable_stairs_steps = dados['q68_suitable_stairs_steps'],
                                    q69_non_slippery_carpet = dados['q69_non_slippery_carpet'],
                                    q70_get_on_stool = dados['q70_get_on_stool'],
                                    q71_turn_lights_off = dados['q71_turn_lights_off'],
                                    q72_safe_shoes = dados['q72_safe_shoes'],
                                    q73_manicure_sidewalks = dados['q73_manicure_sidewalks'],
                                    q74_public_transport_access = dados['q74_public_transport_access'],
                                    q75_commerce_access = dados['q75_commerce_access'],
                                    q76_ease_plasewalking = dados['q76_ease_plasewalking'],
                                    q77_fun_access = dados['q77_fun_access'],
                                    q78_safety = dados['q78_safety'],
                                    need_investigation_env = dados['need_investigation_env'],
                                    max_score_env=16)


    violence_ = Violence.objects.create(q79_afraid_close_person=dados['q79_afraid_close_person'],
                        q80_feels_abandoned=dados['q80_feels_abandoned'],
                        q81_forced=dados['q81_forced'],
                        q82_assauteld=dados['q82_assauteld'],
                        q83_in_need=dados['q83_in_need'],
                        q84_someone_used_money=dados['q84_someone_used_money'],
                        q85_touched_without_permission=dados['q85_touched_without_permission'],
                        q86_dont_take_care_health=dados['q86_dont_take_care_health'],
                        need_investigation_violence=dados['need_investigation_violence'],
                        max_score_violence=8)


    socialAspects_ = SocialAspects.objects.create(lowSocialSupport=lowSocialSupport_,
                                environmentalProblems=environmentalProblems_,
                                violence=violence_,
                                comments_social = dados['comments_social'],
                                maxScore_social=32)

# multidimensional
    falls_ = Falls.objects.create(q87_falls_last_year=dados['q87_falls_last_year'],
               q87_amount_falls_last_year=dados['q87_amount_falls_last_year'],
               q88_fractures_due_to_falls=dados['q88_fractures_due_to_falls'],
               q88_fractures_due_to_falls_list=dados['q88_fractures_due_to_falls_list'],
               q89_fractures_list=dados['q89_fractures_list'],
               q90_strength_mmii=dados['q90_strength_mmii'],
               q91_equilibrium=dados['q91_equilibrium'],
               q92_older_than75=dados['q92_older_than75'],
               q93_female=dados['q93_female'],
               q94_cognitive_alterations=dados['q94_cognitive_alterations'],
               q95_av_ds_commitment=dados['q95_av_ds_commitment'],
               q96_visual_deficit=dados['q96_visual_deficit'],
               q97_domestic_risks=dados['q97_domestic_risks'],
               q98_behavior_risk=dados['q98_behavior_risk'],
               q99_inactivity=dados['q99_inactivity'],
               q100_prior_ave=dados['q100_prior_ave'],
               q101_psychotropic_medications_use=dados['q101_psychotropic_medications_use'],
               q102_has_diseases=dados['q102_has_diseases'],
               need_investigation_falls=dados['need_investigation_falls'],
               max_score_falls=16)

    multidisciplinaryDomain_ =  MultidisciplinaryDomain.objects.create(falls=falls_,
                                comments_multi = dados['comments_multi'],
                                maxScore_multi=16)

    participanteSituation_ = ParticipantSituation.objects.create(   p07_marital_status = dados['p07_marital_status'],
                                                                    p08_schooling = dados['p08_schooling'],
                                                                    p09_study_time = dados['p09_study_time'],
                                                                    p10_is_retired = dados['p10_is_retired'],
                                                                    p10_retired_profession = dados['p10_retired_profession'],
                                                                    p10_actual_profession = dados['p10_actual_profession'],
                                                                    p11_retire_more_time_activity = dados['p11_retire_more_time_activity'],
                                                                    p12_is_working_professionals_activities = dados['p12_is_working_professionals_activities'],
                                                                    p12_professional_activities = dados['p12_professional_activities'],
                                                                    p13_income_I = dados['p13_income_I'],
                                                                    p13_income_F = dados['p13_income_F'],
                                                                    p14_lives_with = dados['p14_lives_with'],
                                                                    p15_has_religion = dados['p15_has_religion'],
                                                                    p15_religion = dados['p15_religion'],
                                                                    p16_health_self_report = dados['p16_health_self_report'],
                                                                    p20_weight = dados['p20_weight'],
                                                                    p20_height = dados['p20_height'],
                                                                    p20_IMC = dados['p20_IMC'],
                                                                    p30_ride_with = dados['p30_ride_with']
                                                                )


    participant_ = Participant.objects.create(  p00_email = dados['p00_email'],
                                                p01_name = dados['p01_name'],
                                                p02_address = dados['p02_address'],
                                                p03_communication = dados['p03_communication'],
                                                p04_birth_date = datetime.strptime(dados['p04_birth_date'],'%d/%m/%Y'),
                                                p05_age = dados['p05_age'],
                                                p06_gender = dados['p06_gender'],
                                                p20_profile_photo_URL = dados['p20_profile_photo_URL']
                                              )

    gerontologist_ = Expert.objects.get(id=1)

 #   participant__= Participant.objects.get(id=1)
 #   participanteSituation_ = ParticipantSituation.objects.get(id=1)

    page = Page.objects.create(service=dados['service'],
            entrance=datetime.strptime(dados['entrance'],'%d/%m/%Y'),
            interviewed=dados['interviewed'],
            interviewer=dados['interviewer'],
            avaliation_date=datetime.strptime(dados['avaliation_date'],'%d/%m/%Y'),
            gerontologist=gerontologist_,
            participant=participant_,
            participant_situation=participanteSituation_ ,
            psychologicalAspects=psychologicalAspects_ ,
            biologicalAspects = biologicalAspects_,
            socialAspects = socialAspects_,
            multidisciplinaryDomain = multidisciplinaryDomain_)

