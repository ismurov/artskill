from django.urls import path

from . import views

app_name = 'artskill'

urlpatterns = [
    path('main/', views.IndexView.as_view(), name='index'),

    path('brand/', views.BrandView.as_view(), name='brand'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('where-to-buy/', views.WhereToBuyView.as_view(), name='where-to-buy'),
    path('collaboration/', views.CollaborationView.as_view(), name='collaboration'),
    path('delivery/', views.DeliveryView.as_view(), name='delivery'),
    path('returned_goods/', views.ReturnView.as_view(), name='return'),

    path('sale/', views.SaleView.as_view(), name='sale'),

    path('thanks/', views.ThanksView.as_view(), name='thanks')
]