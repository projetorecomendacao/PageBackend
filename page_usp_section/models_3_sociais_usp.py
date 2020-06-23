from django.db import models
from .messages_usp import OptionsUsp
# Begin Social Aspects
class LowSocialSupportUsp (models.Model):
    q55_spouse = models.CharField(OptionsUsp.questions[54][0], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q55_mother = models.CharField(OptionsUsp.questions[54][1], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q55_father = models.CharField(OptionsUsp.questions[54][2], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q55_brothers = models.IntegerField(OptionsUsp.questions[54][3],default=0)
    q55_children = models.IntegerField(OptionsUsp.questions[54][4],default=0)
    q55_gran_children = models.IntegerField(OptionsUsp.questions[54][5],default=0)
    q55_great_gran_children = models.IntegerField(OptionsUsp.questions[54][5],default=0)

    q56_meet_family_friends = models.CharField(OptionsUsp.questions[55], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q57_participate_family_decisions = models.CharField(OptionsUsp.questions[56], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q58_satisfied_family_relationship = models.CharField(OptionsUsp.questions[57], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q59_helped_if_need_money = models.CharField(OptionsUsp.questions[58], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q60_someone_helps_if_need = models.CharField(OptionsUsp.questions[59], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q61_someone_to_have_fun = models.CharField(OptionsUsp.questions[60], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q62_participate_social_events = models.CharField(OptionsUsp.questions[61], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q63_regulary_healt_services = models.CharField(OptionsUsp.questions[62], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    low_social_support_obs = models.TextField("Observações: ", null= True)
    need_investigation_low = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score_low = models.IntegerField(default=9)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Baixo Suporte Social'
        verbose_name_plural = 'Baixo Suporte Social'

    def score(self):
        pass


class ViolenceUsp (models.Model):
    q64_afraid_close_person = models.CharField(OptionsUsp.questions[79], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q65_feels_abandoned = models.CharField(OptionsUsp.questions[80], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q66_forced = models.CharField(OptionsUsp.questions[81], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q67_assauteld = models.CharField(OptionsUsp.questions[82], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q68_in_need = models.CharField(OptionsUsp.questions[83], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q69_someone_used_money = models.CharField(OptionsUsp.questions[84], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q70_touched_without_permission = models.CharField(OptionsUsp.questions[85], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q71_dont_take_care_health = models.CharField(OptionsUsp.questions[86], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    violence_obs = models.TextField("Observações", null=True)
    need_investigation_violence = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score_violence = models.IntegerField(default=8)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Violência'
        verbose_name_plural = 'Violência'

    def score(self):
        pass


class EnvironmentalProblemsUsp (models.Model):
    # Internal environment
    q72_estable_furniture = models.CharField(OptionsUsp.questions[63], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q73_loose_objects_carpets = models.CharField(OptionsUsp.questions[64], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q74_slippery_floor = models.CharField(OptionsUsp.questions[65], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q75_non_slippery_carpet = models.CharField(OptionsUsp.questions[69], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q76_stairs = models.CharField(OptionsUsp.questions[65], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q77_lighted_stairs = models.CharField(OptionsUsp.questions[67], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q78_handrail_on_stairs = models.CharField(OptionsUsp.questions[66], max_length=1, default="N", choices=OptionsUsp.CHOICES)

    # riskBehavior
    q79_get_on_stool = models.CharField(OptionsUsp.questions[70], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q80_turn_lights_on = models.CharField(OptionsUsp.questions[71], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q81_safe_shoes = models.CharField(OptionsUsp.questions[72], max_length=1, default="N", choices=OptionsUsp.CHOICES)

    # externalEnvironment
    q82_manicure_sidewalks = models.CharField(OptionsUsp.questions[73], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q83_public_transport_access = models.CharField(OptionsUsp.questions[74], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q84_commerce_access = models.CharField(OptionsUsp.questions[75], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q85_ease_plasewalking = models.CharField(OptionsUsp.questions[76], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q86_fun_access = models.CharField(OptionsUsp.questions[77], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q87_safety = models.CharField(OptionsUsp.questions[78], max_length=1, default="N", choices=OptionsUsp.CHOICES)
    environmental_obs = models.TextField("Observações",null=True)
    need_investigation_env = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score_env = models.IntegerField(default=16)

    def investigate(self):
        pass

    def score(self):
        pass

    def calcular(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Problemas Ambientais'
        verbose_name_plural = 'Problemas Ambientais'



class SocialAspectsUsp (models.Model):
    lowSocialSupport = models.OneToOneField(LowSocialSupportUsp, on_delete=models.CASCADE, null=True)
    environmentalProblems = models.OneToOneField(EnvironmentalProblemsUsp, on_delete=models.CASCADE, null=True)
    violence = models.OneToOneField(ViolenceUsp, on_delete=models.CASCADE, null=True)
    comments_social = models.TextField('Observações Sobre o Bloco Social')
    maxScore_social = models.IntegerField('Pontuação Máxima',default=32)

    def investigate(self):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_score = 0
        #for score in (self.lowSocialSupport, self.environmentalProblems, self.violence):
        #    max_score += score.maxScore
        self.maxScore = max_score

    class Meta:
        ordering = ['id']
        verbose_name = 'Relacionados a Aspectos Sociais'
        verbose_name_plural = 'Relacionados a Aspectos Sociais'

    def score(self):
        pass
# End Social Aspects
