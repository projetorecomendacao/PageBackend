from django.db import models
from activities_section.models import Activity


class ContactMeans(models.Model):
    email = models.EmailField('E-mail')
    phone = models.CharField(max_length=14)
    mobilePhone = models.CharField(max_length=14)
    fax = models.CharField(max_length=14)

    class Meta:
        ordering = ['id']


class Cidade(models.Model):
    cityName = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['id']


class Address(models.Model):
    address = models.CharField(max_length=75)                       # logradouro
    number = models.CharField(max_length=8)
    district = models.CharField(max_length=60)                      # bairro
    cep = models.CharField(max_length=9)
    latitude = models.FloatField()
    longitude = models.FloatField()
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        ordering = ['id']


class WebAddress (models.Model):
    webPage = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    tweeter = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']    


class ExpertiseAreas (models.Model):
    description : models.CharField(max_length=60)

    class Meta:
        ordering = ['id'] 

class AcademicEducation (models.Model):
    description : models.CharField(max_length=60)

    class Meta:
        ordering = ['id']    


class Professional(models.Model):
    name = models.CharField(max_length=45)
    RG = models.CharField(max_length=12, null=True)
    CPF = models.CharField(max_length=15, null=True)
    contactMeans = models.OneToOneField(ContactMeans, on_delete= models.CASCADE, null=True)
    webAddress = models.OneToOneField(WebAddress, on_delete= models.CASCADE, null=True)
    expertiseAreas = models.ManyToManyField(ExpertiseAreas)
    academicEducation = models.ManyToManyField(AcademicEducation)

    class Meta:
        ordering = ['id']


class AssistanceModality (models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']


class Institution(models.Model):
    companyName = models.CharField(max_length=60,null=True)
    companyFancyName = models.CharField(max_length=60,null=True)
    CNPJ = models.TextField(max_length=17,null=True)
    objective = models.TextField(null=True)
    targetAudience = models.TextField(max_length=50, null=True)
    ageTargetAudience = models.TextField(max_length=50, null=True)
    comments = models.TextField(null=True)
    assitence = models.ManyToManyField(AssistanceModality, through='ActingTime', null=True)
    contactMeans = models.OneToOneField (ContactMeans, on_delete=models.CASCADE, null=True)
    address = models.OneToOneField (Address, on_delete= models.CASCADE, null=True)
    webAddress = models.OneToOneField (WebAddress, on_delete= models.CASCADE, null=True)

    class Meta:
        ordering = ['id']


class ActingTime (models.Model):
    assistenceModality = models.ForeignKey(AssistanceModality, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    timeActing = models.IntegerField(default=0)
    historic = models.TextField(null= True)

    class Meta:
        ordering = ['id']


class Capacity(models.Model):
    CAD = models.IntegerField(null=True) # capacidade de atendimento
    CAD_M = models.IntegerField(null=True)
    CAD_F = models.IntegerField(null=True)
    CAP = models.IntegerField(null=True) # capacidade de atendimento preenchida
    CAP_M = models.IntegerField(null=True)
    CAP_F = models.IntegerField(null=True)

    class Meta:
        ordering = ['id']


class LongaDuracao(models.Model):
    capacity = models.OneToOneField (Capacity, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['id']


class Locals(models.Model):
    name = models.CharField(max_length=45)
    objective = models.TextField(null=True)
    targetAudience = models.TextField(max_length=50, null=True)
    ageTargetAudience = models.TextField(max_length=50, null=True)
    comments = models.TextField(null=True)
    contactMeans = models.OneToOneField (ContactMeans, on_delete=models.CASCADE)
    address = models.OneToOneField (Address, on_delete= models.CASCADE)
    webAddress = models.OneToOneField (WebAddress, on_delete= models.CASCADE)
    technicalResponsible = models.ForeignKey(Professional, on_delete=models.DO_NOTHING)
 
    class Meta:
        ordering = ['id']


class Offers(models.Model):
    location = models.ForeignKey(Locals, on_delete=models.DO_NOTHING)
    activities = models.ManyToManyField(Activity)
    responsibles = models.ManyToManyField(Professional, related_name="_responsibles")
    instructors = models.ManyToManyField(Professional,related_name="_instructors")
    date_begin = models.DateField()
    date_end = models.DateField()
    schedule = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    genre_goals = models.CharField(max_length=1)
    ambience = models.CharField(max_length=1)
    active_aging = models.CharField(max_length=1)
    motivation = models.TextField()
    people_class = models.IntegerField()
    loe_income = models.CharField(max_length=1)
    partnership = models.TextField()
    home_care = models.CharField(max_length=1)
    requisites = models.TextField()
    comments = models.TextField()
    capacity = models.OneToOneField (Capacity, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
    