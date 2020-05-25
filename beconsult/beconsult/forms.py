#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator

from beconsult.models import *

# Translating errors messages on forms
from django.forms import Field
from django.utils.translation import ugettext_lazy

PASSWORD_VALIDATOR = RegexValidator(
    regex="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$",
    message='Debes tener mínimo 6 caracteres en la clave, mínimo una letra y un número.',
)

DATE_VALIDATOR = RegexValidator(
    regex='(\d{2})[/.-](\d{2})[/.-](\d{4})$',
    message='Debe introducir una fecha válida.',
)


class UserForm(forms.ModelForm):
    # Associate model fields of model Postulacion to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Roberto Romero]
    #
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

        widgets = {
            'password': forms.PasswordInput(),
            'username': forms.EmailInput(),
        }

        labels = {
            'username': 'Correo electrónico'
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['type'] = 'email'
        self.fields['password'].validators = [PASSWORD_VALIDATOR]

        for key in self.fields:
            self.fields[key].required = True
            self.fields[key].widget.attrs['required'] = 'True'


class UserEditForm(forms.ModelForm):
    # Associate model fields of model Postulacion to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Roberto Romero]
    #
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

        widgets = {
            'username': forms.EmailInput(),
        }

        labels = {
            'username': 'Correo electrónico'
        }

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['type'] = 'email'

        for key in self.fields:
            self.fields[key].required = True
            self.fields[key].widget.attrs['required'] = 'True'


class PostulacionForm1(forms.ModelForm):
    # Associate model fields of model Postulacion to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Roberto Romero]
    #


    class Meta:
        model = Postulacion
        fields = ['name', 'lastName', 'email', 'documentId']

        labels = {
            'name': 'Nombre',
            'lastName': 'Apellido',
            'email': 'Correo',
            'documentId': 'Cédula de identidad',
        }


    def __init__(self, *args, **kwargs):
        super(PostulacionForm1, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['lastName'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['email'].widget.attrs['placeholder'] = 'ej: email@example.com'
        self.fields['email'].widget.attrs['oninvalid'] = "setCustomValidity('Email inválido')"
        self.fields['email'].widget.attrs['onchange'] = "setCustomValidity('')"
        self.fields['documentId'].widget.attrs['placeholder'] = 'ej: 12345678'
        self.fields['documentId'].widget.attrs['pattern'] = '[0-9]{6,9}'
        self.fields['documentId'].widget.attrs['oninvalid'] = "setCustomValidity('Cédula inválida')"
        self.fields['documentId'].widget.attrs['onchange'] = "setCustomValidity('')"

        for key in self.fields:
            self.fields[key].required = True
            self.fields[key].widget.attrs['required'] = 'True'

class PostulacionForm2(forms.ModelForm):
    # Associate model fields of model Postulacion to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Roberto Romero]
    #
    class Meta:
        model = Postulacion
        fields = ['city']

        labels = {
            'city': 'Ciudad de residencia'
        }

    def __init__(self, *args, **kwargs):
        super(PostulacionForm2, self).__init__(*args, **kwargs)

        self.fields['city'].widget.attrs['placeholder'] = 'ej: Caracas'


class PostulacionForm3(forms.ModelForm):
    # Associate model fields of model Postulacion to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Roberto Romero]
    #
    class Meta:
        model = Postulacion
        fields = ['studies']

        labels = {
            'studies': 'Nivel académico'
        }

    def __init__(self, *args, **kwargs):
        super(PostulacionForm3, self).__init__(*args, **kwargs)

        self.fields['studies'].widget.attrs['placeholder'] = 'ej: Bachiller'


class PostulacionForm4(forms.ModelForm):
    # Associate model fields of model Postulacion to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Roberto Romero]
    #
    class Meta:
        model = Postulacion
        fields = ['cv']

        labels = {
            'cv': 'Adjuntar'
        }


class PostulacionForm5(forms.ModelForm):
    # Associate model fields of model Postulacion to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Roberto Romero]
    #
    class Meta:
        model = Postulacion
        fields = ['aspSalarial', 'salActual']

        labels = {
            'aspSalarial': 'Aspiración Salarial',
            'salActual': 'Salario Actual',
        }

    def __init__(self, *args, **kwargs):
        super(PostulacionForm5, self).__init__(*args, **kwargs)

        self.fields['aspSalarial'].widget.attrs['min'] = '0'
        self.fields['salActual'].widget.attrs['min'] = '0'


class TittleForm(forms.ModelForm):
    # Associate model fields of model tittle to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Roberto Romero]
    #
    class Meta:
        model = Tittle
        fields = '__all__'

        labels = {
            'name': 'Nombre del cargo',
            'description': 'Descripción',
            'dep': 'Departamento',
        }

    def __init__(self, *args, **kwargs):
        super(TittleForm, self).__init__(*args, **kwargs)

        self.fields['linkedInLink'].required = False
        self.fields['bumeranLink'].required = False


class QuestionForm(forms.ModelForm):
    # Associate model fields of model question to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Roberto Romero]
    #
    class Meta:
        model = Questions
        fields = '__all__'

        labels = {
            'question': 'Pregunta'
        }


class OfferForm(forms.ModelForm):
    # Associate model fields of model offer to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Roberto Romero]
    #
    class Meta:
        model = JobOffer
        fields = '__all__'

        labels = {
            'tittle': 'Cargo',
            'vacancy': 'Vacantes',
            'active': 'Activa',
        }

    def __init__(self, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)

        self.fields['vacancy'].widget.attrs['min'] = '1'


class MailForm(forms.ModelForm):
    # Associate model fields of model mails to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Roberto Romero]
    #
    class Meta:
        model = Mails
        fields = '__all__'

        labels = {
            'postBeconsultMail': 'HTML de email para beconsult para nueva postulación',
            'postMail': 'HTML de email de confirmación de nueva postulación',
            'pswMail': 'HTML de email para recuperación de contraseña',
        }

class MessageForm(forms.ModelForm):
    # Associate model fields of model mails to the Form
    #
    # @date [14/08/2017]
    #
    # @author [Patricia Valencia]
    #
    class Meta:
        model = Message
        fields = '__all__'

        labels = {
            'messgPost': 'Mensaje de postulación que se mostrará al usuario al realizar dicha acción',
        }
