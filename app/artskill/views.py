from django.views import generic
from django.urls import reverse_lazy

from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = 'artskill/index.html'


class BrandView(generic.TemplateView):
    template_name = 'artskill/brand.html'


class ContactsView(generic.TemplateView):
    template_name = 'artskill/contacts.html'


class WhereToBuyView(generic.TemplateView):
    template_name = 'artskill/where_to_buy.html'


class CollaborationView(generic.FormView):
    template_name = 'artskill/collaboration.html'
    form_class = ContactForm
    success_url = reverse_lazy('artskill:thanks')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


class DeliveryView(generic.TemplateView):
    template_name = 'artskill/delivery.html'


class ReturnView(generic.TemplateView):
    template_name = 'artskill/return.html'


class SaleView(generic.TemplateView):
    template_name = 'artskill/sale.html'


class ThanksView(generic.TemplateView):
    template_name = 'artskill/thanks.html'

