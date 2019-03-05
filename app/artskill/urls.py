from django.urls import path, re_path

from . import views

app_name = 'artskill'

urlpatterns = [
    path('main/', views.IndexView.as_view(), name='index'),

    path('brand/', views.BrandView.as_view(), name='brand'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('where-to-buy/', views.WhereToBuyView.as_view(), name='where-to-buy'),
    path('delivery/', views.DeliveryView.as_view(), name='delivery'),
    path('returned_goods/', views.ReturnView.as_view(), name='return'),

    path('sale/', views.SaleView.as_view(), name='sale'),

    # with forms
    path('collaboration/', views.CollaborationView.as_view(), name='collaboration'),
    path('collaboration/thanks/', views.CollaborationThanksView.as_view(), name='collaboration-thanks'),

    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('subscribe/thanks/', views.SubscribeThanksView.as_view(), name='subscribe-thanks'),
    # re_path(r'^unsubscribe/(?P<subscriber_id>[0-9]{4})/$',
    #         views.EmailUnsubscribeView.as_view(),
    #         name='email-unsubscribe'),
    path('thanks/', views.ThanksView.as_view(), name='thanks')
]