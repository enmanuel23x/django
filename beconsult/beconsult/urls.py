# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from django.contrib import admin

urlpatterns = [
    
    url(r'^form/(?P<pk>\d+)/$', FormView.as_view(), name='form'),
    url(r'^csv/$', exportCsvView.as_view(), name='csv'),
    url(r'^mailSettings/$', MailSettings.as_view(), name='mailSettings'),
    url(r'^messageSettings/$', MessageSettings.as_view(), name='messageSettings'),
    url(r'^', CandView.as_view(), name='home'),
    # ---------------------------------------- BACKOFFICE
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^addTittle/$', AddTittleView.as_view(), name='addTittle'),
    url(r'^viewTittles/$', ViewTittlesView.as_view(), name='viewTittles'),
    url(r'^editTittle/(?P<pk>\d+)/$', TittleEdit.as_view(), name='editTittle'),
    url(r'^deleteTittle/(?P<pk>\d+)/$', DeleteTittleView.as_view(), name='deleteTittle'),
    url(r'^viewPosts/$', ViewPostsView.as_view(), name='viewPosts'),
    url(r'^viewPostsDetails/(?P<pk>\d+)/$', PostDetails.as_view(), name='viewPostsDetails'),
    url(r'^approvedPosts/(?P<pk>\d+)/$', ApprovedPostView.as_view(), name='approvedPosts'),
    url(r'^notApprovedPosts/(?P<pk>\d+)/$', NotApprovedPostView.as_view(), name='notApprovedPosts'),
    url(r'^acceptedPosts/(?P<pk>\d+)/$', AcceptedPostView.as_view(), name='acceptedPosts'),
    url(r'^notAcceptedPosts/(?P<pk>\d+)/$', NotAcceptedPostView.as_view(), name='notAcceptedPosts'),
    url(r'^addReason/(?P<pk>\d+)/$', AddReasonView.as_view(), name='addReason'),
    url(r'^viewQuestions/$', ViewQuestionsView.as_view(), name='viewQuestions'),
    url(r'^editQuestion/(?P<pk>\d+)/$', QuestionEdit.as_view(), name='editQuestion'),
    url(r'^deleteQuestion/(?P<pk>\d+)/$', DeleteQuestionView.as_view(), name='deleteQuestion'),
    url(r'^addQuestion/$', AddQuestionView.as_view(), name='addQuestion'),
    # ---------------------------------------- STATISTICS
    url(r'^insc/$', InscView.as_view(), name='insc'),
    url(r'^cand/$', CandView.as_view(), name='cand'),
    #url(r'^age/$', AgeView.as_view(), name='age'),
    url(r'^sal/$', SalView.as_view(), name='sal'),
    # ----------------------------------------- OFFERS
    url(r'^addOffer/$', AddOfferView.as_view(), name='addOffer'),
    url(r'^viewOfferss/$', ViewOffersView.as_view(), name='viewOffers'),
    url(r'^deleteOffer/(?P<pk>\d+)/$', DeleteOfferView.as_view(), name='deleteOffer'),
    url(r'^editOffer/(?P<pk>\d+)/$', OfferEdit.as_view(), name='editOffer'),
    # -----------------------------------------  USER SESSIONS AND MANAGEMENT
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^viewUsers/$', ViewUsersView.as_view(), name='viewUsers'),
    url(r'^editUser/(?P<pk>\d+)/$', UserEdit.as_view(), name='editUser'),
    url(r'^deleteUser/(?P<pk>\d+)/$', DeleteUserView.as_view(), name='deleteUser'),
    # ----------------------------------------- RESET PASSWORD
    url(r'^resetpassword/$', password_reset, {'template_name': 'password_reset_form.html'}, name='reset_password'),
    url(r'^resetpassword/done/$', password_reset_done, {'template_name': 'password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/complete/$', password_reset_complete, {'template_name': 'password_reset_complete.html'},
        name='password_reset_complete'),
]