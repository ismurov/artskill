from django.urls import path, re_path

from . import views

app_name = 'artskill'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),

    path('brand/', views.BrandView.as_view(), name='brand'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('where-to-buy/', views.WhereToBuyView.as_view(), name='where-to-buy'),
    path('delivery/', views.DeliveryView.as_view(), name='delivery'),
    path('customer_agreement/', views.CustomerAgreementView.as_view(), name='customer-agreement'),
    path('sale/', views.SaleView.as_view(), name='sale'),

    # with forms
    path('return/', views.ReturnView.as_view(), name='return'),
    path('return/thanks/', views.ReturnThanksView.as_view(), name='return-thanks'),
    path('collaboration/', views.CollaborationView.as_view(), name='collaboration'),
    path('collaboration/thanks/', views.CollaborationThanksView.as_view(), name='collaboration-thanks'),

    # thanks
    path('registration/thanks/', views.RegistrationThanksView.as_view(), name='registration-thanks'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),

    # emails
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('subscribe/thanks/', views.SubscribeThanksView.as_view(), name='subscribe-thanks'),
    path('unsubscribe/', views.UnsubscribeView.as_view(), name='unsubscribe'),
    path('unsubscribe/thanks/', views.UnsubscribeThanksView.as_view(), name='unsubscribe-thanks'),

    # emails dashboard
    path('dashboard/mailing_list/', views.DashboardSubscriberView.as_view(), name='mailing-list'),
    path('dashboard/mailing_list/get_csv_file',
         views.DashboardSubscriberGenCSVFileView.as_view(),
         name='mailing-list-csv'),

    # re_path(r'^unsubscribe/(?P<subscriber_id>[0-9]{4})/$',
    #         views.EmailUnsubscribeView.as_view(),
    #         name='email-unsubscribe'),
]
