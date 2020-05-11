from django.db import models
from .messages import Options
# Begin Social Aspects
class LowSocialSupport (models.Model):
    q54_spouse = models.CharField(Options.questions[54][0], max_length=1, default="N", choices=Options.CHOICES)
    q54_mother = models.CharField(Options.questions[54][1], max_length=1, default="N", choices=Options.CHOICES)
    q54_father = models.CharField(Options.questions[54][2], max_length=1, default="N", choices=Options.CHOICES)
    q54_brothers = models.IntegerField(Options.questions[54][3])
    q54_children = models.IntegerField(Options.questions[54][4],)
    q54_gran_children = models.IntegerField(Options.questions[54][5])
    q55_meet_family_friends = models.CharField(Options.questions[55], max_length=1, default="N", choices=Options.CHOICES)
    q56_participate_family_decisions = models.CharField(Options.questions[56], max_length=1, default="N", choices=Options.CHOICES)
    q57_satisfied_family_relationship = models.CharField(Options.questions[57], max_length=1, default="N", choices=Options.CHOICES)
    q58_helped_if_need_money = models.CharField(Options.questions[58], max_length=1, default="N", choices=Options.CHOICES)
    q59_someone_helps_if_need = models.CharField(Options.questions[59], max_length=1, default="N", choices=Options.CHOICES)
    q60_someone_to_have_fun = models.CharField(Options.questions[60], max_length=1, default="N", choices=Options.CHOICES)
    q61_participate_social_events = models.CharField(Options.questions[61], max_length=1, default="N", choices=Options.CHOICES)
    q62_regulary_healt_services = models.CharField(Options.questions[62], max_length=1, default="N", choices=Options.CHOICES)
    need_investigation_low = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score_low = models.IntegerField(default=9)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Baixo Suporte Social'
        verbose_name_plural = 'Baixo Suporte Social'

    def score(self):
        pass


class EnvironmentalProblems (models.Model):
    # Internal environment
    q63_estable_furniture = models.CharField(Options.questions[63], max_length=1, default="N", choices=Options.CHOICES)
    q64_loose_objects_carpets = models.CharField(Options.questions[64], max_length=1, default="N", choices=Options.CHOICES)
    q65_slippery_floor = models.CharField(Options.questions[65], max_length=1, default="N", choices=Options.CHOICES)
    q66_handrail_on_stairs = models.CharField(Options.questions[66], max_length=1, default="N", choices=Options.CHOICES)
    q67_lighted_stairs = models.CharField(Options.questions[67], max_length=1, default="N", choices=Options.CHOICES)
    q68_suitable_stairs_steps = models.CharField(Options.questions[68], max_length=1, default="N", choices=Options.CHOICES)
    q69_non_slippery_carpet = models.CharField(Options.questions[69], max_length=1, default="N", choices=Options.CHOICES)

    # riskBehavior
    q70_get_on_stool = models.CharField(Options.questions[70], max_length=1, default="N", choices=Options.CHOICES)
    q71_turn_lights_off = models.CharField(Options.questions[71], max_length=1, default="N", choices=Options.CHOICES)
    q72_safe_shoes = models.CharField(Options.questions[72], max_length=1, default="N", choices=Options.CHOICES)

    # externalEnvironment
    q73_manicure_sidewalks = models.CharField(Options.questions[73], max_length=1, default="N", choices=Options.CHOICES)
    q74_public_transport_access = models.CharField(Options.questions[74], max_length=1, default="N", choices=Options.CHOICES)
    q75_commerce_access = models.CharField(Options.questions[75], max_length=1, default="N", choices=Options.CHOICES)
    q76_ease_plasewalking = models.CharField(Options.questions[76], max_length=1, default="N", choices=Options.CHOICES)
    q77_fun_access = models.CharField(Options.questions[77], max_length=1, default="N", choices=Options.CHOICES)
    q78_safety = models.CharField(Options.questions[78], max_length=1, default="N", choices=Options.CHOICES)

    need_investigation_env = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
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


class Violence (models.Model):
    q79_afraid_close_person = models.CharField(Options.questions[79], max_length=1, default="N", choices=Options.CHOICES)
    q80_feels_abandoned = models.CharField(Options.questions[80], max_length=1, default="N", choices=Options.CHOICES)
    q81_forced = models.CharField(Options.questions[81], max_length=1, default="N", choices=Options.CHOICES)
    q82_assauteld = models.CharField(Options.questions[82], max_length=1, default="N", choices=Options.CHOICES)
    q83_in_need = models.CharField(Options.questions[83], max_length=1, default="N", choices=Options.CHOICES)
    q84_someone_used_money = models.CharField(Options.questions[84], max_length=1, default="N", choices=Options.CHOICES)
    q85_touched_without_permission = models.CharField(Options.questions[85], max_length=1, default="N", choices=Options.CHOICES)
    q86_dont_take_care_health = models.CharField(Options.questions[86], max_length=1, default="N", choices=Options.CHOICES)
    need_investigation_violence = models.CharField(Options.need_investigation_question,max_length=1, default="N",choices=Options.CHOICES)
    max_score_violence = models.IntegerField(default=8)
    score = models.IntegerField (null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Violência'
        verbose_name_plural = 'Violência'

    def score(self):
        pass


class SocialAspects (models.Model):
    lowSocialSupport = models.OneToOneField(LowSocialSupport, on_delete=models.CASCADE, null=True)
    environmentalProblems = models.OneToOneField(EnvironmentalProblems, on_delete=models.CASCADE, null=True)
    violence = models.OneToOneField(Violence, on_delete=models.CASCADE, null=True)
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
