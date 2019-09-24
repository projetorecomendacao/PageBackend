from django.db import models
from experts_section.models import Gerontologist
from .messages import *
from participant_section.models import Participant, ParticipantSituation
from recommender_section.models import RecommendedActivitiesOffers, RecommendedActivities
from assessment_section.models import DemandMap
from .models_1_psicologico import PsychologicalAspects
from .models_2_Biologicos import BiologicalAspects
from .models_3_sociais import SocialAspects
from .models_4_multidimensional import MultidisciplinaryDomain


class Page (models.Model):
    #Data que foi feita a entrevista
    date = models.DateField("Data da Entrevista", null="True")
    #Data da Criação
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null="True")
    #Data da ùltima atualização
    updated_at = models.DateTimeField('Atualizado em: ', null= True)
    #Gerontólogo Responsável
    gerontologist = models.ForeignKey(Gerontologist, on_delete=models.CASCADE, verbose_name='Gerontologista Resposável')
    #Participante
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, verbose_name = 'Participante')
    #Dados do Participante no Momento da criação do Page
    participant_situation = models.ForeignKey(ParticipantSituation,on_delete=models.CASCADE, null=True, verbose_name = 'Situação do Participante')
    #Auto Relato de Saúde
    p1_self_health_report = models.TextField("Auto Relato de Saúde - Como o senhor(a)", null=True)
    #Dimensões do Page
    psychologicalAspects = models.OneToOneField(PsychologicalAspects, on_delete=models.CASCADE, null=True,verbose_name='Relacionados a Aspectos Psicológicos')
    biologicalAspects = models.OneToOneField(BiologicalAspects, on_delete=models.CASCADE, null=True,verbose_name='Relacionados a Aspectos Biológicos')
    socialAspects = models.OneToOneField(SocialAspects, on_delete=models.CASCADE, null=True,verbose_name='Relacionados a Aspectos Sociais')
    multidisciplinaryDomain = models.OneToOneField(MultidisciplinaryDomain, on_delete=models.CASCADE, null=True,verbose_name='Domínio Multidisciplinar')
    #Mapa de Demandas
    demandMap = models.OneToOneField(DemandMap,on_delete=models.CASCADE, null=True,verbose_name='Mapa de Demandas')
    #Atividades Recomendadas
    recommendedActivities = models.ForeignKey(RecommendedActivities, null=True, verbose_name="Atividades Recomendadas", on_delete=models.CASCADE)
    recommendedActivitiesOffers = models.ForeignKey(RecommendedActivitiesOffers, null=True, verbose_name="Atividades Ofertadas Recomendadas", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Page'
        verbose_name_plural = 'Page'

    def scores(self):
        pass



