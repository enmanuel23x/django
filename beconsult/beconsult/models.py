# ------------------------------------------------------ IMPORTS -------------------------------------------------------

# import base model
from django.db import models
# import for Django's user model
from django.contrib.auth.models import User
# import datetime library
import datetime


# ------------------------------------------------------ MODELS -------------------------------------------------------

class Tittle(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=20)
    dep = models.CharField(max_length=50)
    linkedInLink = models.CharField(max_length=500)
    bumeranLink = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' - ' + self.dep


class Questions(models.Model):
    question = models.CharField(max_length=1000)


class JobOffer(models.Model):
    tittle = models.ForeignKey(Tittle)
    vacancy = models.PositiveIntegerField()
    active = models.BooleanField()


class Postulacion(models.Model):
    tittle = models.ForeignKey(Tittle)
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    documentId = models.CharField(max_length=20)
    birthDate = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50)
    studies = models.CharField(max_length=50)
    cv = models.FileField(upload_to='cvs')
    status = models.CharField(max_length=20)
    postulacionDate = models.DateField()
    approved = models.BooleanField()
    accepted = models.BooleanField()
    whyNotAccepted = models.CharField(max_length=1000)
    age = models.IntegerField(blank=True, null=True)
    aspSalarial = models.FloatField()
    salActual = models.FloatField()


class QuestionsAndAnswers(models.Model):
    postulacionId = models.ForeignKey(Postulacion)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)


class Mails(models.Model):
    pswMail = models.TextField()
    postMail = models.TextField()
    postBeconsultMail = models.TextField()

class Message(models.Model):
    messgPost = models.TextField()
