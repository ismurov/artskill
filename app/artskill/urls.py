from django.urls import path

from . import views

app_name = 'artskill'

urlpatterns = [
    path('main/', views.IndexPage.as_view(), name='index'),

    path('brand/', views.BrandPage.as_view(), name='brand'),
    path('contacts/', views.ContactsPage.as_view(), name='contacts'),
    path('where-to-buy/', views.WhereToBuyPage.as_view(), name='where-to-buy'),
    path('collaboration/', views.CollaborationPage.as_view(), name='collaboration'),
    path('delivery/', views.DeliveryPage.as_view(), name='delivery'),
    path('returned_goods/', views.ReturnPage.as_view(), name='return'),

    path('sale/', views.SalePage.as_view(), name='sale'),
]