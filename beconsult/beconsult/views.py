from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import deprecate_current_app
from django.shortcuts import render, redirect, resolve_url
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import TemplateView
from beconsult.forms import *
from beconsult.models import Tittle
from datetime import date
from django.db.models import Sum
import csv
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.utils.safestring import mark_safe

BECONSULT_EMAIL = 'contactobeconsult@gmail.com'


# Seds a mail with the content subtype HTML.
# @param [Sting] subject The mail subject.
# @param [Sting] message The mail body.
# @param [String] email The user associated email to send the mail message.
# @param [String] from_email Who sends the mail.
#
def send_html_email(subject, message, email, from_email):
    try:
        email_message = EmailMessage(subject, message, to=[email, BECONSULT_EMAIL],
                                     from_email=from_email)
        email_message.content_subtype = 'html'
        email_message.send()
    except Exception as ex:
        print("<< Exception >>", ex)


class SignUpView(LoginRequiredMixin, TemplateView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['form'] = UserForm()
        return context

    def post(self, request, *args, **kwargs):
        post_values = request.POST.copy()
        form = UserForm(post_values)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(post_values['password'])
            new_user.email = post_values['username']
            new_user.save()
        else:
            return render(request, self.template_name,
                          {'form': form, 'error': "Ese nombre de usuario ya se encuentra registrado"})
        return redirect('viewUsers')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


# Form template view
#
# @date [24/11/2016]
#
# @author [Roberto Romero]
#
# @param [None]
#
# @returns [None]
#
class FormView(TemplateView):
    template_name = 'formulario.html'

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        try:
            cargo = Tittle.objects.get(id=int(kwargs['pk']))
        except:
            context['exist'] = False
            return context
        try:
            disp = JobOffer.objects.get(tittle=cargo, active=True)
            context['offer'] = True
            context['form1'] = PostulacionForm1()
            context['form2'] = PostulacionForm2()
            context['form3'] = PostulacionForm3()
            context['form4'] = PostulacionForm4()
            context['form5'] = PostulacionForm5()
            context['cargo'] = Tittle.objects.get(id=int(kwargs['pk']))
            context['questions'] = Questions.objects.all()
            return context
        except:
            context['exist'] = True
            context['cargo'] = Tittle.objects.get(id=int(kwargs['pk']))
            context['offer'] = False
        return context

    def post(self, request, *args, **kwargs):
        post_values = request.POST.copy()
        post_files = request.FILES

        form1 = PostulacionForm1(post_values)
        form2 = PostulacionForm2(post_values)
        form3 = PostulacionForm3(post_values)
        form5 = PostulacionForm5(post_values)
        form4 = PostulacionForm4(post_files['cv'])
        if form4.is_valid():
            form4.save()
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form5.is_valid():
            cargo = Tittle.objects.get(id=int(post_values['cargo']))
            postulacionDate = date.today()
            name=post_values['name']
            lastname=post_values['lastName']
            email=post_values['email']
            documentId=post_values['documentId']
            # creating new object postulacion
            newPostulacion = Postulacion.objects.create(name=name, lastName=lastname, city=post_values['city'], studies=post_values['studies'],
                                                        documentId=documentId, email=email,
                                                        postulacionDate=postulacionDate, approved=False, accepted=False,
                                                        tittle=cargo, aspSalarial=post_values['aspSalarial'], salActual=post_values['salActual'])
            newPostulacion.cv = post_files['cv']
            newPostulacion.save()

            #Q&A
            questions = Questions.objects.all()
            for q in questions:
                qAns = QuestionsAndAnswers.objects.create(question=q.question, answer=post_values["questions"+str(q.id)],
                                                           postulacionId=newPostulacion)
            mails = Mails.objects.all().first()
            # send email to the user
            data = {
                'html': mails.postMail,
            }
            subject = 'Beconsult - Confirmación de postulación'
            message = get_template('postMail.html').render(data)
            send_html_email(subject, message, email, BECONSULT_EMAIL)
            # send email to beconsult
            data = {
                'html': mails.postMail,
                'cargo': cargo.name,
                'nombre': name,
                'apellido': lastname,
                'cedula': documentId,
            }
            subject = 'Beconsult - Nueva postulación'
            message = get_template('postBeconsultMail.html').render(data)
            send_html_email(subject, message, BECONSULT_EMAIL, BECONSULT_EMAIL)
            message =  Message.objects.all().first()
            messages.success(request, message)
            return redirect(reverse('form', kwargs={'pk': int(post_values['cargo'])}))
        else:
            messages.error(request, "Error de registro")
            return render(request, self.template_name, {'form1': form1, 'form2': form2, 'form3': form3})


class AddTittleView(LoginRequiredMixin, TemplateView):
    template_name = 'add_tittle.html'

    def get_context_data(self, **kwargs):
        context = super(AddTittleView, self).get_context_data(**kwargs)
        context['form'] = TittleForm()
        return context

    def post(self, request, *args, **kwargs):
        post_values = request.POST.copy()
        form = TittleForm(post_values)

        if form.is_valid():
            form.save()
            return redirect('viewTittles')
        else:
            return render(request, self.template_name, {'form': form})


class TittleEdit(LoginRequiredMixin, TemplateView):
    template_name = 'edit_tittle.html'

    def get_context_data(self, **kwargs):
        context = super(TittleEdit, self).get_context_data(**kwargs)
        # try:
        tittle = Tittle.objects.get(pk=int(kwargs['pk']))

        context['form'] = TittleForm(instance=tittle)

        return context

    def post(self, request, *args, **kwargs):
        post_values = request.POST.copy()
        tittle = Tittle.objects.get(pk=int(kwargs['pk']))
        form = TittleForm(post_values, instance=tittle)

        if form.is_valid():
            form.save()
        else:
            request.session.pop('msg', False)
            context = {'form': form}
            return render(request, 'edit_tittle.html', context)

        return redirect('viewTittles')


class DeleteTittleView(LoginRequiredMixin, TemplateView):
    template_name = 'add_tittle.html'

    def get(self, request, *args, **kwargs):
        delete = Tittle.objects.get(pk=int(kwargs['pk']))
        delete.delete()
        return redirect('viewTittles')


class ViewTittlesView(LoginRequiredMixin, TemplateView):
    template_name = 'view_tittles.html'

    def get_context_data(self, **kwargs):
        context = super(ViewTittlesView, self).get_context_data(**kwargs)
        context['titles'] = Tittle.objects.all()
        return context


class ViewPostsView(LoginRequiredMixin, TemplateView):
    template_name = 'view_post.html'

    def get_context_data(self, **kwargs):
        context = super(ViewPostsView, self).get_context_data(**kwargs)
        context['posts'] = Postulacion.objects.all()
        return context


class ViewQuestionsView(LoginRequiredMixin, TemplateView):
    template_name = 'view_questions.html'

    def get_context_data(self, **kwargs):
        context = super(ViewQuestionsView, self).get_context_data(**kwargs)
        context['questions'] = Questions.objects.all()
        return context


class QuestionEdit(LoginRequiredMixin, TemplateView):
    template_name = 'edit_question.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionEdit, self).get_context_data(**kwargs)
        # try:
        question = Questions.objects.get(pk=int(kwargs['pk']))

        context['form'] = QuestionForm(instance=question)

        return context

    def post(self, request, *args, **kwargs):
        context = {}
        post_values = request.POST.copy()
        question = Questions.objects.get(pk=int(kwargs['pk']))
        form = QuestionForm(post_values, instance=question)

        if form.is_valid():
            form.save()
        else:
            request.session.pop('msg', False)
            context = {'form': form}
            return render(request, 'edit_question.html', context)

        return redirect('viewQuestions')


class AddQuestionView(LoginRequiredMixin, TemplateView):
    template_name = 'add_question.html'

    def get_context_data(self, **kwargs):
        context = super(AddQuestionView, self).get_context_data(**kwargs)
        context['form'] = QuestionForm()
        return context

    def post(self, request, *args, **kwargs):
        post_values = request.POST.copy()
        form = QuestionForm(post_values)

        if form.is_valid():
            form.save()
            return redirect('viewQuestions')
        else:
            return render(request, self.template_name, {'form': form})


class DeleteQuestionView(LoginRequiredMixin, TemplateView):
    template_name = 'add_question.html'

    def get(self, request, *args, **kwargs):
        delete = Questions.objects.get(pk=int(kwargs['pk']))
        delete.delete()
        return redirect('viewQuestions')


class PostDetails(LoginRequiredMixin, TemplateView):
    template_name = 'post_details.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetails, self).get_context_data(**kwargs)
        # try:
        context['post'] = Postulacion.objects.get(pk=int(kwargs['pk']))
        context['questions'] = QuestionsAndAnswers.objects.filter(postulacionId=int(kwargs['pk']))
        return context


class ApprovedPostView(LoginRequiredMixin, TemplateView):
    template_name = 'post_details.html'

    def get(self, request, *args, **kwargs):
        post = Postulacion.objects.get(pk=int(kwargs['pk']))
        post.approved = True
        post.save()
        return redirect(reverse('viewPostsDetails', kwargs={'pk': int(kwargs['pk'])}))


class NotApprovedPostView(LoginRequiredMixin, TemplateView):
    template_name = 'post_details.html'

    def get(self, request, *args, **kwargs):
        post = Postulacion.objects.get(pk=int(kwargs['pk']))
        post.approved = False
        post.save()
        return redirect(reverse('viewPostsDetails', kwargs={'pk': int(kwargs['pk'])}))


class AcceptedPostView(LoginRequiredMixin, TemplateView):
    template_name = 'post_details.html'

    def get(self, request, *args, **kwargs):
        post = Postulacion.objects.get(pk=int(kwargs['pk']))
        try:
            offer = JobOffer.objects.get(tittle_id=post.tittle)
            if offer.vacancy > 0:
                offer.vacancy -= 1
            if offer.vacancy <= 0:
                offer.active = False
            offer.save()
        except:
            pass
        post.accepted = True
        post.save()
        return redirect(reverse('viewPostsDetails', kwargs={'pk': int(kwargs['pk'])}))


class NotAcceptedPostView(LoginRequiredMixin, TemplateView):
    template_name = 'post_details.html'

    def get(self, request, *args, **kwargs):
        post = Postulacion.objects.get(pk=int(kwargs['pk']))
        post.accepted = False
        post.save()
        return redirect(reverse('viewPostsDetails', kwargs={'pk': int(kwargs['pk'])}))


class AddReasonView(LoginRequiredMixin, TemplateView):
    template_name = 'post_details.html'

    def post(self, request, *args, **kwargs):
        post = Postulacion.objects.get(pk=int(kwargs['pk']))
        post_values = request.POST.copy()
        post.whyNotAccepted = post_values['reason']
        post.save()
        return redirect(reverse('viewPostsDetails', kwargs={'pk': int(kwargs['pk'])}))


class InscView(LoginRequiredMixin, TemplateView):
    template_name = 'insc.html'

    def get_context_data(self, **kwargs):

        class cargo:
            def __init__(self, name, insc):
                self.insc = insc
                self.name = name

        context = super(InscView, self).get_context_data(**kwargs)
        context['total'] = Postulacion.objects.count()
        cargos = Tittle.objects.all()
        cargosid = []
        for i in cargos:
            cargosid.append(i.id)
        cargosobj = []
        for j in cargosid:
            cargoaux = cargo(Tittle.objects.get(id=j).name, Postulacion.objects.filter(tittle_id=j).count())
            cargosobj.append(cargoaux)
        context['cargosobj'] = cargosobj
        return context


class CandView(LoginRequiredMixin, TemplateView):
    template_name = 'cand.html'

    def get_context_data(self, **kwargs):
        context = super(CandView, self).get_context_data(**kwargs)
        context['total'] = Postulacion.objects.count()
        context['accepted'] = Postulacion.objects.filter(accepted=True).count()
        context['noaccepted'] = Postulacion.objects.filter(accepted=False).count()
        context['approved'] = Postulacion.objects.filter(approved=True).count()
        context['noapproved'] = Postulacion.objects.filter(approved=False).count()
        return context


class AddOfferView(LoginRequiredMixin, TemplateView):
    template_name = 'add_offer.html'

    def get_context_data(self, **kwargs):
        context = super(AddOfferView, self).get_context_data(**kwargs)
        context['form'] = OfferForm()
        return context

    def post(self, request, *args, **kwargs):
        post_values = request.POST.copy()
        form = OfferForm(post_values)

        if form.is_valid():
            form.save()
            return redirect('viewOffers')
        else:
            return render(request, self.template_name, {'form': form})


class ViewOffersView(LoginRequiredMixin, TemplateView):
    template_name = 'view_offers.html'

    def get_context_data(self, **kwargs):
        context = super(ViewOffersView, self).get_context_data(**kwargs)
        context['offers'] = JobOffer.objects.all()
        return context


class DeleteOfferView(LoginRequiredMixin, TemplateView):
    template_name = 'view_offers.html'

    def get(self, request, *args, **kwargs):
        delete = JobOffer.objects.get(pk=int(kwargs['pk']))
        delete.delete()
        return redirect('viewOffers')


class OfferEdit(LoginRequiredMixin, TemplateView):
    template_name = 'edit_offer.html'

    def get_context_data(self, **kwargs):
        context = super(OfferEdit, self).get_context_data(**kwargs)
        # try:
        offer = JobOffer.objects.get(pk=int(kwargs['pk']))

        context['form'] = OfferForm(instance=offer)

        return context

    def post(self, request, *args, **kwargs):
        context = {}
        post_values = request.POST.copy()
        offer = JobOffer.objects.get(pk=int(kwargs['pk']))
        form = OfferForm(post_values, instance=offer)

        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return render(request, 'edit_offer.html', context)

        return redirect('viewOffers')


class ViewUsersView(LoginRequiredMixin, TemplateView):
    template_name = 'view_users.html'

    def get_context_data(self, **kwargs):
        context = super(ViewUsersView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all().filter(is_superuser=False)
        return context


class UserEdit(LoginRequiredMixin, TemplateView):
    template_name = 'edit_user.html'

    def get_context_data(self, **kwargs):
        context = super(UserEdit, self).get_context_data(**kwargs)
        # try:
        user = User.objects.get(pk=int(kwargs['pk']))

        context['form'] = UserEditForm(instance=user)

        return context

    def post(self, request, *args, **kwargs):
        context = {}
        post_values = request.POST.copy()
        user = User.objects.get(pk=int(kwargs['pk']))
        form = UserEditForm(post_values, instance=user)

        if form.is_valid():
            form.save()
            user.email = post_values['username']
            user.save()
        else:
            request.session.pop('msg', False)
            context = {'form': form}
            return render(request, 'edit_user.html', context)

        return redirect('viewUsers')


class DeleteUserView(LoginRequiredMixin, TemplateView):
    template_name = 'view_users.html'

    def get(self, request, *args, **kwargs):
        delete = User.objects.get(pk=int(kwargs['pk']))
        delete.delete()
        return redirect('viewUsers')


'''class AgeView(LoginRequiredMixin, TemplateView):
    template_name = 'age.html'

    def get_context_data(self, **kwargs):

        class cargo:
            def __init__(self, name, prom):
                self.prom = prom
                self.name = name

        context = super(AgeView, self).get_context_data(**kwargs)
        cantgeneral = int(Postulacion.objects.all().count())
        context['promgeneral'] = Postulacion.objects.aggregate(Sum('age'))['age__sum'] / cantgeneral
        cargos = Tittle.objects.all()
        cargosid = []
        for i in cargos:
            cargosid.append(i.id)
        cargosobj = []
        for j in cargosid:
            if not Postulacion.objects.filter(tittle_id=j).aggregate(Sum('age'))['age__sum'] is None:
                cant = Postulacion.objects.filter(tittle_id=j).count()
                prom = Postulacion.objects.filter(tittle_id=j).aggregate(Sum('age'))['age__sum'] / cant
                cargoaux = cargo(Tittle.objects.get(id=j).name, prom)
                cargosobj.append(cargoaux)
        context['cargosobj'] = cargosobj
        return context
'''

class SalView(LoginRequiredMixin, TemplateView):
    template_name = 'sal.html'

    def get_context_data(self, **kwargs):

        class cargo:
            def __init__(self, name, prom):
                self.prom = prom
                self.name = name

        context = super(SalView, self).get_context_data(**kwargs)
        # ----------------------------
        # calculating prom aspSalarial
        # ----------------------------
        cantgeneral1 = int(Postulacion.objects.all().count())
        context['promgeneral1'] = Postulacion.objects.aggregate(Sum('aspSalarial'))['aspSalarial__sum'] / cantgeneral1
        cargos1 = Tittle.objects.all()
        cargosid1 = []
        for i in cargos1:
            cargosid1.append(i.id)
        cargosobj1 = []
        for j in cargosid1:
            if not Postulacion.objects.filter(tittle_id=j).aggregate(Sum('aspSalarial'))['aspSalarial__sum'] is None:
                cant1 = Postulacion.objects.filter(tittle_id=j).count()
                prom1 = Postulacion.objects.filter(tittle_id=j).aggregate(Sum('aspSalarial'))[
                            'aspSalarial__sum'] / cant1
                cargoaux = cargo(Tittle.objects.get(id=j).name, prom1)
                cargosobj1.append(cargoaux)
        context['cargosobj1'] = cargosobj1
        # --------------------------
        # calculating prom salActual
        # --------------------------
        cantgeneral2 = int(Postulacion.objects.all().count())
        context['promgeneral2'] = Postulacion.objects.aggregate(Sum('salActual'))['salActual__sum'] / cantgeneral2
        cargos2 = Tittle.objects.all()
        cargosid2 = []
        for i in cargos2:
            cargosid2.append(i.id)
        cargosobj2 = []
        for j in cargosid2:
            if not Postulacion.objects.filter(tittle_id=j).aggregate(Sum('salActual'))['salActual__sum'] is None:
                cant2 = Postulacion.objects.filter(tittle_id=j).count()
                prom2 = Postulacion.objects.filter(tittle_id=j).aggregate(Sum('salActual'))['salActual__sum'] / cant2
                cargoaux = cargo(Tittle.objects.get(id=j).name, prom2)
                cargosobj2.append(cargoaux)
        context['cargosobj2'] = cargosobj2
        return context


def exportCsv(request):
    # creating generic class "cargo"
    class cargo:
        def __init__(self, name, insc, promAge, promSal, promAsp):
            self.insc = insc
            self.name = name
            self.promAge = promAge
            self.promSal = promSal
            self.promAsp = promAsp

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="estadisticasBeconsult.csv"'
    writer = csv.writer(response)
    # Estadisticas de candidatos
    allCand = Postulacion.objects.count()
    accepted = Postulacion.objects.filter(accepted=True).count()
    notAccepted = Postulacion.objects.filter(accepted=False).count()
    approved = Postulacion.objects.filter(approved=True).count()
    notApproved = Postulacion.objects.filter(approved=False).count()
    # Escribiendo en el csv las estadisticas
    writer.writerow(['Estadisticas de candidatos'])
    writer.writerow(['Todos', allCand])
    writer.writerow(['Elegidos', accepted])
    writer.writerow(['No Elegidos', notAccepted])
    writer.writerow(['Ingresaron', approved])
    writer.writerow(['No Ingresaron', notApproved])
    # --------------------------------------
    writer.writerow(['-------------------------'])
    # Estadisticas sobre postulaciones
    allPost = Postulacion.objects.count()
    cargos = Tittle.objects.all()
    cargosid = []
    for i in cargos:
        cargosid.append(i.id)
    cargosobj = []
    for j in cargosid:
        cargoaux = cargo(Tittle.objects.get(id=j).name, Postulacion.objects.filter(tittle_id=j).count(), 0, 0, 0)
        cargosobj.append(cargoaux)
    # Escribiendo en el csv las estadisticas
    writer.writerow(['Estadisticas de postulaciones'])
    writer.writerow(['Todas', allPost])
    for c in cargosobj:
        writer.writerow([c.name, c.insc])
    # --------------------------------------
    writer.writerow(['-------------------------'])
    # Estadisticas sobre edades
    '''cantgeneral = int(Postulacion.objects.all().count())
    promAgeAll = Postulacion.objects.aggregate(Sum('age'))['age__sum'] / cantgeneral
    cargos = Tittle.objects.all()
    cargosid = []
    for i in cargos:
        cargosid.append(i.id)
    cargosobj = []
    for j in cargosid:
        if not Postulacion.objects.filter(tittle_id=j).aggregate(Sum('age'))['age__sum'] is None:
            cant = Postulacion.objects.filter(tittle_id=j).count()
            prom = Postulacion.objects.filter(tittle_id=j).aggregate(Sum('age'))['age__sum'] / cant
            cargoaux = cargo(Tittle.objects.get(id=j).name, 0, prom, 0, 0)
            cargosobj.append(cargoaux)
    # Escribiendo en el csv las estadisticas
    writer.writerow(['Estadisticas de edades'])
    writer.writerow(['Promedio general', promAgeAll])
    for c in cargosobj:
        writer.writerow([c.name, c.promAge])

    # --------------------------------------
    writer.writerow(['-------------------------'])
    '''
    # Estadisticas sobre salarios actuales
    cantgeneral2 = int(Postulacion.objects.all().count())
    promSalActual = Postulacion.objects.aggregate(Sum('salActual'))['salActual__sum'] / cantgeneral2
    cargos2 = Tittle.objects.all()
    cargosid2 = []
    for i in cargos2:
        cargosid2.append(i.id)
    cargosobj2 = []
    for j in cargosid2:
        if not Postulacion.objects.filter(tittle_id=j).aggregate(Sum('salActual'))['salActual__sum'] is None:
            cant2 = Postulacion.objects.filter(tittle_id=j).count()
            prom2 = Postulacion.objects.filter(tittle_id=j).aggregate(Sum('salActual'))['salActual__sum'] / cant2
            cargoaux = cargo(Tittle.objects.get(id=j).name, 0, 0, prom2, 0)
            cargosobj2.append(cargoaux)
    # Escribiendo en el csv las estadisticas
    writer.writerow(['Estadisticas de salarios actuales'])
    writer.writerow(['Promedio general', promSalActual])
    for c in cargosobj2:
        writer.writerow([c.name, c.promSal])
    # --------------------------------------
    writer.writerow(['-------------------------'])
    # Estadisticas sobre aspiracion salarial
    cantgeneral1 = int(Postulacion.objects.all().count())
    promAspAct = Postulacion.objects.aggregate(Sum('aspSalarial'))['aspSalarial__sum'] / cantgeneral1
    cargos1 = Tittle.objects.all()
    cargosid1 = []
    for i in cargos1:
        cargosid1.append(i.id)
    cargosobj1 = []
    for j in cargosid1:
        if not Postulacion.objects.filter(tittle_id=j).aggregate(Sum('aspSalarial'))['aspSalarial__sum'] is None:
            cant1 = Postulacion.objects.filter(tittle_id=j).count()
            prom1 = Postulacion.objects.filter(tittle_id=j).aggregate(Sum('aspSalarial'))[
                        'aspSalarial__sum'] / cant1
            cargoaux = cargo(Tittle.objects.get(id=j).name, 0, 0, 0, prom1)
            cargosobj1.append(cargoaux)
    # Escribiendo en el csv las estadisticas
    writer.writerow(['Estadisticas de aspiraciones salariales'])
    writer.writerow(['Promedio general', promAspAct])
    for c in cargosobj1:
        writer.writerow([c.name, c.promAsp])
    # retorna el archivo
    return response


class exportCsvView(TemplateView):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        return exportCsv(request)


class mailView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(mailView, self).get_context_data(**kwargs)

        return context


class MailSettings(LoginRequiredMixin, TemplateView):
    template_name = 'emailSettings.html'

    def get_context_data(self, **kwargs):
        context = super(MailSettings, self).get_context_data(**kwargs)
        mail = Mails.objects.all().first()

        context['form'] = MailForm(instance=mail)

        return context

    def post(self, request, *args, **kwargs):
        post_values = request.POST.copy()
        mail = Mails.objects.all().first()
        form = MailForm(post_values, instance=mail)

        if form.is_valid():
            form.save()
        else:
            request.session.pop('msg', False)
            context = {'form': form}
            return render(request, 'emailSettings.html', context)

        return redirect('mailSettings')

class MessageSettings(LoginRequiredMixin, TemplateView):
    template_name = 'messageSettings.html'

    def get_context_data(self, **kwargs):
        context = super(MessageSettings, self).get_context_data(**kwargs)
        message = Message.objects.all().first()
        context['form'] = MessageForm(instance=message)
        return context

    def post(self, request, *args, **kwargs):
        post_values = request.POST.copy()
        message = Message.objects.all().first()
        form = MessageForm(post_values, instance=message)

        if form.is_valid():
            form.save()
        else:
            request.session.pop('msg', False)
            context = {'form': form}
            return render(request, 'messageSettings.html', context)

        return redirect('messageSettings')


# 4 views for password reset:
# - password_reset sends the mail
# - password_reset_done shows a success message for the above
# - password_reset_confirm checks the link the user clicked and
#   prompts for a new password
# - password_reset_complete shows a success message for the above

@deprecate_current_app
@csrf_protect
def password_reset(request,
                   template_name='registration/password_reset_form.html',
                   email_template_name='password_reset_email.html',
                   subject_template_name='registration/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=BECONSULT_EMAIL,
                   extra_context=None,
                   html_email_template_name='password_reset_email.html',
                   extra_email_context={'html': None}):

    
    if (extra_email_context['html'] is None) and (Mails.objects.all().count() > 0):
            extra_email_context = {'html': Mails.objects.all().first().pswMail}
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_done')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
                'extra_email_context': extra_email_context,
            }
            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = password_reset_form()
    context = {
        'form': form,
        'title': _('Password reset'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


@deprecate_current_app
def password_reset_done(request,
                        template_name='registration/password_reset_done.html',
                        extra_context=None):
    context = {
        'title': _('Password reset sent'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


# Doesn't need csrf_protect since no-one can guess the URL
@sensitive_post_parameters()
@never_cache
@deprecate_current_app
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='registration/password_reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect=None,
                           extra_context=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    UserModel = get_user_model()
    assert uidb64 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        title = _('Enter new password')
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
        title = _('Password reset unsuccessful')
    context = {
        'form': form,
        'title': title,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


@deprecate_current_app
def password_reset_complete(request,
                            template_name='registration/password_reset_complete.html',
                            extra_context=None):
    context = {
        'login_url': 'login',
        'title': _('Password reset complete'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)
