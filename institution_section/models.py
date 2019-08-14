from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=75)                       # logradouro
    number = models.IntegerField()
    district = models.CharField(max_length=40)                      # bairro
    cep = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def public_transportation(self):
        pass

    class Meta:
        ordering = ['id']


class Professional(models.Model):
    name = models.CharField(max_length=45)
    communication = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']


class Instructor(Professional):
    formation = models.CharField(max_length=45)

    class Meta:
        ordering = ['id']


class Responsible(Professional):
    # area
    class Meta:
        ordering = ['id']


class Institution(models.Model):
    name = models.CharField(max_length=45)
    communication = models.CharField(max_length=50)

    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='institution')

    class Meta:
        ordering = ['id']


class Location(models.Model):
    name = models.CharField(max_length=45)
    communication = models.CharField(max_length=50)
    parking = models.CharField(max_length=50)

    # Confirmar se ondelete é do Nothing
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='locations')
    institution = models.ForeignKey(Institution, on_delete=models.DO_NOTHING, related_name='locations')

    class Meta:
        ordering = ['id']


class Contact(Professional):
    institution = models.ForeignKey(Institution, on_delete=models.DO_NOTHING, related_name='contacts')
    locations = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='contacts')
    # department

    class Meta:
        ordering = ['id']
