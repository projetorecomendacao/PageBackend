from django.db import models
from .messages_usp import OptionsUsp
# Begin Social Aspects
class LowSocialSupportUsp (models.Model):
    q55_spouse = models.CharField( max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q55_mother = models.CharField( max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q55_father = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q55_brothers = models.IntegerField(default=0)
    q55_children = models.IntegerField(default=0)
    q55_gran_children = models.IntegerField(default=0)
    q55_great_gran_children = models.IntegerField(default=0)

    q56_meet_family_friends = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q57_participate_family_decisions = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q58_satisfied_family_relationship = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q59_helped_if_need_money = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q60_someone_helps_if_need = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q61_someone_to_have_fun = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q62_participate_social_events = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q63_regulary_healt_services = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    comments = models.TextField("Observações",null=True, blank=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

    def investigate(self):
        pass

    class Meta:
        ordering = ['id']
        verbose_name = 'Baixo Suporte Social'
        verbose_name_plural = 'Baixo Suporte Social'

    def score(self):
        pass


class ViolenceUsp (models.Model):
    q64_afraid_close_person = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q65_feels_abandoned = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q66_forced = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q67_assauteld = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q68_in_need = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q69_someone_used_money = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q70_touched_without_permission = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q71_dont_take_care_health = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    comments = models.TextField("Observações",null=True, blank=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

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
    q72_estable_furniture = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q73_loose_objects_carpets = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q74_slippery_floor = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q75_non_slippery_carpet = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q76_stairs = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q77_lighted_stairs = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q78_handrail_on_stairs = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)

    # riskBehavior
    q79_get_on_stool = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q80_turn_lights_on = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q81_safe_shoes = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)

    # externalEnvironment
    q82_manicure_sidewalks = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q83_public_transport_access = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q84_commerce_access = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q85_ease_plasewalking = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q86_fun_access = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    q87_safety = models.CharField(max_length=1, default="N", choices=OptionsUsp.CHOICES)
    comments = models.TextField("Observações",null=True, blank=True)
    need_investigation = models.CharField(OptionsUsp.need_investigation_question,max_length=1, default="N",choices=OptionsUsp.CHOICES)
    max_score = models.IntegerField(default=6)
    score = models.IntegerField(null=True)

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
    comments = models.TextField('Observações Sobre o Bloco Social', blank=True, null=True)
    maxScore = models.IntegerField('Pontuação Máxima',default=32)

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
