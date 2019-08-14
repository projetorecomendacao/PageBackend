from django.db import models

from activities_section.models import Activity
from health_section.models import Diseases, Medication


class DA_Attitudes (models.Model):
    description = models.TextField()
    A1_age_self_perception = models.IntegerField()
    A1_why = models.TextField()
    A2_pros = models.TextField()
    A2_cons = models.TextField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class DB_LifeQuality (models.Model):
    description = models.TextField()
    B1_happiness = models.IntegerField()
    B2_health = models.IntegerField()
    B3_life_quality = models.IntegerField()
    B4_capable = models.IntegerField()
    B5_pain = models.IntegerField()
    B6_sleep = models.IntegerField()
    B7_sexually_active = models.BooleanField()
    B7_affective_relationship = models.IntegerField()
    B8_free_time_usage = models.TextField()
    B9_satisfied_with_routine = models.BooleanField()
    B10_practice_pleasurable_activities = models.BooleanField()
    B10_pleasurable_activities = models.ManyToManyField(Activity, related_name='participant')
    B10_pleasurable_activities_description = models.TextField()
    B10_pleasurable_activities_frequency = models.TextField()
    B11_most_important_aspect = models.TextField()
    B_max = models.IntegerField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class DC_Senses (models.Model):
    description = models.TextField()
    C1_vision = models.BooleanField()
    C2_audition = models.BooleanField()
    C3_mouth_wound = models.BooleanField()
    C4_senses_quality = models.IntegerField()
    C5_senses_affects_activities = models.IntegerField()
    C_max = models.IntegerField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class DD_Malnutrition (models.Model):
    description = models.TextField()
    D1_has_nutritional_problem = models.IntegerField()
    D2_daily_meals = models.IntegerField()
    D3_eating_less = models.IntegerField()
    D4_weight_loss = models.IntegerField()
    D5_diseases = models.BooleanField()
    D6_IMC = models.IntegerField()
    D_max = models.IntegerField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class DE_FunctionalCapacity (models.Model):
    description = models.TextField()
    E1_get_dressed = models.BooleanField()
    E2_take_shower = models.BooleanField()
    E3_use_smartphone = models.BooleanField()
    E4_to_cook = models.BooleanField()
    E5_to_shop = models.BooleanField()
    E6_use_transport = models.BooleanField()
    E_max = models.IntegerField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class DF_Depression (models.Model):
    description = models.TextField()
    F1_satisfied_with_life = models.BooleanField()
    F1_why = models.TextField()
    F2_frequently_sad = models.BooleanField()
    F2_why = models.TextField()
    F3_gave_up_things = models.BooleanField()
    F3_why = models.TextField()
    F4_fear = models.BooleanField()
    F4_why = models.TextField()
    F5_anxious = models.BooleanField()
    F5_why = models.TextField()
    F6_concentration_problem = models.BooleanField()
    F6_why = models.TextField()
    F_max = models.IntegerField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class DG_Cognition (models.Model):
    description = models.TextField()
    G1_memory = models.IntegerField()
    G2_language_executive_function_and_attention = models.IntegerField()
    G3_visuospatial_ability = models.IntegerField()
    G4_praxis = models.IntegerField()
    G5_memory_2 = models.IntegerField()
    G_max = models.IntegerField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class DH_CardiovascularFactors (models.Model):
    description = models.TextField()
    H1_DCV_familiar_history = models.BooleanField()
    H2_hypertension = models.IntegerField()
    H3_diabetes = models.IntegerField()
    H4_cholesterol = models.IntegerField()
    H5_IMC = models.IntegerField()
    H6_smoker = models.IntegerField()
    H7_alcohol_ingestion = models.IntegerField()
    H8_exercise_practice = models.IntegerField()
    H_max = models.IntegerField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class DI_MedicationManagement (models.Model):
    description = models.TextField()
    I1_diseases = models.ManyToManyField(Diseases, related_name='patients', blank=True)
    I2_medications = models.ManyToManyField(Medication, related_name='patients', blank=True)
    I3_medications_amount = models.IntegerField()
    I4_aware_medications_effect = models.BooleanField()
    I5_medications_prescribed_by_doctor = models.BooleanField()
    I6_follows_doctor_instructions = models.BooleanField()
    I6_why = models.TextField()
    I7_interrupted_medication_use = models.BooleanField()
    I7_why = models.TextField()
    I8_self_medication = models.BooleanField()
    I9_inappropriate_medication = models.BooleanField()
    I10_too_much_medication = models.BooleanField()
    I_max = models.IntegerField()

    def investigate(self):
        pass

    def medication_amount(self):
        self.I3_medications_amount = len(self.I2_medications)

    class Meta:
        ordering = ['id']


