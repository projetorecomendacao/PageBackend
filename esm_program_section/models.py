from collections import defaultdict
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.timezone import activate, now

# definição dos observadores


class PersonEsm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(default='')
    phoneNumber = models.CharField(
        max_length=20, default='', null=True, blank=True)
    profilePhotoUrl = models.URLField(blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        ordering = ['id']

    def __str__(self):
        return f"{self.id} - {self.name}"


class EditorProgram(PersonEsm):
    role = models.CharField(max_length=50, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    birthDate = models.DateField(blank=True, null=True)
    schooling = models.CharField(max_length=50, blank=True, null=True)
    institution = models.CharField(max_length=40, blank=True, null=True)
    #address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    #contacts = models.ManyToManyField(Participant, related_name='contacts', blank=True)
    #observerContacts = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


# Definição do programa
# Programa ESM
class Program(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500, default="", blank=True)
    activate = models.CharField(max_length=1, default='y')  # y-yes  n=no
    updateDate = models.CharField(max_length=50, blank=True)
    updateDateNew = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    createDate = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    class Meta:
        ordering = ['-updateDate']


# Definição das intervenções

# Event_trigger
class EventTrigger(models.Model):
    triggerType = models.CharField(max_length=10, default="time")
    triggerCondition = models.CharField(max_length=50)
    priority = models.CharField(max_length=20)
    timeOut = models.IntegerField(default=1800000)

    class Meta:
        verbose_name = 'EventTrigger'
        verbose_name_plural = 'EventTriggers'
        ordering = ['id']

# Sensor


class Sensor(models.Model):
    sensorType = models.IntegerField(null=False)
    sensor = models.CharField(max_length=20, default='activity')
    collector = models.CharField(max_length=20, default="smartwatch")

    def __str__(self):
        return f"{self.id} - {self.sensorType} - {self.sensor} - {self.collector}"

    class Meta:
        ordering = ['id']

# Apresentação de mídia


class MediaPresentation(models.Model):
    type = models.CharField(max_length=10, default="image")
    mediaUrl = models.URLField()
    autoPlay = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']


# Condição complexa
class ComplexCondition(models.Model):
    dependentConditions = models.CharField(
        max_length=150, default="MISSED GREATER_THAN 0")
    action = models.CharField(
        max_length=150, default="POSTPONE_EVENT MINUTES 60")

    class Meta:
        ordering = ['id']

# Evento


class Event(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, default="", blank=True)
    type = models.CharField(max_length=50, default="active")
    color = models.CharField(max_length=50, default='#0F5394', blank=True, null=True)
    activate = models.CharField(max_length=1, default='y')  # y-yes  n=no
    program = models.ForeignKey(Program, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['id']


# Evento Ativo
class ActiveEvent(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, default="", blank=True)
    type = models.CharField(max_length=50, default="active")
    activate = models.CharField(max_length=1, default='y')  # y-yes  n=no
    program = models.ForeignKey(Program, null=True, on_delete=models.DO_NOTHING)

    #campos criados para controle do gráfico
    first = models.IntegerField(null=True, blank=True, default=0)
    next = models.IntegerField(null=True, blank=True, default=0)


    ## Esta parte está implementada de forma simplificada para facilitar a implementação da
    ## colaboração.. Deve ser colocada no padrão na próxima versão..
    typeBell = models.CharField(max_length=2, null=True, default='NC')
    durationBell = models.IntegerField(null=True, default=0)
    seg = models.CharField(max_length=1, null=True, default='n') # y=yes n=no
    ter = models.CharField(max_length=1, null=True, default='n')
    qua = models.CharField(max_length=1, null=True, default='n')
    qui = models.CharField(max_length=1, null=True, default='n')
    sex = models.CharField(max_length=1, null=True, default='n')
    sab = models.CharField(max_length=1, null=True, default='n')
    dom = models.CharField(max_length=1, null=True, default='n')
    hour = models.IntegerField(null=True, default=0)
    minute = models.IntegerField(null=True,default=0)
    color = models.CharField(max_length=50, default='#0F5394', blank=True, null=True)
    
    class Meta:
        ordering = ['id']


# Intervenções
class Intervention(models.Model):
    activate = models.CharField(max_length=1, default='y')  # y-yes  n=no
    
 
    #type = models.CharField(max_length=10, default="empty")
    #questionType = models.IntegerField(default=0, null=True, blank=True)

    # o campo statement irá conter todos os dados da intervenção
    # nesta versão de teste não está sendo pensado no app
    #depois precisa ser ampliado isso e transformado tudo em BD
    intervention = models.JSONField(null=True, blank = True)

    #Chave Primária do Evento
    event = models.ForeignKey(ActiveEvent, null=True, on_delete=models.DO_NOTHING)

    #esta é a parte sensível da colaboração
    #todos estes dados serão criados por um dos clientes no frontend
    #mas terá que ser trazida para o backend...
    #inclusive o posicionamento..
    #orderPosition = models.IntegerField(default=1000000)
    #first = models.BooleanField(default=False)
    #next = models.IntegerField(default=-1)
    #obligatory = models.BooleanField(default=False)
    # Pensando no modelo colaborativo a posição é importante
    # Posicionamento


    ## Estes campos ainda não estão sendo utilizados...
    ## Mas deverão ser acertados quando a parte da colaboração for finalizada..

    # Mídias que irão junto com a intervenção
    #medias = models.ManyToManyField(MediaPresentation, blank=True, null=True)



    # As condições complexas serão repensadas na próxima versão
    #complexConditions = models.ManyToManyField(ComplexCondition, blank=True, null=True)

    class Meta:
        ordering = ['id']


class Log(models.Model):
    date = models.CharField(max_length=50, default="", blank=True)
    email = models.EmailField(default='')
    urlForDataFile = models.URLField(blank=True)

    class Meta:
        ordering = ['id']


class ActionsEsm(models.Model):
    # c-create d-delete u-update
    actionType = models.CharField(max_length=1, default="c")
    # p-program e-event i-intervention
    objectType = models.CharField(max_length=1, default="p")
    program_id = models.IntegerField(null=True, blank=True, default=-1)
    event_id = models.IntegerField(null=True, blank=True, default=-1)
    intervention_id = models.IntegerField(null=True, blank=True, default=-1)
    anterior = models.JSONField(null=True, blank=True)
    editor = models.ForeignKey(
        EditorProgram, on_delete=models.DO_NOTHING, null=True, blank=True)
    actionDate = models.CharField(max_length=50, blank=True, null=True)
    createDate = models.DateTimeField(auto_now_add=True, null=True)
