from django.urls import path

from . import views
from . import conf

app_name = 'robokassa'

urlpatterns = [
    path('result', views.receive_result, name='result'),
    path('success', views.success, name='success'),
    path('fail', views.fail, name='fail'),
]

if conf.TEST_MODE:
    urlpatterns += [
        path('send', views.TestSend.as_view(), name='test-send')
    ]