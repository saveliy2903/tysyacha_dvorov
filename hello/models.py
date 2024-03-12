from django.db import models
from django.contrib.auth.models import User


class Type_jobs(models.Model):
    name = models.CharField(max_length=50)


class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=10)


class Application(models.Model):
    quantity_MKD = models.SmallIntegerField()  # число МКД
    number_people = models.PositiveIntegerField()  # количество жильцов
    yard_area = models.FloatField()  # площадь двора
    percentage_of_vote = models.FloatField()  # процент голосов от общего числа собственников
    types = models.ManyToManyField(Type_jobs, through="Application_type")  # тип благоустройства
    address = models.ManyToManyField(Address, through="Application_address")  # адреса
    participation_in_municipal = models.BooleanField()  # участие в муницип. программах по благоустройству двора
    point = models.SmallIntegerField()  # оценка заявки(кол баллов)
    link_to_crt = models.CharField(max_length=255)  # ссылка на ЦРТ дизайн
    link_to_protocol = models.CharField(max_length=255)  # ссылка на протокол собрания
    date_create = models.DateTimeField(auto_now_add=True)  # дата создания заявки
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class Application_type(models.Model):
    type_jobs = models.ForeignKey(Type_jobs, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)


class Application_address(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)