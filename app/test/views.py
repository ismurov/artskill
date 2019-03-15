from django.shortcuts import render
from django.views import generic

# Test
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import send_mail


class TestPage(generic.TemplateView):
    template_name = 'test/test.html'
    # Add in template vars
    extra_context = {'test_var1': 11,
                     'test_var2': 349.633,
                     'test_var3': 150.123,
                     'json': {'a':{'b':{'c':1}, 'd':2}}, 'e':100}

    def get(self, request, *args, **kwargs):
        x = 1
        # Test pop message
        '''
        messages.success(request, 'Check message sender. '
                                  'Args: {}<br>. Kwargs: {}'.format(args, kwargs))
        messages.success(request, 'Check message sender. Messages 2')
        '''

        # Test generate emails
        '''
        msg = get_template('test/test_email.txt').render({
            'test': 'Test done!',
            'var1': 'this is var1',
            'var2': 2,
        })
        send_mail('Test email!',
                  msg, 'email@from.com',
                  ['email@to.com'])
        '''

        # Return base method with render template
        return super(TestPage, self).get(request, *args, **kwargs)


class CategoryPage(generic.TemplateView):
    template_name = 'test/category_page.html'
    # context_object_name = 'latest_question_list'
    #
    # def get_queryset(self):
    #     """
    #     Return the last five published questions (not including those set to be
    #     published in the future).
    #     """
    #     return Question.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by('-pub_date')[:5]


