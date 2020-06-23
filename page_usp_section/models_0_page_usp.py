from django.db import models
from experts_section.models import Expert
from .messages_usp import *
from participant_section.models import Participant, ParticipantSituation
from recommender_section.models import RecommendedActivitiesOffers, RecommendedActivities
from assessment_section.models import DemandMap
#from health_section.models import HealthMonitoring
from .models_1_psicologico_usp import PsychologicalAspectsUsp
from .models_2_Biologicos_usp import BiologicalAspectsUsp
from .models_3_sociais_usp import SocialAspectsUsp
from .models_4_multidimensional_usp import MultidisciplinaryDomainUsp





class PageUsp (models.Model):
    #Serviço ou instituição
    service = models.CharField('Serviço/instituição',max_length=60)
    #Data Entrada no serviçoptimize
    entrance = models.DateField('Data de Entrada no Serviço',null=True,blank=True)
    #Entrevistado
    interviewed = models.CharField('Pessoa entrevistada:', max_length=20, choices=OptionsUsp.INTERVIEW)
    #Entrevistador
    interviewer = models.CharField('Nome do Entrevistador:',max_length=30)
    #Data que foi feita a avaliação
    avaliation_date = models.DateField("Data da Avaliação", null=True)
    #Horário de Início
    start_time = models.TimeField("Hora do início da avaliação: ", null=True)
    #Horário final da avaliação
    end_time = models.TimeField("Hora do Término: ", null=True )
    #Data da Criação
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    #Data da ùltima atualização
    updated_at = models.DateTimeField('Atualizado em: ', auto_now = True, null= True)
    #Gerontólogo Responsável
    gerontologist = models.ForeignKey(Expert, on_delete=models.CASCADE, verbose_name='Gerontólogo Resposável')
    #Participante
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, verbose_name = 'Participante')
    #Dados do Participante no Momento da criação do Page
    participant_situation = models.ForeignKey(ParticipantSituation,on_delete=models.CASCADE, null=True, verbose_name = 'Situação do Participante')
    psychologicalAspects = models.OneToOneField(PsychologicalAspectsUsp, on_delete=models.CASCADE, null=True,verbose_name='Relacionados a Aspectos Psicológicos')
    biologicalAspects = models.OneToOneField(BiologicalAspectsUsp, on_delete=models.CASCADE, null=True,verbose_name='Relacionados a Aspectos Biológicos')
    socialAspects = models.OneToOneField(SocialAspectsUsp, on_delete=models.CASCADE, null=True,verbose_name='Relacionados a Aspectos Sociais')
    multidisciplinaryDomain = models.OneToOneField(MultidisciplinaryDomainUsp, on_delete=models.CASCADE, null=True,verbose_name='Domínio Multidisciplinar')
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



