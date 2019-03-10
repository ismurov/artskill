from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render


from app.catalogue.models import Product

from .forms import ContactForm, SubscriberForm
from .models import Subscriber


class IndexView(generic.TemplateView):
    template_name = 'artskill/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'product_hits': Product.objects.filter(rating__gt=0).order_by('-rating')[:5],
        })
        return context


class BrandView(generic.TemplateView):
    template_name = 'artskill/brand.html'


class ContactsView(generic.TemplateView):
    template_name = 'artskill/contacts.html'


class WhereToBuyView(generic.TemplateView):
    template_name = 'artskill/where_to_buy.html'


class DeliveryView(generic.TemplateView):
    template_name = 'artskill/delivery.html'


class SaleView(generic.TemplateView):
    template_name = 'artskill/sale.html'


class ReturnView(generic.FormView):
    template_name = 'artskill/return.html'
    form_class = ContactForm
    success_url = reverse_lazy('artskill:return-thanks')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email(theme='Возврат')
        return super().form_valid(form)


class ReturnThanksView(generic.TemplateView):
    template_name = 'artskill/thanks.html'
    extra_context = {
        'thanks_head': 'Спасибо',
        'thanks_body': 'Мы свяжемся с вами в ближайшее время.',
    }


class CollaborationView(generic.FormView):
    template_name = 'artskill/collaboration.html'
    form_class = ContactForm
    success_url = reverse_lazy('artskill:collaboration-thanks')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email(theme='Сотрудничество')
        return super().form_valid(form)


class CollaborationThanksView(generic.TemplateView):
    template_name = 'artskill/thanks.html'
    extra_context = {
        'thanks_head': 'Спасибо',
        'thanks_body': 'Мы уже думаем над вашим предложением.',
    }


class SubscribeView(generic.FormView):
    template_name = 'artskill/subscribe.html'
    form_class = SubscriberForm
    success_url = reverse_lazy('artskill:subscribe-thanks')

    def form_valid(self, form):
        subscriber, created = Subscriber.objects.get_or_create(**form.cleaned_data)
        if created:
            subscriber.save()
        return super().form_valid(form)


class SubscribeThanksView(generic.TemplateView):
    template_name = 'artskill/thanks.html'
    extra_context = {
        'thanks_head': 'Спасибо',
        'thanks_body': 'Спасибо, что подписались на наши новости.',
    }


class ThanksView(generic.TemplateView):
    template_name = 'artskill/thanks.html'
    extra_context = {
        'thanks_head': 'Спасибо',
        'thanks_body': '',
    }


class CustomerAgreementView(generic.TemplateView):
    template_name = 'artskill/customer_agreement.html'
