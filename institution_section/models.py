from django.db import models
from activities_section.models import Activity

class Cidade(models.Model):
    cityName = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.cityName


class Address(models.Model):
    address = models.CharField(max_length=75)                       # logradouro
    number = models.CharField(max_length=8)
    complement = models.CharField(max_length=50)
    district = models.CharField(max_length=60)                      # bairro
    cep = models.CharField(max_length=9)
    latitude = models.FloatField()
    longitude = models.FloatField()
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING, null=True)
    reference = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.address + ' , ' + self.number


class TypePhoneEmail(models.Model):
    description = models.CharField(max_length=40)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.description


class TypeDigitalAddress(models.Model):
    description = models.CharField(max_length=50) 
    type = models.CharField(max_length=40) #Rede Social, blog, página web...
    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.description


class AssistanceModality (models.Model): ##Área de atuação
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.title

class TargetAudience (models.Model):
    description = models.TextField(null=True)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.description


class Institution(models.Model):
    companyName = models.CharField(max_length=60,null=True)
    companyFancyName = models.CharField(max_length=60,null=True)
    CNPJ = models.TextField(max_length=17,null=True)
    category = models.CharField(max_length=60, null= True)
    foundedIn = models.IntegerField(default=0, null=True)
    legalKind = models.CharField(max_length=60, null=True) # natureza legal
    objective = models.TextField(null=True)
    schedules = models.TextField(null=True)
    targetAudience = models.OneToOneField(TargetAudience, on_delete=models.DO_NOTHING, null=True)
    assitenceModality = models.ManyToManyField(AssistanceModality, through='ActingTime')
    address = models.OneToOneField (Address, on_delete= models.CASCADE, null=True)
    emailList = models.ManyToManyField(TypePhoneEmail,through='EmailInstitution', related_name='emails_institution')
    phoneList = models.ManyToManyField(TypePhoneEmail,through='PhoneInstitution', related_name='telefones_instituicao')
    webAddressList = models.ManyToManyField(TypeDigitalAddress,through='WebAddressInstitution', related_name='paginas_instituicao')

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.companyName


class ActingTime (models.Model):
    assistenceModality = models.ForeignKey(AssistanceModality, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    timeActing = models.IntegerField(default=0)
    historic = models.TextField(null= True)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.assistenceModality


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
    schedules = models.TextField(null=True)
    haveParking = models.BooleanField(null=True)
    parkingDescription = models.TextField(null=True)
    targetAudience = models.OneToOneField(TargetAudience, on_delete=models.DO_NOTHING, null=True)
    address = models.OneToOneField (Address, on_delete= models.CASCADE)
    emailList = models.ManyToManyField(TypePhoneEmail,through='EmailLocals', related_name='emails_local')
    phoneList = models.ManyToManyField(TypePhoneEmail,through='PhoneLocals', related_name='telefones_local')
    webAddressList = models.ManyToManyField(TypeDigitalAddress,through='WebAddressLocals', related_name='paginas_local')
    #technicalResponsible = models.ForeignKey(Professional, on_delete=models.DO_NOTHING)
 
    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.name


class ExpertiseAreas (models.Model):
    description : models.CharField(max_length=60)

    class Meta:
        ordering = ['id'] 

    def __str__ (self):
        return self.description


class AcademicEducation (models.Model):
    description : models.CharField(max_length=60)

    class Meta:
        ordering = ['id']    

    def __str__ (self):
        return self.description

class Professional(models.Model):
    name = models.CharField(max_length=45)
    RG = models.CharField(max_length=12, null=True)
    CPF = models.CharField(max_length=15, null=True)
    expertiseAreas = models.ManyToManyField(ExpertiseAreas)
    academicEducation = models.ManyToManyField(AcademicEducation)
    emailList = models.ManyToManyField(TypePhoneEmail,through='EmailProfessional', related_name='emails_professional')
    phoneList = models.ManyToManyField(TypePhoneEmail,through='PhoneProfessional', related_name='telefones_professional')
    webAddressList = models.ManyToManyField(TypeDigitalAddress,through='WebAddressProfessional', related_name="paginas_professional")

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.name


class Offers(models.Model):
    location = models.ForeignKey(Locals, on_delete=models.DO_NOTHING)
    activities = models.ManyToManyField(Activity,'atividades_ofertadas')
    responsibles = models.ManyToManyField(Professional, related_name="_responsibles")
    instructors = models.ManyToManyField(Professional,related_name="_instructors")
    targetAudience = models.OneToOneField(TargetAudience, on_delete=models.DO_NOTHING, null=True)
    enrollmentOpen = models.BooleanField(null=True)
    date_begin = models.DateField()
    date_end = models.DateField()
    environmentType = models.CharField(max_length=40, null=True)
    continuosFlow = models.BooleanField(null=True)
    schedule = models.TextField(null=True)
    specificObjectives = models.TextField(null=True)
    cost = models.CharField(max_length=100)
    exemption = models.CharField(max_length=100, null=True)
    motivation = models.TextField()
    requisites = models.TextField()

    healthyAging = models.BooleanField(null=True)

    partnership = models.TextField()
    home_care = models.CharField(max_length=1)

    comments = models.TextField()
    
    capacity = models.OneToOneField (Capacity, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.location


class WebAddress (models.Model):
    digitalAddress = models.CharField(max_length=100)
    type = models.ForeignKey(TypeDigitalAddress, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']    


class WebAddressInstitution (WebAddress):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']    

class WebAddressLocals (WebAddress):
    local = models.ForeignKey(Locals, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']    


class WebAddressProfessional (WebAddress):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']    

class Phone(models.Model):
    type = models.ForeignKey(TypePhoneEmail, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=14)

    class Meta:
        ordering = ['id']


class PhoneInstitution(Phone):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']


class PhoneLocals(Phone):
    local = models.ForeignKey(Locals, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']


class PhoneProfessional(Phone):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']


class Email(models.Model):
    type = models.ForeignKey(TypePhoneEmail, on_delete=models.CASCADE)
    email = models.EmailField()

    class Meta:
        ordering = ['id']


class EmailInstitution(Email):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']


class EmailLocals(Email):
    local = models.ForeignKey(Locals, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']


class EmailProfessional(Email):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']