class DJ_Ambient (models.Model):
    description = models.TextField()

    # risk behavior
    AA_get_on_stool = models.BooleanField()
    AB_turn_lights_on_at_night = models.BooleanField()
    AC_safe_shoes = models.BooleanField()

    # domestic environment
    BA_static_furniture = models.BooleanField()
    BB_disattached_furniture = models.BooleanField()
    BC_slippery_floor = models.BooleanField()
    BD_no_stairs_or_handrail = models.BooleanField()
    BE_lighted_stairs = models.BooleanField()
    BF_suitable_stairs_steps = models.BooleanField()
    BG_non_slippery_carpet = models.BooleanField()

    # external environment
    CA_public_transport_access = models.BooleanField()
    CB_transportation_time = models.BooleanField()
    CC_commerce_access = models.BooleanField()
    CD_walking_quality = models.BooleanField()
    CE_fun_access = models.BooleanField()
    CF_safety = models.BooleanField()
    CG_noise = models.BooleanField()
    CH_neighborhood = models.BooleanField()

    J_max = models.IntegerField()

    def investigate(self):
        pass


class DK_Falls (models.Model):
    description = models.TextField()
    K1_falls = models.BooleanField()
    K2_falls_description = models.TextField()
    K3_strength_MMII = models.BooleanField()
    K4_equilibrium = models.BooleanField()
    K5a_older_than_80 = models.BooleanField()
    K5b_female = models.BooleanField()
    K5c_falls_history = models.BooleanField()
    K5d_fractures_history = models.BooleanField()
    K5e_low_equilibrium = models.BooleanField()
    K5f_low_strength_MMII = models.BooleanField()
    K5g_AVDS_commitment = models.BooleanField()
    K5h_cognitive_alterations = models.BooleanField()
    K5i_domestic_risks = models.BooleanField()
    K5j_prior_ave = models.BooleanField()
    K5k_visual_deficit = models.BooleanField()
    K5l_inactivity = models.BooleanField()
    K5m_march_support_device = models.BooleanField()
    K5n_medication_use = models.IntegerField()
    K5o_other_diseases = models.IntegerField()
    K_max = models.IntegerField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class DL_Violence (models.Model):
    description = models.TextField()
    L1_afraid_close_person = models.BooleanField()
    L2_feels_abandoned = models.BooleanField()
    L3_forced = models.BooleanField()
    L4_yelled = models.BooleanField()
    L5_beated = models.BooleanField()
    L6_used_money = models.BooleanField()
    L7_in_need = models.BooleanField()
    L_max = models.IntegerField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class DM_SocialVulnerability (models.Model):
    description = models.TextField()
    M1_brothers = models.IntegerField()
    M1_children = models.IntegerField()
    M1_grandchildren = models.IntegerField()
    M2_frequency_family_meetings = models.IntegerField()
    M3_frequency_count_on_family = models.IntegerField()
    M4_frequency_decides_things = models.IntegerField()
    M5_satisfied_family = models.IntegerField()
    # M6_family_income
    M7_enough_money = models.BooleanField()
    M8_social_events_participation = models.IntegerField()
    M9_receive_doctors_home = models.BooleanField()
    M10_amount_doctors_visits = models.IntegerField()
    M11_num_diseases = models.IntegerField()
    M_max = models.IntegerField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class DN_Fragility (models.Model):
    description = models.TextField()
    N1_advanced_age = models.BooleanField()
    N2_malnutrition = models.BooleanField()
    N3_functional_capability = models.BooleanField()
    N4_incontinence = models.BooleanField()
    N5_depression = models.BooleanField()
    N6_cognitive_deficit = models.BooleanField()
    N7_more_than_2_chronic_disease = models.BooleanField()
    N8_polypharmacy = models.BooleanField()
    N9_low_strength_or_equilibrium = models.BooleanField()
    N10_low_social_support = models.BooleanField()
    N_max = models.IntegerField()

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']


class Page (models.Model):
    date = models.DateField()
    DA_Attitudes = models.OneToOneField(DA_Attitudes, on_delete=models.CASCADE, related_name='page')
    DB_LifeQuality = models.OneToOneField(DB_LifeQuality, on_delete=models.CASCADE, related_name='page')
    DC_Senses = models.OneToOneField(DC_Senses, on_delete=models.CASCADE, related_name='page')
    DD_Malnutrition = models.OneToOneField(DD_Malnutrition, on_delete=models.CASCADE, related_name='page')
    DE_FunctionalCapacity = models.OneToOneField(DE_FunctionalCapacity, on_delete=models.CASCADE, related_name='page')
    DF_Depression = models.OneToOneField(DF_Depression, on_delete=models.CASCADE, related_name='page')
    DG_Cognition = models.OneToOneField(DG_Cognition, on_delete=models.CASCADE, related_name='page')
    DH_CardiovascularFactors = models.OneToOneField(DH_CardiovascularFactors, on_delete=models.CASCADE,
                                                    related_name='page')
    DI_MedicationsManagement = models.OneToOneField(DI_MedicationManagement, on_delete=models.CASCADE,
                                                    related_name='page')
    DJ_Ambient = models.OneToOneField(DJ_Ambient, on_delete=models.CASCADE, related_name='page')
    DK_Falls = models.OneToOneField(DK_Falls, on_delete=models.CASCADE, related_name='page')
    DL_Violence = models.OneToOneField(DL_Violence, on_delete=models.CASCADE, related_name='page')
    DM_SocialVulnerability = models.OneToOneField(DM_SocialVulnerability, on_delete=models.CASCADE, related_name='page')
    DN_Fragility = models.OneToOneField(DN_Fragility, on_delete=models.CASCADE, related_name='page')
