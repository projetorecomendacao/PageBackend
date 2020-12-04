from django.db import models
from activities_section.models import Activity

class Cidade(models.Model):
    cityName = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class AddressPlace(models.Model):
    public_place = models.CharField(max_length=75, blank=True)     # logradouro
    number_place = models.CharField(max_length=8, blank=True)      #número 
    complement = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=60, blank=True)         # bairro
    cep = models.CharField(max_length=9, blank=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING, null=True, blank=True)
    reference_point = models.CharField(max_length=50, blank=True)
    haveParking = models.BooleanField(null=True, blank=True)
    parkingDescription = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.public_place + ' , ' + self.number_place


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


class ActingArea (models.Model): ##Área de atuação
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.title


class TargetAudience (models.Model):
    most_people_served_type = models.CharField(max_length=40, null=True, blank=True)
    people_can_be_served = models.CharField(max_length=40, null=True, blank=True)
    most_people_served_sex = models.CharField(max_length=40, null=True, blank=True)
    most_people_served_range_age = models.CharField(max_length=40, null=True, blank=True)
    most_people_served_incapacity = models.CharField(max_length=140, null=True, blank=True)
    comments = models.TextField(null=True,blank=True)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.most_people_served_type + ' : ' + self.people_can_be_served + ' : ' + self.most_people_served_sex

class Capacity(models.Model):
    capacity_free_m = models.IntegerField(null=True)
    capacity_used_m = models.IntegerField(null=True)
    capacity_free_f = models.IntegerField(null=True)
    capacity_used_f = models.IntegerField(null=True)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return  'M (free/used): ' + str(self.capacity_free_m) + '/' + str(self.capacity_used_m) +  '-  F(free/used): ' + str(self.capacity_free_f) + '/' + str(self.capacity_used_f) 


class ExpertiseAreas (models.Model):
    description = models.CharField(max_length=60)

    class Meta:
        ordering = ['id'] 

    def __str__ (self):
        return self.description


class AcademicEducation (models.Model):
    description = models.CharField(max_length=60)

    class Meta:
        ordering = ['id']    

    def __str__ (self):
        return self.description


class Professional(models.Model):
    name = models.CharField(max_length=45)
    RG = models.CharField(max_length=12, null=True)
    CPF = models.CharField(max_length=15, null=True)
    expertiseAreas = models.ManyToManyField(ExpertiseAreas, null=True)
    academicEducation = models.ManyToManyField(AcademicEducation, null=True)
    #emailList = models.ManyToManyField(TypePhoneEmail,through='EmailProfessional', related_name='emails_professional', null=True)
    #phoneList = models.ManyToManyField(TypePhoneEmail,through='PhoneProfessional', related_name='telefones_professional', null=True)
    #webAddressList = models.ManyToManyField(TypeDigitalAddress,through='WebAddressProfessional', related_name="paginas_professional", null=True)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.name


class Institution(models.Model):
    company_name = models.CharField(max_length=60,null=True)
    trading_name = models.CharField(max_length=60,null=True)
    trading_name_know = models.CharField(max_length=60,null=True)
    cnpj = models.CharField(max_length=18,null=True)
    category = models.CharField(max_length=60, null= True)
    foundation_year = models.IntegerField(default=0, null=True)
    legal_nature = models.CharField(max_length=60, null=True) # natureza legal
    objective = models.TextField(null=True)
    addressPlace = models.OneToOneField (AddressPlace, on_delete= models.CASCADE, null=True) 
    capacity = models.OneToOneField(Capacity,on_delete=models.CASCADE ,null=True, blank=True)
    mainActingArea = models.ForeignKey(ActingArea, on_delete=models.DO_NOTHING, null=True)
    schedules = models.TextField(null=True)
    targetAudience = models.OneToOneField(TargetAudience, on_delete=models.DO_NOTHING, null=True)
    technicalResponsible = models.ForeignKey(Professional, on_delete=models.DO_NOTHING, null=True)
 
    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.company_name


class Offers(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE,null=True)
    activities = models.ManyToManyField(Activity,'atividades_ofertadas')
    responsibles = models.ManyToManyField(Professional, related_name="_responsibles")
    instructors = models.ManyToManyField(Professional,related_name="_instructors")
    targetAudience = models.OneToOneField(TargetAudience, on_delete=models.DO_NOTHING, null=True)
    enrollmentOpen = models.BooleanField(null=True) ## marículas abertas
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
    peopleRecommender = models.CharField(max_length=100,null=True, blank=True)
    comments = models.TextField()
    capacity = models.OneToOneField (Capacity, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__ (self):
        return self.location


class WebAddress (models.Model):
    digital_address = models.CharField(max_length=100)
    description = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        ordering = ['id']    


class WebAddressInstitution (WebAddress):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']    


class Phone(models.Model):
    description = models.CharField(max_length=40, null=True, blank=True)
    phone_number = models.CharField(max_length=14)

    class Meta:
        ordering = ['id']


class PhoneInstitution(Phone):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']


class Email(models.Model):
    description = models.CharField(max_length=40, null=True, blank=True)
    email_address = models.EmailField()

    class Meta:
        ordering = ['id']


class EmailInstitution(Email):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

'''
class WebAddressProfessional (WebAddress):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']    


class PhoneProfessional(Phone):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']


class EmailProfessional(Email):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

'''

