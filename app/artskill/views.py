from django.shortcuts import render
from django.views import generic


class IndexPage(generic.TemplateView):
    template_name = 'artskill/index.html'


class BrandPage(generic.TemplateView):
    template_name = 'artskill/brand.html'


class ContactsPage(generic.TemplateView):
    template_name = 'artskill/contacts.html'


class WhereToBuyPage(generic.TemplateView):
    template_name = 'artskill/where_to_buy.html'


class CollaborationPage(generic.TemplateView):
    template_name = 'artskill/collaboration.html'


class DeliveryPage(generic.TemplateView):
    template_name = 'artskill/delivery.html'


class ReturnPage(generic.TemplateView):
    template_name = 'artskill/return.html'


class SalePage(generic.TemplateView):
    template_name = 'artskill/sale.html'
